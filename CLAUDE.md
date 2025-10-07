# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository supports training preparation for **Assetto Corsa Competizione (ACC)** amateur racing championships. It manages training plans, lap time data, track guides, and progress reports for multi-day training sessions leading up to race events.

## Core Architecture

### Data Flow
1. **Raw lap data** (JSON) exported from ACC → stored in `events/[year]/[date_track_event]/data/`
2. **Flat lap arrays** converted to **unified schema** (meta + stints) via Python mapper
3. **Session analysis** generates daily training reports and evolution tracking
4. **Track guides** reference video transcriptions and expert advice (Yorkie, Driver61, etc.)

### Directory Structure
```
acc-training/
├── circuits/[track]/
│   ├── transcripts/       # Video transcriptions (JSON)
│   └── reports/           # Track guides (curva a curva)
├── events/[year]/[date_track_event]/
│   ├── data/              # Session JSON files
│   └── reports/           # Training plans + daily reports + evolution
├── templates/             # Markdown templates for reports
├── schemas/               # JSON schema for lap data
└── acc-json-tools/        # Python conversion utilities
```

## Key Commands

### Data Processing
```bash
# Convert flat lap data to unified schema
python acc-json-tools/flat_to_unified_mapper.py <input.json> <output.json>
```

**Input format:** Array of lap objects with fields:
- `lap`, `time`, `splits`, `type` (Regular/Outlap/Inlap)
- `valid`, `tyre.currentTyreSet`, `carInfo.fuel`
- `environment`, `trackGripStatus`

**Output format:** Unified schema with:
- `meta`: Event metadata, track conditions, traffic
- `stints`: Array of stints, each with tyre set, fuel levels, and laps array

### Stint Detection Rules
The mapper applies these rules automatically:
1. **Outlap starts new stint** (closes previous if exists)
2. **Tyre set change splits stint** (for regular laps only)
3. **Inlap ends current stint** (inlap included in that stint)

## Workflow Pattern

### Training Session Workflow
1. Read training plan: `events/[year]/[date_track]/plano_treino.md`
2. Process session data from `data/session[n].json`
3. Generate daily report: `reports/treino[n].md`
4. Update evolution report: `reports/evolucao_treinos.md`

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

## Data Schema

### Unified Lap Schema (schemas/lap_schema.json)
Required fields in `meta`:
- `event`, `track`, `car`, `condition.air_temp_c`, `condition.track_temp_c`

Required fields in each stint:
- `stint_no`, `laps[]` with `lap_no`, `valid`, `lap_time_ms`

Optional fields:
- `tyre_set`, `fuel_start_l`, `fuel_end_l`, `pressures_cold`
- Sector times: `s1_ms`, `s2_ms`, `s3_ms`

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
