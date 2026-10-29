# Árvore de skills

Cinco ramos. Pontos = `(força - 1) + cadeias concluídas + firsts de chefe (cap) + rank de mérito`, limitados por config.

Tiers abrem com pontos já gastos no ramo: **0 / 6 / 15 / 27 / 42**. Keystone (tier 3, custo 3) muda o playstyle. Capstone (tier 5, custo 12) é **exclusivo** — só um por ramo.

Custo de ramo completo ≈ 60 pontos. Crítico da árvore: **×1.5**. Overload (capstone de mana) encarece skills ≥ 20 de custo em 25% e as fortalece. Commander (capstone de summon) corta 12% do seu dano pessoal.

Em PvP os bônus da árvore são atenuados (`TREE_PVP`). Caps de dano/redução/HP existem nas configs de summon/tree.

### Ataque

| Nó | Tipo | Tier | Ranks | Stat | Por rank |
| --- | --- | ---: | ---: | --- | --- |
| Atk Blade (`atk_blade`) | normal | 1 | 4 | Seus golpes corpo a corpo causam mais dano. | 0.03 |
| Atk Spell (`atk_spell`) | normal | 1 | 4 | Suas skills causam mais dano. | 0.03 |
| Atk Momentum (`atk_momentum`) | normal | 2 | 4 | Golpes seguidos (até 2 s entre eles) acumulam dano extra, cheio com 4 acertos. | 0.025 |
| Atk Breaker (`atk_breaker`) | normal | 2 | 4 | Mais dano em quem defende ou está atordoado. | 0.05 |
| Atk Crit (`atk_crit`) | normal | 2 | 4 | Chance de um golpe acertar com x1,5 de dano. | 0.03 |
| Atk Power (`atk_power`) | normal | 3 | 4 | Todo o seu dano aumenta. | 0.02 |
| Atk Hunter (`atk_hunter`) | normal | 3 | 4 | Mais dano contra elites, campeões e chefes. | 0.04 |
| Atk Form (`atk_form`) | normal | 4 | 4 | Mais dano enquanto você está transformado. | 0.03 |
| Atk Combo (`atk_combo`) | normal | 4 | 4 | Golpes seguidos (até 2 s entre eles) acumulam dano extra, cheio com 4 acertos. | 0.025 |
| Atk Skill2 (`atk_skill2`) | normal | 4 | 4 | Suas skills causam mais dano. | 0.03 |
| Atk Master (`atk_master`) | normal | 5 | 5 | Todo o seu dano aumenta. | 0.02 |
| Atk Finale (`atk_finale`) | keystone | 3 | 1 | FINALE | 0.6 |
| Atk Berserker (`atk_berserker`) | capstone | 5 | 1 | BERSERK | 0.3 |
| Atk Executor (`atk_executor`) | capstone | 5 | 1 | EXECUTE | 0.25 |

### Vida

| Nó | Tipo | Tier | Ranks | Stat | Por rank |
| --- | --- | ---: | ---: | --- | --- |
| Life Max (`life_max`) | normal | 1 | 4 | Sua vida máxima aumenta. | 0.03 |
| Life Regen (`life_regen`) | normal | 1 | 4 | Fora de combate, você recupera esta parte da vida por segundo. | 0.005 |
| Life Steal (`life_steal`) | normal | 2 | 4 | Você se cura com parte do dano que causa (até 5%% da vida por segundo). | 0.015 |
| Life Max2 (`life_max2`) | normal | 2 | 4 | Sua vida máxima aumenta. | 0.025 |
| Life Second Wind (`life_second_wind`) | normal | 2 | 4 | Cada abate cura parte da sua vida. | 0.02 |
| Life Regen2 (`life_regen2`) | normal | 3 | 4 | Fora de combate, você recupera esta parte da vida por segundo. | 0.005 |
| Life Bulwark (`life_bulwark`) | normal | 3 | 4 | Acima de 70%% de vida, você recebe menos dano. | 0.02 |
| Life Max3 (`life_max3`) | normal | 4 | 4 | Sua vida máxima aumenta. | 0.025 |
| Life Steal2 (`life_steal2`) | normal | 4 | 4 | Você se cura com parte do dano que causa (até 5%% da vida por segundo). | 0.01 |
| Life Heal Power (`life_heal_power`) | normal | 4 | 4 | Toda cura que você recebe fica mais forte. | 0.05 |
| Life Titan (`life_titan`) | normal | 5 | 5 | Sua vida máxima aumenta. | 0.02 |
| Life Second Chance (`life_second_chance`) | keystone | 3 | 1 | SECOND_CHANCE | 0.2 |
| Life Immortal (`life_immortal`) | capstone | 5 | 1 | REGEN_COMBAT | 0.01 |
| Life Bond (`life_bond`) | capstone | 5 | 1 | HEAL_SUMMONS | 1.0 |

### Resistência

