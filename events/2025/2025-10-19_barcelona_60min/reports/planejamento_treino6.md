# Planejamento Treino 6 – Barcelona (Consolidação Final)

## Contexto e Situação Atual

### Histórico de Performance
| Treino | Melhor Volta | Evolução | Gaps (S1/S2/S3) | Status |
|--------|--------------|----------|-----------------|--------|
| T1 | 1:46.352 | baseline | +0.540 / +1.088 / +0.807 | Reconhecimento |
| T2 | 1:45.512 | -0.840s | +0.495 / +0.646 / +0.356 | Setup ajustado |
| T3 | 1:45.230 | -0.282s | +0.186 / +0.383 / +0.173 | Setup otimizado |
| T4 | **1:45.097** 🏆 | -0.133s | +0.103 / +0.336 / **+0.021** | Melhor semana |
| T5 | 1:45.112 | +0.015s ❌ | +0.161 / **+0.208** / +0.058 | Estagnação |

> **Referência:** 1:44.487 (S1: 29.374 / S2: 40.164 / S3: 34.949)

### Análise de Gaps Atual

**Melhor absoluto por setor:**
| Setor | Melhor | Treino | Gap Ref. | Tendência |
|-------|--------|--------|----------|-----------|
| S1 | 29.477 | T4 | +0.103s | ⚠️ T5 piorou para 29.535 (+0.161s) |
| S2 | **40.372** | T5 | **+0.208s** | ✅ Melhorando (-0.128s vs T4) |
| S3 | 34.970 | T4 | +0.021s | ⚠️ T5 piorou para 35.007 (+0.058s) |

**Maior oportunidade:** S2 com +0.208s (único setor melhorando)

### Problema Persistente: FR Frio

**Histórico temperaturas FR:**
- T4: 79-82°C interno (banda 57-70°C) com RF 25.0 PSI
- T5: 78-85°C interno (banda ~70-80°C estimada) com RF 24.6 PSI
- **Ajuste -0.4 PSI teve impacto mínimo**

**Consequências:**
- Gap FL-FR: 8-14°C (desbalanceamento térmico)
- Perda de grip curvas rápidas (S1)
- Aderência percebida 7.5 → 6.5 no fim dos stints

### Lição Importante do T5

**Trabalho focado não funcionou:**
- S1 focado → piorou +0.058s
- S3 focado → piorou +0.037s
- S2 **sem foco** → melhorou -0.128s ✅

**Hipótese:** Over-driving em setores focados. S2 melhorou naturalmente com pilotagem relaxada.

---

## Objetivo Principal do Treino 6

### Filosofia
**Consolidar desempenho + última tentativa FR + preparação para corrida**

É o último treino antes da corrida - **não arriscar**, mas explorar última oportunidade.

### Objetivos Primários
1. **Validar setup** com última tentativa moderada de resolver FR
2. **Trabalhar S2** naturalmente (maior gap +0.208s, respondendo bem)
3. **Stint médio** para avaliar degradação e ritmo de corrida

### Objetivos Secundários
- Confirmar consumo de combustível para estratégia (meta: 2.75 L/lap)
- Testar consistência em stint de 15+ voltas
- Avaliar comportamento térmico prolongado
- Mentalizar ritmo de corrida (não buscar volta única)

---

## Setup Proposto Treino 6

### Setup Base
**Friedolf Otimizado (T4/T5)** - comprovado em 1:45.097

### Pressões de Pneus (pit)

**OPÇÃO A - Última tentativa FR (recomendada):**
```
FL: 25.2 PSI (manter T5)
RF: 24.3 PSI (T5: 24.6 → redução -0.3) ⭐
LR: 24.9 PSI (manter T5)
RR: 25.2 PSI (manter T4/T5)
```

**Justificativa RF 24.3:**
- Ajuste moderado, não radical (total -0.7 vs T4)
- Última tentativa antes de aceitar limitação
- Reversível no pit se piorar

