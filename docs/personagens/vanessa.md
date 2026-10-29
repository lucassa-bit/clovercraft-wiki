# Vanessa Enoteca

**Magia de Fios** · Touros Negros

<ClientOnly>
<GeoViewer geo="/models/geo/character/vanessa.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/vanessa_base.png"}, {"id": "fate", "label": "Red Thread of Fate", "texture": "/models/textures/character/vanessa_fate.png"}, {"id": "loom", "label": "Fate&#39;s Loom", "texture": "/models/textures/character/vanessa_loom.png"}]' />
</ClientOnly>

Suporte de destino. Red Thread of Fate, bonecas e tear do destino.

- Grimório: **Grimório da Vanessa**
- Magia de Fios: chicotes de linha, fios de marionete, teias, casulos e o Fio Vermelho do Destino. Use para se tornar Vanessa Enoteca.
- Formas: **Base** (`base`), **Red Thread of Fate** (`fate`), **Fate's Loom** (`loom`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Vanessa Enoteca, dos Touros Negros!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `arachnes_web` | Teia de Aracne | — | 30 |
| 2 | `dancing_doll` | Boneca Dançante | — | 30 |
| 3 | `thread_mend` | Remendo de Linha | — | 56 |
| 4 | `thread_swing` | Balanço de Linha | — | 30 |
| 5 | `thread_cocoon` | Casulo de Linha | — | 62 |
### Red Thread of Fate

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `fate/red_thread_of_fate` | Fio Vermelho do Destino: a proteção | — | 40 |
| 2 | `fate/fate_reversal` | Reversão do Destino | — | 28 |
| 3 | `fate/fate_weave_mend` | Remendo Tecido do Destino | — | 44 |
| 4 | `fate/cat_step` | Passo do Gato | — | 26 |
| 5 | `fate/fate_rewrite` | Reescrita do Destino | — | 52 |
### Fate's Loom

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `loom/thread_lattice` | Campo de Treliça de Linha | — | 44 |
| 2 | `loom/puppet_clash` | Choque de Marionetes | — | 34 |
| 3 | `loom/fate_shelter` | Abrigo do Destino | — | 36 |
| 4 | `loom/fate_dodge` | Esquiva do Destino | — | 30 |
| 5 | `loom/fates_loom` | Tear do Destino: a onda | — | 74 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Teia de Aracne |
| Cavaleiro Mágico Júnior de 3ª Classe | Boneca Dançante |
| Cavaleiro Mágico Júnior de 1ª Classe | Remendo de Linha |
| Cavaleiro Mágico Intermediário de 3ª Classe | Balanço de Linha |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Casulo de Linha, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Fio Vermelho do Destino (um gato de linha vermelha, posto 7), Fio Vermelho do Destino: a proteção, Reversão do Destino, Remendo Tecido do Destino, Passo do Gato, Reescrita do Destino |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Tear do Destino (medidor 70), Campo de Treliça de Linha, Choque de Marionetes, Abrigo do Destino, Esquiva do Destino, Tear do Destino: a onda |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Rouge (`rouge`) | Support | 1 | sim |
| Bruxa da Floresta (`witch`) | Caster | 2 | não |
| Boneca de Linha (`thread_doll`) | Bruiser | 3 | sim |

## Quests da jornada

### vanessa_fate

> canon: the Witches' Forest invasion (ch. 98-101, ep. 63-65) where the Black Bulls, Asta and Noelle among them, defend Vanessa's home against the Diamond and Midnight Sun armies and the Witch Queen, and Vanessa awakens the Red Thread of Fate to protect her family (wiki Red Thread of Fate, Vanessa Enoteca vs. Witch Queen). The talk lines and the wave contents inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `noelle` | talk | `black_bulls_hideout` | 30 | `—` | strength 850, merits 430 |
| `forest` | goto | `witches_forest` | 38 | `—` | strength 1440, merits 720 |
| `armies` | trial | `witches_forest` | 46 | `—` | strength 5770, merits 2890, mastery 300 |
| `queen` | boss | `witches_forest` | 60 | `witch_queen` | strength 8360, merits 4180, mastery 500 |

### vanessa_loom

> inv.: Fate's Loom is invented for the roster (the canon's Door of Fate, ch. 361, stays for the story). It extends the Red Thread of Fate from one target to the whole field, as the wiki's Thread Magic lets Vanessa grow her threads with her skill. The whole chain's beats inv.

Requer: `vanessa_fate`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `domina` | talk | `witches_forest` | 80 | `—` | strength 1370, merits 690 |
| `siege` | trial | `black_bulls_hideout` | 84 | `—` | strength 7740, merits 3870, mastery 300 |
| `yami` | talk | `black_bulls_hideout` | 87 | `—` | strength 1430, merits 720 |
| `loom` | boss | `spade_fortress` | 91 | `foe:clovercraft:spade_soldier@A` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
