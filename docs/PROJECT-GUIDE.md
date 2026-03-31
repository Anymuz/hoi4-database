# HOI4 Database Project — Complete Guide

> **What this is**: A fully normalised PostgreSQL database schema designed to represent all Hearts of Iron IV starting-state game data, including every DLC. The database backs a REST API for country stats and starting conditions.

---

## Directory Map

```
hoi4-database/                         ← This repository (standalone, no game files)
│
├── README.md                          ← Top-level quick start
├── .gitignore
│
├── docs/                              ← All design documentation
│   ├── PROJECT-GUIDE.md               ← THIS FILE — start here
│   ├── hoi4-database-design.md        ← Master design document (phases, build order, DLC strategy)
│   ├── hoi4-er-diagram.mmd            ← Mermaid ER diagram (127 tables, 133 relationships)
│   ├── hoi4-table-catalog.md          ← Column-level specs for every table
│   ├── hoi4-source-to-table-map.md    ← Game file path → target table mapping
│   ├── hoi4-data-snapshots.md         ← Sample extracted rows per table
│   └── data-dump/                     ← 137 markdown data-dump files + SUMMARY
│       ├── SUMMARY.md                 ← Row counts for all 137 data dumps (~221K rows)
│       ├── countries_visuals.md       ← Country graphical culture data
│       ├── country_tags.md            ← TAG → file path mapping
│       ├── states.md                  ← All 1,046 state definitions
│       ├── provinces.md               ← All 13,382 province records
│       ├── technologies_all.md        ← All 569 technologies
│       ├── characters_all.md          ← All 5,160 characters
│       ├── focuses_all.md             ← All 8,498 national focuses
│       ├── ideas_all.md               ← All 5,947 ideas
│       ├── divisions_all.md           ← All 4,991 deployed divisions
│       └── ... (126 more files)       ← See SUMMARY.md for full list
│
├── sql/                               ← SQL deliverables
│   ├── schema.sql                     ← DDL for all 127 tables (23 phases)
│   ├── views.sql                      ← 14 API views (3 slices)
│   └── seed-load-order.sql            ← FK-safe insert order (all 127 tables, 7 tiers)
│
├── tools/
│   └── db_etl/                        ← ETL tooling
│       ├── export_markdown_dump.py    ← Extraction script (configurable HOI4 path)
│       ├── md_to_csv.py              ← Markdown → PostgreSQL-ready CSV converter
│       ├── gen_seed_sql.py           ← Regenerates seed-load-order.sql from CSV headers
│       ├── validate_data.py           ← FK/PK/NOT NULL validation on dump files
│       ├── runbook.md                 ← Step-by-step ETL execution guide
│       └── manifest.md               ← Per-module parser inventory with I/O specs
│
├── data/
│   └── csv/                           ← 127 PostgreSQL-ready CSV files (~221K rows)
│       ├── continents.csv
│       ├── countries.csv
│       ├── states.csv
│       └── ... (124 more files)       ← One per schema table
│
└── .github/
    ├── copilot-instructions.md        ← VS Code Copilot workspace instructions
    ├── agents/                        ← Custom Copilot agents
    └── prompts/                       ← Reusable prompt templates
```

> **Note**: Game files are NOT in this repo. The extraction script reads from your HOI4 installation via `--hoi4-root`, `HOI4_ROOT` env var, or auto-detection of default Steam paths.

---

## File-by-File Reference

### Design Documents (read in this order)

| # | File | Purpose | Lines | Key Content |
|---|---|---|---|---|
| 1 | [hoi4-database-design.md](hoi4-database-design.md) | **Master design doc** — read first | ~420 | Executive summary, 23-phase breakdown, 127-table FK build order (123 steps), normalization notes, API access strategy, DLC field register, index recommendations |
| 2 | [hoi4-er-diagram.mmd](hoi4-er-diagram.mmd) | **ER diagram** in Mermaid format | ~1,050 | 127 entity blocks with typed columns (PK/FK annotated), 133 relationship lines. Render with any Mermaid viewer. |
| 3 | [hoi4-table-catalog.md](hoi4-table-catalog.md) | **Column specifications** for every table | ~1,940 | For each table: purpose, source files, grain, PK, FKs, full column table (name, type, required, source field, notes), row estimate, relationship notes |
| 4 | [hoi4-source-to-table-map.md](hoi4-source-to-table-map.md) | **Source → table mapping** | ~125 | Maps every game file pattern to target tables with transformation rules and DLC handling notes |
| 5 | [hoi4-data-snapshots.md](hoi4-data-snapshots.md) | **Sample data** per table | ~360 | Real extracted rows to validate mapping accuracy |

