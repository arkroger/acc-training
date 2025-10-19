# Quick Reference - ACC Training System

Guia rápido de referência para uso diário do sistema de treinamento.

---

## 📁 Onde Salvar Cada Tipo de Arquivo

| Tipo de Arquivo | Diretório | Exemplo |
|-----------------|-----------|---------|
| JSON da sessão | `sessions/` | `session1.json` |
| JSON adversário | `sessions/` | `session10_rival_1.json` |
| Quali oficial | `sessions/` | `qualy_oficial.json` |
| Corrida oficial | `sessions/` | `race_oficial.json` |
| Setup (screenshots) | `setups/setup_treino_N/` | `setup_treino_1/*.png` |
| Setup (JSON) | `setups/setup_treino_N/` | `setup_treino_2/*.json` |
| Análise de pneus | `analysis/session_N/` | `analysis/session10/tyre3.md` |
| Análise de setup | `analysis/session_N/` | `analysis/session3/setup_test.md` |
| Relatório diário | `reports/` | `treino1.md` |
| Evolução | `reports/` | `evolucao_treinos.md` |
| Análise corrida | `reports/` | `analise_corrida_oficial.md` |
| Plano de corrida | `reports/` | `plano_corrida.md` |

---

## 🔄 Workflow Típico

### Treino Normal (Session N)

```bash
1. Exportar JSON do ACC
2. Salvar em: sessions/sessionN.json
3. Pedir ao Claude: "Analise a session N e gere o relatório"
4. Claude gera: reports/treinoN.md
5. Claude atualiza: reports/evolucao_treinos.md
```

### Treino com Análise Técnica

```bash
1. Exportar JSON do ACC
2. Salvar em: sessions/sessionN.json
3. Se tem screenshots de pneus → Salvar em: analysis/session_N/
4. Pedir análise detalhada
5. Claude gera análise técnica em: analysis/session_N/
6. Claude gera relatório em: reports/treinoN.md
```

### Qualifying Oficial

```bash
1. Exportar JSON quali
2. Salvar em: sessions/qualy_oficial.json
3. Exportar adversários (opcional)
4. Pedir análise
5. Claude gera: reports/analise_qualy_oficial.md
```

### Corrida Oficial

```bash
1. Exportar JSON corrida
2. Salvar em: sessions/race_oficial.json
3. Exportar adversários: sessions/race_oficial_rival.json, etc
4. Pedir análise comparativa
5. Claude gera: reports/analise_corrida_oficial.md
6. Claude atualiza: ../analise_campeonato.md
```

---

## 💬 Prompts Úteis para Claude

### Análise de Treino
```
"Analise a session N baseado no plano_treino.md e gere o relatório"
```

### Análise de Pneus
```
"Analise os pneus da session N com base nas imagens em analysis/sessionN/"
```

### Comparação com Adversário
```
"Compare meu desempenho na session N com o adversário rival"
```

### Análise de Corrida
```
"Analise a corrida oficial comparando com rival, silver e p1"
```

### Atualizar Campeonato
```
"Atualize a análise do campeonato com os resultados da corrida N"
```

### Planejamento de Corrida
```
"Crie um plano de corrida baseado nos treinos e análise de adversários"
```

---

## 📊 Arquivos Principais por Fase

### Fase: Preparação Inicial
- ✅ `plano_treino.md` - Objetivos e metas
- ✅ `circuits/barcelona/reports/curvas_comparativo.md` - Guia de pista

### Fase: Treinos (Dia 1-10)
- 📁 `sessions/session1.json` - session12.json
- 📝 `reports/treino1.md` - treino10.md
- 📈 `reports/evolucao_treinos.md`

### Fase: Análise Técnica (Opcional)
- 🔬 `analysis/session_N/tyre*.md`
- ⚙️ `setups/setup_treino_N/`

### Fase: Pré-Corrida
- 🎯 `reports/analise_adversarios.md`
- 📋 `reports/plano_corrida.md`
- ✅ `sessions/session11_pre_qualy.json`

