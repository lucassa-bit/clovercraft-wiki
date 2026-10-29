<script setup lang="ts">
import { computed, ref, watch } from 'vue'

interface Skill { form: string; formLabel: string; slot: number; name: string; duration: string; damage?: string; mastery: string; effect: string; rank?: string }
interface Unlock { rank: string; entries: string[] }
interface Step { label: string; kind: string; place: string; minimum: number; boss?: string; reward: string }
interface Journey { name: string; requires: string[]; steps: Step[] }
interface Summon { name: string; role: string; tier: number; unique: boolean }
const props = defineProps<{ skills: Skill[]; unlocks: Unlock[]; journeys: Journey[]; summons: Summon[] }>()
const forms = computed(() => [...new Map(props.skills.map(skill => [skill.form, skill.formLabel])).entries()].map(([id, label]) => ({ id, label })))
const active = ref('')
watch(forms, list => { if (!list.some(form => form.id === active.value)) active.value = list[0]?.id ?? '' }, { immediate: true })
const visible = computed(() => props.skills.filter(skill => skill.form === active.value))
</script>

<template>
  <section class="character-details">
    <h2 id="habilidades">Habilidades</h2>
    <p class="details-intro">Descrição, duração e dano vêm da action do mod. O dano é o valor-base declarado pela action; nas formas, aplique o multiplicador de maestria mostrado no card antes dos demais modificadores de força, forma, árvore, PvE/PvP e servidor.</p>
    <div class="skill-tabs" role="tablist" aria-label="Habilidades por forma">
      <button v-for="form in forms" :key="form.id" role="tab" :aria-selected="active === form.id" @click="active = form.id">{{ form.label }}</button>
    </div>
    <div class="skill-cards" role="tabpanel">
      <article v-for="skill in visible" :key="`${skill.form}-${skill.slot}-${skill.name}`" class="skill-card" :class="{ ultimate: skill.slot === 5 }">
        <p class="skill-slot">{{ skill.slot === 5 ? 'Slot 5' : `Slot ${skill.slot}` }}</p>
        <h3>{{ skill.name }}</h3>
        <p>{{ skill.effect }}</p>
        <dl><dt>Duração</dt><dd>{{ skill.duration }}</dd><template v-if="skill.damage"><dt>Dano-base</dt><dd>{{ skill.damage }}</dd></template><template v-else><dt>Dano-base</dt><dd>não declarado</dd></template><dt>Maestria</dt><dd>{{ skill.mastery }}</dd><template v-if="skill.rank"><dt>Rank</dt><dd>{{ skill.rank }}</dd></template></dl>
      </article>
    </div>

    <h2 id="desbloqueios">Desbloqueios por rank</h2>
    <div v-if="unlocks.length" class="unlock-list"><article v-for="unlock in unlocks" :key="unlock.rank"><strong>{{ unlock.rank }}</strong><span>{{ unlock.entries.join(' · ') }}</span></article></div>
    <p v-else>Este kit não declara desbloqueios por rank.</p>

    <h2 id="jornada">Jornada</h2>
    <div v-if="journeys.length" class="journey-list"><article v-for="journey in journeys" :key="journey.name" class="journey"><h3>{{ journey.name }}</h3><p v-if="journey.requires.length">Requer: {{ journey.requires.join(', ') }}</p><ol><li v-for="step in journey.steps" :key="step.label"><strong>{{ step.label }}</strong><span>{{ step.kind }} · {{ step.place }} · força {{ step.minimum }}+</span><span v-if="step.boss">Chefe: {{ step.boss }}</span><small>{{ step.reward }}</small></li></ol></article></div>
    <p v-else>Este personagem não tem cadeia de jornada própria registrada.</p>

    <h2 id="subordinados">Subordinados</h2>
    <div v-if="summons.length" class="summon-list"><article v-for="summon in summons" :key="summon.name"><strong>{{ summon.name }}</strong><span>{{ summon.role }} · tier {{ summon.tier }}{{ summon.unique ? ' · único' : '' }}</span></article></div>
    <p v-else>Este personagem não tem pool de subordinados registrado.</p>
  </section>
</template>
