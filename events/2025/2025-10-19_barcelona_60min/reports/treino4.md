# Treino 4 – Barcelona (Validação Setup + Setor 2)

## Informações Gerais
- **Data:** 08/10/2025
- **Duração:** ~50 minutos (2 blocos)
- **Condição de pista:** OPTIMUM (22°C ar / 25-28°C pista - aquecendo progressivamente)
- **Setup:** Friedolf otimizado (base T3 stint 4)
- **Tyre sets:** 1 (laps 1-9), 2 (laps 10-20)
- **Objetivo planejado:** Validar setup otimizado + trabalhar Setor 2 (T5-T9)
- **Objetivo real:** ✅ **Setup validado + melhoria em todos os setores**

---

## Resumo do Treino
| Item | Valor |
|------|------|
| Melhor volta válida | **1:45.097** 🏆 |
| Melhor S1 / S2 / S3 | **29.477** / **40.500** / **34.970** |
| Tempo médio (válidas) | **1:45.514** |
| Nº de voltas válidas | **14 / 20** (70%) |
| Evolução vs Treino 3 | **-0.133s** ✅ |
| Observação curta | **Melhor volta da semana; todos setores melhoraram** |

---

## Estrutura do Treino

### Bloco 1: Validação do Setup (Laps 1-9)
**Duração:** ~20 minutos
**Combustível:** 30L
**Tyre set:** 1 (novo)
**Temperatura pista:** 25.1-26.0°C (ideal)

**Objetivo:** Validar setup otimizado antes de trabalhar S2

**Resultados:**
- Melhor volta: **1:45.195** (lap 9)
- Média válidas: **1:45.534** (8 voltas)
- Voltas válidas: **8 / 9 (89%)** ✅
- **Feeling:** 7.5/10 ✅

**Critérios de validação:**
| Critério | Meta | Resultado | Status |
|----------|------|-----------|--------|
| Melhor volta | ≤ 1:45.5s | **1:45.195** | ✅✅ |
| RF temperatura | 78-85°C | 81°C (JSON) | ✅ (interno OK) |
| Consistência | >80% válidas | **89%** | ✅ |
| Feeling | ≥7/10 | **7.5/10** | ✅ |

**Decisão:** ✅ **Setup validado - seguir para Bloco 2**

---

### Bloco 2: Trabalho Setor 2 (Laps 10-20)
**Duração:** ~30 minutos
**Combustível:** 35L (abastecido no pit)
**Tyre set:** 2 (novo)
**Temperatura pista:** 27.5-28.5°C (+2-3°C vs Bloco 1)

**Objetivo:** Reduzir gap S2 de +0.383s para < +0.300s

**Resultados:**
- Melhor volta: **1:45.097** (lap 15) 🏆
- Melhor S2: **40.500** (lap 15)
- Média válidas: **1:45.499** (6 voltas)
- Voltas válidas: **6 / 11 (55%)** - esperado durante trabalho focado

**Melhoria S2:**
- T3: 40.547 → T4: **40.500** = **-0.047s** ✅
- Meta planejada < 40.400s: não atingida (-0.100s)
- Meta realista < 40.550s: ✅ atingida

**Observações:**
- Temperatura de pista +2-3°C dificultou
- FL/LR superaqueceram (até 97°C)
- TC 2 testado no lap 14 (vs TC 3 padrão)

---

## Evolução por Setor

### Comparativo Melhor Volta (vs Treino 3)
| Setor | Treino 3 | Treino 4 | Evolução | Gap p/ Ref. |
|------|:--------:|:--------:|:--------:|:-----------:|
| **S1** | 0:29.560 | **0:29.477** | **-0.083s** ✅ | +0.103s |
| **S2** | 0:40.547 | **0:40.500** | **-0.047s** ✅ | +0.336s |
| **S3** | 0:35.122 | **0:34.970** | **-0.152s** ✅✅ | +0.021s |
| **Total** | 1:45.230 | **1:45.097** | **-0.133s** ✅ | +0.610s |

> **Referência:** 1:44.487 (S1: 29.374 / S2: 40.164 / S3: 34.949)

