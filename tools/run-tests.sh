#!/usr/bin/env bash
# tools/run-tests.sh — Activate existing venv and run the API test suite.
# Usage: bash tools/run-tests.sh [pytest args...]
# Example: bash tools/run-tests.sh -v --tb=short -k test_countries

set -euo pipefail

cd "$(dirname "$0")/../api"

source .venv/bin/activate

python3 -m pytest tests/ "$@"
