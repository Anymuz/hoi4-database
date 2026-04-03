# HOI4 Database — Workspace Instructions

## About This Repository

This is a **standalone database design repository** — it does NOT contain HOI4 game files. The game files live in a separate HOI4 installation directory. The extraction script (`tools/db_etl/export_markdown_dump.py`) reads from the game install and writes to `docs/data-dump/` in this repo.

To point at the game install, use `--hoi4-root <path>`, the `HOI4_ROOT` env var, or rely on auto-detection of default Steam paths.

---

## Current Project Status (as of April 2026)

### COMPLETED — Design Phase
- **129-table schema** designed across **23 phases** (66 core + 61 DLC + 2 infrastructure)
- **ER diagram**: `docs/hoi4-er-diagram.mmd` — 127 entities, 133 relationships (Mermaid format)
- **Table catalog**: `docs/hoi4-table-catalog.md` — ~2,100 lines, full column specs for every table
- **Design document**: `docs/hoi4-database-design.md` — ~430 lines, phases, FK build order (125 steps), DLC register (38 entries)
- **Source mapping**: `docs/hoi4-source-to-table-map.md` — all 23 phases + localisation mapped including DLC paths

### COMPLETED — Implementation
- **SQL DDL**: `sql/schema.sql` has **all 129 tables** (129 CREATE TABLE, 4 ALTER TABLE, 50 CREATE INDEX) with all FK constraints enforced
- **Data extraction**: 137 markdown data-dump files in `docs/data-dump/` covering all 23 phases including DLC and doctrines
- **Localisation**: 117,490 English display names extracted from 189 `*_l_english.yml` files via `tools/db_etl/export_localisation.py`
- **Markdown → CSV conversion**: `tools/db_etl/md_to_csv.py` produces 127 PostgreSQL-ready CSVs in `data/csv/` (~218K game rows)
- **API views**: `sql/views.sql` has 12 API views + 2 date-parameterised functions (LEFT JOIN localisation for human-readable names)
- **Seed loading**: `sql/seed-load-order.sql` (native) and `sql/seed-docker.sql` (Docker) load all 127 game tables in 7 FK-safe tiers
- **Database loaded**: PostgreSQL 16 with 129 tables, ~335K rows (218K game + 117K localisation), 0 errors
- **Data validation**: `tools/db_etl/validate_data.py` runs FK, PK, NOT NULL checks — 0 errors, 0 warnings

### NOT YET DONE
- REST API implementation in progress (FastAPI + Strawberry GraphQL — see `docs/api-design.md`)
  - Phase 0 (SQL fixes): **DONE**
  - Phase 1 (scaffold + infrastructure): **DONE**
  - Phase 2 (countries + states routers): **DONE**
  - Localisation (cross-cutting): **DONE** — 117K English names, LEFT JOIN in SQL functions, name fields in schemas
  - Phase 3+ (remaining routers, GraphQL, polish): NOT STARTED

---

## Schema Architecture

### Phase Breakdown (23 phases, 129 tables)

| Phases | Domain | Tables | DLC |
|--------|--------|--------|-----|
| 1 | Global refs (terrain, resources, buildings, ideologies, tech categories, equipment) | 12 | — |
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
| 16 | Espionage (operations, phases, tokens, intel agency upgrades) | 14 | La Résistance |
| 17 | Occupation & Resistance (compliance/resistance modifiers, activities) | 5 | La Résistance |
| 18 | Military-Industrial Organizations (templates, orgs, traits, policies) | 12 | Arms Against Tyranny |
| 19 | Raids (categories, raids, equipment requirements) | 3 | Götterdämmerung |
| 20 | Career Profile (medals, ribbons, ace modifiers, unit medals) | 8 | By Blood Alone |
| 21 | Balance of Power & Continuous Focuses | 7 | Various |
| 22 | Misc DLC (tech sharing, dynamic modifiers, scientist traits, peace conference) | 7 | Various |
| 23 | Doctrines (Officer Corps: folders, tracks, grand doctrines, subdoctrines) | 6 | Götterdämmerung |
| — | Infrastructure (user_annotations, localisation) | 2 | — |

### Key Design Decisions
- **Natural keys** for game entities (`tag CHAR(3)`, `technology_key VARCHAR`)
- **Surrogate keys** (SERIAL) for junction/instance tables
- **3NF minimum** throughout
- **Effective dates** on history tables — supports 1936 and 1939 bookmarks
- **`dlc_source VARCHAR(50)` nullable** — NULL = base game, populated = DLC name
- **Separate tables** for DLC-only systems (not columns on base tables)

### How 1936 / 1939 Starts Work
Three mechanisms create distinct starting states:
1. **Bookmarks** (`common/bookmarks/`) — define selectable start dates (1936.1.1.12, 1939.8.14.12)
2. **Date-prefixed history blocks** — game engine replays `date = { ... }` blocks where `date <= start_date`
3. **Separate OOB files** — `GER_1936.txt` vs `GER_1939.txt`, selected via `set_oob` in country history

