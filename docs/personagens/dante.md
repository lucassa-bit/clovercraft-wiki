# Dante Zogratis

**Magia Corporal / Gravidade** · Tríade das Trevas (Spade)

<ClientOnly>
<GeoViewer geo="/models/geo/character/dante.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/dante_base.png"}, {"id": "devil", "label": "Manifestação Demoníaca", "texture": "/models/textures/character/dante_devil.png"}, {"id": "lucifero", "label": "Lucifero (50%)", "texture": "/models/textures/character/dante_lucifero.png"}]' />
</ClientOnly>

Bruiser de gravidade. Regeneração, Presence e singularidade de Lucifero.

- Grimório: **Grimório de Ardósia de Dante**
- A Magia Corporal e a gravidade de Lucifero respondem à Tríade Sombria. Use para se tornar Dante Zogratis.
- Formas: **Base** (`base`), **Lucifero (50%)** (`lucifero`), **Manifestação Demoníaca** (`devil`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Dante Zogratis, da Tríade Sombria!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `flesh_grapple` | Agarrão de Carne | — | 32 |
| 2 | `presence` | Presença do Rei Demônio | — | 30 |
| 3 | `uprooted_hurl` | Arremesso Desenraizado | — | 30 |
| 4 | `regeneration` | Magia Corporal: Regeneração | — | 30 |
| 5 | `hideout_lift` | Erguer a Base | — | 70 |
### Lucifero (50%)

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `lucifero/distortion_step` | Passo de Distorção | — | 22 |
| 2 | `lucifero/levitation_lift` | Levitação | — | 32 |
| 3 | `lucifero/pressure_craft` | Criação de Pressão do Deus Maligno | — | 34 |
| 4 | `lucifero/gravity_repulse` | Distorção Espacial | — | 24 |
| 5 | `lucifero/heavy_infighting` | Combate Pesado | 6.6 | 72 |
### Manifestação Demoníaca

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `devil/wing_dive` | Mergulho das Asas Demoníacas | — | 26 |
| 2 | `devil/many_arms` | Gladiador de Muitos Braços | — | 30 |
| 3 | `devil/crushing_descent` | Descida Esmagadora | — | 36 |
| 4 | `devil/bent_space` | Armadura de Espaço Curvado | — | 26 |
| 5 | `devil/gravity_singularity` | Singularidade Gravitacional | — | 80 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Agarrão de Carne |
| Cavaleiro Mágico Júnior de 3ª Classe | Presença do Rei Demônio |
| Cavaleiro Mágico Júnior de 1ª Classe | Arremesso Desenraizado |
| Cavaleiro Mágico Intermediário de 3ª Classe | Magia Corporal: Regeneração |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Erguer a Base, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Lucifero 60% (gravidade, asas, o sabre de pedra), Passo de Distorção, Levitação, Criação de Pressão do Deus Maligno, Distorção Espacial, Combate Pesado |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Lucifero 100% (medidor 70), Mergulho das Asas Demoníacas, Gladiador de Muitos Braços, Descida Esmagadora, Armadura de Espaço Curvado, Singularidade Gravitacional |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Demônio de Baixo Escalão (`low_devil`) | Bruiser | 1 | não |
| Demônio de Médio Escalão (`mid_devil`) | Skirmisher | 2 | sim |
| Colosso de Carne (`flesh_colossus`) | Tank | 3 | sim |

## Quests da jornada

### dante_lucifero

> canon: Dante Zogratis, leader of the Dark Triad, hosts Lucifero, the strongest devil of the underworld (ch. 243); he fought the Black Bulls at 50 % then 60 % of Lucifero's power -- Asta first, then Yami (ch. 242-246, ep. 162-164) -- and asked his devil about Asta's mid-battle (ch. 242); the human-form levitation of the Black Bulls' base is Lucifero's lent gravity (ch. 240). The voice calling him, the Shadow Palace ruins as the meeting place and the duel/boss staging inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `voice` | talk | `here` | 30 | `—` | strength 850, merits 430 |
| `ruins` | goto | `shadow_altar` | 38 | `—` | strength 1440, merits 720 |
| `pact` | talk | `shadow_altar` | 44 | `—` | strength 1030, merits 510 |
| `asta` | trial | `shadow_altar` | 50 | `—` | strength 6010, merits 3000, mastery 300 |
| `yami` | boss | `shadow_altar` | 58 | `npc:yami` | strength 8220, merits 4110, mastery 500 |

### dante_devil

> canon: Dante can draw up to 80 % of Lucifero (ch. 256: tail, second pair of wings) until the first gate to the underworld opens, then 100 % (ch. 280); the Dark Triad needed Yami as the key (ch. 244-246) and Dante bent his Dimension Slash at 80 % (ch. 256); he held the Qliphoth Advent Ritual's circle in the Spade castle when Nacht and Jack attacked him, and Lilith and Nahamah came out of the opened gate (ch. 275-280). The devils testing the host at the circle, the talks and the Nacht boss (Jack is not in the mod) inv.

Requer: `dante_lucifero`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `demand` | talk | `spade_fortress` | 80 | `—` | strength 1370, merits 690 |
| `key` | trial | `spade_fortress` | 84 | `—` | strength 7740, merits 3870, mastery 300 |
| `ritual` | trial | `spade_fortress` | 87 | `—` | strength 7880, merits 3940, mastery 300 |
| `hundred` | talk | `spade_fortress` | 89 | `—` | strength 1450, merits 720 |
| `nacht` | boss | `spade_fortress` | 91 | `npc:nacht` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
