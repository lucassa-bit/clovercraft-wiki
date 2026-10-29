# Luck Voltia

**Magia de Relâmpago** · Touros Negros

<ClientOnly>
<GeoViewer geo="/models/geo/character/luck.geo.json" skins='[{"id": "base", "label": "Base", "texture": "/models/textures/character/luck_base.png"}, {"id": "black", "label": "Black Lightning", "texture": "/models/textures/character/luck_black.png"}, {"id": "fiend", "label": "Thunder Fiend", "texture": "/models/textures/character/luck_fiend.png"}]' />
</ClientOnly>

Assassino elétrico. Thunder Fiend, Keraunos e Black Lightning.

- Grimório: **Grimório do Trevo de Luck**
- Magia de Raio, as Botas e as Luvas do Deus do Trovão e um sorriso que nunca some. Use para se tornar Luck Voltia.
- Formas: **Base** (`base`), **Thunder Fiend** (`fiend`), **Black Lightning** (`black`)
- Vincular: use o grimório (mensagem `O grimório escolheu você. Você é Luck Voltia, dos Touros Negros!`)

## Skills por forma

Dano é o maior hit do JSON da action, **antes** dos multiplicadores de força/forma/árvore.

### Base

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `thunderclap_orb` | Orbe Estrondoso do Trovão | — | 26 |
| 2 | `spark_chain` | Corrente de Faíscas | — | 28 |
| 3 | `thunder_fiend` | Demônio do Trovão | — | 30 |
| 4 | `afterimage` | Contra-ataque da Imagem Residual | — | 26 |
| 5 | `keraunos` | Keraunos | — | 44 |
### Thunder Fiend

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `fiend/ricochet_rush` | Investida Ricochete | — | 30 |
| 2 | `fiend/thunder_lattice` | Treliça do Trovão | — | 34 |
| 3 | `fiend/overdrive` | Sobrecarga | — | 28 |
| 4 | `fiend/orb_salvo` | Salva de Orbes | — | 26 |
| 5 | `fiend/thunderstorm` | Descida da Tempestade | — | 52 |
### Black Lightning

| Slot | ID | Nome | Dano (hit) | Duração (ticks) |
| ---: | --- | --- | ---: | ---: |
| 1 | `black/overcharge_lunge` | Estocada Sobrecarregada | — | 30 |
| 2 | `black/orb_barrage` | Barragem de Orbes | — | 36 |
| 3 | `black/axe_kick` | Chute Machado Aterrador | — | 36 |
| 4 | `black/static_skin` | Pele Estática | — | 30 |
| 5 | `black/black_chain` | Corrente do Raio Negro | — | 58 |

## Desbloqueio por rank

| Rank | Desbloqueios |
| --- | --- |
| Aspirante a Cavaleiro Mágico | — |
| Cavaleiro Mágico Júnior de 5ª Classe | Orbe Estrondoso do Trovão |
| Cavaleiro Mágico Júnior de 3ª Classe | Corrente de Faíscas |
| Cavaleiro Mágico Júnior de 1ª Classe | Demônio do Trovão |
| Cavaleiro Mágico Intermediário de 3ª Classe | Contra-ataque da Imagem Residual |
| Cavaleiro Mágico Intermediário de 1ª Classe | — |
| Cavaleiro Mágico Sênior de 3ª Classe | Keraunos, 3º dash |
| Cavaleiro Mágico Sênior de 1ª Classe | Demônio de Batalha Relâmpago (ricochetes, garras, cauda, oito orbes), Investida Ricochete, Treliça do Trovão, Sobrecarga, Salva de Orbes, Descida da Tempestade |
| Vice-Capitão | — |
| Capitão de Esquadrão | — |
| Grão-Cavaleiro Mágico | Demônio de Batalha Relâmpago Negro (medidor 70), Estocada Sobrecarregada, Barragem de Orbes, Chute Machado Aterrador, Pele Estática, Corrente do Raio Negro |
| Rei Mago | Domínio das formas (+15% de poder, gasto menor) |



## Subordinados

| Unidade | Função | Tier | Única |
| --- | --- | ---: | --- |
| Orbe do Trovão (`thunder_orb`) | Skirmisher | 1 | não |
| Magna Swing (`magna_swing`) | Bruiser | 2 | sim |
| Gadjah (`gadjah`) | Caster | 3 | sim |

## Quests da jornada

### luck_fiend

> canon: Luck trained in the Heart Kingdom with Gadjah (ch. 248, ep. 155-163) and fought Svenkin Gatard when Vanica's Dark Disciples raided it (ch. 247-248); the Black Bulls then asked Patolli for the elves' Ultimate Magic and were sent to Dryad (ch. 265, ep. 169; ch. 283-284); Luck first used the Lightning Battle Fiend on the mid-ranked devils of the Spade raid (ch. 284). The talk beats and the devil trial's staging inv.

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `gadjah` | talk | `heart_sanctuary` | 28 | `—` | strength 830, merits 410 |
| `svenkin` | boss | `heart_sanctuary` | 38 | `foe:clovercraft:dark_disciple@S` | strength 3830, merits 1910, mastery 500 |
| `patolli` | talk | `elf_ruins` | 46 | `—` | strength 1050, merits 520 |
| `dryad` | talk | `heart_sanctuary` | 52 | `—` | strength 1110, merits 560 |
| `raid` | trial | `spade_fortress` | 58 | `—` | strength 6460, merits 3230, mastery 300 |
| `gate` | boss | `spade_fortress` | 62 | `foe:clovercraft:spade_soldier@A` | strength 8490, merits 4250, mastery 500 |

### luck_black

> canon: after Lucius' clones attacked the Clover Kingdom the Black Bulls received Anti Magic through Asta (ch. 368-369); Luck destroyed the Guardian Angels with the Black Lightning Battle Fiend (ch. 369); Damnatio Kira defeated the squad one by one in the same arc. The Guardian Angels' stand-in foe and the talk beats inv.

Requer: `luck_fiend`

| Etapa | Tipo | Local | Força mín. | Chefe | Recompensa |
| --- | --- | --- | ---: | --- | --- |
| `clones` | talk | `royal_capital` | 80 | `—` | strength 1370, merits 690 |
| `antimagic` | talk | `black_bulls_hideout` | 84 | `—` | strength 1410, merits 700 |
| `damnatio` | talk | `royal_capital` | 87 | `—` | strength 1430, merits 720 |
| `angels` | trial | `royal_capital` | 90 | `—` | strength 8010, merits 4010, mastery 300 |
| `guardian` | boss | `royal_capital` | 91 | `foe:clovercraft:midnight_sun_mage@S/light` | strength 10250, merits 5130, mastery 500 |


Veja também: [combate](/guia/combate) · [progressão](/guia/progressao) · [invocações](/sistemas/invocacoes)
