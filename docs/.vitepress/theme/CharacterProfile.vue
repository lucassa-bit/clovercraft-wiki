<script setup lang="ts">
import GeoViewer from './GeoViewer.vue'
import type { Skin } from './GeoViewer.vue'
defineProps<{
  name: string; magic: string; squad: string; role: string; description: string
  color: string; grimoire: string; forms: string[]; geo: string; skins: Skin[]
  progression: string[]; peculiar?: string
}>()
</script>

<template>
  <section class="character-profile" :style="{ '--character-accent': color }" :aria-label="`Ficha de ${name}`">
    <div class="character-model">
      <ClientOnly><GeoViewer v-if="geo && skins.length" :geo="geo" :skins="skins" :height="350" form-buttons /><template #fallback><p>Carregando visualização 3D…</p></template></ClientOnly>
    </div>
    <div class="character-facts">
      <p class="profile-eyebrow">{{ magic }} · {{ squad }}</p>
      <h2>{{ role }}</h2>
      <p>{{ description }}</p>
      <dl>
        <dt>Grimório</dt><dd>{{ grimoire }}</dd>
        <dt>Formas</dt><dd>{{ forms.join(' → ') }}</dd>
        <template v-if="progression.length"><dt>Regra de transformação</dt><dd class="profile-gate"><strong>Maestria máxima (5★).</strong> No padrão do mod, a Base libera a primeira forma; cada forma libera a seguinte. Jornada, força, rank e recurso do kit continuam sendo exigidos.</dd></template>
        <template v-for="(step, index) in progression" :key="step"><dt>{{ index === 0 ? 'Primeira forma' : 'Segunda forma' }}</dt><dd>{{ step }} <a href="#quests-da-jornada">Ver jornada</a></dd></template>
        <template v-if="peculiar"><dt>Particularidade</dt><dd>{{ peculiar }}</dd></template>
      </dl>
      <p class="profile-binding">Use o grimório com o botão direito para vincular este mago.</p>
    </div>
  </section>
</template>
