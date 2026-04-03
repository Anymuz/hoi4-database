# HOI4 Database — API Implementation Plan

> **Date:** 2026-04-02
> **Branch:** `feature/api-v1`
> **Design doc:** `docs/api-design.md` (FINAL, 2026-03-31)
> **Database:** 129 tables, ~335K rows, 12 views + 2 functions, PostgreSQL 16

---

## Pre-Implementation Findings

Five issues identified during the design-vs-database audit:

| # | Finding | Impact | Resolution |
|---|---------|--------|------------|
| 1 | `user_annotations` table not in `schema.sql` | Annotations endpoints have no backing table | Add DDL from design §6.10 |
| 2 | 6 views hardcode `1936-01-01` — need date parameterisation | Only half the data accessible | Convert to PostgreSQL functions per design §5 |
| 3 | `api_country_technologies` exposes `effective_date` as column | Works fine — WHERE filter in router instead of function call | Simpler than design §5 assumed; document the deviation |
| 4 | `countries.country_file_path` now nullable (SPA fix) | No impact — column not in any view | No action needed |
| 5 | Runbook spot-check counts are stale (e.g. countries ~352 → 428) | Misleading verification | Update runbook numbers |

---

## Progress Tracker

### Phase 0: Pre-Flight — SQL & Docs Fixes
- [x] 0.1 — Add `user_annotations` table to schema
- [x] 0.2 — Convert date-sensitive views to PostgreSQL functions
- [x] 0.3 — Update runbook spot-check counts
- [x] 0.4 — Verify SQL changes

### Phase 1: Project Scaffold & Core Infrastructure
- [x] 1.1 — Create directory structure
- [x] 1.2 — `requirements.txt`
- [x] 1.3 — `config.py`
- [x] 1.4 — `database.py`
- [x] 1.5 — `dependencies.py`
- [x] 1.6 — `main.py`
- [x] 1.7 — `.env.example`
- [x] Test gate: health, openapi, date validation

### Phase 2: Slice A — Countries & States (Date-Sensitive)
- [x] 2.1 — Pydantic schemas (country, state)
- [x] 2.2 — Countries router
- [x] 2.3 — States router
- [x] 2.4 — Register routers in `main.py`
- [x] Test gate: list, detail, 404, pagination, date filtering

### Localisation (cross-cutting, completed after Phase 2)
- [x] Add `localisation` table to `sql/schema.sql` (loc_key PK, loc_value, source_file)
- [x] Write `tools/db_etl/export_localisation.py` extraction script
- [x] Extract 117,490 English loc entries from 189 `*_l_english.yml` files
- [x] Load into live database via `COPY ... CSV HEADER`
- [x] Update `api_country_detail` function — LEFT JOIN localisation for state_name + technology_name in jsonb
- [x] Update `api_state_detail` function — add state_name column via LEFT JOIN localisation
- [x] Update Pydantic schemas — add state_name/technology_name optional fields
- [x] Update states router — add state_name to SELECT queries

### Phase 3: Slice B — Domain Catalogs (8 routers)
- [ ] 3.1 — Technologies (schemas + router)
- [ ] 3.2 — Characters (schemas + router)
- [ ] 3.3 — Military — land / naval / air (schemas + router)
- [ ] 3.4 — Focus Trees (schemas + router)
- [ ] 3.5 — Equipment (schemas + router)
- [ ] 3.6 — Ideas (schemas + router)
- [ ] 3.7 — Register all Phase 3 routers
- [ ] Test gate: all 8 routers with filters and nested models

### Phase 4: Slice C — DLC Systems + Annotations (Read/Write)
- [ ] 4.1 — DLC router (MIOs, operations, BoP)
- [ ] 4.2 — Annotations router (CRUD)
- [ ] 4.3 — Register routers in `main.py`
- [ ] Test gate: DLC reads + annotation CRUD lifecycle

### Phase 5: GraphQL Layer
- [ ] 5.1 — Strawberry types
- [ ] 5.2 — Resolvers
- [ ] 5.3 — Schema & mount
- [ ] Test gate: all queries, field selection, date params

