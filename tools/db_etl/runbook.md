# HOI4 Database - Deployment & ETL Runbook

Complete guide for extracting HOI4 game data, converting it to CSV, and loading
it into PostgreSQL - with both Docker and native deployment options.

---

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Python | 3.10+ | Standard library only - no pip packages needed |
| HOI4 installation | Any | Default Steam path, or specify via `--hoi4-root` / `HOI4_ROOT` |
| **Docker** (Option A) | 20+ | Docker Desktop on Windows/Mac, or Docker Engine on Linux |
| **PostgreSQL** (Option B) | 15+ | With `psql` and `createdb` on PATH |

You need **either** Docker or a native PostgreSQL installation, not both.

### HOI4 Path Resolution

The extraction script finds your HOI4 install in this order:

1. `--hoi4-root <path>` CLI argument (highest priority)
2. `HOI4_ROOT` environment variable
3. Auto-detection:
   - **Windows:** `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
   - **Linux:** `~/.steam/steam/steamapps/common/Hearts of Iron IV`

---

## Step 1: Extract Game Data -> Markdown

```bash
python tools/db_etl/export_markdown_dump.py
# Or with explicit path:
python tools/db_etl/export_markdown_dump.py --hoi4-root "/path/to/Hearts of Iron IV"
```

**Output:** `docs/data-dump/` - 166 markdown files (~360K rows across 28 schema phases + V2).
Check `docs/data-dump/SUMMARY.md` for per-dataset row counts.

> **Windows note:** If you see encoding errors, set `$env:PYTHONIOENCODING='utf-8'` first.

### Step 1b: Extract Localisation

```bash
python tools/db_etl/export_localisation.py
# Or with explicit path:
python tools/db_etl/export_localisation.py --hoi4-root "/path/to/Hearts of Iron IV"
```

**Output:** `data/csv/localisation.csv` - 117,490 English display-name translations from 189 `*_l_english.yml` files.
These are loaded separately from the main seed (the localisation table has no FK dependencies).

---

## Step 2: Convert Markdown -> CSV

```bash
# Convert markdown dumps to PostgreSQL-ready CSVs
python tools/db_etl/md_to_csv.py

```

**Output:** `data/csv/` - 156 CSV files (~360K rows), one per schema table.
(Localisation CSV is produced separately by `export_localisation.py` - see Step 1b.)

The converter handles column renames, multi-source merges (e.g., country_tags +
countries_visuals + country_history -> countries.csv), multi-target splits
(e.g., focus_links -> focus_prerequisites + focus_mutually_exclusive), and
subset filtering.

### Step 2b: Regenerate Seed SQL (only if schema or CSV columns changed)

```bash
python tools/db_etl/gen_seed_sql.py       # generates sql/seed-load-order.sql
python tools/db_etl/gen_seed_docker.py     # generates sql/seed-docker.sql
```

These scripts read CSV headers and produce `\copy` (native) and `COPY` (Docker)
commands with explicit column lists. Re-run after any schema or CSV column change.

---

## Step 3: Deploy PostgreSQL & Load Data

### Option A: Docker (Recommended)

Docker is the simplest option - no local PostgreSQL installation needed.

**1. Start the container:**

```bash
docker run -d \
  --name hoi4-db \
  -e POSTGRES_USER=hoi4 \
  -e POSTGRES_PASSWORD=hoi4pass \
  -e POSTGRES_DB=hoi4 \
  -p 5432:5432 \
  -v hoi4_pgdata:/var/lib/postgresql/data \
  postgres:16-alpine
```

**2. Copy files into the container and load:**

```bash
# Copy schema, CSVs, seed script, and views
docker cp sql/schema.sql       hoi4-db:/tmp/schema.sql
docker cp data/csv              hoi4-db:/data_csv
docker cp sql/seed-docker.sql   hoi4-db:/tmp/seed.sql
docker cp sql/views.sql         hoi4-db:/tmp/views.sql

# Load schema (151 tables, 63 indexes)
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/schema.sql

# Load data (~225K game rows across 7 FK-safe tiers)
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/seed.sql

# Load localisation (~117K rows)
docker cp data/csv/localisation.csv hoi4-db:/data_csv/localisation.csv
docker exec hoi4-db psql -U hoi4 -d hoi4 -c "COPY localisation FROM '/data_csv/localisation.csv' CSV HEADER;"

# Create API views (14 views + 2 functions)
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/views.sql
```

**3. Connect:**

```bash
# Via docker exec
docker exec -it hoi4-db psql -U hoi4 -d hoi4

# Or via any PostgreSQL client
psql -h localhost -p 5432 -U hoi4 -d hoi4
# Password: hoi4pass
```

**Container management:**

```bash
docker stop hoi4-db           # Stop
docker start hoi4-db          # Restart (data persists in volume)
docker rm -f hoi4-db          # Remove container (volume persists)
docker volume rm hoi4_pgdata  # Delete data permanently
```

### Option B: Native PostgreSQL

Requires PostgreSQL 15+ installed locally with `psql` and `createdb` on PATH.

**1. Create the database:**

```bash
createdb hoi4
```

**2. Load schema, data, and views:**

```bash
# Run from the repo root so data/csv/ paths resolve correctly
psql -d hoi4 -f sql/schema.sql
psql -d hoi4 -f sql/seed-load-order.sql
psql -d hoi4 -f sql/views.sql
```

> The seed script uses client-side `\copy` commands that read CSV files from
> your local filesystem. You **must** run `psql` from the repository root.

**Connection with custom credentials:**

```bash
export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=hoi4
export PGUSER=your_user
export PGPASSWORD=your_password
psql -f sql/schema.sql
```

---

## Step 4: Verify

Run these after loading to confirm everything is correct:

```bash
# Table count (expect 151)
psql -d hoi4 -c "SELECT count(*) FROM information_schema.tables WHERE table_schema='public';"

