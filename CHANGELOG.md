# Changelog

All notable changes to the ACC Training System will be documented in this file.

---

## [2.0.0] - 2025-10-19

### Major Restructuring - Championship-Based Organization

#### Changed
- **Directory Structure**: Reorganized from year-based to championship-based structure
  - Old: `events/2025/[event]/`
  - New: `events/[championship]/[event]/`

- **Event Organization**: Split `data/` into four specialized directories
  - `sessions/` - Raw session data (JSON files only)
  - `setups/` - Car setup files and documentation
  - `analysis/` - Technical analyses organized by session
  - `reports/` - Consolidated reports and summaries

#### Added
- **Championship Analysis**: Added `analise_campeonato.md` at championship level
  - Tracks overall championship standings
  - Performance trends and projections
  - Statistical comparison with rivals
  - Title probability calculations

- **Documentation**:
  - Updated `CLAUDE.md` with new structure and workflow
  - Expanded `README.md` with comprehensive guide
  - Created `QUICK_REFERENCE.md` for daily use
  - Added `scripts/create_event.sh` helper script

- **File Organization Rules**: Clear guidelines for where each type of file belongs
  - Session data → `sessions/`
  - Setups → `setups/`
  - Technical analysis → `analysis/`
  - Reports → `reports/`

#### Benefits
- ✅ Clear separation of concerns
- ✅ Easier navigation and file discovery
- ✅ Scalable for multiple championships
- ✅ Championship-level tracking
- ✅ Better organization of technical analyses

---

## [1.0.0] - 2025-10-05

### Initial Structure

#### Added
- Basic directory structure with `data/` and `reports/`
- Training plan templates
- Session analysis workflow
- Evolution tracking system
- Track guides with video transcriptions
- Python tools for data conversion
- JSON schema for lap data

#### Features
- Daily training reports
- Lap time evolution tracking
- Sector-by-sector analysis
- Setup documentation
- Pit stop timing calculations

---

## Migration Guide (1.0 → 2.0)

### For Existing Events

If you have events in the old structure, migrate as follows:

```bash
# Old structure
events/2025/2025-10-19_barcelona_60min/
├── data/
└── reports/

# New structure
events/piloteiro-amador/2025-10-19_barcelona_60min/
├── plano_treino.md
├── sessions/        # Move JSON files from data/
├── setups/          # Move setup files from data/
├── analysis/        # Move session-specific analyses
└── reports/         # Keep as is
```

### Steps

1. **Create championship directory**:
   ```bash
   mkdir -p events/[championship]
   ```

2. **Move event**:
   ```bash
   mv events/2025/[event] events/[championship]/
   ```

3. **Reorganize files**:
   - Move all `.json` files → `sessions/`
   - Move setup folders → `setups/`
   - Move session-specific analysis → `analysis/`
   - Keep `reports/` as is
   - Move `plano_treino.md` to event root

4. **Create championship analysis**:
   ```bash
   # Create analise_campeonato.md at championship level
   touch events/[championship]/analise_campeonato.md
   ```

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible structure changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, documentation updates

---

## Future Plans

### Planned Features
- [ ] Automated session analysis scripts
- [ ] Data visualization dashboards
- [ ] Telemetry integration
- [ ] Multi-championship comparison
- [ ] Performance prediction models
- [ ] Setup optimization suggestions

### Under Consideration
- [ ] Web interface for data exploration
- [ ] Real-time race strategy calculator
- [ ] Integration with ACC telemetry export
- [ ] Machine learning for sector optimization
- [ ] Mobile app for quick reference

---

**Current Version**: 2.0.0
**Last Updated**: 2025-10-19
