#!/usr/bin/env bash
# tools/restart-api.sh - Stop then start the FastAPI server.
# Usage: bash tools/restart-api.sh

set -euo pipefail

SCRIPT_DIR="$(dirname "$0")"

bash "$SCRIPT_DIR/stop-api.sh"
sleep 1
bash "$SCRIPT_DIR/start-api.sh"
