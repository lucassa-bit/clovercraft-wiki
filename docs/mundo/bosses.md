# Chefes

<ClientOnly>
<GeoViewer catalog='[{"id": "ancient_golem", "label": "Golem Ancestral de Mana", "geo": "/models/geo/boss/ancient_golem.geo.json", "texture": "/models/textures/entity/boss/ancient_golem.png"}, {"id": "sally", "label": "Sally", "geo": "/models/geo/boss/sally.geo.json", "texture": "/models/textures/entity/boss/sally.png"}, {"id": "rades", "label": "Rades Spirito", "geo": "/models/geo/boss/rades.geo.json", "texture": "/models/textures/entity/boss/rades.png"}, {"id": "heath_grice", "label": "Heath Graice", "geo": "/models/geo/boss/heath_grice.geo.json", "texture": "/models/textures/entity/boss/heath_grice.png"}, {"id": "valtos", "label": "Valtos", "geo": "/models/geo/boss/valtos.geo.json", "texture": "/models/textures/entity/boss/valtos.png"}, {"id": "lotus_whomalt", "label": "Lotus Whomalt", "geo": "/models/geo/boss/lotus_whomalt.geo.json", "texture": "/models/textures/entity/boss/lotus_whomalt.png"}, {"id": "catherine", "label": "Catherine", "geo": "/models/geo/boss/catherine.geo.json", "texture": "/models/textures/entity/boss/catherine.png"}, {"id": "ladros", "label": "Ladros", "geo": "/models/geo/boss/ladros.geo.json", "texture": "/models/textures/entity/boss/ladros.png"}, {"id": "fana", "label": "Fana", "geo": "/models/geo/boss/fana.geo.json", "texture": "/models/textures/entity/boss/fana.png"}, {"id": "mars", "label": "Mars", "geo": "/models/geo/boss/mars.geo.json", "texture": "/models/textures/entity/boss/mars.png"}, {"id": "gravito_behemoth", "label": "Beemote de Gravito", "geo": "/models/geo/boss/gravito_behemoth.geo.json", "texture": "/models/textures/entity/boss/gravito_behemoth.png"}, {"id": "rhya", "label": "Rhya", "geo": "/models/geo/boss/rhya.geo.json", "texture": "/models/textures/entity/boss/rhya.png"}, {"id": "vetto", "label": "Vetto", "geo": "/models/geo/boss/vetto.geo.json", "texture": "/models/textures/entity/boss/vetto.png"}, {"id": "witch_queen", "label": "Rainha das Bruxas", "geo": "/models/geo/boss/witch_queen.geo.json", "texture": "/models/textures/entity/boss/witch_queen.png"}, {"id": "zagred", "label": "Zagred", "geo": "/models/geo/boss/zagred.geo.json", "texture": "/models/textures/entity/boss/zagred.png"}, {"id": "megicula", "label": "Megicula", "geo": "/models/geo/boss/megicula.geo.json", "texture": "/models/textures/entity/boss/megicula.png"}, {"id": "lilith", "label": "Lilith", "geo": "/models/geo/boss/lilith.geo.json", "texture": "/models/textures/entity/boss/lilith.png"}, {"id": "naamah", "label": "Nahamah", "geo": "/models/geo/boss/naamah.geo.json", "texture": "/models/textures/entity/boss/naamah.png"}, {"id": "beelzebub", "label": "Belzebu", "geo": "/models/geo/boss/beelzebub.geo.json", "texture": "/models/textures/entity/boss/beelzebub.png"}, {"id": "lucifero", "label": "Lucifero", "geo": "/models/geo/boss/lucifero.geo.json", "texture": "/models/textures/entity/boss/lucifero.png"}, {"id": "dominante_code", "label": "Dominante Code", "geo": "/models/geo/boss/dominante_code.geo.json", "texture": "/models/textures/entity/boss/dominante_code.png"}, {"id": "ratri", "label": "Ratri", "geo": "/models/geo/boss/ratri.geo.json", "texture": "/models/textures/entity/boss/ratri.png"}, {"id": "gaderois_godroc", "label": "Gaderois Godroc", "geo": "/models/geo/boss/gaderois_godroc.geo.json", "texture": "/models/textures/entity/boss/gaderois_godroc.png"}, {"id": "damnatio_kira", "label": "Damnatio Kira", "geo": "/models/geo/boss/damnatio_kira.geo.json", "texture": "/models/textures/entity/boss/damnatio_kira.png"}]' :height="460" />
</ClientOnly>

Chefes de quest, eventos mundiais e senhores da Qliphoth compartilham o mesmo cérebro (`BossBrain`): fases, cura interrompível, stagger, clash e persona (agressivo, caster, summoner…).

