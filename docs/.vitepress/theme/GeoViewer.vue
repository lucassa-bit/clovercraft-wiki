<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { applyMaterial, disposeObject, loadBedrockGeo } from './bedrockGeo'

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

const activeSkins = computed<Skin[]>(() => {
  const cat = parsedCatalog.value.find((c) => c.id === catalogId.value)
  if (cat) {
    return [{ id: cat.id, label: cat.label, texture: cat.texture }]
  }
  return parsedSkins.value
})

let renderer: THREE.WebGLRenderer | null = null
let scene: THREE.Scene | null = null
let camera: THREE.PerspectiveCamera | null = null
let controls: OrbitControls | null = null
let model: THREE.Group | null = null
let material: THREE.MeshBasicMaterial | null = null
let frame = 0
let disposed = false

function url(path: string): string {
  if (!path) return ''
  return withBase(path.startsWith('/') ? path : `/${path}`)
}

function fitCamera(object: THREE.Object3D): void {
  if (!camera || !controls) return
  const box = new THREE.Box3().setFromObject(object)
  const size = box.getSize(new THREE.Vector3())
  const center = box.getCenter(new THREE.Vector3())
  const max = Math.max(size.x, size.y, size.z, 8)
  camera.position.set(center.x, center.y + max * 0.15, center.z + max * 1.8)
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
      if (material.map) material.map.dispose()
      material.map = tex
      material.needsUpdate = true
    }
    model = loadBedrockGeo(json, material)
    model.rotation.y = Math.PI
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

function tick(): void {
  if (disposed) return
  frame = requestAnimationFrame(tick)
  controls?.update()
  if (renderer && scene && camera) renderer.render(scene, camera)
}

onMounted(() => {
  if (!host.value) return
  scene = new THREE.Scene()
  scene.background = new THREE.Color(0x101610)
  camera = new THREE.PerspectiveCamera(40, host.value.clientWidth / props.height, 0.1, 500)
  renderer = new THREE.WebGLRenderer({ antialias: false, alpha: false })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.setSize(host.value.clientWidth, props.height)
  host.value.appendChild(renderer.domElement)
  controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
  controls.autoRotate = true
  controls.autoRotateSpeed = 1.4
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
  const tex = await loadTexture(skin.texture)
  if (material.map) material.map.dispose()
  material.map = tex
  material.needsUpdate = true
})

watch(catalogId, async () => {
  const cat = parsedCatalog.value.find((c) => c.id === catalogId.value)
  if (cat) skinId.value = cat.id
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
    <div class="geo-toolbar" v-if="parsedCatalog.length || parsedSkins.length > 1">
      <label v-if="parsedCatalog.length">
        Modelo
        <select v-model="catalogId">
          <option v-for="item in parsedCatalog" :key="item.id" :value="item.id">
            {{ item.label }}
          </option>
        </select>
      </label>
      <label v-if="parsedSkins.length > 1">
        Forma / skin
        <select v-model="skinId">
          <option v-for="skin in parsedSkins" :key="skin.id" :value="skin.id">
            {{ skin.label }}
          </option>
        </select>
      </label>
      <span class="hint">arraste para girar · scroll para zoom</span>
    </div>
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
  background: #0b0f0c;
}
.geo-toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  align-items: center;
  padding: 0.65rem 0.9rem;
  background: #161c16;
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
  margin-left: auto;
  opacity: 0.65;
  font-size: 0.78rem;
}
.geo-stage {
  position: relative;
  width: 100%;
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
</style>
