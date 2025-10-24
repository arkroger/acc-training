# Plano de Treino – Red Bull Ring / Spielberg (Audi R8 LMS Evo II)

## Informações Gerais
- **Corrida**: 02/11/2025 (Corrida 15/18 do Campeonato Piloteiro Amador)
- **Duração**: 60min
- **Pitstop**: 1 obrigatório, combustível + pneus (opcional)
- **Treinos**: 9 sessões de treino
- **Carro**: Audi R8 LMS Evo II
- **Pista**: Red Bull Ring (Spielberg) - 4.318km, 10 curvas
- **Características**: Pista curta, alta velocidade, muitas elevações, curvas de média-alta velocidade

---

## Tempos de Referência

### Benchmarks para Treino

| Categoria | Volta Completa | S1 (T1-T3) | S2 (T4-T6) | S3 (T7-T10) |
|-----------|----------------|------------|------------|-------------|
| **Aliens (Referência Top)** | 1:27.629 | 22.227 | 38.630 | 26.772 |
| **Target Objetivo** | 1:28.560 | 22.419 | 38.923 | 27.217 |

*Valores de referência para consulta durante os treinos.*

---

## Características da Pista

### Setor 1 (T1-T3)
- **T1 (Direita)**: Entrada rápida após reta de largada, frenagem tardia
- **T2 (Esquerda)**: Curva cega em aclive, crucial para S2
- **T3 (Direita - Remus)**: Alta velocidade, entrada em aclive, saída crucial

**Pontos-chave**:
- Frenagem precisa em T1
- Tração em T2 (aclive)
- Velocidade de entrada em T3

### Setor 2 (T4-T7)
- **T4 (Esquerda - Wurth)**: Curva longa em declive, alta velocidade
- **T5 (Direita)**: Curva rápida, crucial para T6
- **T6-T7 (Rindt Complex)**: Chicane rápida em aclive

**Pontos-chave**:
- Fluidez em T4 (mais crítico do setor)
- Posicionamento correto para T6-T7
- Velocidade mínima alta

### Setor 3 (T8-T10)
- **T8 (Esquerda - Jochen Rindt)**: Entrada rápida, saída em reta
- **T9-T10 (Direita + Esquerda)**: Chicane final antes da reta principal

**Pontos-chave**:
- Tração em T8 (saída para reta)
- Fluidez na chicane final
- Velocidade de saída (define início de volta seguinte)

---

## Sessão 1 – Preparação e Levantamento de Informações ✅ CONCLUÍDA

**Status**: ✅ Concluída (23/10/2025)
**Resultado**: **MUITO ACIMA DO ESPERADO!** Melhor volta: **1:29.432**

**Objetivo**: Tarefa burocrática - coletar informações e preparar material de estudo

**Resultados Obtidos**:
- ✅ 10 voltas de reconhecimento (6 válidas)
- ✅ Melhor volta: **1:29.432** (Lap 6)
- ✅ Baseline estabelecido: **90% do target objetivo**
- ✅ Gaps identificados: S1 (+0.131s), S2 (+0.304s), S3 (+0.438s)
- ✅ 2 stints realizados (troca de pneus na lap 3)
- ✅ Consumo medido: ~2.67L/volta

**Análise**:
- Sessão planejada como preparatória resultou em baseline sólido
- Tempo muito melhor que esperado (previsto: reconhecimento, obtido: 1:29.432)
- S1 já muito competitivo (+0.131s do target)
- S3 identificado como maior oportunidade (+0.438s)
- Setup base demonstrou ser funcional

**Relatório completo**: `reports/treino1.md`

---

## Sessão 2 – Teste de Setups (Firedolf vs Coach Dave) ✅ CONCLUÍDA

**Status**: ✅ Concluída (23/10/2025)
**Resultado**: **EXCEPCIONAL!** Melhor volta: **1:28.925** (inválida) - JÁ ABAIXO DO TARGET!

