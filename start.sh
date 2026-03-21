#!/bin/bash
# Hockey DJ - Oppstart (Mac / Linux)
# Dobbeltklikk, eller kjør: bash start.sh

cd "$(dirname "$0")"

# Prøv python3 først, deretter python
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo ""
    echo "  ❌  Python er ikke funnet."
    echo "  Last ned fra https://python.org eller spør IT."
    echo ""
    read -p "Trykk Enter for å lukke..."
    exit 1
fi

echo ""
echo "  Bruker: $($PYTHON --version)"
echo ""
$PYTHON server.py