### Phase 6: Polish & Integration Testing
- [ ] 6.1 — CORS configuration
- [ ] 6.2 — API README
- [ ] 6.3 — Update repo-level docs
- [ ] Final test gate: full suite + manual smoke

---

## Phase 0: Pre-Flight — SQL & Docs Fixes

Fix the 5 audit findings before writing any API code. Everything in this phase is SQL/docs changes — no Python yet.

### Step 0.1 — Add `user_annotations` table to schema

**Design ref:** §6.10 (DDL block)

Add to `sql/schema.sql`:

```sql
CREATE TABLE user_annotations (
    annotation_id  SERIAL PRIMARY KEY,
    entity_type    VARCHAR(50)  NOT NULL,
    entity_key     VARCHAR(200) NOT NULL,
    note           TEXT         NOT NULL,
    created_at     TIMESTAMPTZ  NOT NULL DEFAULT now()
);
CREATE INDEX idx_annotations_entity
    ON user_annotations(entity_type, entity_key);
```

Apply to live DB: `ALTER TABLE` or full reload.

### Step 0.2 — Convert 2 date-sensitive views to PostgreSQL functions

**Design ref:** §5 (The Solution: PostgreSQL Functions)

Convert these 2 views to `FUNCTION ... RETURNS TABLE` with `p_date DATE DEFAULT '1936-01-01'`:
- `api_country_detail` — parameterise the `ownership_1936` and `tech_1936` CTEs
- `api_state_detail` — parameterise `ownership_1936`, `resources_1936`, `state_buildings_1936`, `province_buildings_1936`

The remaining 12 views stay as views:
- `api_country_technologies` already exposes `effective_date` as a column — the API router filters with `WHERE effective_date <= $date`
- `api_country_divisions`, `api_country_naval`, `api_country_air` are filtered by `oob_file` name in the API router (design §6.5)
- The other 8 views have no date sensitivity at all

**Net change:** 2 views become functions, 12 views unchanged.

Update `sql/views.sql` accordingly, replacing the `CREATE OR REPLACE VIEW` statements with `CREATE OR REPLACE FUNCTION` for the two converted views.

### Step 0.3 — Update runbook spot-check counts

**Audit finding #5**

Update `tools/db_etl/runbook.md` Step 4 expected counts:

| Table | Old estimate | Actual |
|---|---|---|
| countries | ~352 | ~428 |
| technologies | ~569 | ~574 |
| characters | ~5160 | ~5138 |
| focuses | ~8900 | ~9906 |

### Step 0.4 — Verify SQL changes

```bash
# Reload schema + views into Docker
docker exec hoi4-db psql -U hoi4 -d hoi4 -c \
  "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
docker cp sql/schema.sql hoi4-db:/tmp/schema.sql
docker cp sql/seed-docker.sql hoi4-db:/tmp/seed.sql
docker cp sql/views.sql hoi4-db:/tmp/views.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/schema.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/seed.sql
docker exec hoi4-db psql -U hoi4 -d hoi4 -f /tmp/views.sql

# Verify functions work with both dates
docker exec hoi4-db psql -U hoi4 -d hoi4 -c \
  "SELECT tag, stability FROM api_country_detail('1936-01-01') WHERE tag='GER';"
docker exec hoi4-db psql -U hoi4 -d hoi4 -c \
  "SELECT tag, stability FROM api_country_detail('1939-08-14') WHERE tag='GER';"
docker exec hoi4-db psql -U hoi4 -d hoi4 -c \
  "SELECT count(*) FROM user_annotations;"  -- expect 0
```

**Exit criteria:** 127 tables + 1 `user_annotations` + 1 `localisation` = 129 tables; 12 views + 2 functions; both date params work; 0 errors.

---

## Phase 1: Project Scaffold & Core Infrastructure

**Design ref:** §2 (Directory Layout), §3 (Configuration), §4 (Database Connection)

