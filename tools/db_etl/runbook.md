# HOI4 Database ETL — Runbook

Status: **COMPLETE** — extracts game data → markdown → CSV → PostgreSQL (all 127 tables)

## Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.10+ |
| PostgreSQL | 15+ |
| HOI4 installation | Default Steam path or specify via `--hoi4-root` / `HOI4_ROOT` |

## Environment Variables

```bash
# Only needed for Phase 1 (extraction from game files)
export HOI4_ROOT="/path/to/Hearts of Iron IV"

# Only needed for Phase 3 (loading into PostgreSQL)
export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=hoi4
export PGUSER=hoi4_etl
export PGPASSWORD=<secret>
```

---

## Phase 1: Extract Game Data → Markdown

```bash
# Run the extractor (auto-detects HOI4 install or use --hoi4-root)
python tools/db_etl/export_markdown_dump.py

# Output: docs/data-dump/ — 137 markdown files (~221K rows)
# Check docs/data-dump/SUMMARY.md for per-dataset row counts
```

---

## Phase 2: Convert Markdown → CSV

```bash
# Convert all markdown dumps to PostgreSQL-ready CSV files
python tools/db_etl/md_to_csv.py

# Output: data/csv/ — 127 CSV files (~221K rows)
# Use --verbose for per-file details
python tools/db_etl/md_to_csv.py --verbose
```

The converter handles:
- Column renames (markdown names → schema names)
- Multi-source merges (country_tags + countries_visuals + country_history → countries.csv)
- Multi-target splits (focus_links → focus_prerequisites + focus_mutually_exclusive)
- Subset filtering (skips _ger/_germany/_infantry review-only extracts when _all version exists)

### Phase 2b: Regenerate Seed-Load SQL (if schema or CSVs changed)

```bash
# Reads CSV headers and regenerates seed-load-order.sql with explicit column lists
python tools/db_etl/gen_seed_sql.py
```

Run this after any change to the schema or CSV column names. It generates `\copy` commands with explicit column lists (so SERIAL PKs auto-generate) and staging temp tables for the 6 tables that need FK resolution from natural keys to surrogate IDs.

---

## Phase 3: Create Database & Load

```bash
# Create the database
createdb hoi4

# Run DDL — creates all 127 tables, FKs, indexes
psql -d hoi4 -f sql/schema.sql

# Verify table count
psql -d hoi4 -c "SELECT count(*) FROM information_schema.tables WHERE table_schema='public';"
# Expected: 127

# Load data (\copy commands are live — runs in a single transaction)
psql -d hoi4 -f sql/seed-load-order.sql

# Or load individual tables manually:
psql -d hoi4 -c "\copy continents FROM 'data/csv/continents.csv' WITH (FORMAT csv, HEADER);"
```

> **Note:** Run `psql` from the repo root so the `data/csv/` paths resolve correctly.
> The seed-load-order.sql script is wrapped in `BEGIN`/`COMMIT` with `\set ON_ERROR_STOP on`,
> so any failure rolls back the entire load.

---

## Phase 4: Validate

```bash
# Markdown-level validation (FK, PK, NOT NULL checks on the dump files)
python tools/db_etl/validate_data.py

# PostgreSQL-level validation (after loading)
psql -d hoi4 -c "SELECT count(*) FROM countries;"    -- Expected: 352
psql -d hoi4 -c "SELECT count(*) FROM states;"       -- Expected: 1046
psql -d hoi4 -c "SELECT count(*) FROM technologies;" -- Expected: 569
```

---

## Phase 5: API Views

```bash
# Create views for API endpoints
psql -d hoi4 -f sql/views.sql
```

---

## Full Reload

To reload all data from scratch (e.g., after a game patch or re-extraction):

```bash
# 1. Re-extract markdown from game files
python tools/db_etl/export_markdown_dump.py

# 2. Re-convert markdown to CSV
python tools/db_etl/md_to_csv.py

# 3. Regenerate seed-load-order.sql (picks up any new/renamed columns)
python tools/db_etl/gen_seed_sql.py

# 4. Drop and recreate the database, then reload
dropdb hoi4
createdb hoi4
psql -d hoi4 -f sql/schema.sql
psql -d hoi4 -f sql/seed-load-order.sql
psql -d hoi4 -f sql/views.sql
```

> Changes to the CSV files do NOT automatically propagate to PostgreSQL.
> You must drop and recreate the database (or `TRUNCATE` all tables) and re-run `seed-load-order.sql` to reload.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| FK violation on `\copy` | Loading out of tier order | Follow the tier order in seed-load-order.sql |
| Duplicate PK error | Re-running without dropping/truncating | Drop and recreate the database, or `TRUNCATE` all tables before reloading |
| CSV column mismatch | Schema changed after CSV generation | Re-run `md_to_csv.py` then `gen_seed_sql.py` to regenerate CSVs and load SQL |
| Missing DLC data | DLC not installed | Check `HOI4_ROOT/dlc/` directory; parser skips missing files |
| Provinces count doubled | Markdown has wrapped rows | Re-run `md_to_csv.py` (handles continuation lines) |
| 0 rows from air/naval parser | Wrong glob pattern | Verify `history/units/` filenames match `*_naval_*` / `*_air_*` patterns |

---

## Full Reload from Scratch

```bash
dropdb hoi4
createdb hoi4
psql -d hoi4 -f sql/schema.sql
python tools/db_etl/export_markdown_dump.py
python tools/db_etl/md_to_csv.py
python tools/db_etl/gen_seed_sql.py
psql -d hoi4 -f sql/seed-load-order.sql
psql -d hoi4 -f sql/views.sql
```