**Destaques:**
- 🏆 **Melhor volta da semana:** 1:45.097 (nova referência pessoal!)
- ✅✅ **TODOS os setores melhoraram** vs T3
- ✅✅ **S3 quase perfeito:** +0.021s da referência (99.4% do alvo!)
- ✅ **S2 melhorou** conforme objetivo do treino
- ✅ **S1 melhorou** apesar do RF banda fria

---

### Progressão Setorial por Lap

**Melhores tempos S1:**
1. **29.477** (lap 5) ← melhor absoluto
2. 29.492 (lap 6)
3. 29.572 (laps 8, 16)

**Melhores tempos S2:**
1. **40.500** (lap 15) ← melhor absoluto
2. 40.512 (lap 13)
3. 40.530 (lap 9)

**Melhores tempos S3:**
1. **34.970** (lap 12) ← melhor absoluto, +0.021s da ref!
2. 34.980 (lap 9)
3. 35.000 (laps 5, 15)

---

## Análise de Temperaturas

### Divergência RF: Interno vs Banda

**Problema identificado:**
- **Temperatura interna (JSON):** 80-83°C ✅ (janela ideal: 75-85°C)
- **Temperatura banda (tela ACC):** 70-63-57°C ❌ (janela ideal: 75-85°C)

**Interpretação:**
- Pneu aquece **internamente** via toe (-0.20°) e fricção estrutural
- Calor **não transfere** eficientemente para superfície de contato
- Resulta em **perda de grip** especialmente em curvas rápidas (S1)

**Setup confirmado:**
- Toe: -0.20° ✅
- Caster: 14.5° ✅ (corrigido de 15.0° no início)
- Brake duct front: 2 ✅
- Pressão RF pit: 25.0 PSI

**Pressões hot medidas (Bloco 1):**
- FL: 27.1-27.4 (+2.3-2.6 vs pit)
- RF: 26.1-26.3 (+1.1-1.3 vs pit) ✅
- LR: 27.0-27.1 (+2.5-2.6 vs pit)
- RR: 26.5-26.7 (+1.3-1.5 vs pit)

---

### Superaquecimento FL/LR (Bloco 2)

**Problema agravado por temperatura de pista:**

| Pneu | Temp. Ideal | Bloco 1 (25-26°C) | Bloco 2 (27.5-28.5°C) | Diferença |
|------|-------------|-------------------|----------------------|-----------|
| **FL** | 86-90°C | 91-96°C (+1-6°C) | **93-97°C** (+3-7°C) | ❌ Piorou |
| **LR** | 88-92°C | 93-96°C (+1-4°C) | **94-97°C** (+2-5°C) | ❌ Piorou |

**Causa:**
- Temperatura de pista subiu **+2.5-3.5°C** entre blocos
- Pressões pit 24.8/24.5 geram muita deformação em pista quente
- Setup otimizado para pista ~26-27°C

**Impacto:**
- Possível degradação acelerada
- Menos margem de segurança em corrida se temperatura subir

---

### Temperaturas por Bloco

**Bloco 1 (Set 1, pista 25-26°C):**
- FL: 91-96°C | RF: 79-82°C (JSON) | LR: 92-96°C | RR: 82-85°C
- Banda RF: 70-63-57°C ❌

**Bloco 2 (Set 2, pista 27.5-28.5°C):**
- FL: 93-97°C | RF: 80-83°C (JSON) | LR: 93-97°C | RR: 83-86°C
- Banda RF: não reportada (provavelmente similar)

---

## Top 5 Voltas

### Voltas Válidas

1. **1:45.097** (lap 15) - 29.597 / **40.500** / 35.000 🏆
   - Tyre set 2, pista 28.0°C
   - Melhor S2 do treino

2. **1:45.195** (lap 9) - 29.685 / 40.530 / **34.980**
   - Tyre set 1, pista 26.0°C
   - Melhor volta do Bloco 1

3. **1:45.252** (lap 5) - **29.477** / 40.770 / 35.005
   - Tyre set 1, pista 25.5°C
   - Melhor S1 do treino

