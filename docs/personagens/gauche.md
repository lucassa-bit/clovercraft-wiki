# Gauche Adlai

**Magia de Espelho** · Touros Negros

<ClientOnly>
<GeoViewer geo="/models/geo/character/gauche.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/gauche_base.png"}, {"id": "kaleidoscope", "label": "Kaleidoscope", "texture": "/models/textures/character/gauche_kaleidoscope.png"}, {"id": "sea", "label": "Mirror Sea", "texture": "/models/textures/character/gauche_sea.png"}]' />
</ClientOnly>

Duelista de espelhos. Reflect Ray, Kaleidoscope e Mirror Sea.

- Grimório: **Grimório do Gauche**
- Magia de Espelho: raios ricocheteando em painéis de vidro, cópias que repetem seus golpes, uma janela que devolve feitiços, o Olho Caleidoscópio e o Mar de Espelhos. Use para se tornar Gauche Adlai.
- Formas: **Base** (`base`), **Kaleidoscope** (`kaleidoscope`), **Mirror Sea** (`sea`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Gauche Adlai dos Touros Negros!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `reflect_ray` | Raio Refletido | — | 34 |
| 2 | `real_double` | Duplo Real | — | 32 |
| 3 | `mirrors_shift` | Passagem de Espelho | — | 26 |
| 4 | `full_reflection` | Reflexão Total | — | 30 |
| 5 | `reflect_refrain` | Refrão Refletido | — | 64 |
### Kaleidoscope

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `kaleidoscope/double_reflect_refrain` | Refrão Refletido Duplo | — | 40 |
| 2 | `kaleidoscope/mirrors_brigade` | Brigada de Espelhos | — | 38 |
| 3 | `kaleidoscope/tracing_mirror` | Espelho Rastreador | — | 26 |
| 4 | `kaleidoscope/large_reflect_ray` | Grande Raio Refletido | — | 34 |
| 5 | `kaleidoscope/giant_mirror` | Espelho Gigante | — | 72 |
### Mirror Sea

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `sea/large_reflect_refrain` | Grande Refrão Refletido | — | 46 |
| 2 | `sea/mirrors_meteorite` | Meteorito de Espelhos | — | 40 |
| 3 | `sea/mirror_legion` | Legião de Espelhos | — | 34 |
| 4 | `sea/mirror_exchange` | Troca de Espelho | — | 28 |
| 5 | `sea/mirror_sea` | Mar de Espelhos: a cúpula | — | 78 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Raio Refletido |
| Cavaleiro Mágico Júnior de 3ª Classe | Duplo Real |
| Cavaleiro Mágico Júnior de 1ª Classe | Passagem de Espelho |
| Cavaleiro Mágico Intermediário de 3ª Classe | Reflexão Total |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Refrão Refletido, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Olho Caleidoscópio (o olho de espelho se abre, rank 7), Refrão Refletido Duplo, Brigada de Espelhos, Espelho Rastreador, Grande Raio Refletido, Espelho Gigante |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Mar de Espelhos (medidor 70), Grande Refrão Refletido, Meteorito de Espelhos, Legião de Espelhos, Troca de Espelho, Mar de Espelhos: a cúpula |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Enxame de Cacos (`shard_swarm`) | Skirmisher | 1 | não |
| Espelho Prisma (`prism_mirror`) | Support | 2 | sim |
| Duplo de Espelho (`mirror_double`) | Elite | 3 | sim |

## Quests da jornada

### gauche_kaleidoscope

> canon: ch. 42-50 (ep. 33-35) -- Marie punches her brother and he goes back for Asta and Theresa; Theresa, the children, Neige and Marie lend him their mana; with the mirror in his left eye he multiplies Asta and raises the giant mirror that returns Licht's Light Shaft (gauche-canon.md). The form itself, the places, the waves and the talk lines inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `photo` | talk | `black_bulls_hideout` | 30 | `—` | strength 850, merits 430 |
| `church` | goto | `royal_capital` | 38 | `—` | strength 1440, merits 720 |
| `church_guard` | trial | `royal_capital` | 46 | `—` | strength 5770, merits 2890, mastery 300 |
| `light_shaft` | boss | `royal_capital` | 60 | `npc:licht` | strength 8360, merits 4180, mastery 500 |

### gauche_sea

> canon: Large Reflect Refrain over Dante with Henry (ch. 240, ep. 162), Mirrors Meteorite and the Spade-arc multiplications (ch. 314-315), the elf mana Drowa left in him (gauche-canon.md). The form itself, the waves and the talk lines inv.

Requer: `gauche_kaleidoscope`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `henry` | talk | `black_bulls_hideout` | 80 | `—` | strength 1370, merits 690 |
| `gate` | goto | `spade_fortress` | 84 | `—` | strength 2110, merits 1060 |
| `array` | trial | `spade_fortress` | 87 | `—` | strength 7880, merits 3940, mastery 300 |
| `dante_sky` | boss | `spade_fortress` | 91 | `npc:dante` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