**PLANO B - Se temperatura pista > 27°C:**
```
FL: 25.2 → 25.4 (+0.2) controlar superaquecimento
LR: 24.9 → 25.1 (+0.2) controlar superaquecimento
```

### Geometria (MANTER T4 - validado)
```
Toe front: -0.20°
Caster: 14.5°
Camber: -4.0° front / -3.5° rear
```

### Suspensão (MANTER T4)
```
ARB: 4 front / 2 rear
Preload: 80 Nm
Bump/Rebound: [confirmar valores exatos T4]
Ride height: [confirmar valores T4]
```

### Freios (MANTER T4)
```
Brake ducts: 2 / 2
Brake pads: Compound 2-3 front / 1 rear
Brake bias: 56%
```

### Eletrônica
```
TC: 3 (validado T4)
ABS: 3
```

---

## Estrutura do Treino

### Duração Total: 50 minutos

---

## BLOCO 1: Validação + Teste Final FR

**Duração:** 15-20 minutos
**Laps estimados:** 9-11 voltas
**Combustível:** 30L
**Tyre set:** 1 (novo)
**Temperatura esperada:** 25-27°C pista

### Objetivos Bloco 1
1. Validar RF 24.3 PSI - banda aqueceu?
2. Baseline de temperaturas e tempos
3. Confirmar feeling e tempo próximo 1:45.0-1:45.2

### Checklist de Validação

| Item | Meta | Fonte | Status |
|------|------|-------|--------|
| **Temp FR banda** | 75-85°C | Tela ACC | ⬜ |
| **Temp FR interno** | 80-85°C | JSON telemetria | ⬜ |
| **Gap FL-FR** | < 8°C | Cálculo | ⬜ |
| **Temp FL** | 86-92°C | JSON telemetria | ⬜ |
| **Temp LR** | 88-94°C | JSON telemetria | ⬜ |
| **Melhor volta** | < 1:45.3s | Timing | ⬜ |
| **Tempo médio** | < 1:45.6s | Timing | ⬜ |
| **% válidas** | ≥ 70% | Contagem | ⬜ |
| **Feeling piloto** | ≥ 7/10 | Sensação | ⬜ |

### Foco de Pilotagem Bloco 1
- **Primeiras 2-3 voltas:** Aquecer pneus, explorar grip
- **Voltas 4-7:** Encontrar ritmo, avaliar FR
- **Voltas 8-10:** Voltas rápidas mas sem forçar
- **Monitorar:** Sensação FR em curvas rápidas (T1, T3, T9)

### DECISÃO CRÍTICA Pós-Bloco 1

**🟢 CENÁRIO A - FR MELHOROU (banda 75-85°C):**
- ✅ **Manter RF 24.3 PSI** no pit
- ✅ **Seguir para Bloco 2A** (foco agressivo S2)
- ✅ **Meta:** 40.250s ou melhor

**🟡 CENÁRIO B - FR IGUAL (banda 70-75°C):**
- ⚠️ **Aceitar limitação FR** (problema estrutural confirmado)
- ⚠️ **Manter RF 24.3 PSI** (não piorou, pode manter)
- ⚠️ **Seguir para Bloco 2B** (stint médio + S2 natural)
- ⚠️ **Meta:** 40.300s (ganho natural)

**🔴 CENÁRIO C - FR PIOROU (banda < 70°C):**
- ❌ **Reverter RF para 24.6 PSI** no pit
- ❌ **Seguir para Bloco 2B** (stint médio conservador)
- ❌ **Meta:** Manter 40.372s, foco em consistência

---

## BLOCO 2A: Trabalho Intensivo S2 (se FR melhorar)

**Duração:** 30-35 minutos
**Laps estimados:** 15-17 voltas
**Combustível:** 40L (pit stop + reabastecimento)
**Tyre set:** 2 (novo)

### Objetivo
Reduzir gap S2 de **+0.208s** para **< +0.100s**

