<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { applyMaterial, disposeObject, loadBedrockGeo } from './bedrockGeo'
import { applyCharacterAppearance } from './characterAppearance'

export interface Skin {
  id: string
  label: string
  texture: string
}

export interface CatalogItem {
  id: string
  label: string
  geo: string
  texture: string
}

const props = withDefaults(
  defineProps<{
    geo?: string
    skins?: Skin[] | string
    catalog?: CatalogItem[] | string
    height?: number
    formButtons?: boolean
  }>(),
  { height: 420 },
)

const host = ref<HTMLDivElement | null>(null)
const status = ref('Carregando modelo…')
const skinId = ref('')
const catalogId = ref('')

const parsedSkins = computed<Skin[]>(() => {
  if (typeof props.skins === 'string') {
    try {
      return JSON.parse(props.skins) as Skin[]
    } catch {
      return []
    }
  }
  return props.skins ?? []
})

const parsedCatalog = computed<CatalogItem[]>(() => {
  if (typeof props.catalog === 'string') {
    try {
      return JSON.parse(props.catalog) as CatalogItem[]
    } catch {
      return []
    }
  }
  return props.catalog ?? []
})

const activeGeo = computed(() => {
  const cat = parsedCatalog.value.find((c) => c.id === catalogId.value)
  return cat?.geo || props.geo || ''
})

const characterId = computed(() => activeGeo.value.split('/').pop()?.replace('.geo.json', '') ?? '')

const activeSkins = computed<Skin[]>(() => {
  const cat = parsedCatalog.value.find((c) => c.id === catalogId.value)
  if (cat) {
    return [{ id: cat.id, label: cat.label, texture: cat.texture }]
  }
  return parsedSkins.value
})

const activeSkin = computed(() => activeSkins.value.find((skin) => skin.id === skinId.value) ?? activeSkins.value[0])

let renderer: THREE.WebGLRenderer | null = null
let scene: THREE.Scene | null = null
let camera: THREE.PerspectiveCamera | null = null
let controls: OrbitControls | null = null
let model: THREE.Group | null = null
let material: THREE.MeshBasicMaterial | null = null
let frame = 0
let disposed = false
let textureRequest = 0

function url(path: string): string {
  if (!path) return ''
  return withBase(path.startsWith('/') ? path : `/${path}`)
}

function fitCamera(object: THREE.Object3D): void {
  if (!camera || !controls) return
  const box = new THREE.Box3().setFromObject(object)
  const size = box.getSize(new THREE.Vector3())
  const center = box.getCenter(new THREE.Vector3())
  let max = Math.max(size.x, size.y, size.z, 8)
  // Character framing follows the body, so long weapons don't shrink the mage.
  const hips = props.formButtons && object.getObjectByName('hips')
  const head = props.formButtons && object.getObjectByName('head')
  if (hips && head) {
    const origin = object.getWorldPosition(new THREE.Vector3())
    const top = head.getWorldPosition(new THREE.Vector3())
    hips.getWorldPosition(center)
    max = Math.max(Math.abs(top.y - origin.y) + 8, 24)
    center.y += max * 0.08
  }
  camera.position.set(center.x, center.y + max * 0.08, center.z + max * 1.8)
  camera.near = max / 100
  camera.far = max * 20
  camera.updateProjectionMatrix()
  controls.target.copy(center)
  controls.minDistance = max * 0.4
  controls.maxDistance = max * 6
  controls.update()
}

async function loadTexture(path: string): Promise<THREE.Texture> {
  const loader = new THREE.TextureLoader()
  const tex = await loader.loadAsync(url(path))
  tex.magFilter = THREE.NearestFilter
  tex.minFilter = THREE.NearestFilter
  tex.colorSpace = THREE.SRGBColorSpace
  tex.flipY = true
  return tex
}

