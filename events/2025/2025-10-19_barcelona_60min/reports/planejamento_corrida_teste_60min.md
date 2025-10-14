# Planejamento: Corrida Teste 60min - Race Simulation

**Data:** 2025-10-12
**Objetivo:** Validar estratégia de degradação e consumo para corrida oficial (19/10/2025)
**Estratégia:** Stint único sem pit stop (baseline completo)

---

## 🎯 Configuração Inicial

### Setup
- **Combustível inicial:** 100L (margem de segurança)
- **Pneus:** Novo set (mapear curva de degradação completa)
- **Condições esperadas:** Grid fraco, pouco tráfego
- **Ritmo alvo:** Controlado (não atacar desnecessariamente)

### Premissas
- **Consumo estimado:** 2.75 L/lap (baseado em races extras)
- **Voltas esperadas:** ~34 laps
- **Ritmo médio projetado:** 1:46.0-1:47.0

---

## 📊 Plano de Monitoramento por Fases

### **FASE 1: Laps 1-10** (Aquecimento + Baseline)
**Pace esperado:** 1:45.5 - 1:46.5

**📝 Dados a registrar:**
- [ ] Melhor lap quando pneu atingir temperatura ideal (lap 3-5)
- [ ] Pace de cruzeiro com pneu no pico
- [ ] Sensação de grip nas curvas rápidas (S2: T5-T9)

**Observações:**
- Não forçar no lap 1-2 (pneu frio)
- Encontrar ritmo sustentável
- Validar consumo inicial vs estimado

---

### **FASE 2: Laps 11-20** (Estabilidade)
**Pace esperado:** 1:46.0 - 1:47.0

**📝 Dados a registrar:**
- [ ] Momento quando pace começar a cair consistentemente
- [ ] Primeira sensação de "escorregamento" (qual curva?)
- [ ] Degradação uniforme ou súbita?

**Observações:**
- Pequena degradação natural é esperada (~0.5s)
- Manter consistência
- Evitar track limits e batalhas desnecessárias

---

### **FASE 3: Laps 21-28** ⚠️ (Zona Crítica - "Cliff Point")
**Pace esperado:** 1:47.0 - 1:48.5

**📝 DADOS CRÍTICOS - Anotar lap exato quando:**
- [ ] **Lap do "cliff":** Quando sentir queda súbita de grip (>1s/lap perdido)
- [ ] Curvas mais afetadas (chicane? última curva?)
- [ ] Necessidade de adaptar pilotagem (mais suave? linhas diferentes?)

**Observações:**
- **ESTE É O DADO MAIS IMPORTANTE**
- Cliff point define janela ideal de pit para corrida real
- Janela de pit = (Lap do cliff - 2 ou 3 laps)

---

### **FASE 4: Laps 29-34** (Sobrevivência)
**Pace esperado:** 1:48.5 - 1:50.0

**📝 Dados a registrar:**
- [ ] Pace final com pneu completamente degradado
- [ ] Combustível restante (validar consumo)
- [ ] Curvas impossíveis de fazer rápido (limite absoluto de grip)

**Observações:**
- Administrar até o final sem erros
- Aceitar perda de pace (faz parte do teste)
- Completar corrida limpa

---

## 🔬 Análise Pós-Corrida

Após enviar o JSON (`session_race_simulation.json`), será calculado:

### 1. **Curva de Degradação**
- Pace médio a cada 5 laps
- Identificação do "cliff point"
- Taxa de degradação por fase

### 2. **Janela Ideal de Pit (Corrida Real)**
- **Sem troca de pneu:** Pit só combustível (25s) no lap do cliff
- **Com troca de pneu:** Pit completo (30s) 3-4 laps antes do cliff

### 3. **Análise de Viabilidade**
Comparar 3 cenários para corrida real:

| Cenário | Stint 1 | Pit | Stint 2 | Tempo Perdido | Tempo Ganho |
|---------|---------|-----|---------|---------------|-------------|
| **A) Sem pit** | 34 laps | - | - | 0s | Pace degrada muito |
| **B) Pit só combustível** | X laps | 25s | Y laps | 25s | Pneu velho no final |
| **C) Pit com troca** | X laps | 30s | Y laps | 30s | Pneu novo = pace forte |

### 4. **Recomendação Final**
- Estratégia ideal para corrida oficial
- Timing de pit
- Troca ou não troca de pneu
- Ritmo alvo por stint

---

## 📂 Arquivos

**Após a corrida:**
- Exportar dados: `events/2025/2025-10-19_barcelona_60min/data/session_race_simulation.json`
- Relatório será gerado: `events/2025/2025-10-19_barcelona_60min/reports/analise_corrida_teste_60min.md`

---

## ✅ Checklist Pré-Corrida

- [ ] Combustível: 100L
- [ ] Pneu: Set novo
- [ ] Setup validado (FRI3dolf ou preferido)
- [ ] Papel/app para anotar observações durante corrida
- [ ] Foco: Completar limpo e coletar dados (não buscar vitória a qualquer custo)

---

## 🎯 Meta Principal

**Não é vencer - é coletar dados para vencer na corrida oficial!**

Prioridades:
1. Completar 60min limpo
2. Identificar "cliff point" do pneu
3. Validar consumo real
4. Mapear degradação completa
5. Testar gestão de corrida (administrar P1 com margem)

---

**Boa corrida e foco na coleta de dados!** 🏁