### Estrutura Bloco 2A
- **Laps 1-3:** Aquecimento, baseline
- **Laps 4-10:** Trabalho focado S2 (T5-T9)
- **Laps 11-17:** Consolidar ganhos, voltas rápidas

### Foco por Curva - Setor 2 (T5-T9)

#### T5 (Elf - Rápida Direita)
**Características:**
- Velocidade ~180-200 km/h
- Curva de tração (saída longa)
- Gear: 4ª marcha

**Pontos de trabalho:**
1. **Entrada:** Velocidade mínima alta, não sobrefrear
2. **Apex:** Tardio, carregar velocidade
3. **Saída:** Tração limpa prioritária (impacta resto do S2)
4. **Evitar:** Over-slow (entrada lenta demais)

**Referência mental:** "Confiar no grip, tracionar cedo"

---

#### T7-T8 (Stadium - Complexo Técnico)
**Características:**
- Sequência esquerda-direita
- Perda de visibilidade em T7
- Saída T8 para descida

**Pontos de trabalho:**
1. **T7 entrada:** Trail braking moderado, não travar muito
2. **T7→T8 transição:** Fluidez, evitar correções de volante
3. **T8 saída:** Acelerar progressivo, preparar T9
4. **Evitar:** Rushear T7, perder T8

**Referência mental:** "Smooth, paciência, construir velocidade"

---

#### T9 (Topo Subida - Direita Média)
**Características:**
- Final de subida, carro leve na entrada
- Saída para reta mais longa
- Gear: 3ª ou 4ª (confirmar)

**Pontos de trabalho:**
1. **Entrada:** Carro instável (subida), suave no freio
2. **Apex:** Antecipado, priorizar saída
3. **Saída:** Tração máxima, reta longa à frente
4. **Evitar:** Entrada agressiva (instabilidade)

**Referência mental:** "Apex cedo, tracionar forte"

---

### Metas Bloco 2A

| Métrica S2 | Mínimo | Alvo | Excelente |
|------------|--------|------|-----------|
| **Melhor S2** | 40.300s | **40.250s** | < 40.200s |
| **Média S2 (válidas)** | 40.450s | **40.400s** | < 40.350s |
| **Gap S2 vs Ref.** | +0.136s | **+0.086s** | < +0.050s |

**Voltas válidas:** ≥ 80% (12-14 de 15-17 laps)

---

## BLOCO 2B: Stint Médio + S2 Natural (se FR não melhorar)

**Duração:** 30-35 minutos
**Laps estimados:** 15-17 voltas
**Combustível:** 40-45L (pit stop + reabastecimento)
**Tyre set:** 2 (novo)

### Objetivo
Simular ritmo de corrida + deixar S2 melhorar naturalmente (lição T5)

### Filosofia Bloco 2B
- **70% foco:** Ritmo de corrida, consistência, degradação
- **30% foco:** S2 natural (não forçar, deixar acontecer)
- **Aceitar FR frio:** Compensar em pilotagem, não lutar contra setup

### Estrutura Bloco 2B
- **Laps 1-5:** Baseline ritmo (1:45.0-1:45.3)
- **Laps 6-12:** Sustentação ritmo (1:45.2-1:45.5)
- **Laps 13-17:** Avaliar degradação (1:45.3-1:45.6)

### Métricas Stint Médio

**Ritmo de corrida esperado:**
| Fase | Laps | Tempo Alvo | Observação |
|------|------|------------|------------|
| Base | 1-5 | 1:45.0-1:45.3 | Pneus frescos |
| Sustentação | 6-12 | 1:45.2-1:45.5 | Pneus estáveis |
| Degradação | 13-17 | 1:45.3-1:45.6 | Avaliar queda |

**Degradação aceitável:** < 0.4s (média primeiras 5 vs últimas 5)

**Combustível:**
- Consumo médio esperado: 2.75-2.80 L/lap
- Autonomia 15 laps: ~42L
- Autonomia 17 laps: ~47L

