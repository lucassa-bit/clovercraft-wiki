# Yami Sukehiro

**Magia das Trevas** · Touros Negros (capitão)

<ClientOnly>
<GeoViewer geo="/models/geo/character/yami.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/yami_base.png"}, {"id": "kikongan", "label": "Kikongan", "texture": "/models/textures/character/yami_kikongan.png"}, {"id": "manazone", "label": "Mana Zone", "texture": "/models/textures/character/yami_manazone.png"}]' />
</ClientOnly>

Espadachim de trevas. Dimension Slash, Black Moon e o modo único Kikongan.

- Grimório: **Grimório de Três Folhas**
- A escuridão responde a quem o carrega. Use para se tornar o Yami.
- Formas: **Base** (`base`), **Mana Zone** (`manazone`), **Kikongan** (`kikongan`)
- Vincular: use o grimório (mensagem `O grimório de três folhas escolheu você. Você é o Yami Sukehiro!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `dark_binding` | Amarra das Trevas | — | 28 |
| 2 | `black_hole` | Buraco Negro | — | 30 |
| 3 | `avidya_slash` | Envolto em Trevas: Corte Avidya | — | 30 |
| 4 | `black_cocoon` | Casulo Negro | — | 26 |
| 5 | `dimension_slash` | Envolto em Trevas: Corte Dimensional | — | 36 |
### Mana Zone

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `manazone/black_moon` | Lua Negra | — | 36 |
| 2 | `manazone/avidya_blunt_strike` | Golpe Contundente Avidya | 19.1 | 28 |
| 3 | `manazone/death_thrust` | Estocada Mortal | 9.8 | 40 |
| 4 | `manazone/blunt_sweep` | Varredura Contundente da Lâmina Negra | 25.4 | 26 |
| 5 | `manazone/equinox` | Corte Dimensional: Equinócio | — | 66 |
### Kikongan

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `kikongan/avidya_wild_slash` | Corte Selvagem Avidya Envolto em Trevas | 5.8 | 42 |
| 2 | `kikongan/kijin_leap` | Salto Kijin | 14.9 | 26 |
| 3 | `kikongan/deep_black_blade` | Lâmina Negra Profunda | 29.9 | 30 |
| 4 | `kikongan/kijin_regeneration` | Regeneração Kijin | — | 32 |
| 5 | `kikongan/dark_light_slash` | Corte Trevas x Luz | 29.9 | 56 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Amarra das Trevas |
| Cavaleiro Mágico Júnior de 3ª Classe | Buraco Negro |
| Cavaleiro Mágico Júnior de 1ª Classe | Envolto em Trevas: Corte Avidya |
| Cavaleiro Mágico Intermediário de 3ª Classe | Casulo Negro |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Envolto em Trevas: Corte Dimensional, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Mana Zone (voo, postura Iai na guarda), Lua Negra, Golpe Contundente Avidya, Estocada Mortal, Varredura Contundente da Lâmina Negra, Corte Dimensional: Equinócio |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Kikongan (uma vez por vida), Corte Selvagem Avidya Envolto em Trevas, Salto Kijin, Lâmina Negra Profunda, Regeneração Kijin, Corte Trevas x Luz |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Magna Swing (`magna`) | Bruiser | 1 | sim |
| Luck Voltia (`luck`) | Skirmisher | 2 | sim |
| Gordon Agrippa (`gordon`) | Support | 3 | sim |
| Grey (`grey`) | Bruiser | 4 | sim |

## Quests da jornada

### yami_manazone

> canon: Julius gives the Black Bulls the Seabed Temple mission; Gifso's game, the Midnight Sun's spatial barrier, and Yami's Dark Cloaked Dimension Slash through Vetto's mana cloud; Yami's Mana Zone plus Ki-sensing is his base technique on the Mana Zone page. The mapping of the form to this fight is inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `julius` | talk | `royal_capital` | 30 | `—` | strength 850, merits 430 |
| `temple` | goto | `seabed_temple` | 38 | `—` | strength 1440, merits 720 |
| `crash` | trial | `seabed_temple` | 44 | `—` | strength 5650, merits 2820, mastery 300 |
| `barrier` | trial | `seabed_temple` | 50 | `—` | strength 6010, merits 3000, mastery 300 |
| `noelle` | talk | `seabed_temple` | 54 | `—` | strength 1130, merits 570 |
| `vetto` | boss | `seabed_temple` | 58 | `vetto` | strength 8220, merits 4110, mastery 500 |

### yami_kikongan

> canon: Judgment Day at the capital: Ryuya's Kikongan pill delivered by Ichika; Yami, wounded by Morgen Faust, takes the clan's drug and is the first to control it; Nacht comes to his aid against Morgen, revived as Lucius's Paladin. The Paladin is not in the mod: an S-rank elite stands in (inv.); waves inv.

Requer: `yami_manazone`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `ichika` | talk | `royal_capital` | 84 | `—` | strength 1410, merits 700 |
| `angels` | trial | `royal_capital` | 86 | `—` | strength 7830, merits 3920, mastery 300 |
| `moon` | trial | `royal_capital` | 88 | `—` | strength 7920, merits 3960, mastery 300 |
| `nacht` | talk | `royal_capital` | 89 | `—` | strength 1450, merits 720 |
| `morgen` | boss | `royal_capital` | 91 | `foe:clovercraft:paladin@S` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
