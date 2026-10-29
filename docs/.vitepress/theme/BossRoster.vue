<script setup lang="ts">
import { computed, ref } from 'vue'
import GeoViewer from './GeoViewer.vue'

type Boss = { id: string; name: string; title: string; magic: string; band: number; zone: 'Mundo' | 'Qliphoth'; style: string; danger: string; strategy: string; moves: string[] }

const bosses: Boss[] = [
  { id: 'ancient_golem', name: 'Golem Ancestral de Mana', title: 'Guardião da Masmorra', magic: 'Pedra e runas de mana', band: 12, zone: 'Mundo', style: 'Tanque de curta distância', danger: 'Golpes de chão e pilares punem quem fica parado.', strategy: 'Mantenha distância após o punho e ataque durante a recuperação.', moves: ['Punho de Rocha', 'Raio Rúnico', 'Sobrecarga Ancestral'] },
  { id: 'sally', name: 'Sally', title: 'Olho do Sol da Meia-Noite', magic: 'Gel', band: 16, zone: 'Mundo', style: 'Zona e perseguição', danger: 'Poças e invocações fecham caminhos.', strategy: 'Evite o chão marcado e elimine pressão lateral antes de avançar.', moves: ['Salamandra Pegajosa', 'Poça de Gel', 'Escorpião Mágico'] },
  { id: 'rades', name: 'Rades Spirito', title: 'Olho do Sol da Meia-Noite', magic: 'Cadáver espiritual', band: 18, zone: 'Mundo', style: 'Invocador', danger: 'A arena fica congestionada com cadáveres e agarrões.', strategy: 'Limpe os lacaios, depois entre para interromper a janela de cura.', moves: ['Exército de Cadáveres', 'Mãos da Cova', 'Raptor de Almas'] },
  { id: 'heath_grice', name: 'Heath Graice', title: 'Olho do Sol da Meia-Noite', magic: 'Gelo', band: 22, zone: 'Mundo', style: 'Controle de área', danger: 'Jaulas e estilhaços restringem a movimentação.', strategy: 'Guarde o dash para sair da prisão e não lute encostado em paredes.', moves: ['Estilhaços de Gelo', 'Jaula de Granizo', 'Funeral de Gelo'] },
  { id: 'valtos', name: 'Valtos', title: 'Olho do Sol da Meia-Noite', magic: 'Espacial', band: 26, zone: 'Mundo', style: 'Mobilidade e emboscada', danger: 'Portais mudam a origem dos ataques.', strategy: 'Use lock-on e espere a saída do portal antes de comprometer um golpe pesado.', moves: ['Guilhotina de Portal', 'Portão Forçado', 'Miríade Negra'] },
  { id: 'lotus_whomalt', name: 'Lotus Whomalt', title: 'Lótus do Inferno', magic: 'Fumaça', band: 30, zone: 'Mundo', style: 'Debuff e confinamento', danger: 'Fumaça reduz leitura da arena e as prisões isolam jogadores.', strategy: 'Lute em espaço aberto e priorize sair da prisão em vez de trocar dano.', moves: ['Chicote de Fumaça', 'Jardim de Fumaça', 'Prisão de Fumaça'] },
  { id: 'catherine', name: 'Catherine', title: 'Olho do Sol da Meia-Noite', magic: 'Cinzas', band: 34, zone: 'Mundo', style: 'Assédio aéreo', danger: 'Cinzas, maldições e mergulhos castigam alvos isolados.', strategy: 'Não persiga a vassoura; espere o pouso e preserve defesa contra a rajada.', moves: ['Rajada de Cinzas', 'Chuva de Cinzas', 'Pira da Bruxa'] },
  { id: 'dominante_code', name: 'Dominante Code', title: 'Bruxa da Floresta das Bruxas', magic: 'Ferramentas mágicas', band: 36, zone: 'Mundo', style: 'Invocador móvel', danger: 'Golens pressionam enquanto ela troca de ferramenta.', strategy: 'Derrube os golens próximos e use a pausa entre ferramentas para atacar.', moves: ['Rajada da Varinha', 'Golens de Segurança', 'Grande Fumaça'] },
  { id: 'ladros', name: 'Ladros', title: 'General Brilhante', magic: 'Absorção e emissão', band: 38, zone: 'Mundo', style: 'Rajadas de alto impacto', danger: 'Absorve recursos e devolve pressão em linha.', strategy: 'Evite canalizações frontais; aproxime-se só após a emissão terminar.', moves: ['Absorção', 'Emissão', 'Laser de Um Milhão'] },
  { id: 'fana', name: 'Fana', title: 'Terceiro Olho · Ódio', magic: 'Fogo e Salamandra', band: 42, zone: 'Mundo', style: 'Pressão explosiva', danger: 'Chamas cobrem áreas grandes e castigam agrupamentos.', strategy: 'Espalhem-se, atravesse a zona segura e interrompa a cura quando aparecer.', moves: ['Sopro da Salamandra', 'Salamandra Desencadeada', 'Laevateinn de Chamas'] },
  { id: 'mars', name: 'Mars', title: 'General Brilhante', magic: 'Mineral', band: 44, zone: 'Mundo', style: 'Tanque blindado', danger: 'Armadura e avanços tornam trocas frontais desfavoráveis.', strategy: 'Ataque pelas laterais depois do avanço e não gaste tudo contra a defesa.', moves: ['Armadura de Nemeia', 'Titã Blindado', 'Laevateinn'] },
  { id: 'gravito_behemoth', name: 'Beemote de Gravito', title: 'Fera de região de magia forte', magic: 'Tempestade e rochas', band: 48, zone: 'Mundo', style: 'Fera de arena', danger: 'Pisão, atropelo e rochas alcançam o grupo inteiro.', strategy: 'Fique fora da linha de carga e volte apenas após o pisão.', moves: ['Atropelo', 'Terremoto de Gravito', 'Rochas Flutuantes'] },
  { id: 'rhya', name: 'Rhya', title: 'Terceiro Olho · Traição', magic: 'Imitação', band: 52, zone: 'Mundo', style: 'Adaptativo', danger: 'Alterna elementos e quebra a rotina da equipe.', strategy: 'Leia o elemento ativo, evite agrupar e guarde mobilidade para a cópia pesada.', moves: ['Dardo de Água', 'Sopro da Salamandra', 'Quinteto Elemental'] },
  { id: 'ratri', name: 'Ratri', title: 'Elfo Reencarnado', magic: 'Espacial', band: 56, zone: 'Mundo', style: 'Duelista móvel', danger: 'Cortes e saltos espaciais punem uma perseguição cega.', strategy: 'Use lock-on e espere o fim do salto antes de iniciar o combo.', moves: ['Corte Entalhado', 'Passo Espacial', 'Talhador de Tronos'] },
  { id: 'vetto', name: 'Vetto', title: 'Terceiro Olho · Desespero', magic: 'Besta', band: 58, zone: 'Mundo', style: 'Brutamontes', danger: 'Investidas e agarrões destroem quem fica no alcance.', strategy: 'Mantenha espaçamento, esquive da investida e castigue o fim dela.', moves: ['Garra de Urso', 'Investida do Guepardo', 'Agarrão Esmagador'] },
  { id: 'witch_queen', name: 'Rainha das Bruxas', title: 'Mãe de todas as bruxas', magic: 'Sangue', band: 64, zone: 'Mundo', style: 'Controle e cura', danger: 'Manipula o espaço e recupera vida se a fase não for pressionada.', strategy: 'Ataquem juntos na cura, mas separem-se quando a arena receber chuva de sangue.', moves: ['Cadafalso de Sangue', 'Fluxo de Sangue', 'Réquiem Carmesim'] },
  { id: 'gaderois_godroc', name: 'Gaderois Godroc', title: 'Discípulo Sombrio', magic: 'Pedra', band: 68, zone: 'Mundo', style: 'Colosso defensivo', danger: 'Armadura, pilares e desabamentos controlam a arena.', strategy: 'Não lute junto a paredes; após o desabamento, aproveite a recuperação.', moves: ['Manoplas de Pedra', 'Desabamento', 'Colosso de Pedra'] },
  { id: 'zagred', name: 'Zagred', title: 'Demônio de alto escalão', magic: 'Kotodama', band: 70, zone: 'Qliphoth', style: 'Caster de comandos', danger: 'Ordens e monstros forçam reações rápidas.', strategy: 'Observe o comando iniciado, atravesse a zona livre e limpe os monstros que bloqueiam a equipe.', moves: ['“Perfure”', 'Monstros do Submundo', 'Tridente'] },
  { id: 'megicula', name: 'Megicula', title: 'Demônio do mais alto escalão', magic: 'Maldição', band: 76, zone: 'Qliphoth', style: 'Debuff e desgaste', danger: 'Maldições acumulam pressão e explosões negam espaço.', strategy: 'Evite trocas longas, recue para reorganizar e interrompa a recuperação.', moves: ['Lanças de Sangue', 'Vida Explosiva', 'Mundo em Decomposição'] },
  { id: 'lilith', name: 'Lilith', title: 'Qliphoth · primeiro nível', magic: 'Gelo demoníaco', band: 82, zone: 'Qliphoth', style: 'Congelamento de arena', danger: 'Ondas e nevasca tiram rotas de fuga.', strategy: 'Lute em movimento circular e reserve dash para a onda de geada.', moves: ['Onda de Geada', 'Nevasca', 'Geada Absoluta'] },
  { id: 'naamah', name: 'Nahamah', title: 'Qliphoth · primeiro nível', magic: 'Fogo demoníaco', band: 82, zone: 'Qliphoth', style: 'Explosão de área', danger: 'Tornados e pilares de fogo punem agrupamentos.', strategy: 'Espalhem-se, entre apenas após a explosão e não fique na trilha do tornado.', moves: ['Onda de Fogo', 'Tornado de Fogo', 'Pilar do Fogo Infernal'] },
  { id: 'damnatio_kira', name: 'Damnatio Kira', title: 'Paladino de Lucius', magic: 'Balança e atmosfera', band: 88, zone: 'Mundo', style: 'Julgamento e rajada', danger: 'A balança reduz margem de erro e o ar corta áreas largas.', strategy: 'Não concentre o grupo na frente; faça dano nas janelas após a guarda angelical.', moves: ['Corte de Ar', 'Balança do Julgamento', 'Anjos da Guarda'] },
  { id: 'beelzebub', name: 'Belzebu', title: 'Soberano do Submundo', magic: 'Espacial', band: 90, zone: 'Qliphoth', style: 'Controle dimensional', danger: 'Portais e compressão reposicionam a luta.', strategy: 'Evite bordas, use lock-on e espere a ruptura espacial terminar.', moves: ['Rasgo Espacial', 'Portais do Vazio', 'Ruptura Abissal'] },
  { id: 'lucifero', name: 'Lucifero', title: 'Rei Demônio', magic: 'Gravidade', band: 97, zone: 'Qliphoth', style: 'Chefe final de pressão', danger: 'Gravidade, braços e distorções cobrem quase toda a arena.', strategy: 'Coordene janelas curtas de dano; sobreviver ao colapso vale mais que insistir no combo.', moves: ['Punho do Rei Demônio', 'Poço Gravitacional', 'Pressão Absoluta'] },
]

