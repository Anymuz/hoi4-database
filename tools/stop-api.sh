#!/usr/bin/env bash
# tools/stop-api.sh - Stop any running Uvicorn/FastAPI process.
# Usage: bash tools/stop-api.sh

set -euo pipefail

PIDS=$(pgrep -f "uvicorn app.main:app" || true)

if [ -z "$PIDS" ]; then
    echo "No running API process found."
else
    echo "Stopping API (PID: $PIDS)..."
    kill $PIDS
    echo "API stopped."
fi
