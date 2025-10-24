# Análise de Setups - Red Bull Ring / Spielberg

## Setups Testados

### 1. Firedolf (FRI3_R8EVO2_RBR_RS_20_25_v1.9.8.json)
**Testado:** Sessão 2, Laps 1-6

**Performance:**
- Melhor volta: **1:29.432**
- Voltas válidas: 4 de 6

**Características:**
- ❌ Steering ratio 4 (16:1) = Menos sensível, carro "não vira"
- ✅ Preload 16 = Boa tração, estável na aceleração
- ✅ ABS 3 = Seguro, mas menos eficiente

**Veredito:** Setup seguro e previsível, mas mais lento.

---

### 2. Coach Dave Academy (CDA_22_25.json)
**Testado:** Sessão 2, Laps 7-13

**Performance:**
- Melhor volta válida: **1:29.412**
- Melhor volta geral: **1:28.925** (INVÁLIDA)
- Voltas válidas: **APENAS 1 de 7** ⚠️

**Características:**
- ✅ Steering ratio 3 (13:1) = Mais direto, carro responsivo
- ❌ Preload 0 = Diferencial muito aberto, instável na aceleração
- ✅ ABS 2 = Menos intrusivo, mais controle
- ✅ Caster 34 = Muito estável em reta

**Veredito:** MUITO rápido (-0.5s), mas incontrolável com preload 0.

**Problema identificado:**
- Preload 0 causa perda de tração na saída de curvas
- Resulta em muitas voltas inválidas (track limits)
- "Carro se perde na aceleração" - diagnóstico preciso do piloto

---

### 3. Coach Dave Ajustado (setup_coachdave_preload8.json) ⭐ RECOMENDADO
**Criado:** Pós-análise Sessão 2
**Status:** Aguardando teste (Sessão 3)

**Mudanças vs Coach Dave original:**
```diff
- "preload": 0
+ "preload": 8
```

**Objetivo:**
- Manter velocidade do Coach Dave (1:28.925)
- Resolver instabilidade na aceleração
- Aumentar taxa de voltas válidas

**Expectativa:**
- Volta: **1:28.6-1:29.2** (consistente, válida)
- Melhor controle em T2, T6-T7, T8 (aclives)
- Menos track limits

---

## Comparação Técnica Detalhada

| Parâmetro | Firedolf | Coach Dave | CDA Preload 8 |
|-----------|----------|------------|---------------|
| **Steering Ratio** | 4 (16:1) ❌ | 3 (13:1) ✅ | 3 (13:1) ✅ |
| **ABS** | 3 | 2 ✅ | 2 ✅ |
| **Caster** | 24 | 34 ✅ | 34 ✅ |
| **Preload** | 16 ⚠️ | 0 ❌ | **8** ✅ |
| **ARB Front** | 4 | 4 | 4 |
| **ARB Rear** | 2 | 0 ✅ | 0 ✅ |
| **Pressões (PSI)** | [53,57,50,51] | [54,58,47,51] ✅ | [54,58,47,51] ✅ |
| **Toe Traseiro** | 52 | 43 ✅ | 43 ✅ |
| **Wheel Rate** | [2,2,1,1] | [0,0,0,0] ✅ | [0,0,0,0] ✅ |
| **Rebound** | 22-30 | 38-49 ✅ | 38-49 ✅ |

**Legenda:**
- ✅ Melhor configuração
- ⚠️ Médio/Compromisso
- ❌ Problemático

---

## Análise por Aspecto

### Steering Ratio (Sensibilidade do Volante)
- **Ratio 4 (Firedolf):** 16:1 = Volante menos sensível
  - Precisa girar mais para mesma rotação das rodas
  - Resulta em subesterço percebido
  - **Não recomendado para Spielberg** (muitas curvas técnicas)

- **Ratio 3 (Coach Dave):** 13:1 = Volante mais direto
  - Resposta mais rápida
  - Melhor para curvas técnicas
  - **Recomendado** ✅

### Preload (Diferencial)
- **0 (Coach Dave original):** Diferencial muito aberto
  - Rodas podem girar em velocidades muito diferentes
  - Perda de tração na saída (rodas patinando)
  - **Problemático em Spielberg** (muitos aclives: T2, T6-T7, T8)

- **8 (Coach Dave ajustado):** Compromisso ideal
  - Mantém agilidade
  - Melhora tração em aclives
  - **Recomendado para Spielberg** ✅

- **16 (Firedolf):** Muito fechado
  - Excelente tração
  - Mas perde agilidade em curvas rápidas
  - Pode causar subesterço

### ABS
- **ABS 3:** Mais intrusivo, mais seguro
- **ABS 2:** Menos intrusivo, mais controle (quando dominado)
  - **Recomendado para pilotos intermediários+** ✅

### Anti-Roll Bar (ARB)
- **ARB Traseiro 0 (Coach Dave):** Mais grip mecânico
  - Traseira mais plantada
  - Melhor em curvas de alta velocidade
  - **Ideal para Spielberg** ✅

---

## Recomendações para Sessão 3

### 🎯 Setup a Usar
**`setup_coachdave_preload8.json`**

### 📋 Validação do Setup (15min)
1. Carregar setup no ACC
2. Fazer 2 stints de 4-5 voltas cada
3. **Testar especificamente:**
   - T2 (aclive): Carro ainda se perde?
   - T6-T7 (Rindt aclive): Tração melhorou?
   - T8 (saída para reta): Controle na aceleração?
4. **Meta:** 4+ voltas válidas em 1:28.6-1:29.2

### 🔧 Ajustes Opcionais (se necessário)

**Se ainda instável na aceleração:**
```diff
- "preload": 8
+ "preload": 10
```

**Se muito estável mas perdendo agilidade:**
```diff
- "preload": 8
+ "preload": 6
```

**Se pressão traseira esquerda muito baixa:**
```diff
- "tyrePressure": [ 54, 58, 47, 51 ]
+ "tyrePressure": [ 54, 58, 49, 51 ]
```

---

## Histórico de Performance

| Setup | Sessão | Melhor Volta | Voltas Válidas | Observações |
|-------|--------|--------------|----------------|-------------|
| Base (S1) | 1 | 1:29.432 | 6 de 10 | Baseline inicial |
| Firedolf | 2 | 1:29.432 | 4 de 6 | Não vira (ratio 4) |
| Coach Dave | 2 | 1:28.925* | 1 de 7 | Rápido mas instável (preload 0) |
| CDA Preload 8 | 3 | TBD | TBD | Aguardando teste |

*Volta inválida

---

## Arquivos

```plaintext
setups/
├── FRI3_R8EVO2_RBR_RS_20_25_v1.9.8.json    (Firedolf - não recomendado)
├── CDA_22_25.json                          (Coach Dave original - muito rápido mas instável)
├── setup_coachdave_preload8.json           (⭐ RECOMENDADO para Sessão 3)
└── setup_analysis.md                       (Este arquivo)
```

---

**Criado:** 23/10/2025 (Pós-Sessão 2)
**Próximo teste:** Sessão 3 - Validação do setup ajustado