History tables use `date DATE` columns. Query with `WHERE date <= :bookmark_date`.

---

## Paradox Script Syntax

Game data files (`.txt` under `common/`, `history/`, `events/`, etc. **inside the HOI4 install**) use **Paradox Script**, not JSON, YAML, or TOML. Key rules:

- **Assignment uses `=`, not `:`.** `capital = 64`, not `capital: 64`.
- **Blocks are `{ }`, not indented.** `set_technology = { infantry_weapons = 1 }`.
- **Strings are unquoted** unless they contain spaces: `tag = GER`, `name = "Units of Germany"`.
- **Comments start with `#`.**
- **Numbers are plain integers or decimals:** `stability = 0.7`, `manpower = 6454865`.
- **Booleans are `yes` / `no`**, not `true` / `false`.
- **Conditional blocks** use `if = { limit = { <trigger> } <effect> }`.
- **DLC guards** appear as `limit = { has_dlc = "DLC Name" }`.
- **Date-prefixed history blocks** look like `1936.1.1 = { ... }`.

---

## HOI4 Game File Reference (inside the game install)

| Purpose | Path (relative to HOI4 root) |
|---|---|
| Country visual definitions | `common/countries/` |
| Country tags | `common/country_tags/` |
| Country starting history | `history/countries/` |
| State geometry & history | `history/states/` |
| Resource definitions | `common/resources/` |
| Building definitions | `common/buildings/` |
| Technology trees | `common/technologies/` |
| National focus trees | `common/national_focus/` |
| Ideas & national spirits | `common/ideas/` |
| Ideologies & parties | `common/ideologies/` |
| Characters (leaders, generals) | `common/characters/` |
| Division/naval/air OOB | `history/units/` |
| Equipment definitions | `common/units/equipment/` |
| Sub-unit types | `common/units/` |
| Province map | `map/definition.csv` |
| Bookmarks | `common/bookmarks/` |
| Intelligence agencies | `common/intelligence_agencies/` |
| MIO templates | `common/military_industrial_organization/` |
| Operations (espionage) | `common/operations/` |
| Operations phases | `common/operation_phases/` |
| Raids | `common/raids/` |
| Medals & ribbons | `common/medals/`, `common/ribbons/` |
| Balance of power | `common/bop/` |
| Continuous focuses | `common/continuous_focus/` |
| Scientist traits | `common/scientist_traits/` |
| Peace conference | `common/peace_conference/` |
| Localisation (English) | `localisation/english/` |

## Repository Structure

| Purpose | Path (in this repo) |
|---|---|
| Design document | `docs/hoi4-database-design.md` |
| ER diagram (Mermaid) | `docs/hoi4-er-diagram.mmd` |
| Table catalog (column specs) | `docs/hoi4-table-catalog.md` |
| Source → table mapping | `docs/hoi4-source-to-table-map.md` |
| Sample data rows | `docs/hoi4-data-snapshots.md` |
| API design | `docs/api-design.md` |
| Extracted data dumps | `docs/data-dump/` (137 files + SUMMARY.md) |
| PostgreSQL-ready CSVs | `data/csv/` (127 game + 1 localisation files, gitignored) |
| SQL DDL / views / seed | `sql/` |
| SQL design rationale | `sql/README.md` |
| Extraction script | `tools/db_etl/export_markdown_dump.py` |
| Localisation extractor | `tools/db_etl/export_localisation.py` |
| MD → CSV converter | `tools/db_etl/md_to_csv.py` |

| Seed SQL generator (native) | `tools/db_etl/gen_seed_sql.py` |
| Seed SQL generator (Docker) | `tools/db_etl/gen_seed_docker.py` |
| Data validator | `tools/db_etl/validate_data.py` |
| Deployment & ETL guide | `tools/db_etl/runbook.md` |
| ETL module manifest | `tools/db_etl/manifest.md` |
| Copilot agent | `.github/agents/hoi4-db-architect.agent.md` |
| Prompt templates | `.github/prompts/` |

## DLC Coverage

37 DLCs total (33 paid in `dlc/` + 4 integrated in `integrated_dlc/` within the game install). Key DLC abbreviations used throughout schema docs:

| Abbreviation | Full Name | Primary Systems |
|---|---|---|
| LaR | La Résistance | Espionage operations, intelligence agencies, operatives, resistance/compliance |
| NSB | No Step Back | Alternate OOB files, tank designer |
| AAT | Arms Against Tyranny | Military-industrial organizations (MIOs) |
| BBA | By Blood Alone | Career profile medals, ace framework, air designer |
| MTG | Man the Guns | Ship designer, naval treaty, governments-in-exile |
| TFV | Together for Victory | Autonomy system, technology sharing |
| WTT | Waking the Tiger | Generals traits, decisions framework |
| DoD | Death or Dishonor | Equipment conversion |
| WUW | Götterdämmerung | Raids system, Officer Corps doctrines |
