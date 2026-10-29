# Julius Novachrono

**Magia do Tempo** · Rei Mago

<ClientOnly>
<GeoViewer geo="/models/geo/character/julius.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/julius_base.png"}, {"id": "lucius", "label": "Lucius", "texture": "/models/textures/character/julius_lucius.png"}, {"id": "zone", "label": "Mana Zone", "texture": "/models/textures/character/julius_zone.png"}]' />
</ClientOnly>

Controle de tempo. Chrono Stasis, Mana Zone e a forma Lucius.

- Grimório: **Grimório sem Capa de Novachrono**
- O tempo responde ao 28º Rei Mago. Use para virar Julius Novachrono.
- Formas: **Base** (`base`), **Mana Zone** (`zone`), **Lucius** (`lucius`)
- Vincular: use o grimório (mensagem `O grimório sem capa escolheu você. Você é Julius Novachrono, o Rei Mago!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `chrono_stasis` | Magia do Tempo: Chrono Stasis | — | 26 |
| 2 | `time_reversal` | Magia do Tempo: Reversão do Tempo (desfaz os ferimentos recentes) | — | 30 |
| 3 | `accelerated_step` | Magia do Tempo: Passo Acelerado | — | 21 |
| 4 | `rapid_aging` | Magia do Tempo: Envelhecimento Rápido | — | 28 |
| 5 | `chrono_anastasis` | Magia do Tempo: Chrono Anastasis | — | 62 |
### Mana Zone

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `zone/grigora` | Mana Zone: Chrono Stasis Grigora (captura feitiços) | — | 26 |
| 2 | `zone/foresight` | Mana Zone: Previsão (contra-ataca o golpe que vê) | — | 24 |
| 3 | `zone/stasis_volley` | Mana Zone: Rajada de Chrono Stasis | — | 26 |
| 4 | `zone/accelerated_return` | Mana Zone: Retorno Acelerado (devolve os feitiços capturados) | — | 24 |
| 5 | `zone/anastasis_field` | Mana Zone: Chrono Anastasis sobre o campo | — | 62 |
### Lucius

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `lucius/soul_touch` | Lucius: Toque da Alma (sela a magia do inimigo) | — | 30 |
| 2 | `lucius/time_restraint` | Lucius: Restrição do Tempo (prende todos à frente) | — | 28 |
| 3 | `lucius/purification` | Lucius: Purificação da Alma (arremessa inimigos, cura aliados) | — | 32 |
| 4 | `lucius/numeral_edge` | Lucius: Lâmina de Numerais (uma faixa de numerais pelo campo) | — | 30 |
| 5 | `lucius/judgment_stasis` | Lucius: Stasis do Julgamento (o campo inteiro parado) | — | 56 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Magia do Tempo: Chrono Stasis |
| Cavaleiro Mágico Júnior de 3ª Classe | Magia do Tempo: Reversão do Tempo (desfaz os ferimentos recentes) |
| Cavaleiro Mágico Júnior de 1ª Classe | Magia do Tempo: Passo Acelerado |
| Cavaleiro Mágico Intermediário de 3ª Classe | Magia do Tempo: Envelhecimento Rápido |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Magia do Tempo: Chrono Anastasis, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Mana Zone (fica no ar, pós-imagens golpeiam de novo), Mana Zone: Chrono Stasis Grigora (captura feitiços), Mana Zone: Previsão (contra-ataca o golpe que vê), Mana Zone: Rajada de Chrono Stasis, Mana Zone: Retorno Acelerado (devolve os feitiços capturados), Mana Zone: Chrono Anastasis sobre o campo |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Lucius Zogratis (Magia da Alma, uma vez por vida), Lucius: Toque da Alma (sela a magia do inimigo), Lucius: Restrição do Tempo (prende todos à frente), Lucius: Purificação da Alma (arremessa inimigos, cura aliados), Lucius: Lâmina de Numerais (uma faixa de numerais pelo campo), Lucius: Stasis do Julgamento (o campo inteiro parado) |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Cavaleiro Mágico do Reino (`kingdom_knight`) | Soldier | 1 | não |
| Paladino (`paladin`) | Paladin | 2 | não |

## Quests da jornada

### julius_zone

> canon: the Eye of the Midnight Sun's raid on the Royal Capital -- Julius appears between two mages and kills them, Valtos teleports; William's farewell at sunset; the tower duel with Patolli, Julius catching his light blades with Chrono Stasis Grigora and raising a giant clock over the city (Eye of the Midnight Sun Raid arc). Patolli is not in the mod: an S-rank elite stands in (inv.); drill and waves inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `report` | talk | `royal_capital` | 30 | `—` | strength 850, merits 430 |
| `valtos` | boss | `royal_capital` | 36 | `valtos` | strength 3730, merits 1860, mastery 500 |
| `william` | talk | `royal_capital` | 42 | `—` | strength 1000, merits 500 |
| `clock` | trial | `training_ring` | 46 | `—` | strength 5770, merits 2890, mastery 300 |
| `blades` | trial | `royal_capital` | 52 | `—` | strength 6130, merits 3060, mastery 300 |
| `patolli` | boss | `royal_capital` | 58 | `foe:clovercraft:midnight_sun_mage@S/light` | strength 8220, merits 4110, mastery 500 |

### julius_lucius

> canon: Julius is born in the Spade Kingdom with two souls, his own and his twin Lucius Zogratis's; Damnatio's doubts after the Spade raid, Julius's panic, the banquet where Lucius freezes the tower and Asta's anti-magic breaks the spell (Spade Raid aftermath and Judgment Day arcs). Trial contents inv.

Requer: `julius_zone`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `damnatio` | talk | `royal_capital` | 80 | `—` | strength 1370, merits 690 |
| `voice` | talk | `royal_capital` | 83 | `—` | strength 1400, merits 700 |
| `walk` | goto | `spade_fortress` | 85 | `—` | strength 2120, merits 1060 |
| `gate` | trial | `spade_fortress` | 87 | `—` | strength 7880, merits 3940, mastery 300 |
| `banquet` | boss | `royal_capital` | 91 | `npc:asta` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