### Step 1.1 — Create directory structure

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   ├── routers/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   └── graphql/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_health.py
│   └── test_date_validation.py
├── requirements.txt
├── .env.example
└── README.md
```

### Step 1.2 — `requirements.txt`

```
fastapi>=0.115,<1
uvicorn[standard]>=0.30
asyncpg>=0.30
pydantic-settings>=2.0
strawberry-graphql[fastapi]>=0.250
httpx>=0.27                  # for test client
pytest>=8.0
pytest-asyncio>=0.24
```

### Step 1.3 — `config.py`

**Design ref:** §3 — implement `Settings` class and `get_settings()` exactly as specified.

### Step 1.4 — `database.py`

**Design ref:** §4 — implement `lifespan()` context manager and `get_db()` dependency exactly as specified.

### Step 1.5 — `dependencies.py`

**Design ref:** §5 (Date Parameter Validation Helper) — implement `get_effective_date()` with the `allowed_dates` whitelist.

### Step 1.6 — `main.py`

**Design ref:** §8 (OpenAPI Tags & Metadata) — create the FastAPI app with `tags_metadata`, lifespan, CORS middleware. Mount a `/health` endpoint. REST routers and GraphQL will be added in later phases.

### Step 1.7 — `.env.example`

```
DATABASE_URL=postgresql://hoi4:hoi4pass@localhost:5432/hoi4
```

### Test Gate: Phase 1

**Scope:** Infrastructure boots correctly, pool connects, health check responds.

```
tests/
├── conftest.py              # shared fixtures: test client, DB override
├── test_health.py           # GET /health, OpenAPI schema
└── test_date_validation.py  # ?date= parameter validation
```

**`conftest.py` approach:**
- Use `httpx.AsyncClient` + `httpx.ASGITransport` for async test client
- Create a real asyncpg pool against the Docker database (test against real data)
- Override `get_db` dependency to use the test pool

**Tests (`test_health.py`):**
| Test | Assertion |
|---|---|
| `test_health_200` | GET `/health` returns `{"status": "ok"}` |
| `test_openapi_schema` | GET `/openapi.json` returns 200 with expected title |

**Tests (`test_date_validation.py`):**
| Test | Assertion |
|---|---|
| `test_default_date` | `get_effective_date(None)` returns `1936-01-01` |
| `test_valid_date_1939` | `get_effective_date("1939-08-14")` returns `1939-08-14` |
| `test_invalid_date_400` | `get_effective_date("2000-01-01")` raises 400 |

**Run:** `pytest tests/ -v`

**Exit criteria:** All 5 tests pass; `uvicorn api.app.main:app --reload` starts without errors; `/docs` loads in browser.

---

## Phase 2: Slice A — Countries & States (Date-Sensitive)

**Design ref:** §6.2

This is the most complex slice — it exercises date parameterisation, jsonb nested models, pagination, and both list/detail patterns. Getting it right here sets the template for all remaining routers.

### Step 2.1 — Pydantic schemas

**Design ref:** §6.2 (The Pydantic schemas)

Create `api/app/schemas/country.py`:
- `ColorRGB` (r, g, b)
- `OwnedState` (state_id, state_name_key, state_name, controller_tag)
- `StartingTech` (technology_key, technology_name, dlc_source)
- `CountrySummary` (tag, capital_state_id, stability, war_support)
- `CountryDetail` (full — includes color_rgb, graphical_culture, owned_states, starting_technologies)

Create `api/app/schemas/state.py`:
- Nested models for resources, buildings, province_buildings, provinces
- `StateSummary` (state_id, state_name_key, state_name, state_category, owner_tag)
- `StateDetail` (full — includes manpower, local_supplies, nested arrays)

### Step 2.2 — Countries router

**Design ref:** §6.2 (countries endpoint code)

Create `api/app/routers/countries.py`:
- `GET /api/v1/countries` — calls `api_country_detail(p_date)` function, returns `list[CountrySummary]`
- `GET /api/v1/countries/{tag}` — calls same function with `WHERE tag = $2`, returns `CountryDetail` or 404

Both use `Depends(get_effective_date)` for date handling.

### Step 2.3 — States router

**Design ref:** §6.2 (states section)

Create `api/app/routers/states.py`:
- `GET /api/v1/states` — calls `api_state_detail(p_date)`, supports `?owner_tag=GER`
- `GET /api/v1/states/{state_id}` — single state or 404

### Step 2.4 — Register routers in `main.py`

```python
app.include_router(countries.router)
app.include_router(states.router)
```

### Test Gate: Phase 2

**Scope:** Date-sensitive endpoints work correctly with both bookmarks.

```
tests/
├── test_countries.py
└── test_states.py
```

**Tests:**
| Test | Assertion |
|---|---|
| `test_list_countries_default` | GET `/api/v1/countries` returns 200, list with 428 items (use limit=500) |
| `test_list_countries_pagination` | `?limit=10&offset=0` returns exactly 10 |
| `test_get_country_ger` | GET `/api/v1/countries/GER` returns 200, tag="GER", has owned_states and starting_technologies arrays |
| `test_get_country_spa` | GET `/api/v1/countries/SPA` returns 200 (event-spawned tag, nullable fields) |
| `test_get_country_404` | GET `/api/v1/countries/ZZZ` returns 404 |
| `test_country_date_1939` | GET `/api/v1/countries/GER?date=1939-08-14` returns different owned_states than 1936 |
| `test_country_invalid_date` | `?date=2000-01-01` returns 400 |
| `test_country_case_insensitive` | `/countries/ger` returns same as `/countries/GER` |
| `test_list_states_default` | Returns 200, list with states |
| `test_get_state_by_id` | GET `/api/v1/states/64` (Ile de France) returns correct owner |
| `test_states_filter_owner` | `?owner_tag=GER` returns only German-owned states |
| `test_state_404` | GET `/api/v1/states/99999` returns 404 |

**Run:** `pytest tests/test_countries.py tests/test_states.py -v`

**Exit criteria:** All tests pass. Swagger at `/docs` shows both endpoints with correct request/response models. Both `?date=` values produce valid but different results for date-sensitive data.

---

## Phase 3: Slice B — Domain Catalogs

**Design ref:** §6.3–§6.8

Eight routers covering non-date-sensitive views plus the 3 date-sensitive military endpoints. Each follows the established pattern from Phase 2.

### Step 3.1 — Technologies

**Design ref:** §6.3

Schemas (`schemas/technology.py`):
- `TechTreeItem` — technology_key, start_year, research_cost, folder_name, dlc_source, prerequisites[], categories[], enables_equipment[], enables_units[]
- `CountryTech` — country_tag, technology_key, start_year, research_cost, folder_name, dlc_source

Router (`routers/technologies.py`):
- `GET /api/v1/technologies` — from `api_technology_tree` view, supports `?folder=`
- `GET /api/v1/technologies/{key}` — single tech or 404
- `GET /api/v1/countries/{tag}/technologies` — from `api_country_technologies` view, date-sensitive via `WHERE effective_date <= $date`

### Step 3.2 — Characters

**Design ref:** §6.4

Schemas (`schemas/character.py`):
- `CharacterRole` — role_type, skills, traits[], dlc_source
- `CharacterDetail` — character_id, name_key, country_tag, gender, roles[]

Router (`routers/characters.py`):
- `GET /api/v1/countries/{tag}/characters` — from `api_country_characters`, not date-sensitive
- `GET /api/v1/characters/{character_id}` — single character or 404

### Step 3.3 — Military (Land / Naval / Air)

**Design ref:** §6.5

Schemas (`schemas/military.py`):
- `Regiment`, `SupportCompany`, `Deployed` — sub-models for jsonb arrays
- `DivisionDetail` — country_tag, template info, regiments[], support[], deployed_divisions[]
- `NavalDetail` — fleet info, nested task_forces[] with ships[]
- `AirWingItem` — country_tag, location, equipment_type, amount, oob_file

Router (`routers/military.py`):
- `GET /api/v1/countries/{tag}/divisions` — date-sensitive via `oob_file LIKE '%_{year}%'`
- `GET /api/v1/countries/{tag}/naval` — same OOB filtering
- `GET /api/v1/countries/{tag}/air` — same OOB filtering

### Step 3.4 — Focus Trees

**Design ref:** §6.6

Schemas (`schemas/focus.py`):
- `FocusItem` — focus_id, cost, position, icon, prerequisites[], mutually_exclusive[]
- `FocusTreeDetail` — focus_tree_id, country_tag, focuses[]

Router (`routers/focuses.py`):
- `GET /api/v1/focus-trees` — list all trees
- `GET /api/v1/focus-trees/{focus_tree_id}` — single tree
- `GET /api/v1/countries/{tag}/focus-tree` — tree for a country

### Step 3.5 — Equipment

**Design ref:** §6.7

Schemas (`schemas/equipment.py`):
- `EquipmentItem` — all stats columns + resources[]

Router (`routers/equipment.py`):
- `GET /api/v1/equipment` — supports `?archetype=`, `?is_archetype=`
- `GET /api/v1/equipment/{equipment_key}` — single item or 404

### Step 3.6 — Ideas

**Design ref:** §6.8

Schemas (`schemas/idea.py`):
- `IdeaDetail` — idea_key, slot, is_law, cost, removal_cost, is_default, dlc_source, modifiers[]

Router (`routers/ideas.py`):
- `GET /api/v1/ideas` — supports `?slot=`, `?is_law=`
- `GET /api/v1/ideas/{idea_key}` — single idea or 404

### Step 3.7 — Register all Phase 3 routers in `main.py`

### Test Gate: Phase 3

**Scope:** All Slice B endpoints return correct data.

```
tests/
├── test_technologies.py
├── test_characters.py
├── test_military.py
├── test_focuses.py
├── test_equipment.py
└── test_ideas.py
```

**Key tests per router (pattern: list, detail, 404, filter):**

| Router | Key tests |
|---|---|
| technologies | List returns 574 techs; `?folder=infantry` filters; single tech has prerequisites[]; country techs are date-sensitive |
| characters | GER has characters with roles[]; single character by ID; role has traits[] |
| military | GER divisions differ between 1936/1939 OOB files; naval fleet has nested task_forces[].ships[]; air wings have equipment_type |
| focuses | 74 focus trees total; GER tree has focuses with prerequisites[]; `/countries/GER/focus-tree` resolved correctly |
| equipment | 470 items total; `?is_archetype=true` filters; single item has resources[] |
| ideas | `?slot=economy` and `?is_law=true` filter correctly; single idea has modifiers[] |

**Run:** `pytest tests/ -v`

**Exit criteria:** All Slice A + B tests pass. Every paginated endpoint respects `?limit=` and `?offset=`. Every detail endpoint returns 404 for missing keys.

---

## Phase 4: Slice C — DLC Systems + Annotations

**Design ref:** §6.9, §6.10

### Step 4.1 — DLC router

**Design ref:** §6.9

Schemas (`schemas/dlc.py`):
- `MioDetail` — organization_key, template_key, icon, equipment_types[], traits[] with nested bonuses[]
- `OperationDetail` — operation_key, name, stats, awarded_tokens[], equipment_requirements[], phase_groups[]
- `BopDetail` — bop_key, initial_value, sides, decision_category, sides[], ranges[] with nested modifiers[]

Router (`routers/dlc.py`):
- `GET /api/v1/mios` + `/{organization_key}` — 459 MIO organisations
- `GET /api/v1/operations` + `/{operation_key}` — 37 espionage operations
- `GET /api/v1/bop` + `/{bop_key}` — Balance of Power definitions

None are date-sensitive.

### Step 4.2 — Annotations router (read/write)

**Design ref:** §6.10

Schemas (`schemas/annotation.py`):
- `AnnotationCreate` — entity_type (max 50), entity_key (max 200), note (min 1)
- `AnnotationOut` — annotation_id, entity_type, entity_key, note, created_at

Router (`routers/annotations.py`):
- `GET /api/v1/annotations` — list, filterable by `?entity_type=` and `?entity_key=`
- `GET /api/v1/annotations/{annotation_id}` — single annotation or 404
- `POST /api/v1/annotations` — create, returns 201 + created row
- `DELETE /api/v1/annotations/{annotation_id}` — returns 204, or 404 if not found

**Security note:** Validate `entity_type` against a known set (e.g. `country`, `state`, `technology`, `character`, `equipment`, `idea`, `focus_tree`, `operation`, `mio`, `bop`) to prevent abuse. The design doesn't mandate this but it's good hygiene.

### Step 4.3 — Register routers in `main.py`

### Test Gate: Phase 4

```
tests/
├── test_dlc.py
└── test_annotations.py
```

| Router | Key tests |
|---|---|
| dlc | 459 MIOs; single MIO has traits[]; 37 operations; single operation has phase_groups[]; BOP has sides[] and ranges[] |
| annotations | POST creates annotation → GET retrieves it → DELETE removes it → GET returns 404; invalid entity_type returns 400; list filters by entity_type+entity_key |

**Annotations specifically test the full CRUD lifecycle:**
1. POST `/annotations` with `{"entity_type": "country", "entity_key": "GER", "note": "test"}` → 201
2. GET `/annotations/{id}` → 200, matches input
3. GET `/annotations?entity_type=country&entity_key=GER` → includes the new annotation
4. DELETE `/annotations/{id}` → 204
5. GET `/annotations/{id}` → 404
6. POST with empty `note` → 422 (Pydantic validation)

**Run:** `pytest tests/ -v`

**Exit criteria:** All REST endpoints implemented and tested. Full Swagger docs at `/docs` show all 14 tags with correct models. Annotations CRUD works end-to-end.

---

## Phase 5: GraphQL Layer

**Design ref:** §7

### Step 5.1 — Strawberry types

**Design ref:** §7 (Defining Types)

Create `api/app/graphql/types.py` — mirror every Pydantic schema as a `@strawberry.type`. Key types:
- `Country`, `OwnedState`, `StartingTech`
- `State` (with nested resource/building/province types)
- `Technology`, `Character`, `CharacterRole`
- `Division`, `Fleet`, `AirWing`
- `FocusTree`, `Focus`
- `Equipment`, `Idea`
- `Mio`, `Operation`, `Bop`
- `Annotation`

### Step 5.2 — Resolvers

**Design ref:** §7 (Writing Resolvers)

Create `api/app/graphql/resolvers.py` — the `Query` class with fields:

| Field | Args | Returns | SQL Source |
|---|---|---|---|
| `country` | tag, date | `Country?` | `api_country_detail($1)` |
| `countries` | date, limit, offset | `[Country]` | `api_country_detail($1)` |
| `state` | state_id, date | `State?` | `api_state_detail($1)` |
| `states` | date, owner_tag, limit, offset | `[State]` | `api_state_detail($1)` |
| `technologies` | folder, limit, offset | `[Technology]` | `api_technology_tree` |
| `characters` | country_tag | `[Character]` | `api_country_characters` |
| `divisions` | country_tag, date | `[Division]` | `api_country_divisions` |
| `focusTrees` | country_tag | `[FocusTree]` | `api_focus_tree_detail` |
| `equipment` | archetype, is_archetype | `[Equipment]` | `api_equipment_catalog` |
| `ideas` | slot, is_law | `[Idea]` | `api_ideas_detail` |
| `mios` | — | `[Mio]` | `api_mio_organization_detail` |
| `operations` | — | `[Operation]` | `api_operation_detail` |
| `bop` | — | `[Bop]` | `api_bop_detail` |
| `annotations` | entity_type, entity_key | `[Annotation]` | `user_annotations` |

Resolvers reuse the same SQL queries as REST routers — extract shared query logic into helper functions if needed, but don't over-abstract.

### Step 5.3 — Schema & mount

**Design ref:** §7 (Building the Schema, Mounting on FastAPI)

Create `api/app/graphql/schema.py`:
```python
schema = strawberry.Schema(query=Query)
```

Mount in `main.py`:
```python
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
```

### Test Gate: Phase 5

```
tests/
└── test_graphql.py
```

| Test | Assertion |
|---|---|
| `test_country_query` | `{ country(tag: "GER") { tag stability ownedStates { stateId } } }` returns correct data |
| `test_country_date_1939` | `{ country(tag: "GER", date: "1939-08-14") { ... } }` returns different owned states |
| `test_characters_query` | `{ characters(countryTag: "GER") { nameKey roles { roleType traits } } }` returns characters with nested roles |
| `test_minimal_fields` | `{ countries(limit: 5) { tag } }` returns only `tag` field (GraphQL field selection works) |
| `test_technologies_filter` | `{ technologies(folder: "infantry") { technologyKey } }` filters correctly |
| `test_annotations_query` | Create via REST POST, query via GraphQL, verify data matches |
| `test_invalid_date` | Invalid date in GraphQL returns error |

**Also verify in browser:**
- `/graphql` loads GraphiQL IDE
- Auto-complete works for all fields
- camelCase conversion works (e.g. `ownedStates`, `technologyKey`)

**Run:** `pytest tests/ -v`

**Exit criteria:** All GraphQL queries work. GraphiQL IDE loads. REST and GraphQL produce identical data for the same query.

---

## Phase 6: Polish & Integration Testing

### Step 6.1 — CORS configuration

**Design ref:** §6.1 (implied by "Frontend country-profile viewer" consumer)

Add CORS middleware in `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten when deployed
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)
```

### Step 6.2 — API README

Create `api/README.md` with:
- Quick start (install deps, set `.env`, run `uvicorn`)
- Endpoint summary table
- Link to Swagger (`/docs`), ReDoc (`/redoc`), GraphiQL (`/graphql`)
- How to run tests

### Step 6.3 — Update repo-level docs

Update the following to reflect the API's existence:
- `README.md` — add API section with quick start
- `.github/copilot-instructions.md` — update "NOT YET DONE" section, add API paths to repository structure
- `tools/db_etl/runbook.md` — mention API views → functions change

### Final Test Gate: Full Integration

Run the complete test suite:

```bash
cd api
pytest tests/ -v --tb=short
```

**Full integration smoke test (manual or scripted):**

```bash
# Start server
uvicorn api.app.main:app --reload &

