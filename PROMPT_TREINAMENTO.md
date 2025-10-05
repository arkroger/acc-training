# 🧠 PROMPT DE TREINAMENTO – ACC Training  
📁 Projeto: [arkroger/acc-training](https://github.com/arkroger/acc-training)

Estamos nos preparando para participar de uma **corrida de campeonato de piloto amador** no **Assetto Corsa Competizione (ACC)**.  
Todo o planejamento, relatórios e guias de pista serão **armazenados e versionados no repositório GitHub**.

---

## 📂 Estrutura do Projeto

O repositório `arkroger/acc-training` deve conter os seguintes diretórios:

```plaintext
acc-training/
├── circuits/
│   ├── [nome-da-pista]/
│   │   ├── transcripts/        # Transcrições de vídeos (JSON, SRT, TXT)
│   │   ├── reports/            # Guias de curva a curva (.md)
│   │   └── references/         # Links de vídeos e fontes
├── events/
│   ├── [ano]/[data_pista_evento]/
│   │   ├── reports/            # Relatórios de treinos, plano e evolução
│   │   └── data/               # Tempos de volta e sessões (.json)
└── templates/
    └── reports/
        ├── curvas_template.md             # Template padrão para curva a curva
        ├── plano_treino_template.md       # Template padrão para plano de treino
        ├── treino_dia_template.md         # Template padrão para relatório diário
        └── evolucao_treinos_template.md   # Template padrão para relatório de evolução
```

---

## ⚙️ Instruções para o Assistente

### 🔁 Leitura e Escrita no GitHub
- Buscar arquivos no repositório **`arkroger/acc-training`** para:
  - Ler dados de **transcrições**, **guias de curva**, **planos de treino**, **relatórios diários** e **relatórios de evolução**.
  - Atualizar ou gerar novos arquivos dentro da estrutura correta.
- Padrões de nome:
  - `circuits/[pista]/reports/curvas_comparativo.md`
  - `events/[ano]/[data_pista]/reports/plano_treino.md`
  - `events/[ano]/[data_pista]/reports/treino_[dia].md`
  - `events/[ano]/[data_pista]/reports/evolucao_treinos.md`

---

## 📆 Plano de Treino

O plano de treino deve ser **progressivo** e **documentado**.  
Cada **dia de treino** gera um **relatório separado** com resumo e evolução.

### 🔹 Passos Iniciais
Confirmar:
1. **Data da corrida**
2. **Pista**
3. **Carro**
4. **Duração da corrida**
5. **Paradas obrigatórias** (troca de pneus / abastecimento)
6. **Tempo de pit stop**
7. **Quantidade de dias de treino**
8. **Tempo de treino por dia**
9. **Tempo de volta de referência**

Registrar essas informações no arquivo:
```plaintext
events/[ano]/[data_pista]/reports/plano_treino.md
```

### 🔹 Objetivos
- **Dia 1**: gerar dados de referência da pista:
  - Tempos de volta e setores.
  - Marchas ideais.
  - Guia curva a curva.
- **Dias seguintes**:
  - Foco em setores mais lentos.
  - Testes de setup.
  - Estratégia de pit stop.

### 🔹 Regra
- Sempre incluir resumo de cada dia.
- Não alterar resumos anteriores — apenas acrescentar novos dias.

---

### 📄 Template do Plano de Treino
Utilize o modelo abaixo para criar novos planos:
```plaintext
templates/reports/plano_treino_template.md
```

Sempre copie o template e renomeie para o evento:
```plaintext
events/[ano]/[data_pista]/reports/plano_treino.md
```

---

## 📝 Relatórios de Treino (Diários)

Cada treino gera um relatório:
```plaintext
events/[ano]/[data_pista]/reports/treino_[dia].md
```

### Conteúdo mínimo:
- Resumo do dia  
- Condições da pista (tempo, temperatura, tráfego)  
- Objetivo do treino  
- Tempos (volta total + setores 1, 2 e 3)  
- Evolução comparada ao dia anterior  
- Ajustes realizados (setup, combustível, pressão)  
- Observações e lições  
- Plano do próximo treino

### 📄 Template de Relatório Diário
Utilize o modelo base:
```plaintext
templates/reports/treino_dia_template.md
```

Copie e renomeie conforme o dia:
```plaintext
events/[ano]/[data_pista]/reports/treino_[n].md
```

---

## 📈 Relatório de Evolução dos Treinos

Após cada dia de treino, o arquivo de **evolução** deve ser **criado ou atualizado**, consolidando os dados gerais de todos os treinos.

### 📄 Template de Evolução
```plaintext
templates/reports/evolucao_treinos_template.md
```

Crie ou atualize o arquivo:
```plaintext
events/[ano]/[data_pista]/reports/evolucao_treinos.md
```

### Deve conter:
- Melhor volta e média de cada dia  
- Voltas válidas  
- Observações de progresso  
- Evolução por setor (melhores e médias)  
- Resumo geral de ganhos e pontos de melhoria  
- Resumo de cada treino (sem sobrescrever os anteriores)

---

## 🏁 Guia de Curvas

Local:
```plaintext
circuits/[pista]/reports/curvas_comparativo.md
```

Baseado em vídeos de referência (**Yorkie**, **Driver61**, **Coach Dave**, etc):
- Marchas
- Pontos de freada
- Observações de traçado, uso de zebra, molhado
- Diferenças entre guias marcadas com itálico:
  ```markdown
  *(_Driver61_: recomenda entrada mais tardia e evitar zebra interna)*
  ```

---

## 📊 Análise de Evolução

- Comparar tempos por **setor** e **volta total**  
- Destacar **setores com ganhos e perdas**  
- Incluir **tabelas ou gráficos** nos relatórios

---

## ⛽ Pit Stops

Configurações padrão (ajustar conforme evento):
- Troca de pneus: **+5s** ao tempo de parada
- Abastecimento:
  - **25s fixos**, ou
  - **1.2s + 0.2s/litro**
- Caso abasteça e troque pneus: **30s totais**

---

## 🧭 Regras para Geração

1. Verifique se o repositório está acessível  
2. Busque o arquivo existente  
3. Preserve conteúdo anterior  
4. Adicione novas seções com data e título  
5. Salve no caminho correto

---

## 🏎️ Regras Gerais

- Corridas com **largada em movimento**
- Foco em **consistência e evolução**
- Priorização por **setores mais lentos**
- Tudo deve ser **versionado no GitHub**

---

## ✅ Exemplos de Caminhos

```plaintext
Plano:      events/2025/2025-10-05_barcelona/reports/plano_treino.md
Treino 1:   events/2025/2025-10-05_barcelona/reports/treino_1.md
Evolução:   events/2025/2025-10-05_barcelona/reports/evolucao_treinos.md
Curvas:     circuits/barcelona/reports/curvas_comparativo.md
```
