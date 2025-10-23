# Red Bull Ring / Spielberg - 60min (02/11/2025)

**Corrida 15/18** - Campeonato Piloteiro Amador

---

## Informações do Evento

| Informação | Detalhes |
|------------|----------|
| **Data** | 02/11/2025 |
| **Pista** | Red Bull Ring (Spielberg) |
| **Distância** | 4.318 km |
| **Duração** | 60 minutos |
| **Carro** | Audi R8 LMS Evo II |
| **Corrida** | 15 de 18 |

---

## Contexto do Campeonato

### Situação Atual (Pós-C14 Barcelona)
- **Posição**: P1 Piloteiro Amador ✅
- **Pontos**: 122 pts
- **Vantagem**: +27 pts sobre P2
- **Corridas restantes**: 4
- **Probabilidade título**: ~70%

### Objetivos para Spielberg
- **Meta mínima**: P6-P7 (14-15 pts)
- **Meta ideal**: P5-P6 (15-18 pts)
- **Meta excelente**: P4 (20 pts)

**Estratégia**: Consistência > Risco

---

## Estrutura do Evento

```
2025-11-02_spielberg_60min/
├── plano_treino.md              # ✅ Plano de treino completo
├── README.md                    # Este arquivo
│
├── sessions/                    # 📁 Dados das sessões
│   ├── session1.json - session12.json
│   ├── qualy_oficial.json
│   └── race_oficial.json
│
├── setups/                      # ⚙️ Configurações do carro
│   └── (a preencher durante treinos)
│
├── analysis/                    # 🔬 Análises técnicas
│   └── (a preencher conforme necessário)
│
└── reports/                     # 📝 Relatórios
    ├── treino1.md - treino10.md
    ├── evolucao_treinos.md
    └── analise_corrida_oficial.md
```

---

## Plano de Treino (8 Sessões Oficiais)

### Fase 1: Preparação e Baseline (S1-S2)
- **Sessão 1**: Preparação/Estudo (track guides, marchas, referências)
- **Sessão 2**: Baseline + Setup ideal + Variações (normal, chuva, calor)

### Fase 2: Domínio de Setores (S3-S5)
- **Sessão 3**: Setor 1 (T1-T3)
- **Sessão 4**: T4 (Wurth) 🎯 *Curva mais crítica da pista*
- **Sessão 5**: Rindt Complex (T6-T7) + Setor 3

### Fase 3: Consolidação (S6)
- **Sessão 6**: Consolidação + Stint longo (30min)

### Fase 4: Preparação Final (S7-S8)
- **Sessão 7**: Qualifying simulation + Pitstops
- **Sessão 8**: Race simulation (60min) + **Análise adversários**

---

## Tempos de Referência

### Objetivos Finais
| Métrica | Tempo Alvo |
|---------|------------|
| **Volta completa** | 1:28.5 - 1:29.0 |
| **Setor 1** | 0:29.5 - 0:30.0 |
| **Setor 2** | 0:35.0 - 0:35.5 |
| **Setor 3** | 0:23.5 - 0:24.0 |

### Baseline Esperado (Dia 1)
- Volta: ~1:31.0 - 1:32.0
- Margem de melhoria: 2.5-3.0s

---

## Características da Pista

### Pontos-Chave
1. **T1**: Entrada rápida, crucial não errar
2. **T2**: Curva em aclive (cega)
3. **T3**: Alta velocidade
4. **T4 (Wurth)**: 🎯 **CURVA MAIS IMPORTANTE** - declive, alta velocidade
5. **T6-T7 (Rindt)**: Chicane em aclive
6. **T8**: Saída crucial para reta principal
7. **T9-T10**: Chicane final

### Desafios Específicos
- ⚠️ Muitas elevações (aclives e declives)
- ⚠️ Curvas de alta velocidade (exigem confiança)
- ⚠️ Pista curta = mais tráfego
- ⚠️ Pouco espaço para erro

### Oportunidades
- ✅ Pista técnica (favorece consistência)
- ✅ Muitas voltas em 60min (chances de recuperação)
- ✅ Setup pode fazer diferença (elevações)

---

## Workflow de Treino

### Antes de Cada Sessão
1. Ler objetivos em `plano_treino.md`
2. Revisar últimas recomendações
3. Carregar setup correto

### Depois de Cada Sessão
1. Exportar JSON → `sessions/sessionN.json`
2. Pedir análise ao Claude:
   ```
   "Analise a sessionN do evento Spielberg baseado no plano_treino.md"
   ```
3. Revisar `reports/treinoN.md` gerado
4. Conferir `reports/evolucao_treinos.md`

---

## Estratégia Preliminar de Corrida

### Configuração Inicial
- **Combustível**: ~68L
- **Setup**: Alta velocidade (menos asa)
- **Pressões**: A validar nos treinos

### Pit Stop
- **Janela**: Volta 17-19
- **Tipo**: Combustível obrigatório + pneus (validar)
- **Tempo alvo**: 25-28s

### Pace Alvo
- **Qualifying**: 1:28.5 - 1:29.0
- **Race Stint 1**: 1:29.5 - 1:30.0
- **Race Stint 2**: 1:29.5 - 1:30.5

### Pontos Críticos
1. **Largada**: Sobreviver T1 sem acidente
2. **T4**: Principal área de ultrapassagem/defesa
3. **Pit timing**: Evitar tráfego na saída
4. **Final de corrida**: Manter concentração

---

## Checklist de Progresso

### Preparação
- [x] Estrutura de diretórios criada
- [x] Plano de treino elaborado
- [x] Objetivos definidos
- [ ] Baseline estabelecido (Sessão 1)

### Treinos (0/10 completos)
- [ ] Sessão 1: Reconhecimento
- [ ] Sessão 2: Setor 1
- [ ] Sessão 3: Setor 2 (T4)
- [ ] Sessão 4: Setor 2 (T6-T7)
- [ ] Sessão 5: Setor 3
- [ ] Sessão 6: Consolidação
- [ ] Sessão 7: Adversários
- [ ] Sessão 8: Stint longo
- [ ] Sessão 9: Qualifying
- [ ] Sessão 10: Race simulation

### Corrida Oficial
- [ ] Qualifying realizado
- [ ] Corrida realizada
- [ ] Análise pós-corrida
- [ ] Campeonato atualizado

---

## Próximos Passos

1. **Agora**: Aguardar data dos treinos
2. **Primeira sessão**: Baseline e reconhecimento
3. **Durante treinos**: Seguir plano dia a dia
4. **Pré-corrida**: Validar estratégia e setup
5. **Pós-corrida**: Atualizar campeonato

---

## Links Úteis

- [Plano de Treino Completo](plano_treino.md)
- [Análise do Campeonato](../analise_campeonato.md)
- [Evento Anterior (Barcelona)](../2025-10-19_barcelona_60min/)

---

**Status**: 📋 Planejamento completo - Aguardando início dos treinos
**Criado em**: 2025-10-19
**Última atualização**: 2025-10-19
