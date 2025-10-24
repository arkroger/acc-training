# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository supports training preparation for **Assetto Corsa Competizione (ACC)** amateur racing championships. It manages training plans, lap time data, track guides, and progress reports for multi-day training sessions leading up to race events.

## Core Architecture

### Data Flow
1. **Raw lap data** (JSON) exported from ACC → stored in `events/[championship]/[event]/sessions/`
2. **Session analysis** processes flat lap data directly to generate daily training reports and evolution tracking
3. **Track guides** reference video transcriptions and expert advice (Yorkie, Driver61, etc.)

### Directory Structure
```
acc-training/
├── circuits/[track]/
│   ├── transcripts/              # Video transcriptions (JSON)
│   └── reports/                  # Track guides (curva a curva)
│
├── events/[championship]/        # Championship-level organization
│   ├── analise_campeonato.md    # Championship overall analysis
│   │
│   └── [YYYY-MM-DD_track_duration]/   # Individual event
│       ├── plano_treino.md       # Event training plan
│       │
│       ├── sessions/             # Raw session data (JSON)
│       │   ├── session1.json - sessionN.json
│       │   ├── qualy_oficial.json
│       │   ├── race_oficial.json
│       │   └── race_oficial_*.json   # Opponent data (rival, silver, p1)
│       │
│       ├── setups/               # Car setups and configurations
│       │   ├── setup_treino_1/   # Setup screenshots/files
│       │   ├── setup_treino_2/   # Setup JSON + analysis
│       │   └── setup_*.md        # Setup proposals and documentation
│       │
│       ├── analysis/             # Technical analysis per session
│       │   ├── session_3/        # Session-specific analysis
│       │   │   ├── tyre_*.md     # Tyre analysis
│       │   │   └── setup_*.md    # Setup analysis
│       │   └── session_N/        # More session analyses
│       │       ├── tyre*.md
│       │       └── *.png         # Analysis images
│       │
│       └── reports/              # Consolidated reports
│           ├── treino1.md - treino10.md    # Daily training reports
│           ├── evolucao_treinos.md         # Evolution tracking
│           ├── analise_adversarios.md      # Opponent analysis
│           ├── analise_corrida_oficial.md  # Race analysis
│           ├── analise_qualy_oficial.md    # Qualifying analysis
│           └── plano_corrida.md            # Race plan
│
├── templates/                    # Markdown templates for reports
├── schemas/                      # JSON schema for lap data
└── acc-json-tools/              # Python conversion utilities
```

### Directory Purpose

**Championship Level (`events/[championship]/`)**
- Groups all events from the same championship
- Contains championship-wide analysis (`analise_campeonato.md`)
- Examples: `piloteiro-amador`, `liga-gt3-pro`, etc.

**Event Level (`events/[championship]/[event]/`)**
- Individual race weekend preparation
- Naming: `YYYY-MM-DD_track_duration` (e.g., `2025-10-19_barcelona_60min`)

**Four Core Directories:**
1. **`sessions/`**: ONLY raw data files (JSON exports from ACC)
2. **`setups/`**: ONLY car setup files and setup-related documentation
3. **`analysis/`**: ONLY technical analyses organized by session
4. **`reports/`**: ONLY consolidated reports and summaries

## Data Format

### Session Data (Flat Format)
Session files contain an array of lap objects with the following fields:
- `lap`: Lap number
- `time`: Lap time (ms and formatted)
- `splits`: Array of sector times [S1, S2, S3]
- `type`: Lap type (Regular/Outlap/Inlap)
- `valid`: Boolean indicating if lap is valid
- `tyre`: Tyre data (pressure, temperature, compound, currentTyreSet)
- `carInfo`: Car data (fuel, damage, TC/ABS settings)
- `environment`: Track conditions (air/road temp, rain, wind)
- `trackGripStatus`: Track grip level (OPTIMUM/FAST/GREEN)

### Stint Detection
When analyzing sessions, stints are identified by:
1. **Outlap** starts new stint (closes previous if exists)
2. **Tyre set change** splits stint (for regular laps only)
3. **Inlap** ends current stint (inlap included in that stint)

## Workflow Pattern

### Training Session Workflow
1. Read training plan: `events/[championship]/[event]/plano_treino.md`
2. Process session data from `sessions/session[n].json`
3. Generate daily report: `reports/treino[n].md`
4. Update evolution report: `reports/evolucao_treinos.md`
5. Technical analysis (optional): `analysis/session_[n]/`

### File Organization Rules

**When creating new files:**

- **Session data (JSON)** → Always goes in `sessions/`
  - Format: `sessionN.json`, `sessionN_stintM.json`
  - Opponents: `sessionN_adversario_type.json`