| Nó | Tipo | Tier | Ranks | Stat | Por rank |
| --- | --- | ---: | ---: | --- | --- |
| Res Guard (`res_guard`) | normal | 1 | 4 | Você recebe menos dano de tudo. | 0.02 |
| Res Poise (`res_poise`) | normal | 1 | 4 | Você resiste mais a ser empurrado. | 0.06 |
| Res Dr2 (`res_dr2`) | normal | 2 | 4 | Você recebe menos dano de tudo. | 0.015 |
| Res Armour (`res_armour`) | normal | 2 | 4 | Você recebe menos dano enquanto ataca. | 0.04 |
| Res Tenacity (`res_tenacity`) | normal | 2 | 4 | Lentidão, fraqueza e atordoamento duram menos em você. | 0.08 |
| Res Magic (`res_magic`) | normal | 3 | 4 | Você recebe menos dano de magia. | 0.03 |
| Res Dr3 (`res_dr3`) | normal | 3 | 4 | Você recebe menos dano de tudo. | 0.015 |
| Res Boss (`res_boss`) | normal | 4 | 4 | Você recebe menos dano de chefes. | 0.03 |
| Res Poise2 (`res_poise2`) | normal | 4 | 4 | Você resiste mais a ser empurrado. | 0.05 |
| Res Lowhp (`res_lowhp`) | normal | 4 | 4 | Abaixo de 40%% de vida, você recebe menos dano. | 0.03 |
| Res Bastion (`res_bastion`) | normal | 5 | 5 | Você recebe menos dano de tudo. | 0.015 |
| Res Wall (`res_wall`) | keystone | 3 | 1 | WALL | 0.3 |
| Res Fortress (`res_fortress`) | capstone | 5 | 1 | STILL_DR | 0.2 |
| Res Advance (`res_advance`) | capstone | 5 | 1 | DASH_DR | 0.4 |

### Invocação

| Nó | Tipo | Tier | Ranks | Stat | Por rank |
| --- | --- | ---: | ---: | --- | --- |
| Sum Vigor (`sum_vigor`) | normal | 1 | 3 | Seus subordinados ganham poder. | 0.04 |
| Sum Fury (`sum_fury`) | normal | 1 | 3 | Seus subordinados ganham poder. | 0.04 |
| Sum Time (`sum_time`) | normal | 2 | 4 | Seus subordinados ficam mais tempo em campo. | 12.0 |
| Sum Haste (`sum_haste`) | normal | 2 | 4 | A recarga das invocações fica mais curta. | 0.075 |
| Sum Xp (`sum_xp`) | normal | 2 | 4 | Seus subordinados ganham mais experiência. | 0.08 |
| Sum Vigor2 (`sum_vigor2`) | normal | 3 | 4 | Seus subordinados ganham poder. | 0.04 |
| Sum Fury2 (`sum_fury2`) | normal | 3 | 4 | Seus subordinados ganham poder. | 0.04 |
| Sum Bond (`sum_bond`) | normal | 4 | 4 | Seus subordinados ganham Vínculo mais rápido. | 0.15 |
| Sum Mana (`sum_mana`) | normal | 4 | 4 | O Despertar dos subordinados custa menos da sua mana. | 0.05 |
| Sum Eternal (`sum_eternal`) | normal | 5 | 5 | Seus subordinados ficam mais tempo em campo. | 12.0 |
| Sum Army (`sum_army`) | keystone | 3 | 1 | SUMMON_COUNT | 1.0 |
| Sum Commander (`sum_commander`) | capstone | 5 | 1 | COMMANDER | 1.0 |
| Sum Side (`sum_side`) | capstone | 5 | 1 | SIDE_BY_SIDE | 0.12 |
| Sum Pact (`sum_pact`) | special | 1 | 1 | SUMMON_UNLOCK | 0 |
| Sum Legion (`sum_legion`) | special | 4 | 1 | SUMMON_COUNT | 0 |

### Mana

| Nó | Tipo | Tier | Ranks | Stat | Por rank |
| --- | --- | ---: | ---: | --- | --- |
| Mana Flow (`mana_flow`) | normal | 1 | 4 | Você ganha mais mana. | 0.08 |
| Mana Thrift (`mana_thrift`) | normal | 1 | 4 | Suas skills custam menos. | 0.04 |
| Mana Reserve (`mana_reserve`) | normal | 2 | 4 | Você guarda mana além da barra cheia. | 6.0 |
| Mana Form (`mana_form`) | normal | 2 | 4 | Sua forma consome menos. | 0.05 |
| Mana Surge (`mana_surge`) | normal | 2 | 4 | Cada abate devolve mana. | 2.0 |
| Mana Flow2 (`mana_flow2`) | normal | 3 | 4 | Você ganha mais mana. | 0.06 |
| Mana Thrift2 (`mana_thrift2`) | normal | 3 | 4 | Suas skills custam menos. | 0.03 |
| Mana Reserve2 (`mana_reserve2`) | normal | 4 | 4 | Você guarda mana além da barra cheia. | 5.0 |
| Mana Form2 (`mana_form2`) | normal | 4 | 4 | Sua forma consome menos. | 0.04 |
| Mana Summon (`mana_summon`) | normal | 4 | 4 | Invocar custa menos mana. | 0.06 |
| Mana Well (`mana_well`) | normal | 5 | 5 | Você ganha mais mana. | 0.04 |
| Mana Flux (`mana_flux`) | keystone | 3 | 1 | FLUX | 0.5 |
| Mana Overload (`mana_overload`) | capstone | 5 | 1 | OVERLOAD | 0.3 |
| Mana Efficiency (`mana_efficiency`) | capstone | 5 | 1 | EFFICIENCY | 0.3 |
