#!/usr/bin/env bash
# tools/setup-api.sh — Create venv, install deps, copy .env, run tests.
# Usage: sudo bash tools/setup-api.sh

set -euo pipefail

cd "$(dirname "$0")/../api"

echo "=== Creating venv ==="
python3 -m venv --copies .venv
source .venv/bin/activate

echo "=== Installing dependencies ==="
python3 -m pip install --upgrade pip -q
python3 -m pip install -r requirements.txt -q

if [ ! -f .env ]; then
    echo "=== Copying .env.example → .env ==="
    cp .env.example .env
else
    echo "=== .env already exists, skipping ==="
fi

echo "=== Running tests ==="
python3 -m pytest tests/ -v

echo "=== Done ==="
