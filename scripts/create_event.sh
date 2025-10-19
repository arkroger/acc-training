#!/bin/bash

# ACC Training - Create New Event Script
# Usage: ./create_event.sh [championship] [YYYY-MM-DD_track_duration]
# Example: ./create_event.sh piloteiro-amador 2025-11-15_monza_60min

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check arguments
if [ $# -ne 2 ]; then
    echo -e "${RED}Error: Missing arguments${NC}"
    echo "Usage: $0 [championship] [YYYY-MM-DD_track_duration]"
    echo "Example: $0 piloteiro-amador 2025-11-15_monza_60min"
    exit 1
fi

CHAMPIONSHIP=$1
EVENT=$2
BASE_DIR="events/${CHAMPIONSHIP}/${EVENT}"

# Validate event naming format
if ! [[ $EVENT =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}_[a-z]+_[0-9]+min$ ]]; then
    echo -e "${YELLOW}Warning: Event name doesn't match recommended format${NC}"
    echo "Recommended: YYYY-MM-DD_track_duration (e.g., 2025-11-15_monza_60min)"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo -e "${GREEN}Creating event structure...${NC}"
echo "Championship: ${CHAMPIONSHIP}"
echo "Event: ${EVENT}"
echo "Path: ${BASE_DIR}"
echo

# Create directory structure
mkdir -p "${BASE_DIR}/sessions"
mkdir -p "${BASE_DIR}/setups"
mkdir -p "${BASE_DIR}/analysis"
mkdir -p "${BASE_DIR}/reports"

echo -e "${GREEN}✓ Created directory structure${NC}"

# Copy training plan template
if [ -f "templates/plano_treino_template.md" ]; then
    cp "templates/plano_treino_template.md" "${BASE_DIR}/plano_treino.md"
    echo -e "${GREEN}✓ Copied training plan template${NC}"
else
    echo -e "${YELLOW}⚠ Warning: Training plan template not found${NC}"
fi

# Create README for the event
cat > "${BASE_DIR}/README.md" << EOF
# ${EVENT}

**Championship:** ${CHAMPIONSHIP}
**Created:** $(date +%Y-%m-%d)

## Event Structure

\`\`\`
${EVENT}/
├── plano_treino.md          # Training plan
├── sessions/                # Raw session data (JSON)
├── setups/                  # Car setups
├── analysis/                # Technical analyses
└── reports/                 # Consolidated reports
\`\`\`

## Quick Start

1. Update \`plano_treino.md\` with event-specific objectives
2. Export session data from ACC → Save to \`sessions/sessionN.json\`
3. Ask Claude to analyze sessions
4. Review reports in \`reports/\`

## Files

### Sessions
- \`sessionN.json\` - Training sessions
- \`qualy_oficial.json\` - Qualifying
- \`race_oficial.json\` - Race

### Reports
- \`treinoN.md\` - Daily training reports
- \`evolucao_treinos.md\` - Evolution tracking
- \`analise_corrida_oficial.md\` - Race analysis

## Status

- [ ] Training plan created
- [ ] Baseline session completed
- [ ] Setup validated
- [ ] Race simulation completed
- [ ] Race completed
EOF

echo -e "${GREEN}✓ Created event README${NC}"

# Create .gitkeep files to preserve empty directories
touch "${BASE_DIR}/sessions/.gitkeep"
touch "${BASE_DIR}/setups/.gitkeep"
touch "${BASE_DIR}/analysis/.gitkeep"
touch "${BASE_DIR}/reports/.gitkeep"

echo -e "${GREEN}✓ Created .gitkeep files${NC}"

# Summary
echo
echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}Event created successfully!${NC}"
echo -e "${GREEN}================================${NC}"
echo
echo "Next steps:"
echo "1. Edit: ${BASE_DIR}/plano_treino.md"
echo "2. Start training and save sessions to: ${BASE_DIR}/sessions/"
echo "3. Ask Claude to analyze sessions"
echo
echo "Quick commands:"
echo "  cd ${BASE_DIR}"
echo "  ls -la"
echo