4. **1:45.332** (lap 6) - 29.492 / 40.692 / 35.147
   - Tyre set 1, pista 25.7°C

5. **1:45.445** (lap 8) - 29.572 / 40.617 / 35.255
   - Tyre set 1, pista 25.9°C

### Voltas Inválidas Notáveis

- **1:45.287** (lap 17, inválida) - 29.632 / 40.617 / 35.037
  - Pista 28.2°C, seria 4ª melhor se válida

---

## Análise de Consistência

### Por Bloco

**Bloco 1 (Validação):**
- Voltas válidas: 8/9 (89%) ✅
- Melhor: 1:45.195 / Média: 1:45.534
- Gap melhor-média: **0.339s** ✅
- **Muito consistente**

**Bloco 2 (Trabalho S2):**
- Voltas válidas: 6/11 (55%)
- Melhor: 1:45.097 / Média: 1:45.499
- Gap melhor-média: **0.402s**
- **Inconsistência esperada** durante trabalho focado

### Degradação (Bloco 1 - Set 1 novo)

**Primeiras 3 voltas válidas:** 1:46.482, 1:46.182, 1:45.475 (média: 1:46.046)
**Últimas 3 voltas válidas:** 1:45.535, 1:45.445, 1:45.195 (média: 1:45.392)

**Ganho de -0.654s** = pneus aquecendo + adaptação ao carro (não degradação)

---

## Combustível e Autonomia

**Consumo médio:** 2.72-2.78 L/lap
**Bloco 1:** 30L → 9 laps (consumo ~2.75 L/lap)
**Bloco 2:** 35L → 11 laps (consumo ~2.72 L/lap)

**Total consumido:** ~65L em 20 laps
**Estimativa corrida 60min:** ~32-34 laps → **87-92L** necessários (2 pit stops)

---

## Observações de Pilotagem

### TC 2 vs TC 3
- **Lap 14:** TC 2 testado (vs TC 3 padrão)
- **Resultado:** 1:45.642 (29.605 / 40.770 / 35.267)
- **Conclusão:** Volta válida e competitiva, mas não melhor que TC 3
- **Decisão:** Manter TC 3 como padrão

### Trabalho Setor 2 (T5-T9)

**Observações por curva:**

**T5 (Elf) - Tração:**
- Foco em apex tardio e saída limpa
- Melhorias visíveis em S2 (40.500 vs 40.547)

**T7-T8 (Stadium) - Fluidez:**
- Sequência técnica trabalhada
- Consistência melhorou (variação S2 ~±0.15s nas melhores)

**T9 (Topo subida) - Saída:**
- Preparação para reta longa
- S2 melhorou mas ainda +0.336s da referência

**Sensação geral S2:**
- Confortável em 7.5/10
- Margem de melhoria existe (+0.336s vs ref.)
- Temperatura alta dificultou trabalho

---

## Lições e Próximos Passos

### Conquistas do Treino 4 ✅

- **🏆 Melhor volta da semana:** 1:45.097 (-0.133s vs T3)
- **✅ Todos os setores melhoraram:**
  - S1: -0.083s (29.560 → 29.477)
  - S2: -0.047s (40.547 → 40.500)
  - S3: -0.152s (35.122 → 34.970)
- **✅ S3 praticamente perfeito:** +0.021s da referência!
- **✅ Setup validado:** Feeling 7.5/10, 89% válidas no Bloco 1
- **✅ S2 melhorou** conforme planejado
- **✅ Alta consistência** no Bloco 1 (gap 0.339s)

### Pontos de Atenção ⚠️

- **RF banda fria persistente:** 57-70°C (vs 75-85°C ideal)
  - Interno OK (81°C), mas não transfere para superfície
  - Limita grip em curvas rápidas

- **FL/LR superaquecem em pista >28°C:**
  - FL: até 97°C (+7°C do ideal)
  - LR: até 97°C (+5°C do ideal)
  - Risco de degradação em corrida quente

- **Temperatura de pista variável:**
  - Bloco 1: 25-26°C (ideal)
  - Bloco 2: 27.5-28.5°C (+2-3°C)
  - Setup sensível a variação térmica

