# Planejamento Treino 3 – Consolidação de Setup

## Informações Gerais
- **Data prevista:** A definir
- **Duração total:** 50 minutos
- **Objetivo:** Comparar setups e consolidar configuração final
- **Condição:** OPTIMUM seca (manter consistência com treinos anteriores)
- **Combustível total necessário:** ~65-70L

---

## Estrutura do Treino

### Bloco 1: Aquecimento + Baseline Setup Atual (21_25_ajustes)
**Duração:** 15 minutos
**Combustível:** 25L
**Voltas estimadas:** 8-9 voltas

**Objetivos:**
1. Aquecer pneus e freios (2-3 voltas progressivas)
2. Estabelecer baseline com setup conhecido (21_25_ajustes.json)
3. Registrar tempos por setor
4. Monitorar temperaturas dos pneus e freios

**Checklist pré-bloco:**
- [ ] Setup: 21_25_ajustes.json carregado
- [ ] Combustível: 25L
- [ ] Pressões a frio: FL 24.8 / FR 26.2 / RL 23.6 / RR 25.3
- [ ] Brake ducts: Front 2 / Rear 6
- [ ] Brake pads: Front 2-3 / Rear 1
- [ ] Brake bias: 56%

**Dados a coletar:**
- Melhor volta e média (válidas)
- Tempos por setor (S1, S2, S3)
- Temperaturas dos pneus após 5-7 voltas (alvo: FL 86-90 / FR 76-82 / RL 88-92 / RR 80-84)
- Sensação de aderência (1-10)

---

### Bloco 2: Teste Setup FRI3dolf
**Duração:** 15 minutos
**Combustível:** 25L
**Voltas estimadas:** 8-9 voltas

**Objetivos:**
1. Adaptar ao setup FRI3dolf (3-4 voltas progressivas)
2. Avaliar aderência e comportamento do carro
3. Comparar tempos com Bloco 1
4. Identificar pontos fortes/fracos do setup

**Checklist pré-bloco:**
- [ ] Setup: FRI3_R8EVO2_BAR_RS_20_25_v1.9.5.json carregado
- [ ] Combustível: 25L (abastecer)
- [ ] **Verificar pressões recomendadas pelo setup FRI3** (conferir no arquivo .json)
- [ ] **Verificar brake ducts no setup FRI3** (ajustar se necessário)
- [ ] Anotar diferenças principais vs setup atual

**Dados a coletar:**
- Melhor volta e média (válidas)
- Tempos por setor (S1, S2, S3)
- Temperaturas dos pneus após 5-7 voltas
- Sensação de aderência (1-10)
- Diferenças sentidas (subesterço/sobresterço, estabilidade, tração)

---

### Bloco 3: Ajustes Finos + Validação
**Duração:** 15-20 minutos
**Combustível:** 25L
**Voltas estimadas:** 8-10 voltas

**Objetivos:**
1. Escolher o melhor setup (baseado em Blocos 1 e 2)
2. Aplicar ajustes finos se necessário
3. Validar setup final com stint longo
4. Confirmar consistência e degradação

**Decisão:**
- Se **FRI3 for melhor:** aplicar aprendizados de brake system se temperaturas desbalancearem
- Se **setup atual for melhor:** manter e fazer apenas ajustes marginais
- Se **empatados:** escolher o mais confortável/consistente

**Checklist pré-bloco:**
- [ ] Setup escolhido carregado
- [ ] Combustível: 25L (abastecer)
- [ ] Ajustes aplicados (se necessário)
- [ ] Meta: >80% voltas válidas

**Dados a coletar:**
- Melhor volta e média (válidas)
- Consistência (gap entre melhor e média)
- Degradação (comparar primeiras 3 vs últimas 3 voltas)
- Temperaturas estáveis

---

## Critérios de Comparação

### Tabela de Avaliação (preencher durante treino)

| Critério | Setup Atual (21_25) | FRI3dolf | Vencedor |
|----------|:-------------------:|:--------:|:--------:|
| **Melhor volta** | _________ | _________ | _______ |
| **Média (válidas)** | _________ | _________ | _______ |
| **S1 melhor** | _________ | _________ | _______ |
| **S2 melhor** | _________ | _________ | _______ |
| **S3 melhor** | _________ | _________ | _______ |
| **Consistência (% válidas)** | _________ | _________ | _______ |
| **Aderência entrada (1-10)** | _________ | _________ | _______ |
| **Aderência meio (1-10)** | _________ | _________ | _______ |
| **Aderência saída (1-10)** | _________ | _________ | _______ |
| **Temperaturas balanceadas** | ☐ Sim ☐ Não | ☐ Sim ☐ Não | _______ |
| **Conforto geral (1-10)** | _________ | _________ | _______ |

**Setup escolhido:** __________________

---

## Metas do Treino 3

### Tempos
- **Melhor volta:** < 1:45.0s (melhoria de -0.512s vs T2)
- **Média válidas:** < 1:45.5s
- **Gap para referência:** < 0.600s

### Setores (melhor de cada)
- **S1:** < 29.600s (ganho de -0.060s)
- **S2:** < 40.500s (ganho de -0.107s)
- **S3:** < 35.150s (ganho de -0.095s)

### Qualidade
- **Voltas válidas:** >80% (vs 75% no T2)
- **Consistência:** gap melhor-média < 0.600s
- **Temperaturas:** dentro do alvo (FL 86-90 / FR 76-82 / RL 88-92 / RR 80-84)

---

## Observações de Combustível

**Consumo médio:** 2.70-2.77 L/lap
**Autonomia por bloco:**
- 25L = ~9 laps (suficiente para cada bloco de 15min)
- 70L total = margem de segurança para ajustes extras

**Estratégia:**
1. Iniciar com 25L (Bloco 1)
2. Pit stop: abastecer +25L (Bloco 2)
3. Pit stop: abastecer +20-25L (Bloco 3)

---

## Checklist Pós-Treino

Após concluir o treino:
- [ ] Exportar session3.json
- [ ] Salvar setup escolhido com nome descritivo (ex: `setup_final_treino3.json`)
- [ ] Anotar ajustes aplicados vs setup base
- [ ] Preencher tabela de comparação
- [ ] Gerar relatório treino3.md
- [ ] Atualizar evolucao_treinos.md
- [ ] **Documentar setup final para Dias 4-6**

---

## Notas Importantes

⚠️ **Atenção:**
- Se RL continuar >92°C, considerar: Rear brake ducts +1, Preload -5-10 Nm
- Se FR continuar <78°C, considerar: Front brake ducts -1, Front pads +1 compound
- Não mudar mais de 2-3 parâmetros por vez (isolar variáveis)

✅ **Prioridades:**
1. Setup que dá **melhor sensação** (conforto > 0.2s de diferença)
2. Setup mais **consistente** (menos voltas inválidas)
3. Setup com temperaturas mais **balanceadas**

📋 **Lembrete:**
- Dias 4-6 usarão o setup consolidado hoje
- Foco total será em pilotagem e setores
- Setup deve estar estável e previsível
