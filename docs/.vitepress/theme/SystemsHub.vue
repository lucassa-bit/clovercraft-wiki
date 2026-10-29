<script setup lang="ts">
const groups = [
  { title: 'Seu cavaleiro', text: 'Escolhas feitas na cerimônia e no exame que definem o estilo de progresso.', cards: [
    { href: '/sistemas/racas', title: 'Raças', meta: 'Atributos iniciais e maestria' },
    { href: '/sistemas/squads', title: 'Esquadrões', meta: 'Bônus leves e manto' },
    { href: '/sistemas/arvore', title: 'Árvore de skills', meta: 'Cinco ramos e capstones' },
  ] },
  { title: 'Progredir e lutar', text: 'Atividades que dão força, méritos, maestria, itens e novas opções de combate.', cards: [
    { href: '/sistemas/quests', title: 'Jornadas e treinos', meta: 'Formas, provas e segredos' },
    { href: '/sistemas/invocacoes', title: 'Subordinados', meta: 'Pacto, ordens e despertar' },
    { href: '/sistemas/reliquias', title: 'Relíquias', meta: 'Ativas, passivas e origens' },
  ] },
  { title: 'Ferramentas e grupo', text: 'Utilidades do mundo, organização com outros jogadores e referência administrativa.', cards: [
    { href: '/sistemas/itens', title: 'Itens e blocos', meta: 'Grimórios, altar e utilitários' },
    { href: '/sistemas/guildas', title: 'Guildas', meta: 'Times de jogadores' },
    { href: '/sistemas/comandos', title: 'Comandos', meta: 'Jogador e administração' },
  ] },
]
</script>

<template>
  <div class="systems-hub">
    <p class="systems-lead">Use esta área como mapa dos sistemas. A ordem recomendada é: definir seu cavaleiro, fortalecer a build e então buscar jornadas, invocações ou relíquias conforme seu estilo.</p>
    <section v-for="group in groups" :key="group.title" class="systems-group">
      <header><h2>{{ group.title }}</h2><p>{{ group.text }}</p></header>
      <div class="systems-grid">
        <a v-for="card in group.cards" :key="card.href" :href="card.href" class="system-card"><strong>{{ card.title }}</strong><span>{{ card.meta }}</span><b>Ver sistema →</b></a>
      </div>
    </section>
  </div>
</template>
