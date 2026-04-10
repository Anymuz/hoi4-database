#!/usr/bin/env bash
# tools/start-api.sh - Start the FastAPI server (Uvicorn).
# Activates the venv and launches on 0.0.0.0:8000 with auto-reload.
# Usage: bash tools/start-api.sh

set -euo pipefail
cd "$(dirname "$0")/../api"
source .venv/bin/activate

echo "Starting FastAPI on http://localhost:8000 ..."
echo "Swagger docs: http://localhost:8000/docs"
echo "Press Ctrl+C to stop."
echo ""

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