### Pilotagem Bloco 2B
- **Mental:** Relaxado, ritmo constante
- **S2:** Deixar vir naturalmente (lição T5)
- **Evitar:** Forçar voltas únicas, over-driving
- **Focar:** Repetibilidade, feeling do carro

### Metas Bloco 2B

| Métrica | Mínimo | Alvo | Excelente |
|---------|--------|------|-----------|
| **Melhor volta** | 1:45.200 | **1:45.100** | < 1:45.000 |
| **Média válidas** | 1:45.600 | **1:45.400** | < 1:45.300 |
| **Melhor S2** | 40.350s | **40.300s** | < 40.250s |
| **Degradação** | < 0.500s | **< 0.400s** | < 0.300s |
| **% válidas** | 75% | **80%** | > 85% |

---

## Metas Gerais Treino 6

### Tempos por Nível

| Métrica | Mínimo | Alvo | Excelente |
|---------|--------|------|-----------|
| **Melhor volta** | 1:45.200 | **1:45.000** | < 1:44.900 |
| **Tempo médio** | 1:45.600 | **1:45.400** | < 1:45.300 |
| **S1** | 29.550 | **29.450** | < 29.400 |
| **S2** | 40.300 | **40.250** | < 40.200 |
| **S3** | 35.050 | **35.000** | < 34.970 |

### Critérios de Temperatura

**FR (Problema Crítico):**
| Medida | Crítico ❌ | Aceitável ⚠️ | Ideal ✅ |
|--------|-----------|-------------|----------|
| Banda (tela ACC) | < 70°C | 70-75°C | **75-85°C** |
| Interno (JSON) | < 78°C | 78-82°C | **80-85°C** |

**FL/LR (Controle):**
| Pneu | Crítico ❌ | Aceitável ⚠️ | Ideal ✅ |
|------|-----------|-------------|----------|
| FL | > 97°C | 93-97°C | **86-92°C** |
| LR | > 97°C | 93-97°C | **88-94°C** |

**Gap térmico FL-FR:**
- Crítico: > 12°C ❌
- Aceitável: 8-12°C ⚠️
- Ideal: < 8°C ✅

### Critérios de Consistência

| Métrica | Mínimo | Alvo | Excelente |
|---------|--------|------|-----------|
| **% voltas válidas** | 70% | **80%** | > 85% |
| **Gap melhor-média** | < 0.500s | **< 0.400s** | < 0.300s |
| **Degradação stint** | < 0.500s | **< 0.400s** | < 0.300s |

---

## Validação Setup para Corrida

### ✅ Setup APROVADO se:
- [ ] Melhor volta ≤ 1:45.100
- [ ] FR banda ≥ 75°C **OU** feeling ≥ 7.5/10 (compensar pilotagem)
- [ ] FL/LR < 95°C (sem risco degradação)
- [ ] Consistência ≥ 75% válidas
- [ ] Feeling geral ≥ 7/10
- [ ] Degradação < 0.4s em stint médio

**→ Usar setup T6 na corrida sem alterações**

---

### ⚠️ Setup APROVADO COM RESSALVAS se:
- [ ] Melhor volta 1:45.100-1:45.250
- [ ] FR banda < 75°C **MAS** feeling ≥ 7/10
- [ ] FL/LR até 97°C (gerenciável em stint)
- [ ] Consistência 70-75%
- [ ] Degradação 0.4-0.5s

**→ Usar setup T6 mas monitorar térmicos durante corrida**

---

### ❌ Setup REPROVADO se:
- [ ] Melhor volta > 1:45.250 (pior que T5)
- [ ] FR banda < 70°C **E** feeling < 7/10
- [ ] FL/LR > 98°C (risco degradação severa)
- [ ] Consistência < 70%
- [ ] Degradação > 0.5s

**→ Rever setup antes da corrida OU aceitar limitação atual**

---

## Checklist Pré-Treino

