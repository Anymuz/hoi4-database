# HOI4 Database

A fully normalised **PostgreSQL 16** database representing all Hearts of Iron IV starting-state game data — every country, state, technology, focus tree, OOB division, naval fleet, air wing, character, idea, and DLC system — loaded and ready to query.

**127 tables · ~218K rows · 14 API views · all 37 DLCs covered**

---

## Quick Start

```bash
git clone <repo-url> && cd hoi4-database

# 1  Extract game data → markdown
python tools/db_etl/export_markdown_dump.py        # auto-detects HOI4 install

# 2  Convert markdown → CSV
python tools/db_etl/md_to_csv.py

# 3a Deploy with Docker (recommended)
python tools/db_etl/gen_seed_sql.py
python tools/db_etl/gen_seed_docker.py
docker run -d --name hoi4-db -e POSTGRES_USER=hoi4 -e POSTGRES_PASSWORD=hoi4pass \
  -e POSTGRES_DB=hoi4 -p 5432:5432 -v hoi4_pgdata:/var/lib/postgresql/data postgres:16-alpine
docker cp sql/schema.sql    hoi4-db:/tmp/schema.sql
docker cp data/csv           hoi4-db:/data_csv
docker cp sql/seed-docker.sql hoi4-db:/tmp/seed.sql
docker cp sql/views.sql      hoi4-db:/tmp/views.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/schema.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/seed.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/views.sql

# 3b Or deploy without Docker (native PostgreSQL)
createdb hoi4
psql -d hoi4 -f sql/schema.sql
psql -d hoi4 -f sql/seed-load-order.sql   # run from repo root
psql -d hoi4 -f sql/views.sql
```

See [tools/db_etl/runbook.md](tools/db_etl/runbook.md) for full deployment instructions, prerequisites, verification steps, and troubleshooting.

---

## HOI4 Installation Path

The extraction script reads game files from your HOI4 installation. It resolves the path in this order:

1. `--hoi4-root <path>` CLI argument (highest priority)
2. `HOI4_ROOT` environment variable
3. Auto-detection from default Steam paths:
   - **Windows:** `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
   - **Linux:** `~/.steam/steam/steamapps/common/Hearts of Iron IV`

---

## Repository Structure

```
hoi4-database/
├── docs/                              Design & reference documentation
│   ├── hoi4-database-design.md        Master design doc (23 phases, FK build order, DLC strategy)
│   ├── hoi4-er-diagram.mmd            Mermaid ER diagram (127 entities, 133 relationships)
│   ├── hoi4-table-catalog.md          Column-level specs for every table (~1,900 lines)
│   ├── hoi4-source-to-table-map.md    Game file → target table mapping
│   ├── hoi4-data-snapshots.md         Sample extracted rows per table
│   ├── api-design.md                  API design (FastAPI + Strawberry GraphQL)
│   └── data-dump/                     137 extracted markdown data files
│       └── SUMMARY.md                 Index with row counts
├── data/
│   └── csv/                           127 PostgreSQL-ready CSV files (generated, gitignored)
├── sql/
│   ├── schema.sql                     DDL — 127 tables, 4 ALTER TABLE, 50 indexes
│   ├── views.sql                      14 API views (3 slices)
│   ├── seed-load-order.sql            FK-safe \copy load (native psql)
│   ├── seed-docker.sql                FK-safe COPY load (Docker container)
│   └── README.md                      SQL design rationale
├── tools/
│   └── db_etl/
│       ├── export_markdown_dump.py    Game file parser → markdown dumps
│       ├── md_to_csv.py               Markdown → CSV converter
│       ├── gen_seed_sql.py            Generates seed-load-order.sql
│       ├── gen_seed_docker.py         Generates seed-docker.sql
│       ├── validate_data.py           FK/PK/NOT NULL validation
│       ├── runbook.md                 Deployment & ETL guide (start here)
│       └── manifest.md               Parser module inventory
└── .github/
    ├── copilot-instructions.md        VS Code Copilot workspace instructions
    ├── agents/                        Custom Copilot agents
    └── prompts/                       Reusable prompt templates
