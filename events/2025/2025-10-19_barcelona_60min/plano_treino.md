# Plano de Treino – Barcelona (2025-10-19 · 60min)

## Informações Iniciais (conforme PROMPT)
- **Data da corrida:** 2025-10-19
- **Pista:** Barcelona (GP)
- **Carro:** Audi R8 LMS Evo II GT3 2022
- **Duração da corrida:** 60 minutos
- **Paradas obrigatórias:** Abastecimento obrigatório; **troca de pneus não é obrigatória**
- **Tempo de pit stop (padrão PROMPT):**
  - Abastecer **sem trocar pneus:** ~**25s**
  - Abastecer **e trocar pneus:** ~**30s** (pneu +5s)
- **Quantidade de dias de treino:** 6 (50 min cada)
- **Tempo de treino por dia:** 50 minutos
- **Tempo de volta de referência (inicial):** _a definir no Dia 1 após baseline_

> *Obs.: manter estes parâmetros alinhados ao PROMPT; ajustes posteriores devem ser registrados nos relatórios diários e consolidados na evolução.* 

---

## Objetivos Gerais
1. **Baseline (Dia 1):** mapear melhor volta, médias por stint e marchas ideais; rascunho do **curva-a-curva**.
2. **Dias seguintes:** atacar setores mais lentos; validar pressões/combustível; comparar **sem troca** × **com troca** no pit.
3. **Consistência:** reduzir variação entre primeiros 5 laps e últimos 5 laps de cada stint.
4. **Estratégia de pit:** simular janela de parada e impacto de pneus.

---

## Plano Progressivo por Dia
- **Dia 1 – Baseline:**  
  - Stint longo (20–25 voltas) com combustível razoável.  
  - Registrar: voltas válidas, melhor volta, **setores S1/S2/S3**, marchas por curva.  
  - Preencher rascunho em `circuits/barcelona/reports/curvas_comparativo.md`.

- **Dia 2 – Foco Setor 1:**  
  - Testar pontos de freada e marcha em T1–T3; validar referência visual.

- **Dia 3 – Foco Setor 2:**  
  - Tração em saídas médias/rápidas; estabilidade em curvas de média.

- **Dia 4 – Foco Setor 3:**  
  - Sequência final e preparo da chicane; consistência em voltas longas.

- **Dia 5 – Simulação corrida (tráfego se possível):**  
  - Stint inicial cheio → pit → stint final.  
  - Coletar degradação e impacto do pit **sem troca**.

- **Dia 6 – Simulação final (A/B Test):**  
  - **A:** parada **sem troca** (25s).  
  - **B:** parada **com troca** (30s).  
  - Comparar médias pós-pit e aquecimento de pneus.

---

## Métricas a Consolidar nos Relatórios
- Melhor volta e **média das voltas válidas** por stint/dia.  
- **Evolução por setor** (melhor e média).  
- **Degradação** (últimos 5 vs. primeiros 5 válidos no stint).  
- Observações de setup (combustível/pressão/altura/asa).  
- Resumo incremental na **evolução** do evento.

---

## Arquivos do Evento (conforme PROMPT)
- **Dados (JSON):** `events/2025/2025-10-19_barcelona/data/`  
- **Relatórios diários:** `events/2025/2025-10-19_barcelona/reports/treino_[n].md`  
- **Evolução consolidada:** `events/2025/2025-10-19_barcelona/reports/evolucao_treinos.md`  
- **Curva a curva:** `circuits/barcelona/reports/curvas_comparativo.md`
