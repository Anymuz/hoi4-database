#!/usr/bin/env bash
# -------------------------------------------------------------
# stop-db.sh - Stop the HOI4 PostgreSQL database container
#
# Stops the container but keeps it and its data volume intact.
# Run start-db.sh to bring it back up.
#
# Usage:
#   bash tools/stop-db.sh
# -------------------------------------------------------------
set -euo pipefail

CONTAINER="hoi4-db"

if docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "Stopping '$CONTAINER'..."
    docker stop "$CONTAINER"
    echo "Stopped. Data is preserved - run 'bash tools/start-db.sh' to restart."
else
    echo "Container '$CONTAINER' is not running."
fi
