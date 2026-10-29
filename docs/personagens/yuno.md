# Yuno

**Magia de Vento** · Alvorecer Dourado

<ClientOnly>
<GeoViewer geo="/models/geo/character/yuno.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/yuno_base.png"}, {"id": "dive", "label": "Spirit Dive", "texture": "/models/textures/character/yuno_dive.png"}, {"id": "zephyr", "label": "Complete Spirit Dive", "texture": "/models/textures/character/yuno_zephyr.png"}]' />
</ClientOnly>

Mago aéreo. Lâminas de vento, tornados e o espírito Sylph (Bell).

- Grimório: **Grimório de Quatro Folhas**
- O vento responde a quem o carrega. Use para se tornar o Yuno.
- Formas: **Base** (`base`), **Spirit Dive** (`dive`), **Complete Spirit Dive** (`zephyr`)
- Vincular: use o grimório (mensagem `O grimório de quatro folhas escolheu você. Você é o Yuno!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `wind_blade_shower` | Chuva de Lâminas de Vento | — | 30 |
| 2 | `tornado_fang` | Presa do Tornado | — | 32 |
| 3 | `towering_tornado` | Tornado Colossal | — | 34 |
| 4 | `sylphs_breath` | Sopro da Sílfide | — | 30 |
| 5 | `spirit_storm` | Tempestade Espiritual | — | 40 |
### Spirit Dive

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `dive/crescent_kamaitachi` | Crescent Kamaitachi | — | 26 |
| 2 | `dive/swift_white_hawk` | Swift White Hawk | — | 34 |
| 3 | `dive/gale_white_bow` | Gale White Bow | — | 36 |
| 4 | `dive/spirits_hushed_dance` | Spirits Hushed Dance | — | 24 |
| 5 | `dive/spirit_of_boreas` | Spirit Of Boreas | — | 42 |
### Complete Spirit Dive

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `zephyr/conjunction` | Conjunction | 12.0 | 28 |
| 2 | `zephyr/quartile_hasta` | Quartile Hasta | — | 32 |
| 3 | `zephyr/quartile_flagellum` | Quartile Flagellum | — | 32 |
| 4 | `zephyr/quartile_scutum` | Quartile Scutum | — | 26 |
| 5 | `zephyr/never_never_land` | Never-Never Land (Terra do Nunca) | — | 60 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Chuva de Lâminas de Vento |
| Cavaleiro Mágico Júnior de 3ª Classe | Voo do vento |
| Cavaleiro Mágico Júnior de 1ª Classe | Presa do Tornado |
| Cavaleiro Mágico Intermediário de 3ª Classe | Tornado Colossal |
| Cavaleiro Mágico Intermediário de 1ª Classe | Bell, a Espírito do Vento |
| Cavaleiro Mágico Sênior de 3ª Classe | Sopro da Sílfide, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Mergulho Espiritual |
| Vice-Capitão | Tempestade Espiritual |
| Capitão de Esquadrão | Spirit Dive Completo + Espírito de Zéfiro (espada de vento) |
| Grão-Cavaleiro Mágico | Never-Never Land (Terra do Nunca) |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Bell (`bell`) | Caster | 1 | sim |
| Cavaleiro da Aurora Dourada (`golden_dawn`) | Soldier | 2 | não |

## Quests da jornada

### yuno_dive

> canon: Yuno found Sylph's scroll in the dungeon's treasure room and she saved Asta from Mars; the Star Awards; Mereoleona's Ultime-Volcano training; Spirit Dive, Mana Zone plus Mana Skin, debuts in the Royal Knights Selection final against Rill. Waves and the Rill stand-in inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `dungeon` | goto | `ancient_dungeon` | 30 | `—` | strength 1280, merits 640 |
| `mars` | boss | `ancient_dungeon` | 34 | `mars` | strength 3630, merits 1810, mastery 500 |
| `stars` | talk | `royal_capital` | 40 | `—` | strength 980, merits 490 |
| `volcano` | goto | `volcano_camp` | 44 | `—` | strength 1540, merits 770 |
| `lava` | trial | `volcano_camp` | 49 | `—` | strength 5950, merits 2980, mastery 300 |
| `dive` | trial | `volcano_camp` | 54 | `—` | strength 6240, merits 3120, mastery 300 |
| `exam` | trial | `exam_colosseum` | 58 | `—` | strength 6460, merits 3230, mastery 300 |
| `rill` | boss | `exam_colosseum` | 62 | `foe:clovercraft:diamond_mage@S/water` | strength 8490, merits 4250, mastery 500 |

### yuno_zephyr

> canon: Zenon's raid on the Golden Dawn base, Yuno impaled at 55 %; six months of training and Langris's help against Spatial Magic; Ralph's Resistance and the Spade grimoire found in a Grimoire Tower in the Spade raid; Yuno and Langris against Zenon at 80 % and 100 %. Wave contents inv.

Requer: `yuno_dive`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `raid` | trial | `royal_capital` | 68 | `—` | strength 6980, merits 3490, mastery 300 |
| `langris` | talk | `royal_capital` | 71 | `—` | strength 1300, merits 650 |
| `training` | trial | `training_ring` | 74 | `—` | strength 7280, merits 3640, mastery 300 |
| `fortress` | goto | `spade_fortress` | 77 | `—` | strength 2020, merits 1010 |
| `grimoire` | talk | `spade_fortress` | 79 | `—` | strength 1370, merits 680 |
| `stars` | trial | `spade_fortress` | 80 | `—` | strength 7560, merits 3780, mastery 300 |
| `zenon` | boss | `spade_fortress` | 82 | `npc:zenon` | strength 9740, merits 4870, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
