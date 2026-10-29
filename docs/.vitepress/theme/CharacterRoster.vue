<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { withBase } from 'vitepress'
import * as THREE from 'three'
import { disposeObject, loadBedrockGeo } from './bedrockGeo'

interface Character {
  id: string; name: string; magic: string; squad: string; role: string
  color: string; group: string; geo: string; texture: string
}
const props = defineProps<{ characters: Character[] }>()
const group = ref('all')
const magic = ref('')
const portraits = ref<Record<string, string>>({})
const groups = [{ id: 'all', label: 'Todos' }, { id: 'bulls', label: 'Touros' }, { id: 'spade', label: 'Spade' }, { id: 'other', label: 'Outros' }]
const visible = computed(() => props.characters.filter(c => (group.value === 'all' || c.group === group.value) && (!magic.value || c.magic === magic.value)))
let stopped = false
onBeforeUnmount(() => { stopped = true })

// One renderer produces still portraits for the whole roster, then releases WebGL.
onMounted(async () => {
  let renderer: THREE.WebGLRenderer | undefined
  try {
    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true })
    renderer.setSize(360, 240)
    const scene = new THREE.Scene()
    const camera = new THREE.PerspectiveCamera(35, 1.5, 0.1, 1000)
    for (const character of props.characters) {
      if (stopped) break
      let model: THREE.Group | undefined
      let material: THREE.MeshBasicMaterial | undefined
      let texture: THREE.Texture | undefined
      try {
        const response = await fetch(withBase(character.geo))
        if (!response.ok) continue
        const geometry = await response.json()
        texture = await new THREE.TextureLoader().loadAsync(withBase(character.texture))
        if (stopped) break
        texture.magFilter = THREE.NearestFilter
        texture.minFilter = THREE.NearestFilter
        texture.colorSpace = THREE.SRGBColorSpace
        material = new THREE.MeshBasicMaterial({ map: texture, transparent: true, alphaTest: 0.1 })
        model = loadBedrockGeo(geometry, material)
        model.rotation.y = Math.PI + 0.2
        scene.add(model)
        const box = new THREE.Box3().setFromObject(model)
        const center = box.getCenter(new THREE.Vector3())
        const size = box.getSize(new THREE.Vector3())
        const distance = Math.max(size.y, size.x / camera.aspect, 8) / (2 * Math.tan(THREE.MathUtils.degToRad(17.5))) * 1.1
        camera.position.set(center.x, center.y + size.y * 0.06, center.z + distance)
        camera.lookAt(center)
        renderer.render(scene, camera)
        portraits.value[character.id] = renderer.domElement.toDataURL('image/png')
      } catch {
        // The character name remains usable when WebGL or an asset is unavailable.
      } finally {
        if (model) { scene.remove(model); disposeObject(model) }
        material?.dispose()
        texture?.dispose()
      }
    }
  } catch {
    // Text cards also work without WebGL.
  } finally { renderer?.dispose() }
})
</script>

<template>
  <section class="character-roster" aria-label="Magos jogáveis">
    <div class="roster-filters">
      <div class="roster-groups" role="group" aria-label="Filtrar por grupo">
        <button v-for="item in groups" :key="item.id" :aria-pressed="group === item.id" @click="group = item.id">{{ item.label }}</button>
      </div>
      <div class="roster-magic"><label for="roster-magic">Magia</label>
        <select id="roster-magic" v-model="magic"><option value="">Todas</option><option v-for="item in [...new Set(characters.map(c => c.magic))]" :key="item">{{ item }}</option></select>
      </div>
    </div>
    <p class="roster-count" role="status">{{ visible.length }} de {{ characters.length }} magos</p>
    <div class="roster-grid">
      <a v-for="character in visible" :key="character.id" class="character-card" :href="withBase(`/personagens/${character.id}`)" :style="{ '--character-accent': character.color }">
        <div class="character-portrait"><img v-if="portraits[character.id]" :src="portraits[character.id]" alt="" width="360" height="240"><span v-else aria-hidden="true">{{ character.name.slice(0, 1) }}</span></div>
        <div class="character-card-copy"><h2>{{ character.name }}</h2><p class="character-magic">{{ character.magic }}</p><p>{{ character.role }}</p><small>{{ character.squad }}</small></div>
      </a>
    </div>
    <p v-if="!visible.length">Nenhum mago nessa combinação. Selecione outro grupo ou magia.</p>
  </section>
</template>
