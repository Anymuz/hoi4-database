# HOI4 Database

A fully normalised **PostgreSQL database schema** representing all Hearts of Iron IV starting-state game data — every country, state, technology, focus tree, OOB division, naval fleet, air wing, character, idea, and DLC system — ready to back a REST API.

## Quick Start

```bash
# Clone
git clone <repo-url> && cd hoi4-database

# 1. Extract game data → markdown dumps
python tools/db_etl/export_markdown_dump.py          # auto-detects HOI4 install
# Or: python tools/db_etl/export_markdown_dump.py --hoi4-root "/path/to/Hearts of Iron IV"

# 2. Convert markdown → PostgreSQL-ready CSVs
python tools/db_etl/md_to_csv.py

# 3. Create database, load data, create views
createdb hoi4
psql -d hoi4 -f sql/schema.sql
psql -d hoi4 -f sql/seed-load-order.sql
psql -d hoi4 -f sql/views.sql
```

See [tools/db_etl/runbook.md](tools/db_etl/runbook.md) for detailed instructions, prerequisites, and troubleshooting.

## HOI4 Installation Path

The extraction script needs to read game files from your HOI4 installation. It resolves the path in this order:

1. `--hoi4-root <path>` CLI argument (highest priority)
2. `HOI4_ROOT` environment variable
3. Auto-detection from default Steam paths:
   - Windows: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`
   - Linux: `~/.steam/steam/steamapps/common/Hearts of Iron IV`

## Repository Structure

```
hoi4-database/
├── docs/                              Design documentation
│   ├── PROJECT-GUIDE.md               Master guide — start here
│   ├── hoi4-database-design.md        Design doc (23 phases, 127 tables)
│   ├── hoi4-er-diagram.mmd            Mermaid ER diagram (127 entities, 133 relationships)
│   ├── hoi4-table-catalog.md          Column-level specs for every table
│   ├── hoi4-source-to-table-map.md    Game file → target table mapping
│   ├── hoi4-data-snapshots.md         Sample extracted rows
│   └── data-dump/                     137 extracted markdown data files
│       └── SUMMARY.md                 Index with row counts (~221K rows)
├── data/
│   └── csv/                           127 PostgreSQL-ready CSV files (~221K rows)
├── sql/
│   ├── schema.sql                     DDL (all 127 tables, 50 indexes)
│   ├── views.sql                      14 API views (3 slices)
│   └── seed-load-order.sql            FK-safe \copy load (127 tables, 7 tiers)
├── tools/
│   └── db_etl/
│       ├── export_markdown_dump.py    Extraction script (configurable HOI4 path)
│       ├── md_to_csv.py              Markdown → CSV converter
│       ├── gen_seed_sql.py           Regenerates seed-load-order.sql from CSV headers
│       ├── validate_data.py           FK/PK/NOT NULL validation
│       ├── runbook.md                 ETL execution guide
│       └── manifest.md               Parser module inventory
└── .github/
    ├── copilot-instructions.md        VS Code Copilot workspace instructions
    ├── agents/                        Custom Copilot agents
    └── prompts/                       Reusable prompt templates
```

## Schema Summary

**127 tables** across **23 design phases**, covering:

| Phases | Domain | Tables |
|--------|--------|--------|
| 1–3 | Geography, countries, references | 30 |
| 4–5 | Technologies, characters | 8 |
| 6–8 | Land/naval/air OOB | 9 |
| 9–10 | Ideas, focus trees | 6 |
| 11–15 | Governance, intel, bookmarks, decisions | 13 |
| 16–17 | Espionage & resistance (La Résistance) | 19 |
| 18 | Military-industrial orgs (Arms Against Tyranny) | 12 |
| 19 | Raids (Götterdämmerung) | 3 |
| 20 | Career profile (By Blood Alone) | 8 |
| 21–22 | Balance of power, continuous focus, misc DLC | 13 |
| 23 | Doctrines (Officer Corps) | 6 |

All DLC-conditional data is flagged with a `dlc_source` column.

## Key Design Decisions

- **Natural keys** for game entities (`tag CHAR(3)`, `technology_key VARCHAR`)
- **Surrogate keys** (SERIAL) for junction/instance tables
- **3NF minimum** throughout
- **Effective dates** on history tables — supports both 1936 and 1939 bookmark starts
- **Separate tables** for DLC-only systems (operations, MIOs, raids, medals)

## Project Status

### Complete
- 127-table schema with full column specs and ER diagram
- SQL DDL, 14 API views, FK-safe seed-load-order
- 137 data-dump files (~221K extracted rows) covering all 23 phases including DLC
- 127 PostgreSQL-ready CSVs (~221K rows)
- Data validation (FK, PK, NOT NULL) — 0 errors, 0 warnings

### Not Yet Done
- Stand up PostgreSQL and load (pipeline is ready — see runbook)
- REST API implementation (FastAPI planned)

## Documentation

Start with [docs/PROJECT-GUIDE.md](docs/PROJECT-GUIDE.md) for a full walkthrough of every file, schema phases, how 1936/1939 starts work, and the complete pipeline.

## License

This project documents game data structures from Hearts of Iron IV by Paradox Interactive. The database schema, extraction tools, and documentation are original work. Game data belongs to Paradox Interactive.
