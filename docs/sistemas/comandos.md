# Comandos

## Jogador

| Comando | Função |
| --- | --- |
| `/exam` | Inicia o exame no Coliseu |
| `/missions` | Abre missões |
| `/story` | Jornada / quest tracker |
| `/tutorial skip` | Pula o tutorial |
| `/skin <id>` | Skin do seu mago (`own`, `classic`, Asta também `spade`) |
| `/roulette` | Reabre a roleta se ainda não rolou |
| `/music` | Liga/desliga a trilha |
| `/guilda ...` | Ver [guildas](/sistemas/guildas) |

## Admin (`/clover`)

Requer permissão de operador.

| Subcomando | Função |
| --- | --- |
| `character set <id> [players]` | Define o mago |
| `character clear [players]` | Remove o mago |
| `skin <id> [players]` | Skin |
| `form <nome> [players]` | Força forma (`ba`, `dive`, `kikongan`…) |
| `rank <n> [players]` | Rank 0–11 |
| `strength <n> [players]` | Força 1–100 |
| `merits add <n> [players]` | Méritos |
| `mastery <form> <nível> [players]` | Maestria 0–5 (`all`, `base`, formas) |
| `meter <0–100> [players]` | Barra de mana/anti-magia |
| `autosheathe <true/false>` | Embainhar automático |
| `clash` | Força clash com o alvo próximo |
| `arena [mages] [raio]` | Constrói arena de teste com Test Mages |
| `season wipe` | Nova temporada (zera jornadas) |
| `difficulty <nome>` | Dificuldade do mod |
| `potencial unlock/lock` / `potential ...` | Maxa ou zera o jogador (cheat de kit completo) |
| `exam reset/pass [players]` | Controle do exame |
| `roulette <modo>` | Força modo da roleta |
| `npc spawn/duel/clear/results` | NPCs de treino e duelo |
| `story ...` | Debug da jornada |

Chefes: `/boss` (summon/clear) — ver código `BossCommand`. Subordinados: `/summon` do mod (`SummonCommand`).
