# 🔧 Setup Otimizado – Proposta (Base: Friedolf)

## 🎯 Objetivos
1. **Aquecer o dianteiro direito (RF)** – atualmente 59-67°C (muito frio)
2. **Manter boa rotação** que o Friedolf oferece
3. **Melhorar estabilidade no final do stint**

---

## ⚙️ Ajustes Recomendados

### **1. Geometria Dianteira**
| Parâmetro | Friedolf | Proposta | Razão |
|-----------|----------|----------|-------|
| **Camber LF** | -3.6° | **-4.0°** | Manter |
| **Camber RF** | -3.6° | **-4.3°** | ⬆️ +0.3° para aquecer RF |
| **Toe LF** | -0.15° | **-0.18°** | ⬆️ Mais temperatura |
| **Toe RF** | -0.15° | **-0.18°** | ⬆️ Mais temperatura |
| **Caster** | 14.5° | **14.5°** | Manter |

**Impacto**: Aumentar camber RF e toe ajuda a aquecer o pneu frio sem perder demais em velocidade de reta.

---

### **2. Pressões dos Pneus**
| Posição | Friedolf (Pit) | Proposta | Razão |
|---------|----------------|----------|-------|
| **LF** | 25.0 | **24.8** | ⬇️ -0.2 (estava +1.7 hot) |
| **RF** | 25.8 | **25.3** | ⬇️ -0.5 (ajudar aquecimento) |
| **LR** | 24.8 | **24.5** | ⬇️ -0.3 (estava +2.2 hot) |
| **RR** | 25.5 | **25.2** | ⬇️ -0.3 (estava +1.2 hot) |

**Impacto**: Pressões mais baixas = mais deformação = mais trabalho = mais temperatura no RF. Cuidado para não sair da janela ideal (27.0-27.5 hot).

---

### **3. Refrigeração (Brake Ducts)**
| Eixo | Friedolf | Proposta | Razão |
|------|----------|----------|-------|
| **Dianteiro** | 3 | **2** | ⬇️ Menos ar frio no RF |
| **Traseiro** | 2 | **2** | Manter |

**Impacto**: Reduzir brake duct ajuda a elevar temperatura do RF. Monitore para não superaquecer os freios.

---

### **4. Anti-roll Bar (Barras Estabilizadoras)**
| Eixo | Friedolf | Proposta | Razão |
|------|----------|----------|-------|
| **Dianteiro** | 4 | **4** | Manter |
| **Traseiro** | 1 | **2** | ⬆️ +1 para estabilidade fim de stint |

**Impacto**: ARB traseiro em 1 deixa muito solto. Aumentar para 2 melhora estabilidade sem perder rotação drasticamente.

---

### **5. Bumpstops Traseiros**
| Parâmetro | Friedolf | Proposta | Razão |
|-----------|----------|----------|-------|
| **Bumpstop Rate** | 300 | **400** | ⬆️ Mais progressivo sobre kerbs |
| **Bumpstop Range** | 14 | **12** | ⬇️ Engaja um pouco antes |

**Impacto**: Aumentar stiffness ajuda estabilidade em T9-T10 sem perder conforto em kerbs baixos.

---

### **6. Amortecedores (mantidos do Friedolf)**
| Posição | Bump | Fast Bump | Rebound | Fast Rebound |
|---------|------|-----------|---------|--------------|
| LF/RF | 22 | 20 | 25 | 30 |
| LR/RR | 20 | 18 | 22 | 25 |

**Impacto**: Valores do Friedolf estão bons. Não mexer.

---

### **7. Aerodinâmica (mantida)**
| Parâmetro | Friedolf | Proposta |
|-----------|----------|----------|
| **Wing** | 5 | **5** |
| **Splitter** | 0 | **0** |
| **Ride Height Front** | 54mm | **54mm** |
| **Ride Height Rear** | 62mm | **62mm** |

---

## 📋 Resumo das Mudanças

| Categoria | Mudanças |
|-----------|----------|
| **Geometria** | Camber RF: -4.0° → -4.3° <br> Toe dianteiro: -0.15° → -0.18° |
| **Pressões** | RF: 25.8 → 25.3 <br> LF: 25.0 → 24.8 <br> LR/RR: -0.3 cada |
| **Refrigeração** | Brake duct dianteiro: 3 → 2 |
| **Suspensão** | ARB traseiro: 1 → 2 <br> Bumpstop rate: 300 → 400 <br> Bumpstop range: 14 → 12 |

---

## 🎯 Resultados Esperados

### ✅ **Ganhos**
1. **RF aquecendo melhor**: De 59-67°C para ~70-78°C (janela ideal)
2. **Menos escorregamento em T7**: Com RF mais quente, aderência melhora
3. **Mais estabilidade no final do stint**: ARB traseiro +1 reduz oversteer em pneus degradados
4. **Lap time estimado**: **1:45.0 - 1:45.2** (ganho de 0.1-0.2s)

### ⚠️ **Trade-offs**
- Pode perder 0.05s no S1 (mais arrasto com RF trabalhando mais)
- Rotação em baixa velocidade pode diminuir levemente (ARB traseiro +1)

---

## 🧪 Teste em Etapas

**Bloco 3 (próximo treino)**:
1. Aplicar **APENAS** ajustes de pressão e brake duct
2. Fazer 3-4 voltas e medir temperatura do RF
3. Se RF chegar em 72-75°C → aplicar ajustes de geometria
4. Se continuar frio (<70°C) → considerar camber RF -4.5°

---

## 📊 Checklist de Validação

Após aplicar setup, verificar:
- [ ] RF está entre 72-80°C (outer-middle)?
- [ ] Pressões hot ficam entre 27.0-27.5 PSI?
- [ ] Oversteer no final do stint diminuiu?
- [ ] Lap time melhorou 0.1-0.2s?
- [ ] Sensação de aderência em T7 melhorou (7→8)?

---

## 🔄 Próximos Passos

Se setup otimizado funcionar bem:
1. **Bloco 4**: Stint longo (12-15 voltas) para validar degradação
2. **Bloco 5**: Simulação de corrida (race fuel + pit stop)
3. **Bloco 6**: Race simulation completa (60min)

---

**Criado em**: 07/10/2025
**Base**: Setup Friedolf
**Objetivo**: Resolver temperatura RF + melhorar estabilidade final de stint
