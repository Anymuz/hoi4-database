#!/usr/bin/env bash
# -------------------------------------------------------------
# reload-db.sh - Nuke and reload the HOI4 database from scratch
#
# What it does:
#   1. Drops everything in the database (tables, functions, views)
#   2. Recreates the schema (all 151 tables)
#   3. Copies CSV files into the container
#   4. Loads all data (~225K rows)
#   5. Creates views/functions
#   6. Prints a quick row-count sanity check
#
# Usage (from the repo root):
#   bash tools/reload-db.sh
# -------------------------------------------------------------
set -euo pipefail

CONTAINER="hoi4-db"
DB="hoi4"
USER="hoi4"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== HOI4 Database Reload ==="
echo "Repo root: $REPO_ROOT"
echo "Container: $CONTAINER"
echo ""

# --- Check container is running ---
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "Container '$CONTAINER' is not running. Starting it..."
    docker start "$CONTAINER"
    sleep 2
fi

# --- Step 1: Drop everything ---
echo "[1/5] Dropping all objects..."
docker exec "$CONTAINER" psql -U "$USER" -d "$DB" -c \
    "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

# --- Step 2: Create schema ---
echo "[2/5] Creating schema..."
docker cp "$REPO_ROOT/sql/schema.sql" "$CONTAINER:/tmp/schema.sql"
docker exec "$CONTAINER" psql -U "$USER" -d "$DB" -f /tmp/schema.sql \
    > /dev/null

# --- Step 3: Copy CSVs into container ---
echo "[3/5] Copying CSV files into container..."
docker exec "$CONTAINER" rm -rf /data_csv
docker cp "$REPO_ROOT/data/csv" "$CONTAINER:/data_csv"

# --- Step 4: Load data ---
echo "[4/5] Loading data (~225K rows)..."
docker cp "$REPO_ROOT/sql/seed-docker.sql" "$CONTAINER:/tmp/seed.sql"
docker exec "$CONTAINER" psql -U "$USER" -d "$DB" -f /tmp/seed.sql \
    > /dev/null

# --- Step 5: Create views ---
echo "[5/5] Creating views..."
docker cp "$REPO_ROOT/sql/views.sql" "$CONTAINER:/tmp/views.sql"
docker exec "$CONTAINER" psql -U "$USER" -d "$DB" -f /tmp/views.sql \
    > /dev/null

# --- Sanity check ---
echo ""
echo "=== Sanity Check ==="
docker exec "$CONTAINER" psql -U "$USER" -d "$DB" -c "
SELECT 'tables' AS what, count(*)::text AS count
  FROM information_schema.tables
 WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
UNION ALL
SELECT 'views', count(*)::text
  FROM information_schema.views
 WHERE table_schema = 'public'
UNION ALL
SELECT 'functions', count(*)::text
  FROM information_schema.routines
 WHERE routine_schema = 'public'
UNION ALL
SELECT 'countries', count(*)::text FROM countries
UNION ALL
SELECT 'states', count(*)::text FROM states
UNION ALL
SELECT 'technologies', count(*)::text FROM technologies
UNION ALL
SELECT 'characters', count(*)::text FROM characters
ORDER BY what;
"

echo ""
echo "Done. Database reloaded."