```

---

## Schema Summary

**127 tables** across **23 design phases**:

| Phases | Domain | Tables | DLC |
|--------|--------|--------|-----|
| 1 | Global refs (terrain, resources, buildings, ideologies, equipment) | 12 | — |
| 2 | Geography (provinces, strategic regions, supply nodes, adjacencies) | 10 | — |
| 3 | Countries (tags, history, starting techs/ideas, visuals) | 8 | — |
| 4 | Technologies (categories, prerequisites, unlocks) | 4 | — |
| 5 | Characters (leaders, generals, advisors, traits) | 4 | — |
| 6–8 | Military OOB (land divisions, naval fleets, air wings) | 9 | — |
| 9–10 | Ideas, national spirits, focus trees | 6 | — |
| 11–15 | Governance, intel agencies, bookmarks, decisions | 13 | — |
| 16–17 | Espionage & resistance | 19 | La Résistance |
| 18 | Military-industrial organisations | 12 | Arms Against Tyranny |
| 19 | Raids | 3 | Götterdämmerung |
| 20 | Career profile (medals, ribbons, aces) | 8 | By Blood Alone |
| 21–22 | Balance of power, continuous focuses, misc DLC | 13 | Various |
| 23 | Doctrines (Officer Corps) | 6 | Götterdämmerung |

All DLC-conditional rows have a nullable `dlc_source VARCHAR(50)` column (NULL = base game).

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Natural keys** for game entities (`tag CHAR(3)`, `technology_key VARCHAR`) | API lookups by game ID, no surrogate join needed |
| **Surrogate keys** (SERIAL) for junction/instance tables | Game data lacks stable unique IDs for these |
| **3NF minimum** throughout | Every non-key column depends on the whole key and nothing but the key |
| **Effective dates** on history tables | Supports both 1936 and 1939 bookmarks |
| **Separate tables** for DLC systems | Operations, MIOs, raids, medals are distinct domains |
| **Self-referencing FKs** as `DEFERRABLE INITIALLY DEFERRED` | Equipment inheritance chain loads correctly in a single transaction |

---

## How 1936 / 1939 Start Dates Work

HOI4 offers two start dates. Three mechanisms create distinct starting states:

1. **Bookmarks** (`common/bookmarks/`) — define selectable dates (1936.1.1, 1939.8.14)
2. **Date-prefixed history blocks** — game engine replays `date = { … }` blocks where `date ≤ start_date`
3. **Separate OOB files** — `GER_1936.txt` vs `GER_1939.txt`, selected via `set_oob`

History tables use `effective_date DATE` columns. Query with `WHERE effective_date <= :bookmark_date`.

---

## How to Read the ER Diagram

The file [docs/hoi4-er-diagram.mmd](docs/hoi4-er-diagram.mmd) is a **Mermaid erDiagram** with 127 entities and 133 relationships. To render it:

- **VS Code**: Install "Markdown Preview Mermaid Support", open in preview
- **GitHub**: Paste into any `.md` file — GitHub renders Mermaid natively
- **Online**: Copy into [mermaid.live](https://mermaid.live)
- **CLI**: `npx -p @mermaid-js/mermaid-cli mmdc -i docs/hoi4-er-diagram.mmd -o docs/hoi4-er-diagram.svg`

> With 127 entities the full diagram is large. For focused viewing, copy only the phases you need.

---

## Documentation Index

| Document | Purpose |
|----------|---------|
| [tools/db_etl/runbook.md](tools/db_etl/runbook.md) | **Deployment guide** — Docker + native PostgreSQL setup, full ETL pipeline, verification, troubleshooting |
| [docs/hoi4-database-design.md](docs/hoi4-database-design.md) | Schema design — 23 phases, FK build order, normalization, API strategy, DLC register |
| [docs/hoi4-table-catalog.md](docs/hoi4-table-catalog.md) | Column specs for every table |
| [docs/hoi4-er-diagram.mmd](docs/hoi4-er-diagram.mmd) | ER diagram (Mermaid) |
| [docs/hoi4-source-to-table-map.md](docs/hoi4-source-to-table-map.md) | Game file → table mapping |
| [docs/hoi4-data-snapshots.md](docs/hoi4-data-snapshots.md) | Sample rows per table (design-phase reference) |
| [docs/api-design.md](docs/api-design.md) | API design (FastAPI + Strawberry GraphQL) |
| [sql/README.md](sql/README.md) | SQL design rationale (indexes, views, staging) |
| [tools/db_etl/manifest.md](tools/db_etl/manifest.md) | Parser module inventory |

---

## Project Status

### Complete

- **Schema**: 127 tables, 4 ALTER TABLE, 50 indexes — all FK constraints enforced
- **Data extraction**: 137 markdown dumps covering all 23 phases including DLC
- **ETL pipeline**: markdown → CSV → PostgreSQL with 0 errors
- **Database loaded**: 127 tables, ~218K rows, 14 API views
- **Validation**: FK, PK, NOT NULL checks — 0 errors, 0 warnings

### Not Yet Done

- REST API implementation (FastAPI + Strawberry GraphQL — see [docs/api-design.md](docs/api-design.md))

---

## License

This project documents game data structures from Hearts of Iron IV by Paradox Interactive. The database schema, extraction tools, and documentation are original work. Game data belongs to Paradox Interactive.