### SQL Files

| File | Status | Content |
|---|---|---|
| [schema.sql](../sql/schema.sql) | **Complete** — all 127 tables | Full DDL for all 23 phases: countries, technologies, states, provinces, characters, OOB, ideas, focuses, DLC systems, doctrines, and all junction tables |
| [views.sql](../sql/views.sql) | **Complete** — 14 views across 3 slices | API views for country, state, technology, character, focus, OOB, and DLC access |
| [seed-load-order.sql](../sql/seed-load-order.sql) | **Complete** — all 127 tables | FK-safe load order across 7 tiers with explicit column lists and staging tables for FK resolution |

### ETL Tools

| File | Status | Content |
|---|---|---|
| [export_markdown_dump.py](../tools/db_etl/export_markdown_dump.py) | **Complete** | Python script that parses game files and outputs 137 markdown data-dump files (~221K rows) covering all 23 phases including DLC and doctrines |
| [md_to_csv.py](../tools/db_etl/md_to_csv.py) | **Complete** | Converts markdown dumps → 127 PostgreSQL-ready CSVs (~221K rows) with column renames, merges, splits |
| [gen_seed_sql.py](../tools/db_etl/gen_seed_sql.py) | **Complete** | Reads CSV headers and regenerates `seed-load-order.sql` with explicit column lists and FK staging |
| [validate_data.py](../tools/db_etl/validate_data.py) | **Complete** | FK, PK, NOT NULL validation on dump files — 0 errors, 0 warnings |
| [runbook.md](../tools/db_etl/runbook.md) | **Complete** | Step-by-step guide for the full extraction → CSV → PostgreSQL pipeline |
| [manifest.md](../tools/db_etl/manifest.md) | **Complete** | Inventory of 24 parser modules with input/output specs |

### Other Documents

| File | Purpose |
|---|---|
| [data-dump/SUMMARY.md](data-dump/SUMMARY.md) | Index of all 137 data-dump files with row counts (~221K total rows) |

---

## Schema Overview

**127 tables across 23 phases:**

| Phase | Domain | Tables | DLC |
|---|---|---|---|
| 1 | Global References (terrain, resources, buildings, ideologies, tech categories, equipment) | 12 | — |
| 2 | Geography (provinces, strategic regions, supply nodes, adjacencies, railways) | 10 | — |
| 3 | Countries (tags, history, starting techs/ideas, visuals) | 8 | — |
| 4 | Technologies (categories, prerequisites, unlocks) | 4 | — |
| 5 | Characters (leaders, generals, advisors, traits) | 4 | — |
| 6 | Land OOB (division templates, regiments, support, deployed divisions) | 4 | — |
| 7 | Naval OOB (fleets, task forces, ships, equipment variants) | 4 | — |
| 8 | Air OOB (air wings) | 1 | — |
| 9 | Ideas & National Spirits (ideas, modifiers) | 2 | — |
| 10 | Focus Trees (trees, focuses, prerequisites, mutual exclusions) | 4 | — |
| 11 | Governance (autonomy states, occupation laws + modifiers) | 4 | — |
| 12–15 | Extensions (intel agencies, bookmarks, decisions) | 9 | — |
| 16 | **Espionage** (operations, phases, tokens, intel agency upgrades) | 14 | La Résistance |
| 17 | **Occupation & Resistance** (compliance/resistance modifiers, activities) | 5 | La Résistance |
| 18 | **Military-Industrial Organizations** (templates, orgs, traits, policies) | 12 | Arms Against Tyranny |
| 19 | **Raids** (categories, raids, equipment requirements) | 3 | Götterdämmerung |
| 20 | **Career Profile** (medals, ribbons, ace modifiers, unit medals) | 8 | By Blood Alone |
| 21 | **Balance of Power & Continuous Focuses** | 7 | Various |
| 22 | **Misc DLC** (tech sharing, dynamic modifiers, scientist traits, peace conference) | 7 | Various |
| 23 | **Doctrines** (Officer Corps: folders, tracks, grand doctrines, subdoctrines) | 6 | Götterdämmerung |

