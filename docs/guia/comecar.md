# Começar a jogar

Clover Craft começa com a cerimônia do grimório e termina no loop de força, mérito, maestria e jornadas. Esta é a rota prática para a primeira sessão; depois, use as fichas de [personagens](/personagens/) para escolher um kit e acompanhar sua evolução.

> Os passos abaixo descrevem o padrão do 0.4.0. Um servidor pode mudar custos, dificuldade e o portão de maestria nas configurações.

## Requisitos

| Peça | Versão |
| --- | --- |
| Minecraft | 1.21.1 |
| NeoForge | 21.1.259 ou superior |
| GeckoLib | 4.9.3+ |
| Photon | 2.2.7+ (cliente — partículas e pós-FX) |
| O mod | `clovercraft-0.4.0-neoforge-1.21.1.jar` |

## Os primeiros minutos

1. Entre no mundo. **Padre Orsi** fala no overlay (não há NPC no chão) e um marcador aponta a Torre.
2. Chegue a uns 10 blocos do altar. Abre a **Cerimônia do Grimório**: grimório, sangue ([raça](/sistemas/racas)) e berço. É uma vez só.
3. Use o grimório (botão direito) para **vincular**. O mago não troca depois — Grimoire Scroll rerola o grimório; um admin também pode resetar.
4. Complete as **Lições de Hage** no HUD — ou digite `/tutorial skip`.
5. Em **sobrevivência**, digite `/exam`. O jogo te leva ao Coliseu e spawna um examinador (clone NPC de outro mago).
6. Escolha um [esquadrão](/sistemas/squads). O fluxo do exame entrega a **vassoura mágica**; use `J` para voar.

Asta usa o voo próprio liberado após o exame; a vassoura é recusada por ele. Regras de voo: [Combate](/guia/combate#voo).

## Lições de Hage

O tutorial não é conversa com villagers. São cinco ações, nessa ordem:

| # | Lição | O que fazer | Default |
| --- | --- | --- | --- |
| 1 | Combo | Acerte um combo completo (três hits) | clique esquerdo |
| 2 | Dash | Dash | `Alt` esquerdo |
| 3 | Guarda | Segure a guarda | `F` |
| 4 | Heavy | Segure o ataque e solte | clique esquerdo (segurar) |
| 5 | Magia | Lance uma skill | `Z` (`X` `C` `V` ao lado) |

Ao terminar, aparece o convite clicável para `/exam`. Lista completa de teclas: [Controles](/guia/controles).

## Depois do exame

Você já é Cavaleiro Mágico. O resto do jogo é ficar mais forte.

Aperte **K** para abrir a **Jornada**. É o hub: força, rank, maestria, diário de quests, missões, história do reino e árvore. Três coisas diferentes saem daí:

| O quê | Para quê | Como abrir |
| --- | --- | --- |
| **Missões** | Caçadas e defesas, várias diárias. Pagam **méritos** (rank) | `/missions`, quadro de madeira, ou o botão na Jornada |
| **Diário** | Cadeia da **transformação** do seu mago (viajar, trial, boss) | botão de quests na Jornada |
| **História** | Capítulos do reino (Saussey, masmorra, Capital) | `/story` — não é a tela da Jornada |

Combate e jornadas também sobem **força**. A cadeia e os requisitos variam por personagem; veja a seção **Jornada** na ficha de cada [personagem](/personagens/). No padrão do mod, a primeira transformação exige 5★ da Base e as seguintes exigem 5★ da forma anterior.

O primeiro marco comum de voo é **Júnior 3º** (12.000 méritos). A vassoura permite voo a magos com mana; Asta segue a exceção do próprio kit.

Detalhe de força, méritos, maestria e ranks: [Progressão](/guia/progressao).

## Se travar

| Situação | O que fazer |
| --- | --- |
| A roleta não abriu | Vá até a Torre e digite `/roulette` |
| `/exam` recusa | Grimório vinculado, cerimônia feita, modo sobrevivência, chão plano à frente |
| “Treine e volte” | Espere ~2 min e tente de novo |
| Personagem já pego no servidor | Claims — outro jogador vinculou aquele mago |
| Pular o tutorial | `/tutorial skip` |

Admin pode avançar a temporada (`/clover season wipe`): no próximo login todo mundo recomeça na Torre, sem mago. Roleta e claims são configuráveis no servidor.
