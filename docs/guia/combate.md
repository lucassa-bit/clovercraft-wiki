# Combate

O kit de combate combina combo, heavy, guarda, dash e cinco slots de magia. Transformar (`B`) pode trocar o conjunto de actions disponível.

Teclas: [Controles](/guia/controles). O que destrava cada forma: [Progressão](/guia/progressao).

## Como se luta

1. **Toque no clique esquerdo** — combo de 3–5 hits no chão. No ar, um golpe só. Depois de um dash, o clique vira **dash slash**.
2. **Segure o clique** — heavy / charge. Soltar no timing faz a versão mais forte (*release*).
3. **Segure `F`** — guarda no arco da frente. Gasta **stamina**. Stamina no zero = **guard break**: você fica aberto.
4. **Toque no `F` no timing** — **parry**: atordoa quem bateu e enche a barra de mana.
5. **`Z` `X` `C` `V` `R`** — os cinco slots de magia. Consulte a ficha do seu [personagem](/personagens/) para entender o efeito de cada um.
6. **Botão do meio** — lock-on. Câmera e skills seguem o alvo. Use no exame e em chefe.

Ordem prática: lock-on → combo/guarda → magia. Não fique parado enchendo skill.

## Duas barras

Há dois recursos, e eles não são a mesma coisa.

**Stamina** alimenta a guarda. Acabou = guard break.

**Mana** (a barra do grimório) alimenta skills e transformação. Ela é recuperada por combate e meditação; kits com escudo de mana têm regras próprias. Sem recurso suficiente, a action pode ser recusada.

**Asta** não tem mana: a barra dele é **Anti-Magia**. A guarda **anula magia**. Hits **selam** o alvo por alguns instantes — o selado não lança.

**Meditar (`Y`)** — segurar parado, fora de luta. Recupera mana / anti-magia mais rápido.

**Dash (`Alt`)** — quatro direções, i-frames curtos. O 3º dash só abre no rank Sênior 3º.

## Voo

**Voo (`J`)** — a regra base de voo do kit começa no rank Júnior 3º. Alguns kits sobrescrevem essa regra. A vassoura exige mana e não funciona para Asta; depois do exame, Asta usa o voo próprio. A implementação também recusa voo durante estados inválidos, como exaustão, queda forçada ou uma action cinemática.

## Transformar

Cada kit tem suas próprias formas. Asta e Mereoleona têm estágios internos na primeira transformação; eles não ganham um grupo de skills novo a cada estágio. A ficha de cada personagem separa essas formas de modo jogável.

Rank, jornada, recurso e maestria podem limitar uma transformação. `FORM_GATE` vem ligado na configuração padrão: 5★ da Base abre a primeira forma e 5★ da forma atual abre a próxima. Por isso, não trate força 30, força 80 ou barra 70 como regra universal — nem suponha que o servidor desligou o portão de maestria.

Sair da forma devolve o kit base. Barra no zero pode aplicar `exhausted`; o comportamento final depende da action e da configuração.

## Clash

Dois heavies se encontram: mini-game de círculos (Perfect / Good / Miss). O vencedor atravessa com dano extra. Empate empurra os dois.

Chefes e mobs também clasham. Errar contra boss dói mais.

## PvE e PvP

Dano a mobs e a jogadores escala separado. A [árvore](/sistemas/arvore) rende menos em PvP. Ultimates de forma têm multiplicador próprio contra jogador.

O dano final pode combinar força, forma, rank, árvore, PvE/PvP e configuração do servidor. As fichas de personagem mostram o dano-base quando ele existe; esse número não é o dano final exibido em jogo.
