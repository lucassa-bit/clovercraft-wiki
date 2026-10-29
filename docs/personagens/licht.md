# Licht

**Magia de Espada / Luz** · Elfos / Olho do Sol da Meia-Noite

<ClientOnly>
<GeoViewer geo="/models/geo/character/licht.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/licht_base.png"}, {"id": "awakened", "label": "Licht Desperto", "texture": "/models/textures/character/licht_awakened.png"}, {"id": "demon", "label": "Forma Demoníaca", "texture": "/models/textures/character/licht_demon.png"}]' />
</ClientOnly>

Espadachim élfico. Origin Flash, espadas invocadas e forma demoníaca de quatro braços.

- Grimório: **Grimório de Quatro Folhas de Licht**
- A Magia de Espada atende ao rei dos elfos. Use para se tornar Licht.
- Formas: **Base** (`base`), **Licht Desperto** (`awakened`), **Forma Demoníaca** (`demon`)
- Vincular: use o grimório (mensagem `O grimório de quatro folhas escolheu você. Você é Licht, rei dos elfos!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `leg_strength_boost` | Fortalecimento das Pernas | 7.0 | 26 |
| 2 | `dweller_absorption` | Espada Habitante Demoníaca: Absorção | — | 40 |
| 3 | `flying_slashes` | Cortes Voadores | — | 34 |
| 4 | `mana_levitation` | Levitação de Mana | — | 34 |
| 5 | `origin_flash` | Clarão da Origem | — | 44 |
### Licht Desperto

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `awakened/summoned_swords` | Espadas de Luz Invocadas | — | 30 |
| 2 | `awakened/mana_blast` | Explosão de Mana | — | 32 |
| 3 | `awakened/origin_flash_barrage` | Rajada do Clarão da Origem | — | 40 |
| 4 | `awakened/protecting_light` | Espada Habitante Demoníaca: Luz Protetora | — | 34 |
| 5 | `awakened/conquering_eon` | Éon Conquistador | — | 64 |
### Forma Demoníaca

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `demon/palm_beams` | Raios das Palmas | — | 28 |
| 2 | `demon/mana_wings` | Asas que Bebem Mana | — | 40 |
| 3 | `demon/capital_spell` | O Feitiço sobre a Capital | — | 40 |
| 4 | `demon/four_arm_crush` | Esmagamento dos Quatro Braços | 1.5 | 40 |
| 5 | `demon/charged_blast` | Rajada Carregada | — | 84 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Fortalecimento das Pernas |
| Cavaleiro Mágico Júnior de 3ª Classe | Espada Habitante Demoníaca: Absorção |
| Cavaleiro Mágico Júnior de 1ª Classe | Cortes Voadores |
| Cavaleiro Mágico Intermediário de 3ª Classe | Levitação de Mana |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Clarão da Origem, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Licht Desperto (voo em mana condensada), Espadas de Luz Invocadas, Explosão de Mana, Rajada do Clarão da Origem, Espada Habitante Demoníaca: Luz Protetora, Éon Conquistador |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | O Demônio (uma vez por vida), Raios das Palmas, Asas que Bebem Mana, O Feitiço sobre a Capital, Esmagamento dos Quatro Braços, Rajada Carregada |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Guerreiro Elfo (`elf`) | Soldier | 1 | não |
| Patolli (`patolli`) | Caster | 2 | sim |
| Rhya, o Desleal (`rhya`) | Elite | 3 | sim |

## Quests da jornada

### licht_awakened

> canon: the massacre of the elf tribe after Licht's wedding to Tetia; Patolli reincarnates the elves from the dungeon's magic stones; Licht, unresponsive, wakes at the sight of Klaus and Hamon falling, steals the Demon-Dweller Sword from Asta and faces Asta and Yuno (Elf Reincarnation arc). Grave-robber waves inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `ruins` | goto | `elf_ruins` | 30 | `—` | strength 1280, merits 640 |
| `robbers` | trial | `elf_ruins` | 36 | `—` | strength 5130, merits 2560, mastery 300 |
| `dungeon` | goto | `ancient_dungeon` | 42 | `—` | strength 1510, merits 750 |
| `patolli` | talk | `ancient_dungeon` | 46 | `—` | strength 1050, merits 520 |
| `kin` | trial | `ancient_dungeon` | 54 | `—` | strength 6240, merits 3120, mastery 300 |
| `asta` | boss | `ancient_dungeon` | 60 | `npc:asta` | strength 8360, merits 4180, mastery 500 |

### licht_demon

> canon: Zagred planned the elf massacre to corrupt Licht's grimoire and take his body; Licht turned demon and was slain by Lemiel; in the Shadow Palace, Secre unseals his soul, Licht draws on the underworld's Forbidden Magic and fights Zagred with Lemiel, Asta and Yuno (Elf Reincarnation arc). Waves and the hold trial inv.

Requer: `licht_awakened`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `wedding` | goto | `elf_ruins` | 80 | `—` | strength 2060, merits 1030 |
| `zagred` | talk | `elf_ruins` | 82 | `—` | strength 1390, merits 700 |
| `monsters` | trial | `shadow_altar` | 85 | `—` | strength 7790, merits 3890, mastery 300 |
| `lemiel` | talk | `shadow_altar` | 87 | `—` | strength 1430, merits 720 |
| `grimoire` | trial | `shadow_altar` | 89 | `—` | strength 7970, merits 3980, mastery 300 |
| `end` | boss | `shadow_altar` | 91 | `npc:julius` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