# REST smoke tests
curl localhost:8000/health
curl localhost:8000/api/v1/countries?limit=5
curl localhost:8000/api/v1/countries/GER
curl localhost:8000/api/v1/countries/GER?date=1939-08-14
curl localhost:8000/api/v1/states/64
curl localhost:8000/api/v1/technologies?folder=infantry
curl localhost:8000/api/v1/countries/GER/characters
curl localhost:8000/api/v1/countries/GER/divisions
curl localhost:8000/api/v1/countries/GER/naval
curl localhost:8000/api/v1/countries/GER/air
curl localhost:8000/api/v1/focus-trees
curl localhost:8000/api/v1/equipment?is_archetype=true
curl localhost:8000/api/v1/ideas?slot=economy
curl localhost:8000/api/v1/mios
curl localhost:8000/api/v1/operations
curl localhost:8000/api/v1/bop

# GraphQL smoke test
curl -X POST localhost:8000/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "{ country(tag: \"GER\") { tag stability ownedStates { stateId } } }"}'

# Annotations CRUD
curl -X POST localhost:8000/api/v1/annotations \
  -H "Content-Type: application/json" \
  -d '{"entity_type": "country", "entity_key": "GER", "note": "Integration test"}'
```

**Exit criteria:**
- All automated tests pass
- Swagger UI (`/docs`) fully renders all endpoints with models
- GraphiQL (`/graphql`) loads with auto-complete
- Both `?date=1936-01-01` and `?date=1939-08-14` return valid, different data
- Annotations CRUD lifecycle works
- No Python warnings or deprecation notices on startup

---

## Summary: Implementation Order & Dependencies

```
Phase 0  SQL fixes (annotations DDL, view→function, runbook counts)
   │
Phase 1  Scaffold (config, database, dependencies, main, health)
   │     └─ TEST GATE: health, openapi, date validation
   │
Phase 2  Slice A: countries + states (date-sensitive, jsonb)
   │     └─ TEST GATE: list, detail, 404, pagination, date filtering
   │
Phase 3  Slice B: techs, characters, military, focuses, equipment, ideas
   │     └─ TEST GATE: all 8 routers with filters and nested models
   │
Phase 4  Slice C: DLC + annotations (first write endpoint)
   │     └─ TEST GATE: DLC reads + annotation CRUD lifecycle
   │
Phase 5  GraphQL layer (types, resolvers, schema, mount)
   │     └─ TEST GATE: all queries, field selection, date params
   │
Phase 6  Polish (CORS, docs, integration smoke test)
         └─ FINAL TEST GATE: full suite + manual smoke
```

**Estimated test count:** ~50–60 tests across 10 test files.

**Files created:** ~30 Python files + 2 SQL changes + 3 doc updates.
