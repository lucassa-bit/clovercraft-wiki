# Noelle Silva

**Magia de Água** · Touros Negros

<ClientOnly>
<GeoViewer geo="/models/geo/character/noelle.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/noelle_base.png"}, {"id": "saint", "label": "Saint Valkyrie", "texture": "/models/textures/character/noelle_saint.png"}, {"id": "valkyrie", "label": "Valkyrie Dress", "texture": "/models/textures/character/noelle_valkyrie.png"}]' />
</ClientOnly>

Tanque/lanceira. Ninho do Dragão Marinho, Valkyrie Dress e forma santa.

- Grimório: **Grimório de Três Folhas dos Silva**
- A água responde à sua portadora real. Use para se tornar a Noelle.
- Formas: **Base** (`base`), **Valkyrie Dress** (`valkyrie`), **Saint Valkyrie** (`saint`)
- Vincular: use o grimório (mensagem `O grimório de três folhas escolheu você. Você é a Noelle Silva!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `waterball_barrage` | Rajada de Bolas d'Água | — | 26 |
| 2 | `sea_dragons_nest` | Ninho do Dragão Marinho | — | 26 |
| 3 | `sea_dragons_cradle` | Berço do Dragão Marinho | — | 28 |
| 4 | `mana_skin` | Pele de Mana | — | 24 |
| 5 | `sea_dragons_roar` | Rugido do Dragão Marinho | — | 40 |
### Valkyrie Dress

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `valkyrie/lance_drill` | Broca da Lança Valquíria | 7.5 | 30 |
| 2 | `valkyrie/point_blank_roar` | Rugido do Dragão Marinho à Queima-Roupa | 3.8 | 36 |
| 3 | `valkyrie/mermaid_form` | Forma Sereia | — | 26 |
| 4 | `valkyrie/true_magic_runes` | Magia Verdadeira: Gêiseres Rúnicos | — | 38 |
| 5 | `valkyrie/sea_dragon_god` | Vórtice e Cauda do Deus Dragão Marinho (Forma Dragão) | — | 52 |
### Saint Valkyrie

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `saint/water_sword_crescent` | Crescente da Espada d'Água | — | 22 |
| 2 | `saint/purifying_glow` | Brilho Purificador | 9.1 | 30 |
| 3 | `saint/undine_wing_strike` | Golpe das Asas de Undine | 13.7 | 26 |
| 4 | `saint/saint_aura` | Aura Santa | — | 24 |
| 5 | `saint/heart_piercing_lance` | Lança Perfura-Coração | 74.1 | 48 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Rajada de Bolas d'Água |
| Cavaleiro Mágico Júnior de 3ª Classe | Ninho do Dragão Marinho |
| Cavaleiro Mágico Júnior de 1ª Classe | Berço do Dragão Marinho |
| Cavaleiro Mágico Intermediário de 3ª Classe | Pele de Mana |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Rugido do Dragão Marinho, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Vestido Valquíria (lança, planar na água), Broca da Lança Valquíria |
| Vice-Capitão | Rugido do Dragão Marinho à Queima-Roupa, Forma Sereia |
| Capitão de Esquadrão | Magia Verdadeira: Gêiseres Rúnicos, Vórtice e Cauda do Deus Dragão Marinho (Forma Dragão) |
| Grão-Cavaleiro Mágico | Vestido Valquíria Santa (uma vez por vida), Crescente da Espada d'Água, Brilho Purificador, Golpe das Asas de Undine, Aura Santa, Lança Perfura-Coração |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Dragão Marinho (`sea_dragon`) | Caster | 1 | não |
| Undine (`undine`) | Support | 2 | sim |
| Nozel Silva (`nozel`) | Elite | 3 | sim |

## Quests da jornada

### noelle_valkyrie

> canon: Noelle's Sea Dragon's Nest training at the Raque beach with Asta and Kahono, then the Seabed Temple where her Sea Dragon's Roar answers Vetto (Underwater Temple arc); the Royal Knights' strike on the Gravito dungeon under Mereoleona; the elves' assault on Clover Castle, where Noelle, Nozel and the Silvas fight the elf Kivn and Noelle creates the Valkyrie Dress (Elf Reincarnation arc). The elf Kivn is not in the mod: an S-rank elite stands in (inv.); waves inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `vanessa` | talk | `black_bulls_hideout` | 30 | `—` | strength 850, merits 430 |
| `nest` | trial | `seabed_temple` | 36 | `—` | strength 5130, merits 2560, mastery 300 |
| `gifso` | talk | `seabed_temple` | 40 | `—` | strength 980, merits 490 |
| `vetto` | boss | `seabed_temple` | 44 | `vetto` | strength 4110, merits 2050, mastery 500 |
| `gravito` | goto | `gravito_zone` | 48 | `—` | strength 1610, merits 800 |
| `possessed` | trial | `gravito_zone` | 52 | `—` | strength 6130, merits 3060, mastery 300 |
| `nozel` | talk | `royal_capital` | 56 | `—` | strength 1150, merits 580 |
| `kivn` | boss | `royal_capital` | 60 | `foe:clovercraft:midnight_sun_mage@S/water` | strength 8360, merits 4180, mastery 500 |

### noelle_saint

> canon: the Heart Kingdom arc -- Undine and the Princess's underground chamber, Vanica's attack, six months of training under Lolopechka; the Spade raid -- Saint Stage with Undine against Vanica and Megicula, whose curse breaks Undine's link, and the heart Noelle destroys (Spade Kingdom Raid arc). Vanica is not in the mod: Megicula's boss stands for both; waves inv.

Requer: `noelle_valkyrie`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `heart` | goto | `heart_sanctuary` | 80 | `—` | strength 2060, merits 1030 |
| `undine` | talk | `heart_sanctuary` | 82 | `—` | strength 1390, merits 700 |
| `spring` | trial | `heart_sanctuary` | 84 | `—` | strength 7740, merits 3870, mastery 300 |
| `curse` | trial | `heart_sanctuary` | 86 | `—` | strength 7830, merits 3920, mastery 300 |
| `spade` | goto | `spade_fortress` | 88 | `—` | strength 2160, merits 1080 |
| `megicula` | boss | `spade_fortress` | 90 | `npc:vanica` | strength 10200, merits 5100, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
