# Quests

Definidas em JSON (`clover/quests/`). Tipos de cadeia: `form` (libera transformação), `training` (repeatable), `secret` (condição `reveal`).

Etapas: `talk`, `goto`, `boss`, `trial` (survive / duel / dodge / nohit). Trials spawnam waves `id@tier*n`.

| Cadeia | Tipo | Personagem | Etapas | Força da 1ª |
| --- | --- | --- | ---: | ---: |
| `asta_black` | form | asta | 7 | 30 |
| `asta_union` | form | asta | 7 | 66 |
| `yuno_dive` | form | yuno | 8 | 30 |
| `yuno_zephyr` | form | yuno | 7 | 68 |
| `yami_manazone` | form | yami | 6 | 30 |
| `yami_kikongan` | form | yami | 5 | 84 |
| `noelle_valkyrie` | form | noelle | 8 | 30 |
| `noelle_saint` | form | noelle | 6 | 80 |
| `mereoleona_hellfire` | form | mereoleona | 7 | 30 |
| `mereoleona_leonum` | form | mereoleona | 6 | 80 |
| `julius_zone` | form | julius | 6 | 30 |
| `julius_lucius` | form | julius | 5 | 80 |
| `nacht_canis` | form | nacht | 7 | 30 |
| `nacht_fourfold` | form | nacht | 5 | 80 |
| `licht_awakened` | form | licht | 6 | 30 |
| `licht_demon` | form | licht | 6 | 80 |
| `dante_lucifero` | form | dante | 5 | 30 |
| `dante_devil` | form | dante | 5 | 80 |
| `luck_fiend` | form | luck | 6 | 28 |
| `luck_black` | form | luck | 5 | 80 |
| `mimosa_robe` | form | mimosa | 5 | 28 |
| `mimosa_utopia` | form | mimosa | 4 | 80 |
| `vanessa_fate` | form | vanessa | 4 | 30 |
| `vanessa_loom` | form | vanessa | 4 | 80 |
| `gauche_kaleidoscope` | form | gauche | 4 | 30 |
| `gauche_sea` | form | gauche | 4 | 80 |
| `vanica_megicula` | form | vanica | 5 | 30 |
| `vanica_megicula70` | form | vanica | 5 | 80 |
| `zenon_beelz` | form | zenon | 5 | 30 |
| `zenon_devil` | form | zenon | 5 | 80 |
| `zora_seal` | form | zora | 6 | 28 |
| `zora_labyrinth` | form | zora | 5 | 78 |
| `train_ki` | training | todos | 2 | 12 |
| `train_volcano` | training | todos | 2 | 25 |
| `train_mana` | training | todos | 2 | 18 |
| `train_spar` | training | todos | 2 | 8 |
| `train_time` | training | todos | 2 | 20 |
| `train_dungeon` | training | todos | 2 | 6 |
| `train_gravito` | training | todos | 2 | 40 |
| `secret_midnight` | secret | todos | 2 | 30 |
| `secret_unbroken` | secret | todos | 2 | 50 |
| `secret_wanderer` | secret | todos | 2 | 15 |
| `secret_flawless` | secret | todos | 2 | 1 |
| `secret_collector` | secret | todos | 2 | 36 |
| `secret_king` | secret | todos | 2 | 95 |
| `secret_ashes` | secret | todos | 1 | 30 |
| `secret_star` | secret | todos | 2 | 15 |
| `dark_triad` | secret | todos | 6 | 45 |
| `dark_triad_2` | secret | todos | 6 | 56 |
| `dark_triad_3` | secret | todos | 6 | 74 |

Treinos globais (qualquer personagem): Ki no ringue, acampamento do vulcão da Mereoleona, e outros em `training.json`.

Segredos em `secrets.json` — exemplos: caçar Ladros à noite, trial sem hit, wanderer. Pagam título e às vezes troféu.

Painel: tecla Journey. `/story` reabre a jornada. `/missions` o quadro de missões diárias (`mission_board`).