- **Gap S2 ainda significativo:** +0.336s vs referência (maior gap remanescente)

---

## Ajustes Propostos para Treino 5

### 🔧 Prioridade 1: Resolver FL/LR Quentes

**Justificativa:** Mais crítico que RF frio (risco de degradação vs perda de grip)

**Ajuste:**
```
Pressão FL: 24.8 → 25.2 pit (+0.4) ⭐ CRÍTICO
Pressão LR: 24.5 → 24.9 pit (+0.4) ⭐ CRÍTICO
```

**Objetivo:** Reduzir deformação e temperatura em pista >27°C

**Resultado esperado:**
- FL: 97°C → 90-92°C ✅
- LR: 97°C → 92-94°C ✅

---

### 🔧 Prioridade 2: Tentar Aquecer RF Banda

**Justificativa:** Melhorar grip em curvas rápidas (S1)

**Ajuste:**
```
Pressão RF: 25.0 → 24.6 pit (-0.4)
```

**Objetivo:** Aumentar deformação → mais calor na banda de rodagem

**Resultado esperado:**
- Banda RF: 57-70°C → 72-78°C (melhoria parcial)
- Interno RF: manter ~81°C

**Plano B (se não funcionar):**
- Reduzir mais: RF 24.6 → 24.4 pit
- OU Brake duct front: 2 → 1

---

### 🔧 Setup Completo Proposto Treino 5

**Pressões pit (alteradas):**
- FL: ~~24.8~~ → **25.2** (+0.4)
- RF: ~~25.0~~ → **24.6** (-0.4)
- LR: ~~24.5~~ → **24.9** (+0.4)
- RR: **25.2** (manter)

**Geometria (manter):**
- Toe front: -0.20°
- Caster: 14.5°
- Camber: -4.0° / -3.5°

**Refrigeração (manter):**
- Brake ducts: 2 / 2

**Suspensão (manter):**
- ARB: 4 / 2

---

## Plano para Treino 5

**Estrutura:** S1 (Bloco 1) + S3 (Bloco 2)

### Bloco 1: Setor 1 (T1-T4)
**Duração:** 20-25 minutos
**Foco:** Melhorar gap de +0.103s → alvo < +0.050s

**Curvas-alvo:**
- **T1:** Freada forte, entrada agressiva
- **T3:** Curva longa, lift suave, tracionar cedo
- **T4:** Apex antecipado, tração limpa

**Meta S1:** < 29.400s (ganho de -0.077s vs 29.477 atual)

---

### Bloco 2: Setor 3 (T10-T16)
**Duração:** 25-30 minutos
**Foco:** Refinar gap de +0.021s → alvo 0.000s (igualar referência!)

**Curvas-alvo:**
- **T10:** Trail braking, evitar camber negativo
- **T14-T15 (chicane):** Fluidez, evitar sausage curbs, saída limpa
- **T16:** Não usar zebra interna, reaceleração cedo

**Meta S3:** ≤ 34.949s (igualar ou bater referência!)

---

### Metas Gerais Treino 5
- **Melhor volta:** < 1:45.0s (vs 1:45.097 atual)
- **S1:** < 29.400s (ganho -0.077s)
- **S3:** ≤ 34.949s (igualar referência)
- **S2:** Manter ~40.500s (foco nos outros setores)
- **Consistência:** >80% válidas
- **Temperaturas:** FL/LR controlados, RF melhor se possível

---

## Plano para Treino 6

**Objetivo:** Stint longo + degradação

**Estrutura:**
- 1 stint de 18-20 laps (pneus novos)
- Monitorar degradação média
- Simular ritmo de corrida
- Avaliar comportamento térmico em stint longo

**Observação:** Condição de corrida desconhecida, mas treino dará base para diferentes cenários

**Após T6:** Voltar para S2 se necessário (último ajuste fino antes da corrida)

---

## Anexos
- **data/session4.json** (fonte dos tempos - 20 laps)
- **data/session_4/tyre_stint1_friedolffinal.md** (dados de pneus - Bloco 1)
