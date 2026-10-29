# Zora Ideale

**Magia de Armadilha (Ash)** · Touros Negros

<ClientOnly>
<GeoViewer geo="/models/geo/character/zora.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/zora_base.png"}, {"id": "labyrinth", "label": "Ash Labyrinth", "texture": "/models/textures/character/zora_labyrinth.png"}, {"id": "seal", "label": "Grand Seal", "texture": "/models/textures/character/zora_seal.png"}]' />
</ClientOnly>

Armadilheiro. Trap Counter, Grand Seal e Ash Labyrinth.

- Grimório: **Grimório de Cinzas do Zora**
- Magia de Cinzas, Magia de Armadilhas e um medo muito sensato de tudo. Use para virar Zora Ideale.
- Formas: **Base** (`base`), **Grand Seal** (`seal`), **Ash Labyrinth** (`labyrinth`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Zora Ideale dos Touros Negros!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `paralytic_trap` | Armadilha Paralisante | — | 26 |
| 2 | `counterattack_weak` | Contra-ataque: Magia Fraca | — | 30 |
| 3 | `revelation_cowardly` | Revelação do Covarde | — | 34 |
| 4 | `ash_smoke_step` | Passo de Fumaça de Cinzas | — | 24 |
| 5 | `trap_chain_detonation` | Detonação em Cadeia de Armadilhas | — | 54 |
### Grand Seal

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `seal/secret_counter_trap` | Armadilha de Contra-ataque Secreta | — | 32 |
| 2 | `seal/sealing_net` | Rede de Selamento | — | 30 |
| 3 | `seal/mirror_gauntlet` | Manoplas-Espelho | — | 30 |
| 4 | `seal/sealed_step` | Passo Selado | — | 26 |
| 5 | `seal/grand_seal` | Grande Selo | — | 58 |
### Ash Labyrinth

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `labyrinth/labyrinth_walls` | Paredes do Labirinto | — | 34 |
| 2 | `labyrinth/counter_field` | Campo de Contra-ataque | — | 34 |
| 3 | `labyrinth/ash_burial` | Sepultamento de Cinzas | — | 30 |
| 4 | `labyrinth/decoy_ash_doll` | Boneco de Cinzas Isca | — | 28 |
| 5 | `labyrinth/ash_labyrinth` | Labirinto de Cinzas: a Espiral | — | 74 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Armadilha Paralisante |
| Cavaleiro Mágico Júnior de 3ª Classe | Contra-ataque: Magia Fraca |
| Cavaleiro Mágico Júnior de 1ª Classe | Revelação do Covarde |
| Cavaleiro Mágico Intermediário de 3ª Classe | Passo de Fumaça de Cinzas |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Detonação em Cadeia de Armadilhas, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Armadilha de Contra-ataque Secreta (forma Selo: palmas, marcas, espelhos), Armadilha de Contra-ataque Secreta, Rede de Selamento, Manoplas-Espelho, Passo Selado, Grande Selo |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Labirinto de Cinzas (medidor 70), Paredes do Labirinto, Campo de Contra-ataque, Sepultamento de Cinzas, Boneco de Cinzas Isca, Labirinto de Cinzas: a Espiral |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Boneco de Cinzas (`ash_doll`) | Bruiser | 1 | não |
| Percevejo Arco-Íris (`stink_bug`) | Skirmisher | 2 | sim |
| Armadilha Rúnica (`rune_trap`) | Caster | 3 | não |

## Quests da jornada

### zora_seal

> canon: Zora's Trap Magic and Ash Magic carry the Black Bulls' ambushes (Spade raid, ch. 275-285), where Secre's Sealing Magic is shared with him as a union (solo adaptation here). The training talks with Magna and the gate keeper's staging inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `magna` | talk | `black_bulls_hideout` | 28 | `—` | strength 830, merits 410 |
| `cloud` | trial | `spade_fortress` | 38 | `—` | strength 5260, merits 2630, mastery 300 |
| `secre` | talk | `spade_fortress` | 48 | `—` | strength 1070, merits 540 |
| `mark` | trial | `training_ring` | 54 | `—` | strength 6240, merits 3120, mastery 300 |
| `form` | talk | `spade_fortress` | 58 | `—` | strength 1170, merits 590 |
| `gate` | boss | `spade_fortress` | 62 | `foe:clovercraft:spade_soldier@A` | strength 8490, merits 4250, mastery 500 |

### zora_labyrinth

> canon: during the Royal Knights Selection Test the Black Bulls' Zora laid his rune traps for the examinees (Asta, Mimosa, Kirsch and Langris share that arc, ch. 120s). The Ash Labyrinth's staging and Mereoleona's dungeon trial inv.

Requer: `zora_seal`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `exam` | talk | `exam_colosseum` | 78 | `—` | strength 1360, merits 680 |
| `rivals` | talk | `exam_colosseum` | 82 | `—` | strength 1390, merits 700 |
| `maze` | trial | `ancient_dungeon` | 86 | `—` | strength 7830, merits 3920, mastery 300 |
| `mereoleona` | talk | `ancient_dungeon` | 89 | `—` | strength 1450, merits 720 |
| `spiral` | boss | `ancient_dungeon` | 91 | `npc:mereoleona` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
