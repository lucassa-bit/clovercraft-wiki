# Combate

O combate é de ação, não de cooldown de hotbar. Cada personagem tem um **kit** (`CharacterKit`) com combo, charge, dash, guard, 4–5 skills e 2 transformações.

## Estrutura de um kit

| Slot | O que é |
| --- | --- |
| Combo 1–4 (às vezes 5) | String leve. Cancela no `cancel_at` para o próximo hit |
| Charge / tap / release | Heavy. Segurar aumenta o golpe |
| Dash F/L/B/R | I-frames curtos + deslocamento |
| Air | Um golpe aéreo |
| Dash slash | Conversão depois do dash |
| Skill 1–4 | Magias do grimório |
| Skill 5 | Ultimate da forma atual |
| Transform | Gasta meter e troca o kit inteiro |
| Exhausted | Stun curto se a forma acabar no zero |

Dano dos hits vem dos JSON em `clover/actions/` (campo `hits[].damage`), depois multiplicado por **força**, **forma**, **rank**, **esquadrão**, **árvore** e **PvE/PvP**.

## Formas

Quase todo mago tem forma 0 (base), 1 e 2. Mereoleona e Asta têm **estágios** internos (Black Asta 1–3, Hellfire 1–3). A forma 2 em geral pede:

- forma 1 com **maestria 5★**
- meter ≥ 70
- ainda não gasta nesta vida (várias ultimates são *once per life*)

Sair da forma (`revert`) devolve o kit base. Meter no zero aplica **exhausted**.

## Guard, parry, selo

- Guard reduz dano (config `guard_reduction`) num arco em graus.
- Parry na janela (`parry_ticks`) stagger o atacante.
- Hits de Asta **selam** magia do alvo por alguns ticks — o selado não lança.

## Clash

Dois fighters com charge suficiente entram no minigame. Círculos aparecem; timing Perfect vence. Empate empurra os dois. Chefes e mobs têm “skill” de clash própria (mais fácil errar contra boss).

## Meditação

Segurar fora de combate, depois de alguns ticks de calma. Regenera mana/anti-magia mais rápido.

## PvP vs PvE

A config separa dano a mobs e a jogadores, e a árvore aplica só uma fração dos bônus em PvP (`TREE_PVP`). Ultimates de forma têm multiplicador PvP próprio.
