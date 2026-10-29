# Mimosa Vermillion

**Magia de Plantas** · Alvorecer Dourado

<ClientOnly>
<GeoViewer geo="/models/geo/character/mimosa.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/mimosa_base.png"}, {"id": "robe", "label": "Magic Robe", "texture": "/models/textures/character/mimosa_robe.png"}, {"id": "utopia", "label": "Flower Princess Utopia", "texture": "/models/textures/character/mimosa_utopia.png"}]' />
</ClientOnly>

Suporte/curandeira. Cestas de cura, canhões florais e Flower Princess Utopia.

- Grimório: **Grimório da Mimosa**
- Magia de Plantas e Magia de Criação: vinhas, flores, cura e um canhão de flor. Use para se tornar Mimosa Vermillion.
- Formas: **Base** (`base`), **Magic Robe** (`robe`), **Flower Princess Utopia** (`utopia`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Mimosa Vermillion, da Aurora Dourada!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `flower_on_the_roadside` | Flor à Beira do Caminho | — | 26 |
| 2 | `control_magic_grass` | Grama de Controle Mágico | — | 28 |
| 3 | `magic_flower_guidepost` | Placa-Guia de Flor Mágica | — | 30 |
| 4 | `dream_healing_flower_basket` | Cesto de Flores Curativo dos Sonhos | — | 56 |
| 5 | `magic_cannon_flower` | Flor-Canhão Mágica | — | 54 |
### Magic Robe

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `robe/flower_cannons` | Flores-Canhão da Magia Verdadeira | — | 34 |
| 2 | `robe/magic_pollen` | Pólen Mágico | — | 30 |
| 3 | `robe/briar_barrage` | Barragem de Espinhos | — | 28 |
| 4 | `robe/mana_pour` | Derrame de Mana do Reino Heart | — | 40 |
| 5 | `robe/banishing_bloom` | Magia Verdadeira: Flor Banidora de Demônios | — | 50 |
### Flower Princess Utopia

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `utopia/flower_paradise` | Paraíso de Flores Cura-Princesa | — | 44 |
| 2 | `utopia/array_spire` | Grande Torre de Círculo | — | 32 |
| 3 | `utopia/borrowed_mana` | Mana Natural Emprestado | — | 26 |
| 4 | `utopia/flower_of_truth` | Flor da Verdade | — | 30 |
| 5 | `utopia/flower_princess_utopia` | Utopia da Princesa das Flores | — | 96 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Flor à Beira do Caminho |
| Cavaleiro Mágico Júnior de 3ª Classe | Grama de Controle Mágico |
| Cavaleiro Mágico Júnior de 1ª Classe | Placa-Guia de Flor Mágica |
| Cavaleiro Mágico Intermediário de 3ª Classe | Cesto de Flores Curativo dos Sonhos |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Flor-Canhão Mágica, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Veste de Flores Cura-Princesa (asas de pétalas, magia verdadeira de plantas), Flores-Canhão da Magia Verdadeira, Pólen Mágico, Barragem de Espinhos, Derrame de Mana do Reino Heart, Magia Verdadeira: Flor Banidora de Demônios |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Princesa das Flores (medidor 70), Paraíso de Flores Cura-Princesa, Grande Torre de Círculo, Mana Natural Emprestado, Flor da Verdade, Utopia da Princesa das Flores |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Flor Canhão Mágica (`cannon_flower`) | Caster | 1 | não |
| Flor Curativa (`healing_flower`) | Support | 2 | sim |
| Klaus Lunettes (`klaus`) | Tank | 3 | sim |

## Quests da jornada

### mimosa_robe

> canon: Mimosa trained in the Heart Kingdom, where Gadjah rated her improvement Third Stage, and mastered the Mana Method that extends her healing and raises her offence (True Plant Magic, wiki Mimosa Vermillion and Plant Magic); the Princess-Healing Flower Robe is the dress of vines and flowers she heals Noelle's wounds in; the Heart Kingdom raid is the one Luck's chain fights (Svenkin Gatard, Vanica's Dark Disciples). The talk lines, the trial's staging and the place of the healing inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `gadjah` | talk | `heart_sanctuary` | 28 | `—` | strength 830, merits 410 |
| `method` | trial | `heart_sanctuary` | 34 | `—` | strength 4990, merits 2490, mastery 300 |
| `noelle` | talk | `black_bulls_hideout` | 40 | `—` | strength 980, merits 490 |
| `garden` | trial | `heart_sanctuary` | 46 | `—` | strength 5770, merits 2890, mastery 300 |
| `svenkin` | boss | `heart_sanctuary` | 52 | `foe:clovercraft:dark_disciple@S` | strength 7800, merits 3900, mastery 500 |

### mimosa_utopia

> canon: after training under Dryad Mimosa learned the elves' Ultimate Magic, which fully embodies her magic and, because she has less magic than the elves, borrows natural mana to make up the lack (wiki Mimosa Vermillion; Flower Princess Utopia is her Ultimate Magic spell, ch. 265, ep. 169 and ch. 283-284 for Patolli and Dryad as in Luck's chain). The array trial and the Spade gate's stand-in foe and the talk beats inv.

Requer: `mimosa_robe`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `patolli` | talk | `elf_ruins` | 80 | `—` | strength 1370, merits 690 |
| `dryad` | talk | `heart_sanctuary` | 84 | `—` | strength 1410, merits 700 |
| `array` | trial | `heart_sanctuary` | 88 | `—` | strength 7920, merits 3960, mastery 300 |
| `utopia` | boss | `spade_fortress` | 91 | `foe:clovercraft:spade_soldier@A` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