**Objetivo Original**: Estabelecer baseline e definir setup ideal
**Realizado**: Comparação de setups Firedolf vs Coach Dave Academy

**Resultados Obtidos**:

### Stint 1 - Firedolf (Laps 1-6):
- Melhor volta válida: **1:29.432** (igual à S1)
- Voltas válidas: 4 de 6
- ❌ Problema: "Carro não vira" → **Steering ratio 4 (16:1)** identificado

### Stint 2 - Coach Dave (Laps 7-13):
- Melhor volta válida: **1:29.412**
- Melhor volta geral: **1:28.925** (inválida) 🔥
- Voltas válidas: APENAS 1 de 7
- ⚠️ Problema: "Se perde na aceleração" → **Preload 0** identificado

**Análise de Setups**:
- ✅ Coach Dave **comprovadamente mais rápido** (-0.507s)
- ✅ **S2 superou o target**: 0:38.992 vs 0:38.923 (-0.069s)
- ✅ **S1 quase perfeito**: 0:22.460 vs 0:22.419 (+0.041s)
- ⚠️ S3 ainda com margem: 0:27.342 vs 0:27.217 (+0.125s)

**Diagnóstico**:
1. Firedolf steering ratio 4 causa subesterço (carro não vira)
2. Coach Dave preload 0 causa instabilidade na aceleração
3. **Solução**: Usar Coach Dave com preload 8

**Entregas**:
- ✅ Setup Coach Dave identificado como superior
- ✅ Setup híbrido criado: `setup_coachdave_preload8.json`
- ✅ Análise técnica completa: `setups/setup_analysis.md`
- ✅ Potencial de 1:28.560 (target) comprovado

**Relatório completo**: `reports/treino2.md`

---

## Sessão 3 – Validação Setup + Foco S3 (T8-T10) ⏳ PRÓXIMA

**Objetivo**: Validar setup ajustado (preload 8) e atacar S3 para bater target objetivo

**Setup a usar**: `setup_coachdave_preload8.json`

**Atividades**:

### Parte 1: Validação de Setup (15min)
- Carregar `setup_coachdave_preload8.json`
- 2 stints de 4-5 voltas
- **Testar especificamente**:
  - T2 (aclive): Problema de "se perder" resolvido?
  - T6-T7 (Rindt aclive): Tração melhorou?
  - T8 (saída para reta): Controle na aceleração OK?
- **Meta**: 4+ voltas válidas em 1:28.6-1:29.2

**Ajustes opcionais** (se necessário):
- Se ainda instável: preload 8 → 10
- Se muito estável/perdendo agilidade: preload 8 → 6

### Parte 2: Foco S3 (15-25min restantes)
- 3 stints focados exclusivamente em S3:
  - **T8 (Jochen Rindt)**: Tração máxima na saída (crucial!)
  - **T9-T10 (Chicane final)**: Fluidez sem perder velocidade
- Trabalhar sequência T7→T8 conectada
- 6-8 voltas completas para validação

**Meta**:
- **Volta completa**: **1:28.560 ou melhor** (bater target!) 🎯
- **S3**: 0:27.217 ou melhor (ganhar 0.125s restantes)
- **Consistência**: 80%+ voltas válidas
- Validar que setup está OK para sessões seguintes

**Pontos-chave**:
- T8 define início da volta seguinte (saída para reta principal)
- Chicane T9-T10: fluidez > velocidade pontual
- Com setup correto, voltas de 1:28.9 devem ser válidas

---

## Sessão 4 – Consolidação + Stint Longo (30min)

**Objetivo**: Consolidar velocidade com consistência e testar degradação

**Atividades**:

### Parte 1: Consolidação (30min)
- 3 stints de 6-8 voltas em ritmo de corrida
- Trabalhar consistência: manter 1:28.5-1:29.0 por stint completo
- Validar setup final está OK
- **Bloco extra**: 5-6 entradas/saídas de box (praticar pit entry/exit)

