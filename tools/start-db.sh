#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
# start-db.sh — Start the HOI4 PostgreSQL database container
#
# If the container doesn't exist yet, creates it from docker-compose.
# If it exists but is stopped, starts it.
# If it's already running, just confirms the connection.
#
# Usage:
#   bash tools/start-db.sh
# ─────────────────────────────────────────────────────────────
set -euo pipefail

CONTAINER="hoi4-db"
DB="hoi4"
USER="hoi4"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# --- Already running? ---
if docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "Container '$CONTAINER' is already running."

# --- Exists but stopped? ---
elif docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "Starting stopped container '$CONTAINER'..."
    docker start "$CONTAINER"
    echo "Waiting for PostgreSQL to be ready..."
    sleep 3

# --- Doesn't exist — create via docker-compose ---
else
    echo "Creating container from docker-compose.yml..."
    docker compose -f "$REPO_ROOT/docker-compose.yml" up -d
    echo "Waiting for PostgreSQL to be ready..."
    sleep 3
fi

# --- Verify connection (retry up to 10 seconds) ---
echo ""
for i in $(seq 1 10); do
    if docker exec "$CONTAINER" psql -U "$USER" -d "$DB" -c "SELECT 1;" > /dev/null 2>&1; then
        echo "Database is ready at localhost:5432"
        docker exec "$CONTAINER" psql -U "$USER" -d "$DB" -c "
        SELECT 'tables' AS what, count(*)::text AS n
          FROM information_schema.tables
         WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
        UNION ALL
        SELECT 'total rows', sum(n)::text FROM (
            SELECT schemaname, relname, n_live_tup AS n
              FROM pg_stat_user_tables
        ) t;
        "
        exit 0
    fi
    echo "Waiting for PostgreSQL... ($i/10)"
    sleep 1
done

echo "ERROR: Could not connect to database after 10 seconds."
echo "Check 'docker logs $CONTAINER' for details."
exit 1
