# ACC Training Log

Data-driven training and race preparation system for **Assetto Corsa Competizione** amateur racing championships.

## Overview

This repository provides a structured approach to:
- 📊 Track training progress across multiple events
- 🏎️ Analyze lap times, sectors, and race pace
- 📈 Monitor evolution and identify improvement areas
- 🎯 Prepare race strategies based on data
- 🏆 Track championship standings and projections

## Quick Start

### 1. Create New Event

```bash
# Create event structure
mkdir -p events/[championship]/[YYYY-MM-DD_track_duration]/{sessions,setups,analysis,reports}

# Example
mkdir -p events/piloteiro-amador/2025-10-19_barcelona_60min/{sessions,setups,analysis,reports}
```

### 2. Copy Training Plan Template

```bash
cp templates/plano_treino_template.md events/[championship]/[event]/plano_treino.md
```

### 3. Training Workflow

1. **Export session data** from ACC → Save to `sessions/sessionN.json`
2. **Analyze session** → Generate `reports/treinoN.md`
3. **Update evolution** → Update `reports/evolucao_treinos.md`
4. **Technical analysis** (optional) → Create `analysis/session_N/`

## Directory Structure

```
acc-training/
├── events/[championship]/           # Championship organization
│   ├── analise_campeonato.md       # Championship analysis
│   └── [event]/                     # Individual event
│       ├── plano_treino.md          # Training plan
│       ├── sessions/                # Raw data (JSON)
│       ├── setups/                  # Car setups
│       ├── analysis/                # Technical analyses
│       └── reports/                 # Consolidated reports
│
├── circuits/[track]/                # Track-specific data
│   ├── transcripts/                 # Video transcriptions
│   └── reports/                     # Track guides
│
├── templates/                       # Report templates
├── schemas/                         # Data schemas
└── acc-json-tools/                  # Conversion utilities
```

## File Organization

### Sessions Directory (`sessions/`)
Raw data files only:
- `sessionN.json` - Training sessions
- `qualy_oficial.json` - Qualifying data
- `race_oficial.json` - Race data
- `race_oficial_rival.json` - Opponent data

### Setups Directory (`setups/`)
Car configurations:
- `setup_treino_N/` - Setup files and screenshots
- `setup_*.md` - Setup documentation and proposals

### Analysis Directory (`analysis/`)
Technical analyses organized by session:
- `session_N/tyre_*.md` - Tyre analysis
- `session_N/*.png` - Analysis images
- `session_N/setup_*.md` - Setup tests

### Reports Directory (`reports/`)
Consolidated reports:
- `treinoN.md` - Daily training reports
- `evolucao_treinos.md` - Evolution tracking
- `analise_corrida_oficial.md` - Race analysis
- `analise_adversarios.md` - Opponent analysis
- `plano_corrida.md` - Race strategy

## Key Features

### Training Progression
1. **Baseline** - Collect initial data (lap times, sectors)
2. **Sector Focus** - Improve weakest sectors
3. **Long Stint** - Practice race pace and pit stops
4. **Race Simulation** - Full race preparation

### Championship Tracking
- Current standings and points
- Performance trends (last 3-5 races)
- Statistical comparison vs rivals
- Projections for remaining races
- Title probability calculations

### Data Analysis
- Lap time evolution
- Sector-by-sector comparison
- Consistency tracking
- Opponent pace analysis
- Setup validation

## Tools

### Data Conversion
```bash
# Convert flat lap data to unified schema
python acc-json-tools/flat_to_unified_mapper.py <input.json> <output.json>
```

### Templates Available
- `plano_treino_template.md` - Training plan structure
- `treino_dia_template.md` - Daily session report
- `evolucao_treinos_template.md` - Evolution tracking

## Best Practices

### File Naming
- **Sessions**: `sessionN.json` (sequential)
- **Opponents**: `sessionN_adversario_type.json`
- **Reports**: `treinoN.md` (matches session number)

### Workflow
- Never overwrite previous reports
- Always append new training days
- Update evolution tracking after each session
- Compare against reference times
- Prioritize improvements by gap size

### Championship Management
- Update `analise_campeonato.md` after each race
- Track performance trends
- Adjust strategy based on standings
- Monitor rival performance

## Common Tasks

### After Training Session
1. Export JSON from ACC
2. Save to `sessions/sessionN.json`
3. Analyze data
4. Generate `reports/treinoN.md`
5. Update `reports/evolucao_treinos.md`

### Before Race
1. Review `reports/evolucao_treinos.md`
2. Analyze opponents
3. Create race strategy
4. Validate setup

### After Race
1. Export race data
2. Analyze performance
3. Update championship standings
4. Adjust strategy for next race

## Documentation

### 📚 Complete Documentation

- **[CLAUDE.md](CLAUDE.md)** - Detailed guide for Claude Code
  - Directory structure and purpose
  - Data flow and schemas
  - Workflow patterns
  - Report guidelines
  - Championship analysis

- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Daily use reference
  - File organization quick guide
  - Common workflows
  - Useful prompts
  - Checklists

- **[CHANGELOG.md](CHANGELOG.md)** - Version history
  - Structure changes
  - New features
  - Migration guides

### 🛠️ Utilities

- **[scripts/create_event.sh](scripts/create_event.sh)** - Create new event structure
  ```bash
  ./scripts/create_event.sh piloteiro-amador 2025-11-15_monza_60min
  ```

## Examples

### Championship Organization
```
events/piloteiro-amador/
├── analise_campeonato.md              # Season tracking (14/18 races)
├── 2025-10-19_barcelona_60min/        # Event 1
├── 2025-11-15_monza_60min/            # Event 2
└── 2025-12-03_spa_120min/             # Event 3
```

### Event Structure
```
2025-10-19_barcelona_60min/
├── plano_treino.md                    # Training objectives
├── sessions/
│   ├── session1.json - session12.json # 12 training sessions
│   ├── qualy_oficial.json             # Qualifying
│   └── race_oficial.json              # Race
├── reports/
│   ├── treino1.md - treino10.md       # Daily progress
│   ├── evolucao_treinos.md            # Overall evolution
│   └── analise_corrida_oficial.md     # Race analysis
└── analysis/
    └── session10/                      # Technical analysis
        ├── tyre3.md
        └── tyre5.md
```

## License

Personal training repository.

---

**Last Updated:** 2025-10-19
**Current Championship:** Piloteiro Amador (14/18 races complete)
**Status:** P1 in championship (+27 points)
