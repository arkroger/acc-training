# ACC Training Log

Repositório para organizar **treinos diários** e **relatórios** das corridas no **Assetto Corsa Competizione (ACC)**.

## Estrutura
```
.
├── docs/                          # Documentação geral
├── events/
│   └── YYYY/
│       └── YYYY-MM-DD_track_event/
│           ├── data/              # Dados brutos (JSON/CSV) por sessão
│           ├── processed/        # Agregações/outputs (CSV)
│           └── reports/          # Relatórios em Markdown
├── car_setups/                    # Setups por carro/pista (json/md/png)
├── schemas/                       # Schemas (ex.: JSON Schema dos dados)
├── templates/                     # Templates de relatórios
├── examples/                      # Exemplos de arquivos
├── .gitattributes                 # LFS para imagens/vídeos
└── .gitignore
```

## Convenções de nomes
- Evento: `YYYY-MM-DD_<pista>_<duração|tipo>` — ex.: `2025-10-05_imola_60min`
- Sessão raw: `session{N}.json` — ex.: `session1.json`
- Relatório: `report.md`
- Agregado: `laps_aggregated.csv`

## Workflow sugerido
1. Criar pasta do evento em `events/YYYY/`.
2. Salvar dados brutos em `raw/` (um arquivo por sessão/stint).
3. (Opcional) Gerar `processed/` com métricas agregadas.
4. Escrever relatório em `reports/report.md` baseado no template em `templates/daily_report_template.md`.
5. Commit + push.

## Leitura pelo Bartolomeu (ChatGPT)
- **Público**: se o repositório for público, basta me passar o link do arquivo (ou do diretório) que eu leio.
- **Privado**: publique os artefatos (relatórios/JSON) num storage público só de leitura, ou sincronize com um Google Drive compartilhado para eu acessar (recomendado).

> Dica: Ative **Git LFS** para imagens (prints de pneus, setup). Veja `.gitattributes`.


##json-tools
```python flat_to_unified_mapper.py seu_raw.json saida_unificada.json```