# Total row count (expect ~225K)
psql -d hoi4 -c "
  SELECT sum(n_live_tup)::int AS total_rows
  FROM pg_stat_user_tables;" 

# Spot-check key tables
psql -d hoi4 -c "SELECT count(*) FROM countries;"       -- ~428
psql -d hoi4 -c "SELECT count(*) FROM states;"          -- ~1046
psql -d hoi4 -c "SELECT count(*) FROM technologies;"    -- ~574
psql -d hoi4 -c "SELECT count(*) FROM characters;"      -- ~5138
psql -d hoi4 -c "SELECT count(*) FROM focuses;"         -- ~9906

# FK integrity check (all should return rows)
psql -d hoi4 -c "
  SELECT 'equipment FK' AS check_name, count(*) AS rows 
  FROM equipment_definitions ed 
  JOIN equipment_definitions arch ON ed.archetype_key = arch.equipment_key
  WHERE ed.archetype_key IS NOT NULL;"
```

For Docker, prefix each `psql` command with `docker exec hoi4-db`.

### Pre-load validation (optional)

Run FK/PK/NOT NULL checks against the markdown dumps before loading:

```bash
python tools/db_etl/validate_data.py
```

---

## Step 5: API Views

The 14 views + 2 functions are created during Step 3. To reload them independently:

```bash
# Native
psql -d hoi4 -f sql/views.sql

# Docker
docker cp sql/views.sql hoi4-db:/tmp/views.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/views.sql
```

---

## Full Reload

To reload all data from scratch (e.g., after a game patch or schema change):

### Docker

```bash
# Re-extract and re-convert
python tools/db_etl/export_markdown_dump.py
python tools/db_etl/export_localisation.py
python tools/db_etl/md_to_csv.py
python tools/db_etl/gen_seed_sql.py
python tools/db_etl/gen_seed_docker.py

# Reset database and reload
docker exec hoi4-db psql -U hoi4 -d hoi4 -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
docker cp sql/schema.sql       hoi4-db:/tmp/schema.sql
docker exec hoi4-db rm -rf /data_csv
docker cp data/csv              hoi4-db:/data_csv
docker cp sql/seed-docker.sql   hoi4-db:/tmp/seed.sql
docker cp sql/views.sql         hoi4-db:/tmp/views.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/schema.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/seed.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -c "COPY localisation FROM '/data_csv/localisation.csv' CSV HEADER;"
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/views.sql
```

### Native PostgreSQL

```bash
python tools/db_etl/export_markdown_dump.py
python tools/db_etl/md_to_csv.py
python tools/db_etl/gen_seed_sql.py

dropdb hoi4 && createdb hoi4
psql -d hoi4 -f sql/schema.sql
psql -d hoi4 -f sql/seed-load-order.sql
psql -d hoi4 -f sql/views.sql
```

> CSV changes do NOT automatically propagate to PostgreSQL. You must drop/recreate
> the schema and re-run the seed script to reload.

---

## ETL Pipeline Summary

```
export_markdown_dump.py     HOI4 game files -> 160 markdown dumps
        v
md_to_csv.py                Markdown -> 149 CSV files (renames, merges, splits)
        v
gen_seed_sql.py             Generates seed-load-order.sql (native \copy)
gen_seed_docker.py          Generates seed-docker.sql (Docker COPY)
        v
psql -f schema.sql          Create 151 tables + indexes
psql -f seed[-docker].sql   Load ~225K rows in FK-safe tier order
psql -f views.sql           Create 14 API views + 2 functions
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Encoding errors on Windows | Non-UTF-8 console | Set `$env:PYTHONIOENCODING='utf-8'` before running Python scripts |
| FK violation during load | CSV data loaded out of tier order | Always use the generated seed script - it handles FK ordering |
| Duplicate PK error | Re-loading without clearing data | Drop and recreate: `DROP SCHEMA public CASCADE; CREATE SCHEMA public;` then reload |
| CSV column mismatch | Schema changed after CSV generation | Re-run `md_to_csv.py` -> `gen_seed_sql.py` |
| Missing DLC data | DLC not installed in HOI4 | Check `HOI4_ROOT/dlc/` directory; parsers skip missing files gracefully |
| 0 rows from air/naval parser | Wrong file pattern | Verify `history/units/` filenames match `*_naval_*` / `*_air_*` patterns |
| `seed-docker.sql` not found | Not generated yet | Run `python tools/db_etl/gen_seed_docker.py` |
| `\copy` fails with path error | psql not run from repo root | `cd` to the repository root before running `psql -f sql/seed-load-order.sql` |
| Docker: "container not found" | Container not started | Run `docker start hoi4-db` or create with `docker run` command above |