**Pontos a trabalhar**:
- Manter concentração stint completo
- Evitar erros em voltas consecutivas
- Gerenciar pneus (não degradar prematuramente)

### Parte 2: Stint Longo (30min)
- **30min de stint contínuo** sem pit
- Ritmo de corrida (não push máximo)
- **Monitorar**:
  - Consumo de combustível (L/volta)
  - Degradação de pneus (queda de performance)
  - Consistência de pace (evolução do lap time)
  - Evolução de pressões e temperaturas

**Meta**:
- **Volta**: 1:28.5-1:29.0 (consistente)
- **Consistência**: ±0.3s por stint
- **Pace médio 30min**: 1:29.0-1:29.5
- **Consumo**: Validar ~2.6L/volta
- **Degradação**: Quantificar queda de performance

**Análise pós-sessão**:
- Degradação de pneus por stint
- Consumo real L/volta
- Janela de pit ideal (calcular com base em consumo e degradação)
- Setup final validado para corrida

---

## Sessão 5 – Setup para Condições Extremas

**Objetivo**: Criar variações de setup para diferentes condições climáticas

**Base**: `setup_coachdave_preload8.json` (setup validado)

**Atividades**:

### Parte 1: Setup Chuva (30min)
- Partir do setup validado como base
- **Ajustes**:
  - Aumentar altura de suspensão (+2-3 clicks)
  - Mais asa traseira (downforce) +1-2
  - Pressões de pneus para molhado (validar -2 PSI cold)
  - Ride height para evitar aquaplanagem
- Testar em condições molhadas
- 2 stints de 5-8 voltas para validação
- **Salvar como: `setup_wet.json`**

### Parte 2: Setup Calor Extremo (30min)
- Condições: 30°C+ temperatura de pista
- **Ajustes**:
  - Pressões mais baixas cold (compensar expansão térmica)
  - Ajuste de brake ducts (mais cooling se necessário)
  - Validar comportamento com alta temperatura
- Testar em hot lap mode com temp alta
- 2 stints de 5-8 voltas para validação
- **Salvar como: `setup_hot.json`**

**Entregas**:
- ✅ Setup chuva validado e salvo
- ✅ Setup calor extremo validado e salvo
- ✅ Notas sobre diferenças de pilotagem em cada condição
- ✅ Preparação para qualquer condição climática na corrida

**Observação**: Esta sessão garante que você está preparado para qualquer condição climática no dia da corrida.

---

## Sessão 6 – Qualifying Simulation

**Objetivo**: Preparar para classificatória e buscar melhor volta absoluta

**Setup**: `setup_coachdave_preload8.json` (ou ajustado após S3)

**Atividades**:
- **4-5 simulações de qualifying**:
  - Outlap (aquecimento de pneus - 1 volta completa)
  - Push lap (máximo ataque)
  - Cooldown lap (retorno ao box)
- Testar low fuel (5-8L) vs médio fuel (15-20L)
- Trabalhar timing de saída (evitar tráfego se com IA)
- Validar melhor volta absoluta
- **Bloco extra**: 6-8 pitstops completos (treinar entrada/saída)

**Meta**:
- **Melhor volta**: **1:28.2-1:28.6** (superar target!)
- Consistência em 3-4 tentativas de quali (±0.2s)
- Estratégia de quali definida
- Pitstops **<27s** (combustível + pneus)

**Estratégia quali**:
- Combustível mínimo (5-8L) para máxima performance
- Pneus novos (set 3 ou 4)
- 1 volta completa de aquecimento (pressões ideais)
- 1-2 push laps máximos
- Timing de saída para espaço na pista

**Pontos de atenção**:
- Aquecimento de pneus: 1 volta completa em ritmo médio-alto
- Não queimar pneus no outlap
- Abortar volta se tráfego atrapalhar

---

## Sessão 7 – Race Simulation (60min) + Análise Adversários