---

## How to Read the ER Diagram

The file [hoi4-er-diagram.mmd](hoi4-er-diagram.mmd) is a **Mermaid erDiagram**. To render it:

1. **VS Code**: Install the "Markdown Preview Mermaid Support" extension, then open the file in preview
2. **GitHub**: Paste contents into any `.md` file — GitHub renders Mermaid natively
3. **Online**: Copy-paste into [mermaid.live](https://mermaid.live)
4. **CLI**: Use `mmdc` (Mermaid CLI) to export as SVG/PNG:
   ```bash
   npx -p @mermaid-js/mermaid-cli mmdc -i docs/hoi4-er-diagram.mmd -o docs/hoi4-er-diagram.svg
   ```

> **Note**: With 127 entities, the full diagram is very large. For focused viewing, copy just the phases you care about.

---

## What's Done vs. What's Left

### DONE (Design Phase)
- [x] 127-table schema designed across 23 phases with full column specs
- [x] ER diagram with all entities and relationships
- [x] Source-to-table mapping for every game file
- [x] FK dependency build order (123 steps)
- [x] API view designs for primary access patterns
- [x] DLC field register (38 entries)

### DONE (Implementation Phase)
- [x] **SQL DDL for all 127 tables** — `sql/schema.sql` covers all 23 phases (127 CREATE TABLE, 4 ALTER TABLE, 50 CREATE INDEX)
- [x] **Data extraction for all 23 phases** — 137 data-dump files with ~221K extracted rows, including all DLC systems and doctrines
- [x] **Markdown → CSV conversion** — `md_to_csv.py` produces 127 PostgreSQL-ready CSVs (~221K rows) with column renames, merges, and splits
- [x] **Seed-load-order** — `sql/seed-load-order.sql` is live (uncommented `\copy` commands) for all 127 tables in 7 FK-safe tiers, wrapped in a transaction
- [x] **Views** — `sql/views.sql` has 14 API views across 3 slices
- [x] **Data validation** — `tools/db_etl/validate_data.py` runs FK, PK, NOT NULL checks — 0 errors, 0 warnings
- [x] **Source-to-table map** — All 23 phases mapped including DLC paths

### NOT YET DONE
- [ ] **Stand up PostgreSQL and load** — Run the pipeline end-to-end (`schema.sql` → `seed-load-order.sql` → `views.sql`). See [runbook.md](../tools/db_etl/runbook.md) for steps.
- [ ] **API implementation** — REST API endpoints (`/countries/{tag}`, `/states/{id}`, etc.) are designed but not built.

---

## Quick Reference: Key Decisions

| Decision | Rationale |
|---|---|
| **Natural keys** for game entities (e.g., `tag CHAR(3)`, `technology_key VARCHAR`) | Avoids surrogate-to-natural joins for API lookups |
| **Surrogate keys** (SERIAL) for junction/instance tables | Game data lacks stable unique IDs for these |
| **`dlc_source VARCHAR(50)` nullable** on DLC-conditional rows | NULL = base game, populated = DLC name |
| **Separate tables** for DLC-only systems (not columns on existing tables) | Operations, MIOs, raids, medals are distinct domains — not extensions of existing entities |
| **3NF minimum** everywhere | Every non-key column depends on the whole key and nothing but the key |
| **Effective dates** on history tables | Supports both 1936 and 1939 bookmarks |

---

## How 1936 / 1939 Start Dates Work

HOI4 offers two selectable start dates. Three game-data mechanisms combine to produce distinct starting states, and the database mirrors all three.

### 1. Bookmarks (`common/bookmarks/`)

Each bookmark defines a selectable scenario on the main menu:

| Bookmark | File | `date` field |
|---|---|---|
| The Gathering Storm (1936) | `common/bookmarks/the_gathering_storm.txt` | `1936.1.1.12` |
| Blitzkrieg (1939) | `common/bookmarks/blitzkrieg.txt` | `1939.8.14.12` |

The bookmark also lists which countries are highlighted and their per-scenario descriptions. In the database these live in the `bookmarks` and `bookmark_countries` tables.

### 2. Date-prefixed history blocks

Files in `history/countries/` and `history/states/` contain **date-keyed blocks**. The game engine loads the base (undated) state, then replays every block whose date is `<=` the chosen start date in chronological order.

**Country example** — `history/countries/USA - USA.txt`:
```
1939.1.1 = {
    add_political_power = 1199
    add_ideas = { USA_robert_taft  isolation  volunteer_only  great_depression_3 }
}
```
This block only takes effect when the start date is 1939 or later.

**State example** — `history/states/9-Czechoslovakia.txt`:
```
1939.3.14 = {
    owner = GER
    controller = GER
}
```
Czechoslovakia belongs to itself in 1936 but transfers to Germany for the 1939 start.

In the database, every history row carries a `date DATE` column. Querying the 1936 snapshot means `WHERE date <= '1936-01-01'`; the 1939 snapshot means `WHERE date <= '1939-08-14'`. The API views accept a bookmark date parameter to resolve the correct state.

### 3. Separate OOB files (`history/units/`)

Military deployments are stored in per-country, per-year files:

| File | Content |
|---|---|
| `GER_1936.txt` | Smaller pre-war Wehrmacht |
| `GER_1939.txt` | Fully mobilised wartime forces |

Country history files select the correct OOB via `set_oob`:
```
set_oob = "GER_1936"      # base
1939.1.1 = { set_oob = "GER_1939" }
```

DLC variants add further branching (e.g. `GER_1936_nsb` when No Step Back is active). In the database, `oob_assignments` records each `(tag, date, oob_file, dlc_source)` tuple.

### Summary for API consumers

To fetch a country's full starting state for a given scenario:
1. Look up the bookmark's `date` in `bookmarks`
2. Query history tables with `WHERE date <= :bookmark_date`
3. For each country, take the **latest row per field** (most recent date wins)

The views `api_country_detail` and `api_state_detail` already encode this logic for the default 1936 bookmark.

---

## How to Run the Full Pipeline

The complete workflow is: **extract markdown → convert to CSV → create database → load data → create views**.

For detailed step-by-step instructions see [tools/db_etl/runbook.md](../tools/db_etl/runbook.md).

### Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.10+ |
| PostgreSQL | 15+ (with `psql` and `createdb` on PATH) |
| HOI4 installation | Default Steam path, or specify via `--hoi4-root` / `HOI4_ROOT` env var |

### Quick Start (5 commands)

```bash
# 1. Extract game data → markdown dumps
python tools/db_etl/export_markdown_dump.py

# 2. Convert markdown → PostgreSQL-ready CSVs
python tools/db_etl/md_to_csv.py

# 3. Create the database and all 127 tables
createdb hoi4
psql -d hoi4 -f sql/schema.sql

# 4. Load all data (run from repo root so csv paths resolve)
psql -d hoi4 -f sql/seed-load-order.sql

# 5. Create API views
psql -d hoi4 -f sql/views.sql
```

### Verify

```bash
# Table count (expect 127)
psql -d hoi4 -c "SELECT count(*) FROM information_schema.tables WHERE table_schema='public';"

# Spot-check row counts
psql -d hoi4 -c "SELECT count(*) FROM countries;"       -- 352
psql -d hoi4 -c "SELECT count(*) FROM states;"          -- 1,046
psql -d hoi4 -c "SELECT count(*) FROM technologies;"    -- 569
psql -d hoi4 -c "SELECT count(*) FROM characters;"      -- 5,160
```

### Full Reload (after game patch or re-extraction)

```bash
python tools/db_etl/export_markdown_dump.py   # re-extract
python tools/db_etl/md_to_csv.py              # re-convert
python tools/db_etl/gen_seed_sql.py            # regenerate load SQL
dropdb hoi4 && createdb hoi4                   # fresh database
psql -d hoi4 -f sql/schema.sql                 # recreate schema
psql -d hoi4 -f sql/seed-load-order.sql        # reload data
psql -d hoi4 -f sql/views.sql                  # recreate views
```

### Next Steps

- **Build the REST API**: Generate a FastAPI application using the views in `sql/views.sql` with endpoints for `/countries/{tag}`, `/states/{id}`, etc.
