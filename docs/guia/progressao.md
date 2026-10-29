# Progressão

A primeira hora (Torre, tutorial, `/exam`) está em [Começar](/guia/comecar). Aqui é o que sobe depois — e as regras do exame.

Quatro sistemas aparecem juntos, mas não são a mesma moeda: **força**, **méritos** (rank), **maestria** e pontos da [árvore](/sistemas/arvore). Entender como eles se combinam evita investir no atributo errado.

## Força (1–100)

É o poder bruto. Sobe com inimigos, chefes e recompensas de quest.

A curva é exponencial: os últimos níveis demoram bem mais. Cada 9 de força equivalem a um “tier” de rank para HP e dano.

Não existe um limiar universal de transformação: cada cadeia de jornada tem seus próprios mínimos de força. Consulte a seção **Jornada** na ficha do seu [personagem](/personagens/).

## Méritos e rank

Méritos de guerra sobem o rank (Aspirante → Rei Mago). Algumas habilidades e transformações também pedem um rank mínimo; a ficha de cada personagem mostra os desbloqueios relevantes.

Limiares do mod (o servidor pode multiplicar por dificuldade):

| # | Rank | Méritos | O que muda para todo mundo |
| --- | --- | ---: | --- |
| 0 | Aspirante a Cavaleiro Mágico | 0 | — |
| 1 | Cavaleiro Mágico Júnior de 5ª Classe | 5.000 | — |
| 2 | Cavaleiro Mágico Júnior de 3ª Classe | 12.000 | Voo do kit |
| 3 | Cavaleiro Mágico Júnior de 1ª Classe | 20.000 | — |
| 4 | Cavaleiro Mágico Intermediário de 3ª Classe | 30.000 | — |
| 5 | Cavaleiro Mágico Intermediário de 1ª Classe | 40.000 | — |
| 6 | Cavaleiro Mágico Sênior de 3ª Classe | 55.000 | 3º dash |
| 7 | Cavaleiro Mágico Sênior de 1ª Classe | 75.000 | — |
| 8 | Vice-Capitão | 100.000 | — |
| 9 | Capitão de Esquadrão | 130.000 | — |
| 10 | Grão-Cavaleiro Mágico | 170.000 | — |
| 11 | Rei Mago | 220.000 | +15% de poder de forma |

O restante dos desbloqueios é por personagem e por action. A tabela de habilidades mostra o rank efetivo que cada JSON declara — incluindo as exceções do kit do Asta.

## Maestria: requisito real das formas

Cada forma tem no máximo 5 níveis. A maestria ganha XP em combate, jornadas e treinos — e é um requisito de transformação no padrão do mod: `formMasteryGate`/`FORM_GATE` vem **ligado**.

Com a configuração padrão, faça nesta ordem:

1. Leve a **forma base a 5★** para liberar a primeira transformação.
2. Conclua a jornada, tenha a força/rank exigidos e o recurso pedido pelo kit.
3. Leve a **forma atual a 5★** antes de tentar a próxima.

O servidor pode desligar esse portão, mas não é seguro presumir isso. A maestria também melhora a forma: no código, 5★ reduz o multiplicador de dreno de `1,8` para `0,6`, eleva o poder de `0,86` para `1,10` e reduz exaustão. O limiar-base de 5★ é 25.000 XP, multiplicado por `masteryScale` (padrão 4,0) e pela dificuldade. Importante: o piso visual concedido por rank não substitui o XP de maestria que o portão testa.

## Árvore

Pontos vêm de força, cadeias concluídas, firsts de chefe e rank. Veja os efeitos e prioridades de cada ramo em [Árvore](/sistemas/arvore).

## Exame de Cavaleiro Mágico

`/exam` teleporta você ao Coliseu. Não existe NPC parado para conversar.

Precisa: grimório vinculado, cerimônia feita, ainda não passou, **sobrevivência**, chão plano. Se a estrutura ainda carrega, espera “Preparando o Coliseu…”.

1. Countdown de ~3 s. O examinador é um **NPC clone** de outro mago jogável, dificuldade Normal.
2. Duelo de **90 s**. O primeiro a cair a **25% de vida** perde — ninguém morre de verdade. No tempo, ganha quem tiver mais % de HP.
3. Nota 0–100. Em seguida você **escolhe qualquer um dos 9 [esquadrões](/sistemas/squads)**; a nota só muda a ordem dos cards.
4. O capitão entrega a **vassoura** (`J`). Se fechar a tela sem escolher, `/exam` reabre a escolha.

Exame anulado (logout, longe demais, sem chão): tente de novo. “Treine e volte” é cooldown de ~2 min.

## O que farmar

Três filas diferentes — não misture:

| Fila | O que é | Onde |
| --- | --- | --- |
| **Missões** | Caçadas, defesas, duelos do quadro. Várias diárias. Méritos | `/missions` ou o quadro |
| **Diário do mago** | Cadeia da transformação (viajar, trial, boss) | Jornada (`K`) → quests |
| **História** | Capítulos do reino: Saussey, masmorra antiga, Capital, ruínas élficas | `/story` |

Treinos globais (`train_spar` na força 8, vulcão da Mereoleona na 25…) repetem e pagam maestria. Lista: [Quests](/sistemas/quests).

## Reroll e temporada

**Race Scroll** (8% em chefe mundial) rerola a [raça](/sistemas/racas). **Grimoire Scroll** (3%) rerola o mago.

Admin: `/clover season wipe`. No próximo login todo cavaleiro recomeça na Torre, sem vínculo. Não é troca de personagem — é reset do servidor.