- **Setup files** → Always goes in `setups/`
  - Screenshots: `setups/setup_treino_N/`
  - JSON configs: `setups/setup_treino_N/config.json`
  - Analysis: `setups/setup_analysis.md`

- **Technical analysis** → Always goes in `analysis/session_N/`
  - Tyre analysis: `analysis/sessionN/tyre_stintM.md`
  - Images: `analysis/sessionN/*.png`
  - Setup tests: `analysis/sessionN/setup_test.md`

- **Reports** → Always goes in `reports/`
  - Daily: `reports/treinoN.md`
  - Evolution: `reports/evolucao_treinos.md`
  - Race analysis: `reports/analise_corrida_oficial.md`

### Report Guidelines (from PROMPT_TREINAMENTO.md)
- **Never overwrite** previous training summaries
- **Always append** new training days
- **Preserve** existing sector analysis and progression data
- **Compare** against reference times defined in training plan
- **Prioritize** sector improvements by gap size

### Track Guide References
When analyzing track performance:
- Check `circuits/[track]/reports/curvas_comparativo.md` for corner-by-corner guide
- Reference transcriptions in `circuits/[track]/transcripts/`
- Note differences between expert sources (marked in italics)

## Analysis Guidelines

### Key Metrics to Extract
When analyzing session data, focus on:
- **Best lap time** and sector times
- **Valid laps** only (unless analyzing errors)
- **Consistency:** Average lap time, standard deviation
- **Fuel consumption:** Average L/lap, estimate for race distance
- **Tyre data:** Pressures (hot), temperatures, degradation across stint
- **Track conditions:** Air/road temperature, grip status
- **Stint breakdown:** Identify stints by tyre changes and outlap/inlap patterns

## Training Plan Philosophy

Event naming: `YYYY-MM-DD_track_duration` (e.g., `2025-10-19_barcelona_60min`)

Training progression:
1. **Day 1**: Baseline data collection (lap times, sectors, gear mapping)
2. **Days 2-4**: Sector-focused improvement (prioritized by gap to reference)
3. **Day 5**: Long stint + pit stop practice
4. **Day 6**: Full race simulation

Pit stop timing (configurable per event):
- Fuel only: 25s
- Fuel + tyres: 30s
- Fuel rate: 1.2s + 0.2s/liter (alternative)

## Report Templates

All templates in `templates/`:
- `plano_treino_template.md` → Training plan structure
- `treino_dia_template.md` → Daily session report
- `evolucao_treinos_template.md` → Cumulative evolution tracking
- `circuits/_template/report/curva-a-curva-template.md` → Track guide

When generating reports, always:
- Copy template to correct event path
- Fill all placeholders with actual data
- Preserve markdown formatting and tables
- Include timestamp and session metadata

## Championship Analysis

Championship-level analysis (`analise_campeonato.md`) should include:
- **Current standings**: Position, points, gap to rivals
- **Recent form**: Last 3-5 races performance trend
- **Statistical comparison**: You vs main rivals
- **Projections**: Scenarios for remaining races
- **Strategy**: Tactical approach for title fight

Update after each race with:
- New race results
- Updated standings and projections
- Performance analysis vs competitors
- Adjusted probability of championship victory

## Best Practices

### Adding New Event
```bash
# Create event structure
mkdir -p events/[championship]/[event]/{sessions,setups,analysis,reports}

# Copy training plan template
cp templates/plano_treino_template.md events/[championship]/[event]/plano_treino.md
```

### File Naming Conventions
- **Sessions**: `sessionN.json` (sequential numbers)
- **Opponents**: `sessionN_adversario_type.json` (type: rival, silver, pro, p1)
- **Training reports**: `treinoN.md` (matches session number)
- **Analysis**: Descriptive names with context (`tyre_stint1_analysis.md`)

### Keeping Analysis Organized
- One folder per analyzed session in `analysis/`
- Group related files (markdown + images) in same folder
- Use clear, descriptive filenames
- Include session number in folder name

## Common Tasks

### Analyzing a Training Session
1. Export JSON from ACC → Save to `sessions/sessionN.json`
2. Read `plano_treino.md` for objectives
3. Analyze data (lap times, sectors, consistency)
4. If needed, create `analysis/session_N/` for technical details
5. Generate `reports/treinoN.md` with findings
6. Update `reports/evolucao_treinos.md` with progress

### Preparing for Race
1. Review `reports/evolucao_treinos.md`
2. Analyze opponents: `reports/analise_adversarios.md`
3. Create race strategy: `reports/plano_corrida.md`
4. Validate setup in `setups/`

### Post-Race Analysis
1. Export race data → `sessions/race_oficial.json`
2. Export opponent data → `sessions/race_oficial_*.json`
3. Analyze performance → `reports/analise_corrida_oficial.md`
4. Update championship standing → `analise_campeonato.md`
