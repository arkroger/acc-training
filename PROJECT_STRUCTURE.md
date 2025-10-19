# Project Structure - ACC Training System

Visual guide to the complete project organization.

---

## 📁 Complete Directory Tree

```
acc-training/
│
├─── 📚 Documentation
│    ├── README.md                      # Project overview and quick start
│    ├── CLAUDE.md                      # Detailed guide for Claude Code
│    ├── QUICK_REFERENCE.md             # Daily use cheat sheet
│    ├── CHANGELOG.md                   # Version history
│    └── PROJECT_STRUCTURE.md           # This file
│
├─── 🏆 Events (Championship Organization)
│    └── events/[championship]/
│        │
│        ├── analise_campeonato.md     # 📊 Championship overall analysis
│        │                              #    - Standings and points
│        │                              #    - Performance trends
│        │                              #    - Projections
│        │
│        └── [YYYY-MM-DD_track_duration]/   # Individual event
│            │
│            ├── plano_treino.md       # 📋 Event training plan
│            │
│            ├── sessions/              # 💾 Raw session data
│            │   ├── session1.json ... sessionN.json
│            │   ├── qualy_oficial.json
│            │   ├── race_oficial.json
│            │   └── race_oficial_*.json   # (rival, silver, p1)
│            │
│            ├── setups/                # ⚙️ Car setups
│            │   ├── setup_treino_1/
│            │   ├── setup_treino_2/
│            │   └── setup_*.md
│            │
│            ├── analysis/              # 🔬 Technical analyses
│            │   ├── session_3/
│            │   │   ├── tyre_*.md
│            │   │   └── setup_*.md
│            │   └── session_N/
│            │       ├── *.md
│            │       └── *.png
│            │
│            └── reports/               # 📝 Consolidated reports
│                ├── treino1.md ... treino10.md
│                ├── evolucao_treinos.md
│                ├── analise_adversarios.md
│                ├── analise_corrida_oficial.md
│                ├── analise_qualy_oficial.md
│                └── plano_corrida.md
│
├─── 🏁 Track Data
│    └── circuits/[track]/
│        ├── transcripts/              # Video transcriptions (JSON)
│        └── reports/                  # Track guides (curva a curva)
│
├─── 📋 Templates
│    └── templates/
│        ├── plano_treino_template.md
│        ├── treino_dia_template.md
│        └── evolucao_treinos_template.md
│
├─── 🔧 Tools & Scripts
│    ├── acc-json-tools/               # Python conversion utilities
│    ├── schemas/                      # JSON schemas
│    └── scripts/
│        └── create_event.sh           # Event creation helper
│
└─── ⚙️ Configuration
     ├── .gitignore
     └── .gitattributes
```

---

## 🗂️ File Types by Location

### Sessions Directory (sessions/)
**Purpose**: Raw data only - JSON exports from ACC

```
sessions/
├── session1.json               # Training session 1
├── session2.json               # Training session 2
├── ...
├── session12.json              # Training session 12
├── qualy_oficial.json          # Official qualifying
├── race_oficial.json           # Your race data
├── race_oficial_rival.json     # Rival race data
├── race_oficial_silver.json    # Silver driver data
└── race_oficial_p1.json        # P1 (PRO) driver data
```

### Setups Directory (setups/)
**Purpose**: Car configurations and setup documentation

```
setups/
├── setup_treino_1/             # Setup screenshots/files (training 1)
│   ├── screenshot1.png
│   └── ...
├── setup_treino_2/             # Setup JSON + documentation
│   ├── config.json
│   └── notes.md
└── setup_otimizado_proposta.md # Setup optimization proposals
```

### Analysis Directory (analysis/)
**Purpose**: Technical analyses organized by session

```
analysis/
├── session_3/                  # Session 3 technical analysis
│   ├── tyre_stint1.md         # Tyre analysis stint 1
│   ├── setup_test.md          # Setup test results
│   └── notes.md
├── session10/                  # Session 10 technical analysis
│   ├── tyre3.md
│   ├── tyre3.png
│   ├── tyre5.md
│   └── tyre5.png
└── ...
```

### Reports Directory (reports/)
**Purpose**: Consolidated reports and summaries