### Setup
- [ ] **Pressões pit confirmadas:** FL 25.2 / **RF 24.3** / LR 24.9 / RR 25.2
- [ ] **Toe front:** -0.20° (crítico)
- [ ] **Caster:** 14.5°
- [ ] **Camber:** -4.0° / -3.5°
- [ ] **ARB:** 4 / 2
- [ ] **Preload:** 80 Nm
- [ ] **Brake ducts:** 2 / 2
- [ ] **Brake pads:** Compound 2-3 / 1
- [ ] **Brake bias:** 56%
- [ ] **TC:** 3
- [ ] **ABS:** 3

### Combustível
- [ ] **Bloco 1:** 30L (9-11 laps)
- [ ] **Bloco 2:** 40-45L (15-17 laps)
- [ ] **Reserva:** Suficiente para outlap/inlap

### Planejamento
- [ ] Checklist temperaturas disponível (impressa ou tela)
- [ ] Plano B RF pronto (24.6 se piorar)
- [ ] Plano B FL/LR (+0.2 se pista > 27°C)
- [ ] Critérios decisão Bloco 1 → 2A/2B claros

### Mental
- [ ] **Mentalidade:** Consolidar, não arriscar
- [ ] **Lembrar:** S2 melhora sem pressão (lição T5)
- [ ] **Aceitar:** FR frio pode ser limitação estrutural
- [ ] **Foco:** Ritmo de corrida, não volta única
- [ ] **Último treino:** Validar setup para corrida

---

## Plano de Contingência

### Se Bloco 1 desastroso (> 1:45.5)
1. Verificar pressões hot no pit
2. Conferir setup (toe, caster, ARB)
3. Reverter RF 24.6 se muito frio
4. Considerar reverter total para setup T4

### Se temperaturas críticas (FL/LR > 98°C)
1. Aumentar pressões: FL +0.2-0.4 / LR +0.2-0.4
2. Verificar brake ducts (considerar 3/3)
3. Reduzir agressividade frenagem

### Se FR extremamente frio (< 65°C banda)
1. Reverter RF imediatamente para 24.6
2. Se continuar: testar RF 25.0 (T4)
3. Considerar brake duct 2→1 (mais radical)
4. OU aceitar limitação e focar compensação pilotagem

---

## Dados de Referência

### Melhor Volta da Semana (T4)
**1:45.097** - lap 15, stint 2, pista 28.0°C
- S1: 29.597 (não o melhor individual)
- S2: **40.500** (melhor S2 até T4)
- S3: 35.000

### Melhores Setores Individuais
- **S1:** 29.477 (T4, lap 5)
- **S2:** 40.372 (T5, lap 6) ← recorde atual
- **S3:** 34.970 (T4, lap 12)

**Volta teórica:** 1:44.819 (+0.332s da ref. 1:44.487)

### Referência Oficial
**1:44.487**
- S1: 29.374
- S2: 40.164
- S3: 34.949

---

## Observações Finais

### Aprendizados da Semana
1. **Setup T4 funciona:** 1:45.097 comprovado
2. **FR frio persistente:** Ajustes pressão têm impacto limitado
3. **S2 responde bem:** Melhorou -0.128s sem foco direto (T5)
4. **Over-driving não funciona:** T5 mostrou que trabalho focado piorou S1/S3
5. **Consistência > volta única:** Preparação para corrida 60min

### Estratégia Mental T6
- **Foco primário:** Validar setup para corrida
- **Foco secundário:** S2 natural (não forçar)
- **Aceitar:** FR pode ser limitação (compensar pilotagem)
- **Evitar:** Buscar volta heroica, over-driving
- **Priorizar:** Ritmo repetível, feeling do carro

### Próximos Passos Pós-T6
- Analisar session6.json (telemetria completa)
- Gerar relatório treino6.md
- Atualizar evolucao_treinos.md
- **Decisão final setup corrida** (baseado em critérios validação)
- Planejar estratégia corrida (pit stops, combustível, pneus)

---

**Última atualização:** 09/10/2025
**Próximo treino:** T6 (último antes da corrida 19/10)
**Status:** Planejamento finalizado ✅
