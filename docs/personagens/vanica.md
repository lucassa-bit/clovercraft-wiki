# Vanica Zogratis

**Magia de Sangue** · Tríade das Trevas (Spade)

<ClientOnly>
<GeoViewer geo="/models/geo/character/vanica.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/vanica_base.png"}, {"id": "megicula", "label": "Megicula 50%", "texture": "/models/textures/character/vanica_megicula.png"}, {"id": "megicula70", "label": "Megicula 70%", "texture": "/models/textures/character/vanica_megicula70.png"}]' />
</ClientOnly>

Agressora de sangue. Red Beast, maldições de Megicula e manifestação a 70%.

- Grimório: **Grimório de Vanica**
- Magia de Sangue e a maldição de Megicula: garras, espinhos e uma maldição que se acumula e detona. Use para se tornar Vanica Zogratis.
- Formas: **Base** (`base`), **Megicula 50%** (`megicula`), **Megicula 70%** (`megicula70`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Vanica Zogratis, da Tríade Sombria!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `blood_spikes` | Espinhos de Sangue | — | 32 |
| 2 | `blood_tendrils` | Tentáculos de Sangue | — | 30 |
| 3 | `giant_claw` | Garra Gigante de Sangue | — | 40 |
| 4 | `blood_cocoon` | Casulo de Sangue Quebra-Maldição | — | 80 |
| 5 | `red_beast` | Fera Vermelha | — | 80 |
### Megicula 50%

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `megicula/wing_rush` | Investida de Asa | — | 28 |
| 2 | `megicula/deterioration` | Maldição da Deterioração | — | 28 |
| 3 | `megicula/exploding_life` | Vida Explosiva | — | 34 |
| 4 | `megicula/resurrection` | Maldição da Ressurreição | — | 30 |
| 5 | `megicula/decaying_world` | Mundo em Decomposição | — | 110 |
### Megicula 70%

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `megicula70/heart_lance` | Lança da Cauda-Coração | — | 30 |
| 2 | `megicula70/wing_gaze` | Olhar dos Olhos das Asas | — | 32 |
| 3 | `megicula70/red_herd` | Manada de Feras Vermelhas | — | 36 |
| 4 | `megicula70/wing_shroud` | Mortalha de Asas | — | 66 |
| 5 | `megicula70/megicula_manifest` | Escrava Desatada: Manifestação de Megicula | — | 110 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Espinhos de Sangue |
| Cavaleiro Mágico Júnior de 3ª Classe | Tentáculos de Sangue |
| Cavaleiro Mágico Júnior de 1ª Classe | Garra Gigante de Sangue |
| Cavaleiro Mágico Intermediário de 3ª Classe | Casulo de Sangue Quebra-Maldição |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Fera Vermelha, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Megicula 50% (garras tocadas pela maldição, uma asa, acúmulos de Maldição), Investida de Asa, Maldição da Deterioração, Vida Explosiva, Maldição da Ressurreição |
| Vice-Capitão | — |
| Capitão de Esquadrão | Mundo em Decomposição |
| Grão-Cavaleiro Mágico | Megicula 70% (medidor 70), Lança da Cauda-Coração, Olhar dos Olhos das Asas, Manada de Feras Vermelhas, Mortalha de Asas |
| Rei Mago | Escrava Desatada: Manifestação de Megicula, Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Fera Vermelha (`red_beast`) | Bruiser | 1 | não |
| Svenkin Gatard (`svenkin`) | Cursed | 2 | sim |
| Robero Ringert (`robero`) | Cursed | 3 | sim |

## Quests da jornada

### vanica_megicula

> canon: Vanica Zogratis, Blood Magic user of the Dark Triad, hosts Megicula, the curse devil, and takes her power in stages (ch. 251-255): her Dark Disciples raided the Heart Kingdom (ch. 247-248) and at the Ludic Sanctuary she fought Noelle at the Black Bulls' side with the half-devil body, the black claws and the curse (Resurrection Curse ch. 251, Exploding Life ch. 255, Decaying World ch. 254). The talk beats, the Heart Kingdom's order of events and the trial's staging inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `voice` | talk | `here` | 30 | `—` | strength 850, merits 430 |
| `heart` | goto | `heart_sanctuary` | 36 | `—` | strength 1400, merits 700 |
| `raid` | trial | `heart_sanctuary` | 42 | `—` | strength 5520, merits 2760, mastery 300 |
| `pact` | talk | `heart_sanctuary` | 48 | `—` | strength 1070, merits 540 |
| `noelle` | boss | `heart_sanctuary` | 54 | `npc:noelle` | strength 7940, merits 3970, mastery 500 |

### vanica_megicula70

> canon: Vanica draws up to 70 % of Megicula (ch. 253 p.12 wings and tail; ch. 295-296 the herd of red beasts) and at the Spade raid Megicula takes her body, Unbound Slave (ch. 297-298), against Noelle's Saint Stage; the Qliphoth Advent Ritual's circle in the Spade castle (ch. 275-280) is shared with Dante's chain. The devils testing the host at the circle, the talks and the final duel's staging inv.

Requer: `vanica_megicula`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `demand` | talk | `spade_fortress` | 80 | `—` | strength 1370, merits 690 |
| `ritual` | trial | `spade_fortress` | 84 | `—` | strength 7740, merits 3870, mastery 300 |
| `eyes` | trial | `spade_fortress` | 88 | `—` | strength 7920, merits 3960, mastery 300 |
| `slave` | talk | `spade_fortress` | 90 | `—` | strength 1460, merits 730 |
| `noelle` | boss | `spade_fortress` | 91 | `npc:noelle` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
