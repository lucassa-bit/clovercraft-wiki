# Zenon Zogratis

**Magia de Ossos / Espacial** · Tríade das Trevas (Spade)

<ClientOnly>
<GeoViewer geo="/models/geo/character/zenon.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/zenon_base.png"}, {"id": "beelz", "label": "Beelzebub", "texture": "/models/textures/character/zenon_beelz.png"}, {"id": "devil", "label": "Manifestação Demoníaca", "texture": "/models/textures/character/zenon_devil.png"}]' />
</ClientOnly>

Controle espacial. Prisão de ossos, Mana Domination e coração demoníaco.

- Grimório: **Grimório de Espadas de Zenon**
- Magia de Ossos e, quando o portão abre, a Magia Espacial de Belzebu: osso que cresce onde ele quer, cubos de espaço que aprisionam. Use para se tornar Zenon Zogratis.
- Formas: **Base** (`base`), **Beelzebub** (`beelz`), **Manifestação Demoníaca** (`devil`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Zenon Zogratis, da Tríade Sombria!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `bone_fang` | Presa Infinita de Osso | — | 30 |
| 2 | `bone_prison` | Prisão de Ossos | — | 30 |
| 3 | `eternal_fangs` | Presas Eternas | — | 44 |
| 4 | `bone_vault` | Salto de Osso | — | 26 |
| 5 | `grand_bone_spear` | Grande Lança de Osso | — | 64 |
### Beelzebub

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `beelz/spatial_severance` | Corte Espacial | — | 28 |
| 2 | `beelz/mana_domination` | Domínio Espacial da Mana | — | 32 |
| 3 | `beelz/gate_barrage` | Rajada de Portais | — | 36 |
| 4 | `beelz/spatial_grasp` | Aperto Espacial | — | 30 |
| 5 | `beelz/cube_storm` | Tempestade de Cubos | — | 70 |
### Manifestação Demoníaca

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `devil/bone_whips` | Chicotes de Osso | — | 36 |
| 2 | `devil/tail_pin` | Cravada da Cauda Tridente | — | 32 |
| 3 | `devil/spatial_rupture` | Ruptura Espacial | — | 44 |
| 4 | `devil/bone_exoskeleton` | Exoesqueleto de Osso | — | 30 |
| 5 | `devil/devil_heart` | Coração de Demônio | — | 64 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Presa Infinita de Osso |
| Cavaleiro Mágico Júnior de 3ª Classe | Prisão de Ossos |
| Cavaleiro Mágico Júnior de 1ª Classe | Presas Eternas |
| Cavaleiro Mágico Intermediário de 3ª Classe | Salto de Osso |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Grande Lança de Osso, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Belzebu 55% (magia espacial, chifres, asas, cubos de vidro), Corte Espacial, Domínio Espacial da Mana, Rajada de Portais, Aperto Espacial, Tempestade de Cubos |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Belzebu 100% (medidor 70), Chicotes de Osso, Cravada da Cauda Tridente, Ruptura Espacial, Exoesqueleto de Osso, Coração de Demônio |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Soldado de Osso (`bone_soldier`) | Bruiser | 1 | não |
| Gaderois Godroc (`gaderois`) | Tank | 2 | sim |
| Foyal Migusteau (`foyal`) | Caster | 3 | sim |

## Quests da jornada

### zenon_beelz

> canon: Zenon Zogratis, Spatial Magic user of the Dark Triad, host of Beelzebub; his raid on the Golden Dawn base (ch. 234-238) where he took the devil's power to 55 % -- both horns, both wings, dark substance over more than half his body -- and impaled Yuno. Spatial Mana Domination (ch. 276) and the Eternal Fangs (ch. 235) are his. The talks, wave contents and trial staging inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `voice` | talk | `here` | 30 | `—` | strength 850, merits 430 |
| `base` | goto | `royal_capital` | 38 | `—` | strength 1440, merits 720 |
| `raid` | trial | `royal_capital` | 44 | `—` | strength 5650, merits 2820, mastery 300 |
| `pact` | talk | `royal_capital` | 50 | `—` | strength 1090, merits 550 |
| `yuno` | boss | `royal_capital` | 56 | `npc:yuno` | strength 8080, merits 4040, mastery 500 |

### zenon_devil

> canon: at the Spade raid (ch. 275-282) Zenon, with the Qliphoth Advent Ritual's circle, opens the first gate and takes Beelzebub to 100 % (ch. 280) -- the bone ribcage, the helmet over the left horn and half the face, forehead horns, the trident tail and the whips -- against Yuno and Langris (shared with Yuno's Zephyr chain, which ends on the same fortress). Beelzebub's talks and the trial staging inv.

Requer: `zenon_beelz`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `demand` | talk | `spade_fortress` | 80 | `—` | strength 1370, merits 690 |
| `ritual` | trial | `spade_fortress` | 84 | `—` | strength 7740, merits 3870, mastery 300 |
| `langris` | trial | `spade_fortress` | 88 | `—` | strength 7920, merits 3960, mastery 300 |
| `devil` | talk | `spade_fortress` | 90 | `—` | strength 1460, merits 730 |
| `yuno` | boss | `spade_fortress` | 91 | `npc:yuno` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