## Eventos mundiais

Com `clovercraft-world.toml` → `boss_events`. A cada ciclo o servidor escolhe um headliner conforme a força média dos online:

| Força dos jogadores | Headliners (peso 6×) |
| --- | --- |
| &lt; 40 | Sally, Rades, Heath Graice, Dominante Code |
| 40–61 | Vetto, Fana, Witch Queen, Ratri |
| 62–84 | Witch Queen, Vetto, Rhya, Gaderois |
| 85+ | Witch Queen, Vetto, Damnatio Kira |

Outros bosses cujo `band` está entre `força-25` e `força+6` entram com peso 1. Demônios da Qliphoth **não** spawnam no overworld.

Recompensas: força, méritos, chance de `race_scroll` (8%) e `grimoire_scroll` (3%), relíquia assinatura do chefe, título *Vanquisher of X*. Duo (dois chefs) paga 60% extra. Sair da arena faz o chefe *withdraw*.

## Roster

| Chefe | Título | Magia | Força (band) | Tipo |
| --- | --- | --- | ---: | --- |
| [Golem Ancestral de Mana](/mundo/bosses#ancient_golem) | Guardião da Masmorra | Pedra e runas de mana | 12 | Mundo / quest |
| [Sally](/mundo/bosses#sally) | Olho do Sol da Meia-Noite | Magia de Gel | 16 | Mundo / quest |
| [Rades Spirito](/mundo/bosses#rades) | Olho do Sol da Meia-Noite | Magia de Cadáver Espiritual | 18 | Mundo / quest |
| [Heath Graice](/mundo/bosses#heath_grice) | Olho do Sol da Meia-Noite | Magia de Gelo | 22 | Mundo / quest |
| [Valtos](/mundo/bosses#valtos) | Olho do Sol da Meia-Noite | Magia Espacial | 26 | Mundo / quest |
| [Lotus Whomalt](/mundo/bosses#lotus_whomalt) | Lótus do Inferno | Magia de Fumaça | 30 | Mundo / quest |
| [Catherine](/mundo/bosses#catherine) | Olho do Sol da Meia-Noite | Magia de Cinzas | 34 | Mundo / quest |
| [Ladros](/mundo/bosses#ladros) | General Brilhante | Absorção e Emissão | 38 | Mundo / quest |
| [Fana](/mundo/bosses#fana) | Terceiro Olho · Ódio | Magia de Fogo + Magia Espiritual (Salamandra) | 42 | Mundo / quest |
| [Mars](/mundo/bosses#mars) | General Brilhante | Magia Mineral | 44 | Mundo / quest |
| [Beemote de Gravito](/mundo/bosses#gravito_behemoth) | Fera Mágica da Região de Magia Forte | Tempestade e rochas flutuantes | 48 | Mundo / quest |
| [Rhya](/mundo/bosses#rhya) | Terceiro Olho · Traição | Magia de Imitação | 52 | Mundo / quest |
| [Vetto](/mundo/bosses#vetto) | Terceiro Olho · Desespero | Magia de Besta | 58 | Mundo / quest |
| [Rainha das Bruxas](/mundo/bosses#witch_queen) | Ursula Bloodlord, Mãe de Todas as Bruxas | Magia de Sangue | 64 | Mundo / quest |
| [Zagred](/mundo/bosses#zagred) | Demônio de Alto Escalão | Magia Kotodama | 70 | Demônio |
| [Megicula](/mundo/bosses#megicula) | Demônio do Mais Alto Escalão | Magia de Maldição | 76 | Demônio |
| [Lilith](/mundo/bosses#lilith) | Demônio do Qliphoth, Primeiro Nível | Magia de Gelo Demoníaco | 82 | Demônio |
| [Nahamah](/mundo/bosses#naamah) | Demônio do Qliphoth, Primeiro Nível | Magia de Fogo Demoníaco | 82 | Demônio |
| [Belzebu](/mundo/bosses#beelzebub) | Soberano do Submundo | Magia Espacial | 90 | Demônio |
| [Lucifero](/mundo/bosses#lucifero) | Rei Demônio | Magia de Gravidade | 97 | Demônio |
| [Dominante Code](/mundo/bosses#dominante_code) | Bruxa da Floresta das Bruxas | Ferramentas mágicas: varinha, vassoura, manto e Golens de Segurança | 36 | Mundo / quest |
| [Ratri](/mundo/bosses#ratri) | Elfo Reencarnado | Magia Espacial | 56 | Mundo / quest |
| [Gaderois Godroc](/mundo/bosses#gaderois_godroc) | Discípulo Sombrio do Reino de Espadas | Magia de Pedra | 68 | Mundo / quest |
| [Damnatio Kira](/mundo/bosses#damnatio_kira) | Paladino de Lucius · Hospedeiro de Baal | Magia de Balança + Magia de Atmosfera (Baal) | 88 | Mundo / quest |

## Golem Ancestral de Mana {#ancient_golem}

- Título: **Guardião da Masmorra**
- Magia: Pedra e runas de mana
- Cura de fase: Recarga do Núcleo
- Força recomendada (band): **12**
- Moves: `Punho de Rocha`, `Golpe no Chão`, `Raio Rúnico`, `Arremesso de Pedregulho`, `Pilares Erguidos`, `Casca de Pedra`, `Despertar Sísmico`, `Sobrecarga Ancestral`

## Sally {#sally}

- Título: **Olho do Sol da Meia-Noite**
- Magia: Magia de Gel
- Cura de fase: Magia de Cura
- Força recomendada (band): **16**
- Moves: `Bala Mágica`, `Salamandra Pegajosa`, `Poça de Gel`, `Propriedades Especiais +α, Reforço`, `Escorpião Mágico`, `Deslize de Gel`, `Salamandra Pegajosa Gigante`, `Propriedades Especiais +α, Absorção`, `Explosão de Cadáver +α`

## Rades Spirito {#rades}

- Título: **Olho do Sol da Meia-Noite**
- Magia: Magia de Cadáver Espiritual
- Cura de fase: Costura de Cadáveres
- Força recomendada (band): **18**
- Moves: `Bala Mágica`, `Magia de Cadáver: Exército de Cadáveres`, `Raptor de Almas`, `Mãos da Cova`, `Exorcismo`, `Nº 0 – Michael Caesal`, `Nº 1 – Nº 4`, `Raptor de Almas: Chamado em Massa`, `Explosão de Cadáver +α`

## Heath Graice {#heath_grice}

- Título: **Olho do Sol da Meia-Noite**
- Magia: Magia de Gelo
- Cura de fase: Estase Congelada
- Força recomendada (band): **22**
- Moves: `Estilhaços de Gelo`, `Presa de Gelo Celestial`, `Escudo de Cristal de Gelo`, `Jaula de Granizo Infinito`, `Presas de Gelo Infinitas`, `Passo Gélido`, `Funeral de Gelo`, `Em Três Segundos, Todos Morrem`, `Funeral de Gelo: Inverno Sem Fim`

## Valtos {#valtos}

- Título: **Olho do Sol da Meia-Noite**
- Magia: Magia Espacial
- Cura de fase: Bolsão Espacial
- Força recomendada (band): **26**
- Moves: `Bala Mágica`, `Bala Mágica: Pelos Portais`, `Blecaute`, `Guilhotina de Portal`, `Portão Forçado`, `Miríade Negra`, `Blecaute: Abismo`, `Miríade Negra: Colapso`

## Lotus Whomalt {#lotus_whomalt}

- Título: **Lótus do Inferno**
- Magia: Magia de Fumaça
- Cura de fase: Fumaça Densa do Eremita: Descanso
- Força recomendada (band): **30**
- Moves: `Chicote de Fumaça`, `Prisão Cruzada de Fumaça`, `Jardim de Fumaça da Usurpação`, `Veículo Preguiçoso Agitado`, `Fumaça Densa do Eremita`, `Prisão de Fumaça do Rei Degenerado`, `Jardim de Fumaça: Florada Plena`, `Prisão de Fumaça: Lótus do Inferno`

## Catherine {#catherine}

- Título: **Olho do Sol da Meia-Noite**
- Magia: Magia de Cinzas
- Cura de fase: Formação de Absorção de Cinzas
- Força recomendada (band): **34**
- Moves: `Rajada de Cinzas`, `Cinzas Destrutivas Alegres`, `Maldição: Cego, Surdo e Dormente`, `Mergulho de Vassoura`, `Chuva de Cinzas`, `Cinzas Destrutivas Alegres: Grande`, `Formação de Absorção: Berço`, `Pira da Bruxa`

## Ladros {#ladros}

- Título: **General Brilhante**
- Magia: Absorção e Emissão
- Cura de fase: Absorção de Mana
- Força recomendada (band): **38**
- Moves: `Bala Mágica`, `Bala Mágica: Raio`, `Magia de Reforço: Golpe`, `Absorção`, `Emissão`, `Investida do Tapete Voador`, `Laser de Um Milhão`, `Laser de Um Milhão: Transbordo`

## Fana {#fana}

- Título: **Terceiro Olho · Ódio**
- Magia: Magia de Fogo + Magia Espiritual (Salamandra)
- Cura de fase: Manto de Penas da Fênix
- Força recomendada (band): **42**
- Moves: `Magia de Fogo: Balas de Chama`, `Sopro da Salamandra`, `Garra da Salamandra`, `Harpe`, `Sopro da Salamandra: Inferno`, `Salamandra Desencadeada`, `Magia Espiritual: Chama Final`, `Laevateinn de Chamas`

## Mars {#mars}

- Título: **General Brilhante**
- Magia: Magia Mineral
- Cura de fase: Manto de Penas da Fênix
- Força recomendada (band): **44**
- Moves: `Laevateinn`, `Marionete Talos`, `Harpe`, `Armadura de Nemeia`, `Aglomerado de Marionetes Talos`, `Laevateinn: Estocada de Diamante`, `Titã Blindado Pesado`, `Titã Blindado: Avanço Estilhaçante`, `Laevateinn de Chamas`

## Beemote de Gravito {#gravito_behemoth}

- Título: **Fera Mágica da Região de Magia Forte**
- Magia: Tempestade e rochas flutuantes
- Cura de fase: Fonte de Mana
- Força recomendada (band): **48**
- Moves: `Chifrada`, `Atropelo`, `Pisão`, `Sopro da Tempestade`, `Rochas Flutuantes`, `Terremoto de Gravito`, `Fúria do Chifre-Trovão`, `Desabamento das Rochas do Céu`

## Rhya {#rhya}

- Título: **Terceiro Olho · Traição**
- Magia: Magia de Imitação
- Cura de fase: Raio de Luz Curativo
- Força recomendada (band): **52**
- Moves: `Magia de Imitação`, `Dardo de Água`, `Espada de Luz do Julgamento`, `Lâmina Negra Coberta de Trevas`, `Magia de Luz: Passo Relâmpago`, `Sopro da Salamandra`, `Quinteto Elemental`, `Miríade Negra e Lampejo Partidor de Céus`

## Vetto {#vetto}

- Título: **Terceiro Olho · Desespero**
- Magia: Magia de Besta
- Cura de fase: Couro de Besta
- Força recomendada (band): **58**
- Moves: `Garra de Urso`, `Investida do Guepardo`, `Armadura de Rinoceronte`, `Arremesso de Rocha`, `Magia de Selamento Trindade`, `Magia de Besta: Frenesi`, `Magia de Besta: Baleia`, `Investida do Guepardo: Desespero`, `Forma Demoníaca: Desespero Liberto`, `Agarrão Esmagador`

## Rainha das Bruxas {#witch_queen}

- Título: **Ursula Bloodlord, Mãe de Todas as Bruxas**
- Magia: Magia de Sangue
- Cura de fase: Casulo de Sangue Quebra-Maldição
- Força recomendada (band): **64**
- Moves: `Controle dos Pássaros`, `Foice do Sangue Vital`, `Cadafalso de Sangue Fresco`, `Fluxo de Sangue Marionete`, `Chuva de Sangue`, `Cadafalso de Sangue: Forca`, `Fluxo de Sangue: Marionete`, `Réquiem Carmesim da Rainha`

## Zagred {#zagred}

- Título: **Demônio de Alto Escalão**
- Magia: Magia Kotodama
- Cura de fase: Monstros do Submundo: Banquete de Vida
- Força recomendada (band): **70**
- Moves: `Kotodama: "Perfure"`, `Kotodama: "Esmague"`, `Kotodama: "Queime"`, `Monstros do Submundo`, `Feitiço Absorvedor de Magia`, `Tridente`, `Kotodama: "Estilhace"`, `Monstros Gigantes do Submundo`, `Tridente: Distorção Desmanteladora`

## Megicula {#megicula}

- Título: **Demônio do Mais Alto Escalão**
- Magia: Magia de Maldição
- Cura de fase: Maldição de Recuperação Rápida
- Força recomendada (band): **76**
- Moves: `Lanças de Sangue`, `Vida Explosiva`, `Mundo em Decomposição`, `Revestimento de Aço`, `Escravo Liberto`, `Açoite de Tentáculos`, `Encantamento Malévolo`, `Vida Explosiva: Corrente`, `Mundo em Decomposição: Manifestação Plena`

## Lilith {#lilith}

- Título: **Demônio do Qliphoth, Primeiro Nível**
- Magia: Magia de Gelo Demoníaco
- Cura de fase: Corpo de Gelo
- Força recomendada (band): **82**
- Moves: `Barragem de Estilhaços de Gelo`, `Onda de Geada Congelante`, `Nevasca`, `Fusão com o Gelo`, `Congelar: Até as Sombras`, `Geada Absoluta`, `Nevasca do Primeiro Nível`, `Submundo Congelado`, `Fusão: Aniquilação de Gelo e Fogo`, `Calamidade Gêmea`

## Nahamah {#naamah}

- Título: **Demônio do Qliphoth, Primeiro Nível**
- Magia: Magia de Fogo Demoníaco
- Cura de fase: Corpo de Fogo
- Força recomendada (band): **82**
- Moves: `Barragem de Balas de Chama`, `Onda de Fogo Ardente`, `Tornado de Fogo`, `Corpo de Chamas`, `Fusão com o Fogo`, `Pilar do Fogo Infernal`, `Tornados do Primeiro Nível`, `Conflagração do Submundo`, `Fusão: Aniquilação de Gelo e Fogo`, `Calamidade Gêmea`

## Belzebu {#beelzebub}

- Título: **Soberano do Submundo**
- Magia: Magia Espacial
- Cura de fase: Recompressão Espacial
- Força recomendada (band): **90**
- Moves: `Garra da Fenda`, `Rasgo Espacial`, `Esfera de Compressão`, `Portão Espacial`, `Portais do Vazio`, `Colapso Dimensional`, `Mil Portões`, `Ruptura Abissal`

## Lucifero {#lucifero}

- Título: **Rei Demônio**
- Magia: Magia de Gravidade
- Cura de fase: Possessão Demoníaca: Os Demônios Afluem
- Força recomendada (band): **97**
- Moves: `Punho do Rei Demônio`, `Magia de Gravidade: Esmagar`, `Distorção Espacial Destrutiva`, `Distorção Espacial Evasiva`, `Poço Gravitacional`, `Possessão Demoníaca`, `Asas em Braços`, `Magia de Gravidade: Colapso`, `Distorção Destrutiva: Dilacerar`, `Magia de Gravidade: Pressão Absoluta`, `Meia-Manifestação: Rei do Submundo`, `Garra do Rei Demônio`

## Dominante Code {#dominante_code}

- Título: **Bruxa da Floresta das Bruxas**
- Magia: Ferramentas mágicas: varinha, vassoura, manto e Golens de Segurança
- Cura de fase: Conserto de Ferramenta Mágica
- Força recomendada (band): **36**
- Moves: `Bala Mágica`, `Rajada da Varinha`, `Cuspir-Fumaça`, `Manto Suma-Daqui`, `Mergulho de Vassoura`, `Golens de Segurança`, `Barragem de Golens Aprimorados`, `Ferramenta Mágica: Grande Fumaça`

## Ratri {#ratri}

- Título: **Elfo Reencarnado**
- Magia: Magia Espacial
- Cura de fase: Recarga da Pedra Mágica
- Força recomendada (band): **56**
- Moves: `Magia Espacial: Corte Entalhado`, `Abate do Arcanjo`, `Defesa Automática`, `Passo Espacial`, `Corte do Espaço`, `Abate do Arcanjo: Salva`, `Talhador de Tronos`, `Fúria do Elfo Sombrio`

## Gaderois Godroc {#gaderois_godroc}

- Título: **Discípulo Sombrio do Reino de Espadas**
- Magia: Magia de Pedra
- Cura de fase: Recomposição da Pedra Endurecida
- Força recomendada (band): **68**
- Moves: `Manoplas de Pedra`, `Pancada de Pedra`, `Magia de Pedra: Espinhos de Rocha`, `Armadura de Pedra Endurecida pelo Demônio`, `Barragem de Pedregulhos`, `Magia de Pedra: Desabamento`, `Magia de Pedra: Pilar da Fortaleza`, `Colosso de Pedra`, `Fúria do Discípulo Sombrio`

## Damnatio Kira {#damnatio_kira}

- Título: **Paladino de Lucius · Hospedeiro de Baal**
- Magia: Magia de Balança + Magia de Atmosfera (Baal)
- Cura de fase: Costura do Demônio Purificado
- Força recomendada (band): **88**
- Moves: `Magia de Atmosfera: Corte de Ar`, `Regular a Balança`, `Espada Mágica`, `Guarda das Quatro Asas`, `Explosão do Halo`, `Anjos da Guarda`, `Raio Combinado dos Anjos da Guarda`, `Balança do Julgamento`, `Dominar a Balança`, `Magia de Atmosfera: Vendaval Aniquilador`


IA: o boss lê ki (percepts), evita cheese (teto, pillar, kiting infinito) e troca de move por utilidade (`BossUtility`). Fairness reduz dano se o grupo está muito abaixo do band.