const selectedId = ref(bosses[0].id)
const zone = ref<'Todos' | Boss['zone']>('Todos')
const zones: Array<typeof zone.value> = ['Todos', 'Mundo', 'Qliphoth']
const visible = computed(() => bosses.filter(boss => zone.value === 'Todos' || boss.zone === zone.value))
const selected = computed(() => bosses.find(boss => boss.id === selectedId.value) ?? bosses[0])
function selectBoss(id: string) { selectedId.value = id }
</script>

<template>
  <section class="boss-roster">
    <p class="boss-lead">Escolha um chefe para abrir seu modelo 3D e preparar a luta. A força é uma referência de progressão, não uma garantia de vitória: mecânica, grupo e servidor alteram o resultado.</p>
    <div class="boss-filter" role="group" aria-label="Filtrar chefes por região">
      <button v-for="item in zones" :key="item" :aria-pressed="zone === item" @click="zone = item">{{ item }}</button>
    </div>
    <div class="boss-layout">
      <div class="boss-list" aria-label="Lista de chefes">
        <button v-for="boss in visible" :key="boss.id" class="boss-card" :class="{ selected: selectedId === boss.id }" @click="selectBoss(boss.id)">
          <span class="boss-band">Força {{ boss.band }}</span><strong>{{ boss.name }}</strong><small>{{ boss.style }}</small>
        </button>
      </div>
      <article class="boss-detail" :style="{ '--boss-accent': selected.zone === 'Qliphoth' ? '#b85cff' : '#d79b35' }">
        <ClientOnly><GeoViewer :geo="`/models/geo/boss/${selected.id}.geo.json`" :skins="[{ id: selected.id, label: selected.name, texture: `/models/textures/entity/boss/${selected.id}.png` }]" :height="390" /><template #fallback><p>Carregando modelo 3D…</p></template></ClientOnly>
        <p class="boss-kicker">{{ selected.zone }} · força {{ selected.band }}</p><h2>{{ selected.name }}</h2><p>{{ selected.title }} · {{ selected.magic }}</p>
        <dl><dt>Estilo de luta</dt><dd>{{ selected.style }}</dd><dt>Maior perigo</dt><dd>{{ selected.danger }}</dd><dt>Como responder</dt><dd>{{ selected.strategy }}</dd></dl>
        <p class="boss-moves"><strong>Golpes para reconhecer:</strong> {{ selected.moves.join(' · ') }}</p>
      </article>
    </div>
  </section>
</template>