```
reports/
├── treino1.md                  # Daily training report 1
├── treino2.md                  # Daily training report 2
├── ...
├── treino10.md                 # Daily training report 10
├── evolucao_treinos.md         # Evolution tracking (cumulative)
├── analise_adversarios.md      # Opponent analysis
├── analise_pre_qualy.md        # Pre-qualifying analysis
├── analise_qualy_oficial.md    # Official qualifying analysis
├── analise_corrida_oficial.md  # Official race analysis
└── plano_corrida.md           # Race strategy plan
```

---

## 📊 Information Flow

### Training Phase (Day 1-10)

```
ACC Game
   ↓ Export JSON
sessions/sessionN.json
   ↓ Analysis
reports/treinoN.md
   ↓ Update
reports/evolucao_treinos.md
```

### Technical Analysis (Optional)

```
ACC Game
   ↓ Export + Screenshots
sessions/sessionN.json + Images
   ↓ Deep Analysis
analysis/session_N/*.md
   ↓ Document
reports/treinoN.md
```

### Race Weekend

```
Training Data
   ↓ Review
reports/evolucao_treinos.md
   ↓ Strategy
reports/plano_corrida.md
   ↓ Execute
Race
   ↓ Export
sessions/race_oficial*.json
   ↓ Analysis
reports/analise_corrida_oficial.md
   ↓ Update
../analise_campeonato.md
```

---

## 🎯 File Purpose Matrix

| File Type | Location | When Created | Purpose |
|-----------|----------|--------------|---------|
| sessionN.json | sessions/ | After each training | Raw lap data |
| treinoN.md | reports/ | After analysis | Daily summary |
| evolucao_treinos.md | reports/ | Updated daily | Progress tracking |
| tyre_*.md | analysis/session_N/ | When needed | Tyre analysis |
| setup_*.md | setups/ or analysis/ | When testing | Setup documentation |
| plano_corrida.md | reports/ | Before race | Race strategy |
| analise_corrida_oficial.md | reports/ | After race | Race analysis |
| analise_campeonato.md | ../ (championship level) | After each race | Championship tracking |

---

## 🏗️ Championship Organization

### Single Championship Example

```
events/piloteiro-amador/
├── analise_campeonato.md              # Season overview (14/18 races)
├── 2025-10-19_barcelona_60min/        # Race 1
├── 2025-11-15_monza_60min/            # Race 2
├── 2025-12-03_spa_120min/             # Race 3
└── ...                                # More races
```

### Multiple Championships

```
events/
├── piloteiro-amador/                  # Amateur championship
│   ├── analise_campeonato.md
│   └── [events]/
│
├── liga-gt3-pro/                      # Pro league
│   ├── analise_campeonato.md
│   └── [events]/
│
└── endurance-series/                  # Endurance championship
    ├── analise_campeonato.md
    └── [events]/
```

---

## 🔄 Typical Workflow

### 1. Create Event (One-time)

```bash
./scripts/create_event.sh piloteiro-amador 2025-11-15_monza_60min
```

### 2. Daily Training (Repeating)

```
1. Drive training session in ACC
2. Export JSON → sessions/sessionN.json
3. Ask Claude: "Analyze session N"
4. Review reports/treinoN.md
5. Check reports/evolucao_treinos.md
```

### 3. Pre-Race Preparation

```
1. Review all training reports
2. Analyze opponents
3. Create race strategy
4. Validate final setup
```

### 4. Post-Race Analysis

```
1. Export race data (you + opponents)
2. Analyze performance
3. Update championship standings
4. Plan improvements for next race
```

---

## 📖 Documentation Hierarchy

```
Quick Reference
      ↓
README.md (Overview)
      ↓
CLAUDE.md (Detailed Guide)
      ↓
Individual Reports (Event-specific)
```

**For daily use**: Start with QUICK_REFERENCE.md
**For understanding**: Read README.md
**For deep dive**: Consult CLAUDE.md

---

## ✅ Project Status

**Version**: 2.0.0
**Structure**: Championship-based organization
**Current Championship**: Piloteiro Amador
**Events Completed**: 14/18 races
**Championship Position**: P1 (+27 points)

**Last Updated**: 2025-10-19

---

## 🚀 Quick Commands

```bash
# Create new event
./scripts/create_event.sh [championship] [event]

# Navigate to event
cd events/[championship]/[event]

# View structure
ls -la

# Check championship status
cat ../analise_campeonato.md
```