async function rebuild(): Promise<void> {
  if (!scene || !material) return
  status.value = 'Carregando modelo…'
  if (model) {
    scene.remove(model)
    disposeObject(model)
    model = null
  }
  const geoPath = activeGeo.value
  if (!geoPath) {
    status.value = 'Sem modelo'
    return
  }
  try {
    const res = await fetch(url(geoPath))
    if (!res.ok) throw new Error(String(res.status))
    const json = await res.json()
    const skin = activeSkins.value.find((s) => s.id === skinId.value) ?? activeSkins.value[0]
    if (skin) {
      const tex = await loadTexture(skin.texture)
      if (disposed) { tex.dispose(); return }
      if (material.map) material.map.dispose()
      material.map = tex
      material.needsUpdate = true
    }
    if (disposed) return
    model = loadBedrockGeo(json, material)
    model.rotation.y = Math.PI
    applyCharacterAppearance(model, characterId.value, skin?.id ?? '')
    scene.add(model)
    fitCamera(model)
    status.value = ''
  } catch (err) {
    status.value = `Falha ao carregar o modelo (${err instanceof Error ? err.message : 'erro'})`
  }
}

function resize(): void {
  if (!host.value || !renderer || !camera) return
  const w = host.value.clientWidth
  const h = props.height
  renderer.setSize(w, h)
  camera.aspect = w / h
  camera.updateProjectionMatrix()
}

function resetView(): void {
  if (model) fitCamera(model)
}

function tick(): void {
  if (disposed) return
  frame = requestAnimationFrame(tick)
  controls?.update()
  if (renderer && scene && camera) renderer.render(scene, camera)
}

onMounted(() => {
  if (!host.value) return
  scene = new THREE.Scene()
  camera = new THREE.PerspectiveCamera(40, host.value.clientWidth / props.height, 0.1, 500)
  renderer = new THREE.WebGLRenderer({ antialias: false, alpha: true })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.setSize(host.value.clientWidth, props.height)
  host.value.appendChild(renderer.domElement)
  controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
  // The viewer is intentionally static: forms are easier to compare without
  // motion constantly changing their silhouette.
  controls.autoRotate = false
  material = new THREE.MeshBasicMaterial({ map: null, transparent: true, alphaTest: 0.1 })
  window.addEventListener('resize', resize)
  if (parsedCatalog.value[0]) {
    catalogId.value = parsedCatalog.value[0].id
  } else {
    if (parsedSkins.value[0]) skinId.value = parsedSkins.value[0].id
    void rebuild()
  }
  tick()
})

watch(skinId, async () => {
  const skin = activeSkins.value.find((s) => s.id === skinId.value)
  if (!skin || !material) return
  const request = ++textureRequest
  try {
    const tex = await loadTexture(skin.texture)
    if (disposed || request !== textureRequest) { tex.dispose(); return }
    if (material.map) material.map.dispose()
    material.map = tex
    material.needsUpdate = true
    if (model) applyCharacterAppearance(model, characterId.value, skin.id)
    status.value = ''
  } catch {
    if (!disposed && request === textureRequest) status.value = 'Falha ao carregar este visual. Selecione outra forma para tentar novamente.'
  }
})

watch(catalogId, async () => {
  const cat = parsedCatalog.value.find((c) => c.id === catalogId.value)
  if (cat) skinId.value = cat.id
})

// A roster can supply a new geo/texture pair directly. Reload when that
// selected entry changes as well as when this component's own picker changes.
watch(activeGeo, async () => {
  await rebuild()
})

onBeforeUnmount(() => {
  disposed = true
  cancelAnimationFrame(frame)
  window.removeEventListener('resize', resize)
  controls?.dispose()
  if (model) disposeObject(model)
  material?.map?.dispose()
  material?.dispose()
  renderer?.dispose()
  renderer?.domElement.remove()
})
</script>

