# Progressão

Há três eixos que sobem juntos — força, méritos/rank e maestria — mais a [árvore](/sistemas/arvore) e as [quests](/sistemas/quests).

## Ranks (méritos de guerra)

Limiares vanilla do mod (multiplicados por `merit_scale` e pela dificuldade):

| # | Rank | Méritos |
| --- | --- | ---: |
| 0 | Aspirante a Cavaleiro Mágico | 0 |
| 1 | Cavaleiro Mágico Júnior de 5ª Classe | 5.000 |
| 2 | Cavaleiro Mágico Júnior de 3ª Classe | 12.000 |
| 3 | Cavaleiro Mágico Júnior de 1ª Classe | 20.000 |
| 4 | Cavaleiro Mágico Intermediário de 3ª Classe | 30.000 |
| 5 | Cavaleiro Mágico Intermediário de 1ª Classe | 40.000 |
| 6 | Cavaleiro Mágico Sênior de 3ª Classe | 55.000 |
| 7 | Cavaleiro Mágico Sênior de 1ª Classe | 75.000 |
| 8 | Vice-Capitão | 100.000 |
| 9 | Capitão de Esquadrão | 130.000 |
| 10 | Grão-Cavaleiro Mágico | 170.000 |
| 11 | Rei Mago | 220.000 |

Cada rank desbloqueia skills/formas **do seu personagem** (veja a página dele). Coisas comuns a todos:

- **Junior 3º** — voo do kit (rank 2)
- **Senior 3º** — 3º dash
- **Rei Mago** — *Form mastery* (+15% poder, forma drena mais devagar)

## Força (1–100)

XP de força vem de inimigos, chefes e recompensas de quest. A curva é exponencial (`STRENGTH_TOP = 200000`, expoente 1.5). Cada 9 níveis de força equivalem a um “tier” de rank para scaling de HP/dano.

HP, regen, resistência e dano PvE/PvP interpolam entre o valor do Aspirante e o do Rei Mago (configs `health_min/max`, `damage_pve_*`, etc.).

## Maestria

Cada forma tem 5 níveis. Combate na forma, quests (`mastery` nas recompensas) e treinos enchem a barra. A config `form_gate` impede pular formas.

## Cerimônia e roleta

Na Torre, a roleta escolhe personagem + [raça](/sistemas/racas). Há pergaminhos para rerolar raça (`race_scroll`) e grimório (`grimoire_scroll`) — drops raros de chefes mundiais (8% e 3%).

## Exame de Cavaleiro Mágico

Comando `/exam` (ou o NPC no Coliseu). Requisitos: personagem vinculado, cerimônia feita, ainda não passou, modo sobrevivência, cooldown de retry (~2 min).

Você luta contra um examinador NPC. Vitória oferece **três esquadrões**. A escolha aplica o bônus permanente do [esquadrão](/sistemas/squads).

## Temporada

Admin pode avançar a temporada (`/clover season wipe`). Todo mundo recomeça na Torre no próximo login.
