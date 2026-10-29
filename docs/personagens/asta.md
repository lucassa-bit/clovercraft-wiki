# Asta

**Anti-Magia** · Touros Negros

<ClientOnly>
<GeoViewer geo="/models/geo/character/asta.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/asta_base.png"}, {"id": "ba1", "label": "Black Asta I", "texture": "/models/textures/character/asta_ba1.png"}, {"id": "ba2", "label": "Black Asta II", "texture": "/models/textures/character/asta_ba2.png"}, {"id": "ba3", "label": "Black Asta III", "texture": "/models/textures/character/asta_ba3.png"}, {"id": "du", "label": "Devil Union", "texture": "/models/textures/character/asta_du.png"}, {"id": "spade", "label": "Spade", "texture": "/models/textures/character/asta_spade.png"}]' />
</ClientOnly>

Duelista corpo-a-corpo. Cancela magia, troca entre quatro espadas demoníacas e escala com transformações.

- Grimório: **Grimório de Cinco Folhas**
- Um demônio habita aqui. Use para se tornar o Asta.
- Formas: **Base** (`base`), **Black Asta I** (`ba1`), **Black Asta II** (`ba2`), **Black Asta III** (`ba3`), **Devil Union** (`du`)
- Vincular: use o grimório (mensagem `O grimório de cinco folhas escolheu você. Você é o Asta!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `slayer_slash` | Investida do Touro de Um Chifre | 11.5 | 26 |
| 2 | `meteorite` | Investida do Touro | 12.0 | 34 |
| 3 | `dweller_slash` | Espada Habitante-Demônio: Corte Negro | 8.0 | 24 |
| 4 | `causality_break` | Quebra de Causalidade | — | 32 |
### Black Asta I

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `ba/black_slash` | Black Slash | 4.0 | 30 |
| 2 | `ba/black_hurricane` | Black Hurricane | 10.0 | 40 |
| 3 | `ba/bull_thrust` | Bull Thrust | 12.0 | 28 |
| 4 | `ba/black_meteorite` | Black Meteorite | 14.0 | 40 |
### Devil Union

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `du/zetten` | Zetten | 26.0 | 30 |
| 2 | `du/infinite_slash` | Infinite Slash | 12.0 | 38 |
| 3 | `du/comrademons` | Comrademons | — | 34 |
| 4 | `du/demon_destroyer` | Devil Union: Espada Destruidora de Demônios | — | 36 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Investida do Touro de Um Chifre |
| Cavaleiro Mágico Júnior de 3ª Classe | Voo na espada (Black Asta) |
| Cavaleiro Mágico Júnior de 1ª Classe | Espada Habitante-Demônio, Espada Habitante-Demônio: Corte Negro |
| Cavaleiro Mágico Intermediário de 3ª Classe | Investida do Touro |
| Cavaleiro Mágico Intermediário de 1ª Classe | Espada Destruidora-Demônio, Quebra de Causalidade |
| Cavaleiro Mágico Sênior de 3ª Classe | Espada Rasga-Demônios, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Black Asta, Divisor Negro |
| Vice-Capitão | — |
| Capitão de Esquadrão | União Demoníaca, Supremo da União Demoníaca |
| Grão-Cavaleiro Mágico | — |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |


## Espadas demoníacas

Asta troca quatro armas (`swap`). Cada uma muda o combo, o dash slash e skills ligadas:

| Espada | Item | Notas |
| --- | --- | --- |
| Demon-Slayer | `slayer_sword` | Kit inicial. One-Horn / Bull Thrust |
| Demon-Dweller | `dweller_sword` | Absorve e devolve magia — Black Slash |
| Demon-Destroyer | `destroyer_sword` | Causality Break (campo que anula magia) |
| Demon-Slasher | `slasher_sword` | Katana. Black Divider, 5º hit no combo |

Guard de Asta é **anti-magia**: selo no oponente em vez de escudo de mana.


## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Liebe (`liebe`) | Elite | 1 | sim |
| Nero (`nero`) | Support | 2 | sim |

## Quests da jornada

### asta_black

> canon: after the Seabed Temple Asta's arms are shattered and Owen cannot heal them; the Black Bulls take him to the Witch Queen; Fana's Salamander, Mars's and Ladros's armies, Ladros's betrayal where the black form first rises, and the Queen's Puppet Bloodflow; Mereoleona's volcano taught him to control it afterwards (train_volcano). Wave contents inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `owen` | talk | `royal_capital` | 30 | `—` | strength 850, merits 430 |
| `vanessa` | talk | `black_bulls_hideout` | 35 | `—` | strength 920, merits 460 |
| `forest` | goto | `witches_forest` | 40 | `—` | strength 1470, merits 740 |
| `salamander` | boss | `witches_forest` | 46 | `fana` | strength 4200, merits 2100, mastery 500 |
| `armies` | trial | `witches_forest` | 52 | `—` | strength 6130, merits 3060, mastery 300 |
| `ladros` | boss | `witches_forest` | 57 | `ladros` | strength 4660, merits 2330, mastery 500 |
| `queen` | boss | `witches_forest` | 62 | `witch_queen` | strength 8490, merits 4250, mastery 500 |

### asta_union

> canon: Asta and Yami's fight with Dante at the Black Bulls' base, where Asta bargains his arm with Liebe and loses; Nacht takes him to House Faust's secret chamber: the devil-binding ritual, Liebe's duel, the contract of equals and Nacht's Unite Mode: Canis challenge; Asta's first united form cuts Nahamah's hand in the Spade raid. Waves inv.

Requer: `asta_black`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `dante` | boss | `black_bulls_hideout` | 66 | `npc:dante` | strength 5000, merits 2500, mastery 500 |
| `meeting` | talk | `royal_capital` | 69 | `—` | strength 1280, merits 640 |
| `estate` | goto | `faust_estate` | 72 | `—` | strength 1960, merits 980 |
| `circle` | talk | `faust_estate` | 74 | `—` | strength 1320, merits 660 |
| `liebe` | trial | `faust_estate` | 76 | `—` | strength 7370, merits 3690, mastery 300 |
| `canis` | trial | `faust_estate` | 79 | `—` | strength 7510, merits 3760, mastery 300 |
| `twins` | boss | `spade_fortress` | 82 | `npc:vanica` | strength 9740, merits 4870, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