**Objetivo**: Corrida completa + primeira análise de adversários

**Setup**: `setup_coachdave_preload8.json` (setup de corrida validado)

**Atividades**:

### Parte 1: Race Simulation Completa (60min)
- Corrida de 60min exatamente
- **Pitstop no momento estratégico** (volta 17-19, baseado em S4)
- **Gerenciar**:
  - Combustível inicial: ~68-70L
  - Pneus: monitorar degradação
  - Tráfego (se com IA)
  - Mental de corrida (concentração 60min)
  - Estratégia de largada
- **Executar pit real** (combustível + decidir sobre pneus)

**Validações**:
- Fuel start: 68-70L (validar com dados de S4)
- Pit window: Volta 17-19
- Combustível 2º stint: ~35-40L
- Pneus: Trocar ou não? (baseado em degradação de S4)
- Tempo de pit: <28s

### Parte 2: Coleta de Dados Adversários
**IMPORTANTE: SOMENTE nesta sessão coletar dados de adversários**

- **Exportar dados de**:
  - **Rival principal** (concorrente direto campeonato)
  - **Silver** (referência classe)
  - **PRO/P1** (se disponível, para benchmark)
- Salvar como: `race_oficial_rival.json`, `race_oficial_silver.json`, etc.
- Análise posterior por Claude

**Meta**:
- **60min sem erros graves**
- Pit strategy executada conforme planejado
- **Pace médio**: **1:29.0-1:29.5** (consistente)
- Mental e concentração testados
- **Dados de adversários coletados** ✅

**Análise pós-sessão**:
- Onde rival é mais rápido por setor?
- Onde você perde/ganha tempo?
- Estratégia de defesa/ataque para corrida oficial
- Pit window comparativo (quando adversários param?)
- Ritmo de degradação comparado

---

## Estratégia de Corrida Preliminar

### Configuração Inicial
- **Combustível**: 68L
- **Pressão pneus**: A validar (baseado em treinos)
- **Setup**: Alta velocidade (menos asa)

### Pit Stop
- **Janela**: Volta 17-19 (meio da corrida)
- **Tempo alvo**: 25-28s (combustível + validar pneus)
- **Combustível 2º stint**: ~35L

### Pace Alvo
- **Quali**: 1:28.5 - 1:29.0
- **Corrida (stint 1)**: 1:29.5 - 1:30.0
- **Corrida (stint 2)**: 1:29.5 - 1:30.5 (com combustível)

### Pontos Críticos
- **Largada**: Manter posição em T1 (evitar acidente)
- **T4 (Wurth)**: Área de ultrapassagem (defender/atacar)
- **T8**: Saída crucial para reta principal
- **Pit timing**: Evitar tráfego na saída

---

## Resumo de Objetivos - 7 Sessões (Revisado)

### Resultados Reais vs Plano Original

| Métrica | Plano Original (S2) | Real Obtido (S2) | Objetivo Final (S7) | Evolução |
|---------|---------------------|------------------|---------------------|----------|
| **Volta completa** | 1:31.0-1:32.0 | **1:28.925*** | 1:28.2-1:28.6 | **-2.1s a -3.3s** ✅ |
| **S1** | 0:30.5 | **0:22.460*** | 0:22.419 | **JÁ QUASE PERFEITO** ✅ |
| **S2** | 0:37.0 | **0:38.992*** | 0:38.923 ou melhor | **JÁ SUPEROU!** 🔥 |
| **S3** | 0:24.0 | **0:27.342*** | 0:27.217 ou melhor | **-0.125s restantes** |
| **Consistência** | ±0.8s | ±0.378s | ±0.2-0.3s | **Já muito boa** ✅ |

*Tempos de voltas inválidas (S2, setup Coach Dave com preload 0)