### Fase: Corrida Oficial
- 🏁 `sessions/qualy_oficial.json`
- 🏁 `sessions/race_oficial.json`
- 📊 `reports/analise_corrida_oficial.md`
- 🏆 `../analise_campeonato.md` (atualizado)

---

## 🎯 Checklist Rápido

### Antes de Cada Treino
- [ ] Ler objetivos em `plano_treino.md`
- [ ] Verificar últimas recomendações em `evolucao_treinos.md`
- [ ] Carregar setup correto

### Depois de Cada Treino
- [ ] Exportar JSON da sessão
- [ ] Salvar em `sessions/sessionN.json`
- [ ] Pedir análise ao Claude
- [ ] Verificar `reports/treinoN.md` gerado
- [ ] Conferir atualização em `evolucao_treinos.md`

### Antes da Corrida
- [ ] Revisar `evolucao_treinos.md`
- [ ] Ler `analise_adversarios.md`
- [ ] Confirmar `plano_corrida.md`
- [ ] Validar setup final

### Depois da Corrida
- [ ] Exportar race_oficial.json + adversários
- [ ] Pedir análise comparativa
- [ ] Conferir `analise_corrida_oficial.md`
- [ ] Verificar atualização do campeonato
- [ ] Ler recomendações para próxima corrida

---

## 🏗️ Criar Novo Evento

```bash
# 1. Criar estrutura de diretórios
mkdir -p events/piloteiro-amador/YYYY-MM-DD_track_duration/{sessions,setups,analysis,reports}

# 2. Copiar template do plano
cp templates/plano_treino_template.md events/piloteiro-amador/YYYY-MM-DD_track_duration/plano_treino.md

# 3. Pedir ao Claude para personalizar o plano
"Personalize o plano_treino.md para o evento YYYY-MM-DD em [track]"
```

---

## 🔍 Encontrar Informações

### "Onde está...?"

| Procurando | Local |
|------------|-------|
| Dados brutos de sessão | `sessions/` |
| Relatório de um treino | `reports/treinoN.md` |
| Evolução geral | `reports/evolucao_treinos.md` |
| Análise de pneus | `analysis/sessionN/` |
| Setup usado | `setups/setup_treino_N/` |
| Análise de corrida | `reports/analise_corrida_oficial.md` |
| Situação do campeonato | `../analise_campeonato.md` |
| Guia da pista | `circuits/[track]/reports/` |

### "Como fazer...?"

| Tarefa | Consultar |
|--------|-----------|
| Analisar sessão | Ver workflow acima |
| Preparar corrida | `CLAUDE.md` → "Preparing for Race" |
| Analisar adversários | Ver "Prompts Úteis" |
| Criar novo evento | Ver "Criar Novo Evento" |
| Entender estrutura | `README.md` + `CLAUDE.md` |

---

## ⚡ Dicas Rápidas

### Nomenclatura
- Sessions: Numeração sequencial `session1.json`, `session2.json`
- Adversários: Incluir tipo `sessionN_rival_1.json`, `sessionN_silver_2.json`
- Reports: Coincidir com sessão `treino1.md` = análise de `session1.json`

### Organização
- 1 pasta por sessão analisada em `analysis/`
- Agrupar markdown + imagens relacionadas
- Usar nomes descritivos: `tyre_stint1_analysis.md`

### Workflow
- Nunca sobrescrever reports anteriores
- Sempre anexar novos treinos
- Atualizar evolução após cada sessão
- Comparar contra tempos de referência

### Campeonato
- Atualizar após CADA corrida
- Monitorar tendências (últimas 3-5)
- Ajustar estratégia conforme classificação

---

## 📞 Suporte

### Documentação Completa
- `README.md` - Visão geral e quick start
- `CLAUDE.md` - Guia detalhado para Claude
- `PROMPT_TREINAMENTO.md` - Diretrizes de análise

### Estrutura de Dados
- `schemas/lap_schema.json` - Schema unificado
- `acc-json-tools/` - Scripts de conversão

### Templates
- `templates/plano_treino_template.md`
- `templates/treino_dia_template.md`
- `templates/evolucao_treinos_template.md`

---

**Última atualização:** 2025-10-19