<template>
  <div class="geo-viewer">
    <header class="geo-heading">
      <span>Modelo 3D</span>
      <strong v-if="activeSkin">{{ activeSkin.label }}</strong>
    </header>
    <div class="geo-toolbar">
      <label v-if="parsedCatalog.length">
        Modelo
        <select v-model="catalogId">
          <option v-for="item in parsedCatalog" :key="item.id" :value="item.id">
            {{ item.label }}
          </option>
        </select>
      </label>
      <div v-if="formButtons && parsedSkins.length > 1" class="geo-forms" role="group" aria-label="Forma ou visual do modelo">
        <button v-for="skin in parsedSkins" :key="skin.id" :aria-pressed="skinId === skin.id" @click="skinId = skin.id">{{ skin.label }}</button>
      </div>
      <label v-else-if="parsedSkins.length > 1">
        Forma / skin
        <select v-model="skinId">
          <option v-for="skin in parsedSkins" :key="skin.id" :value="skin.id">
            {{ skin.label }}
          </option>
        </select>
      </label>
      <button class="geo-reset" type="button" @click="resetView">Redefinir visão</button>
    </div>
    <p class="hint">Arraste para girar · role para aproximar · selecione uma forma para comparar o visual</p>
    <div ref="host" class="geo-stage" :style="{ height: height + 'px' }">
      <p v-if="status" class="geo-status">{{ status }}</p>
    </div>
  </div>
</template>

<style scoped>
.geo-viewer {
  margin: 1.25rem 0 1.75rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  overflow: hidden;
  background: radial-gradient(ellipse 75% 65% at 50% 46%, color-mix(in srgb, var(--character-accent, #3dba6e) 25%, var(--vp-c-bg)), var(--vp-c-bg-alt) 70%);
}
.geo-heading {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  padding: 0.7rem 0.9rem 0.55rem;
  color: var(--vp-c-text-1);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: .04em;
  text-transform: uppercase;
}
.geo-heading strong {
  max-width: 68%;
  overflow: hidden;
  color: var(--character-accent, var(--vp-c-brand-1));
  font-size: 0.78rem;
  letter-spacing: 0;
  text-overflow: ellipsis;
  text-transform: none;
  white-space: nowrap;
}
.geo-toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  align-items: center;
  padding: 0.65rem 0.9rem;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  font-size: 0.85rem;
}
.geo-toolbar select {
  margin-left: 0.4rem;
  background: #101610;
  color: var(--vp-c-text-1);
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  padding: 0.2rem 0.4rem;
}
.hint {
  margin: 0;
  padding: 0.4rem 0.9rem;
  color: var(--vp-c-text-2);
  font-size: 0.78rem;
}
.geo-forms { display: flex; flex-wrap: wrap; gap: 6px; }
.geo-forms button, .geo-reset { padding: 5px 9px; border: 1px solid var(--vp-c-divider); border-radius: 6px; color: var(--vp-c-text-1); background: var(--vp-c-bg); font: inherit; }
.geo-forms button[aria-pressed="true"] { border-color: var(--character-accent, var(--vp-c-brand-1)); background: var(--vp-c-bg); box-shadow: inset 0 -2px var(--character-accent, var(--vp-c-brand-1)); }
.geo-reset { margin-left: auto; color: var(--vp-c-text-2); font-size: 0.8rem; }
.geo-forms button:focus-visible, .geo-reset:focus-visible { outline: 2px solid var(--vp-c-brand-1); outline-offset: 2px; }
.geo-stage {
  position: relative;
  width: 100%;
  background: radial-gradient(ellipse 52% 8% at 50% 86%, color-mix(in srgb, var(--character-accent, #3dba6e) 20%, transparent), transparent 72%);
}
.geo-stage :deep(canvas) {
  display: block;
  width: 100% !important;
}
.geo-status {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  margin: 0;
  color: var(--vp-c-text-2);
  pointer-events: none;
}
@media (max-width: 480px) { .geo-reset { width: 100%; margin-left: 0; } }
</style>
