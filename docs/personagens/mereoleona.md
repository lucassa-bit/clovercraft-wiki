# Mereoleona Vermillion

**Magia de Fogo** · Leão Carmesim

<ClientOnly>
<GeoViewer geo="/models/geo/character/mereoleona.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/mereoleona_base.png"}, {"id": "hellfire", "label": "Hellfire Incarnate", "texture": "/models/textures/character/mereoleona_hellfire.png"}, {"id": "leonum", "label": "Exercitus Leonum", "texture": "/models/textures/character/mereoleona_leonum.png"}]' />
</ClientOnly>

Brawler de fogo. Calidus Brachium, Hellfire Incarnate e o exército Exercitus Leonum.

- Grimório: **Grimório de Três Folhas Vermillion**
- O fogo responde à Leoa Invicta Sem Coroa. Use para virar Mereoleona.
- Formas: **Base** (`base`), **Hellfire Incarnate** (`hellfire`), **Exercitus Leonum** (`leonum`)
- Vincular: use o grimório (mensagem `O grimório de três folhas escolheu você. Você é Mereoleona Vermillion!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `fire_paw` | Pata de Fogo (agarrão) | — | 24 |
| 2 | `calidus_brachium` | Calidus Brachium | 12.0 | 28 |
| 3 | `calidus_barrage` | Mana Zone: Rajada de Calidus Brachium | — | 38 |
| 4 | `mana_zone` | Mana Zone (voo, postura Iai na guarda) | — | 22 |
| 5 | `purgatory` | Purgatory | — | 82 |
### Hellfire Incarnate

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `hellfire/meteor_dive` | Fogo Infernal: Mergulho Meteoro | 5.3 | 32 |
| 2 | `hellfire/streamer_lash` | Fogo Infernal: Açoite das Flâmulas | — | 28 |
| 3 | `hellfire/purgatory_abyss` | Calidus Brachium Purgatório: Abismo | — | 47 |
| 4 | `hellfire/overdrive` | Sobrecarga | — | 30 |
| 5 | `hellfire/flame_burial` | Calidus Brachium Purgatório: Sepultura de Chamas | — | 64 |
### Exercitus Leonum

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `leonum/vanguard_charge` | Exercitus Leonum: Carga da Vanguarda | — | 26 |
| 2 | `leonum/comrade_volley` | Exercitus Leonum: Rajada dos Camaradas | — | 24 |
| 3 | `leonum/white_flame_body` | Exercitus Leonum: Corpo de Chama Branca | — | 24 |
| 4 | `leonum/pride_guard` | Exercitus Leonum: Guarda do Orgulho | — | 24 |
| 5 | `leonum/army_charge` | Exercitus Leonum: A Carga do Exército | — | 60 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Pata de Fogo (agarrão) |
| Cavaleiro Mágico Júnior de 3ª Classe | Calidus Brachium |
| Cavaleiro Mágico Júnior de 1ª Classe | Mana Zone: Rajada de Calidus Brachium |
| Cavaleiro Mágico Intermediário de 3ª Classe | Mana Zone (lê o próximo golpe) |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Mana Zone Liberação Total: Calidus Brachium Purgatório, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Encarnação do Fogo Infernal (voo, mais quente quanto mais dura), Fogo Infernal: Mergulho Meteoro, Fogo Infernal: Açoite das Flâmulas, Calidus Brachium Purgatório: Abismo, Sobrecarga do Fogo Infernal (vida por calor), Calidus Brachium Purgatório: Sepultura de Chamas |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Magia Suprema de Fogo: Exercitus Leonum (uma vez por vida), Exercitus Leonum: Carga da Vanguarda, Exercitus Leonum: Rajada dos Camaradas, Exercitus Leonum: Corpo de Chama Branca, Exercitus Leonum: Guarda do Orgulho, Exercitus Leonum: A Carga do Exército |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Leão de Chamas (`flame_lion`) | Soldier | 1 | não |
| Leopold Vermillion (`leopold`) | Skirmisher | 2 | sim |
| Fuegoleon Vermillion (`fuegoleon`) | Elite | 3 | sim |

## Quests da jornada

### mereoleona_hellfire

> canon: in the Shadow Palace Mereoleona's magic has no effect on Zagred's (Elf Reincarnation arc), so she returns to train in the Ultime-Volcano; six months later Nacht asks her to join the rescue of Yami and William, and in the Spade raid she assimilates a great amount of Fire Magic against Zenon's giant demon (Hellfire Incarnate). The giant demon stands as the Gravito behemoth (inv.); the camp's waves inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `palace` | goto | `shadow_altar` | 30 | `—` | strength 1280, merits 640 |
| `volcano` | goto | `volcano_camp` | 36 | `—` | strength 1400, merits 700 |
| `heat` | trial | `volcano_camp` | 42 | `—` | strength 5520, merits 2760, mastery 300 |
| `blaze` | trial | `volcano_camp` | 48 | `—` | strength 5890, merits 2950, mastery 300 |
| `nacht` | talk | `royal_capital` | 54 | `—` | strength 1130, merits 570 |
| `spade` | goto | `spade_fortress` | 58 | `—` | strength 1760, merits 880 |
| `demon` | boss | `spade_fortress` | 62 | `gravito_behemoth` | strength 8490, merits 4250, mastery 500 |

### mereoleona_leonum

> canon: after Lucifero's half-manifestation Mereoleona's arm disintegrates; Hellfire Incarnate forges a new one against Moris's tentacles; Fuegoleon arrives with Salamander and her grimoire writes Ultimate Flame Magic: Exercitus Leonum, the spirits of the fallen Crimson Lions at her side (Spade raid). Moris is not in the mod: the underworld's fire devil Naamah stands for him (inv.); trial contents inv.

Requer: `mereoleona_hellfire`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `brother` | talk | `royal_capital` | 80 | `—` | strength 1370, merits 690 |
| `crater` | goto | `volcano_camp` | 82 | `—` | strength 2090, merits 1040 |
| `edge` | trial | `volcano_camp` | 84 | `—` | strength 7740, merits 3870, mastery 300 |
| `arm` | trial | `volcano_camp` | 87 | `—` | strength 7880, merits 3940, mastery 300 |
| `spade` | goto | `spade_fortress` | 89 | `—` | strength 2170, merits 1090 |
| `lions` | boss | `spade_fortress` | 91 | `npc:zenon` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
