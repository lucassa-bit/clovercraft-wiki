# Nacht Faust

**Magia das Sombras** · Touros Negros (vice-capitão)

<ClientOnly>
<GeoViewer geo="/models/geo/character/nacht.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/nacht_base.png"}, {"id": "canis", "label": "Unite: Canis", "texture": "/models/textures/character/nacht_canis.png"}, {"id": "fourfold", "label": "Unite: Equinox", "texture": "/models/textures/character/nacht_fourfold.png"}]' />
</ClientOnly>

Assassino de sombras. Devils Canis/Equinox, Hunting Ground e teleporte por sombra.

- Grimório: **Grimório de Quatro Folhas Faust**
- A sombra responde ao Vice-Capitão dos Touros Negros. Use para virar Nacht Faust.
- Formas: **Base** (`base`), **Unite: Canis** (`canis`), **Unite: Equinox** (`fourfold`)
- Vincular: use o grimório (mensagem `O grimório de quatro folhas te escolheu. Você é Nacht Faust!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `shadow_bind` | Prisão das Sombras | — | 30 |
| 2 | `shadow_hands` | Mãos das Sombras | — | 36 |
| 3 | `shadow_corridor` | Corredor das Sombras | — | 34 |
| 4 | `shadow_dive` | Mergulho na Sombra | — | 36 |
| 5 | `dark_garden` | Magia das Sombras: Convite ao Jardim Sombrio | — | 46 |
### Unite: Canis

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `canis/pack` | Matilha de Cães das Sombras | — | 34 |
| 2 | `canis/pack_ambush` | Emboscada da Matilha | — | 34 |
| 3 | `canis/pack_decoy` | Isca da Matilha | — | 32 |
| 4 | `canis/pack_encirclement` | Cerco da Matilha | — | 40 |
| 5 | `canis/hunting_ground` | Território de Caça (uma cúpula de trevas) | — | 44 |
### Unite: Equinox

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `fourfold/crow` | Asas do Corvo | — | 34 |
| 2 | `fourfold/dog_heads` | Cabeças de Cão | — | 38 |
| 3 | `fourfold/agility` | Agilidade do Gato | 11.2 | 34 |
| 4 | `fourfold/monument` | Monumento das Sombras | — | 42 |
| 5 | `fourfold/shadow_blade` | Lâmina Sombria dos Quatro Demônios | 27.9 | 40 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Prisão das Sombras |
| Cavaleiro Mágico Júnior de 3ª Classe | Mãos das Sombras |
| Cavaleiro Mágico Júnior de 1ª Classe | Corredor das Sombras |
| Cavaleiro Mágico Intermediário de 3ª Classe | Mergulho na Sombra |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Magia das Sombras: Convite ao Jardim Sombrio, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Modo União: Canis, Matilha de Cães das Sombras, Emboscada da Matilha, Isca da Matilha, Cerco da Matilha, Território de Caça (uma cúpula de trevas) |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Modo União: os quatro demônios, Asas do Corvo, Cabeças de Cão, Agilidade do Gato, Monumento das Sombras, Lâmina Sombria dos Quatro Demônios |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Gimodelo (`gimodelo`) | Bruiser | 1 | sim |
| Plumede (`plumede`) | Skirmisher | 2 | sim |
| Slotos (`slotos`) | Tank | 3 | sim |
| Walgner (`walgner`) | Support | 4 | sim |

## Quests da jornada

### nacht_canis

> canon: Nacht and Morgen, the four devils bound in House Faust's underground chamber (Gimodelo, Slotos, Plumede, Walgner), Morgen's death and Yami's vice-captain promise at the grave; Nacht spying in Spade, pulling a Dark Disciple into his shadow; then Unite Mode: Canis with Gimodelo as the next stage of Asta and Liebe's training (Spade Kingdom Raid arc). Trial waves inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `grave` | talk | `black_bulls_hideout` | 30 | `—` | strength 850, merits 430 |
| `spy` | goto | `spade_fortress` | 36 | `—` | strength 1400, merits 700 |
| `unseen` | trial | `spade_fortress` | 42 | `—` | strength 5520, merits 2760, mastery 300 |
| `estate` | goto | `faust_estate` | 48 | `—` | strength 1610, merits 800 |
| `gimodelo` | talk | `faust_estate` | 52 | `—` | strength 1110, merits 560 |
| `bind` | trial | `faust_estate` | 56 | `—` | strength 6350, merits 3180, mastery 300 |
| `asta` | boss | `faust_estate` | 60 | `npc:asta` | strength 8360, merits 4180, mastery 500 |

### nacht_fourfold

> canon: the captains' meeting and Julius's vouching; the Spade raid -- Nacht in Unite Mode: Equus against Dante's gravity with Jack's Slash Magic; the first gate opens, Nahamah and Lilith appear, Nacht merges with Walgner and then with Plumede to cast Monument of Atonement and seal himself with them (Spade Kingdom Raid arc). Waves inv.

Requer: `nacht_canis`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `meeting` | talk | `royal_capital` | 80 | `—` | strength 1370, merits 690 |
| `gate` | goto | `spade_fortress` | 83 | `—` | strength 2100, merits 1050 |
| `equus` | trial | `spade_fortress` | 85 | `—` | strength 7790, merits 3890, mastery 300 |
| `dante` | boss | `spade_fortress` | 87 | `npc:dante` | strength 5730, merits 2870, mastery 500 |
| `twins` | boss | `spade_fortress` | 91 | `npc:vanica` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