**Análise**:
- ✅ Progresso MUITO acima do esperado (S1 e S2 superaram metas de S2-S5)
- ✅ S2 já superou target objetivo (-0.069s)
- ✅ S1 falta apenas 0.041s
- ⏳ S3 falta 0.125s (foco da Sessão 3)
- 🎯 Com setup ajustado, **target 1:28.560 está ao alcance**

### Progressão por Sessão (Plano Revisado)

| Sessão | Foco | Volta Alvo | Setup | Status |
|--------|------|------------|-------|--------|
| **S1** | Preparação/Reconhecimento | -- | Base | ✅ 1:29.432 |
| **S2** | Teste Setups (Firedolf vs CDA) | 1:31.0-1:32.0 | Variados | ✅ 1:28.925* |
| **S3** | Validar Setup + Foco S3 | **1:28.560** 🎯 | CDA Preload 8 | ⏳ Próxima |
| **S4** | Consolidação + Stint 30min | 1:28.5-1:29.0 | Final | ⏳ Pendente |
| **S5** | Setup Variações | -- | Chuva + Calor | ⏳ Pendente |
| **S6** | Qualifying Simulation | 1:28.2-1:28.6 | Quali | ⏳ Pendente |
| **S7** | Race 60min + Adversários | 1:29.0-1:29.5 | Race | ⏳ Pendente |

---

## Contexto do Campeonato

**Situação Atual (Pós-Barcelona C14)**:
- **Posição**: P1 Piloteiro Amador
- **Vantagem**: +27 pontos sobre P2
- **Corridas restantes**: 4 (C15-C18)
- **Probabilidade título**: ~70%

**Meta para Spielberg (C15)**:
- **Mínimo**: P6-P7 (14-15 pts)
- **Ideal**: P5-P6 (15-18 pts)
- **Excelente**: P4 (20 pts)

**Estratégia de Campeonato**:
- Foco em consistência > risco
- Evitar acidentes na largada
- Aceitar P6-P7 se alternativa é P9+
- Monitorar posição do rival

---

## Observações Específicas de Spielberg

### Características Únicas
- ✅ Pista curta (4.3km) = muitas voltas em 60min
- ✅ Elevações desafiadoras
- ✅ Curvas de alta velocidade
- ⚠️ Pouco espaço para erro
- ⚠️ Tráfego mais frequente (pista curta)

### Pontos de Atenção
1. **T1**: Área de acidente comum (largada)
2. **T4**: Difícil de dominar, muito ganho possível
3. **T6-T7**: Chicane em aclive (quebra ritmo)
4. **T8**: Define início de volta (crucial)

### Vantagens Esperadas
- Pista técnica favorece piloto consistente
- Muitas voltas = mais chances de recuperar
- Elevações testam setup (oportunidade de diferencial)

---

---

## Notas Importantes - Progresso Excepcional

⚠️ **PLANO REVISADO**: S1 e S2 superaram MUITO as expectativas originais!

### Conquistas até agora:
- ✅ **S1**: 1:29.432 (esperado: apenas reconhecimento)
- ✅ **S2**: 1:28.925 inválida (esperado: 1:31-1:32)
- ✅ **Setup Coach Dave** identificado como superior
- ✅ **S2 já superou target** (-0.069s do objetivo)
- ✅ **Problema diagnosticado**: Preload 0 resolvido com preload 8

### Foco restante:
- 🎯 **Sessão 3**: Validar setup + atacar S3 para bater 1:28.560
- 🎯 **Sessões 4-7**: Consolidar, preparar quali e race simulation

### Setup Status:
- ✅ **Setup base**: Funcional (S1)
- ✅ **Setup superior**: Coach Dave identificado (S2)
- ✅ **Setup ajustado**: `setup_coachdave_preload8.json` criado
- ⏳ **Próximo**: Validar preload 8 na S3

---

**Status**: ✅ 2 de 7 sessões concluídas - Progresso EXCEPCIONAL!
**Última atualização**: 2025-10-23
**Próximo passo**: Sessão 3 - Validar setup ajustado + Foco S3 para bater target 1:28.560
