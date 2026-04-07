# HOI4 Database — API Implementation Plan

> **Date:** 2026-04-02
> **Branch:** `feature/api-v1`
> **Design doc:** `docs/api-design.md` (FINAL, 2026-03-31)
> **Database:** 149 tables, ~219K rows, 14 views + 2 functions, PostgreSQL 16

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
- [x] 3.1 — Technologies (schemas + router)
- [x] 3.2 — Characters (schemas + router)
- [x] 3.3 — Military — land / naval / air (schemas + router)
- [ ] 3.4 — Focus Trees (schemas + router)
- [ ] 3.5 — Equipment (schemas + router)
- [ ] 3.6 — Ideas (schemas + router)
- [ ] 3.7 — Register all Phase 3 routers
- [ ] Test gate: all 8 routers with filters and nested models

### Phase 4: Slice C — DLC Systems + Annotations (Read/Write)
- [ ] 4.1 — DLC router (MIOs, operations, BoP, factions, special projects)
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

**Exit criteria:** 149 tables; 14 views + 2 functions; both date params work; 0 errors.

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

**File:** `tests/conftest.py` — Shared fixtures used by ALL test files. You never import it — pytest finds it automatically.
- Creates a real asyncpg pool against the Docker database (tests run against real game data, not mocks)
- Uses `httpx.AsyncClient` + `httpx.ASGITransport` to send requests to the app without a running server
- Overrides the `get_db` dependency so all test requests use the test pool
- Every test function receives a `client` parameter — that's the AsyncClient, injected by pytest

**File:** `tests/test_health.py` (2 tests)
- `test_health_200` — GET `/health`, expect 200 and `{"status": "ok"}`
- `test_openapi_schema` — GET `/openapi.json`, expect 200 and `"HOI4"` in the title. This validates FastAPI's auto-generated docs render

**File:** `tests/test_date_validation.py` (3 tests) — These test the `get_effective_date()` dependency **directly** (no HTTP), by importing it from `app.dependencies`:
- `test_default_date` — call with `None`, expect `date(1936, 1, 1)`
- `test_valid_date_1939` — call with `"1939-08-14"`, expect `date(1939, 8, 14)`
- `test_invalid_date_400` — call with `"2000-01-01"`, expect `HTTPException` with status 400. Use `pytest.raises(HTTPException)` to catch it

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

**SQL for list countries** (paginated, date-sensitive):
```sql
SELECT tag, country_name, capital_state_id, stability, war_support
FROM api_country_detail($1)
ORDER BY tag
LIMIT $2 OFFSET $3
```
- `$1` = `effective_date` (e.g. `date(1936, 1, 1)`)
- `$2` = `limit`
- `$3` = `offset`
- `api_country_detail` is a **function** (not a view) — you call it with `$1` as a positional argument, then filter the result set with WHERE/ORDER/LIMIT
- The list query only selects 5 lightweight columns for `CountrySummary`

**SQL for single country** (date-sensitive):
```sql
SELECT * FROM api_country_detail($1) WHERE tag = $2
```
- `$1` = `effective_date`
- `$2` = `tag.upper()` (e.g. `'GER'`)
- Returns one row or None → 404 if None
- `SELECT *` pulls all columns including jsonb arrays — maps to `CountryDetail` (see §6.2 in design doc for field shapes)

### Step 2.3 — States router

**Design ref:** §6.2 (states section)

Create `api/app/routers/states.py`:
- `GET /api/v1/states` — calls `api_state_detail(p_date)`, supports `?owner_tag=GER`
- `GET /api/v1/states/{state_id}` — single state or 404

**SQL for list states** (paginated, date-sensitive, no filter):
```sql
SELECT state_id, state_name_key, state_name, state_category, manpower, owner_tag
FROM api_state_detail($1)
ORDER BY state_id
LIMIT $2 OFFSET $3
```
- `$1` = `effective_date`
- `$2` = `limit`
- `$3` = `offset`
- Same function-call pattern as countries — `api_state_detail` is a function, not a view
- The list query only selects 6 lightweight columns for `StateSummary`

**SQL for list states with ?owner_tag= filter**:
```sql
SELECT state_id, state_name_key, state_name, state_category, manpower, owner_tag
FROM api_state_detail($1)
WHERE owner_tag = $2
ORDER BY state_id
LIMIT $3 OFFSET $4
```
- `$1` = `effective_date`
- `$2` = `owner_tag.upper()` (e.g. `'GER'`)
- `$3` = `limit`
- `$4` = `offset`
- The filter adds one parameter — note `$3`/`$4` shift vs the unfiltered version
- The router uses an `if owner_tag:` branch to pick which SQL string to run

**SQL for single state** (date-sensitive):
```sql
SELECT * FROM api_state_detail($1) WHERE state_id = $2
```
- `$1` = `effective_date`
- `$2` = `state_id` (int, e.g. `64`)
- Returns one row or None → 404 if None
- `SELECT *` pulls all columns including jsonb arrays — maps to `StateDetail` (see §6.2 in design doc for field shapes)

### Step 2.4 — Register routers in `main.py`

```python
app.include_router(countries.router)
app.include_router(states.router)
```

### Test Gate: Phase 2

**Scope:** Date-sensitive endpoints work correctly with both bookmarks.

**File:** `tests/test_countries.py` (7 tests)

Every test follows the same pattern: send a GET request via `client`, check status code, parse `resp.json()`, assert on fields. The `client` fixture comes from `conftest.py`.

| Test | URL | What to check |
|---|---|---|
| `test_list_countries_200` | `GET /api/v1/countries` | Status 200, response is a non-empty list |
| `test_list_countries_has_tag` | `GET /api/v1/countries?limit=5` | Every item in the list has a `"tag"` field |
| `test_list_countries_pagination` | `GET /api/v1/countries?limit=3&offset=0` | Exactly 3 items returned — proves LIMIT works |
| `test_country_detail_ger` | `GET /api/v1/countries/GER` | `tag` == `"GER"`, `capital_state_id` is not None, `owned_states` and `starting_technologies` are both non-empty lists. This is the key test for jsonb — if these come back as strings instead of lists, asyncpg's jsonb codec isn't registered |
| `test_country_detail_lowercase_tag` | `GET /api/v1/countries/ger` | Status 200, `tag` == `"GER"` — proves the router uppercases the path parameter |
| `test_country_detail_404` | `GET /api/v1/countries/ZZZ` | Status 404 — proves the router returns a proper error for missing countries |
| `test_country_detail_1939` | `GET /api/v1/countries/GER?date=1939-08-14` | Status 200, `tag` == `"GER"` — proves the 1939 bookmark returns valid data |

> **Tip:** You can also add `test_country_list_invalid_date` (GET `?date=2000-01-01` → 400) as an integration-level check, but `test_date_validation.py` already covers the function directly.

**File:** `tests/test_states.py` (6 tests)

| Test | URL | What to check |
|---|---|---|
| `test_list_states_200` | `GET /api/v1/states` | Status 200, non-empty list |
| `test_list_states_pagination` | `GET /api/v1/states?limit=5&offset=0` | Exactly 5 items |
| `test_list_states_filter_by_owner` | `GET /api/v1/states?owner_tag=GER` | Non-empty list, and **every** item has `owner_tag` == `"GER"`. Loop through the results and assert on each one |
| `test_state_detail_64` | `GET /api/v1/states/64` | `state_id` == 64, `resources`, `state_buildings`, `provinces` are all lists, `provinces` is non-empty (every state has at least one province) |
| `test_state_detail_404` | `GET /api/v1/states/99999` | Status 404 |
| `test_state_detail_1939` | `GET /api/v1/states/64?date=1939-08-14` | Status 200, `state_id` == 64 |

**Run:** `pytest tests/test_countries.py tests/test_states.py -v`

**Exit criteria:** All 13 tests pass. Swagger at `/docs` shows both endpoints with correct request/response models. Both `?date=` values produce valid results.

---

## Phase 3: Slice B — Domain Catalogs

**Design ref:** §6.3–§6.8

Eight routers covering non-date-sensitive views plus the 3 date-sensitive military endpoints. Each follows the established pattern from Phase 2.

### Step 3.1 — Technologies

**Design ref:** §6.3

Schemas (`schemas/technology.py`):
- `TechSummary` — technology_key, start_year, research_cost, folder_name, dlc_source (lightweight, for list)
- `TechTreeItem` — everything in TechSummary + prerequisites[], categories[], enables_equipment[], enables_units[] (full, for detail)
- `CountryTech` — country_tag, technology_key, technology_name, dlc_source

The list endpoint queries the `technologies` table directly (lightweight). Only the detail endpoint hits the `api_technology_tree` view. This mirrors the `CountrySummary`/`CountryDetail` split.

Router (`routers/technologies.py`):
- `GET /api/v1/technologies` — from `technologies` table (not the view), returns `list[TechSummary]`, supports `?folder=`
- `GET /api/v1/technologies/{key}` — from `api_technology_tree` view, returns `TechTreeItem` or 404
- `GET /api/v1/countries/{tag}/technologies` — from `api_country_technologies` view, returns `list[CountryTech]`, date-sensitive via `WHERE effective_date <= $date`

**SQL for list technologies** (paginated, no filter):
```sql
SELECT t.technology_key,
       COALESCE(l.loc_value, t.technology_key) AS technology_name,
       t.start_year, t.research_cost, t.folder_name
FROM technologies t
LEFT JOIN localisation l ON l.loc_key = t.technology_key
ORDER BY t.technology_key
LIMIT $1 OFFSET $2
```
- `$1` = `limit`
- `$2` = `offset`
- This queries the **table directly** (not a view) — lightweight, no jsonb aggregation
- The `LEFT JOIN localisation` gives a human-readable name; `COALESCE` falls back to the key if no translation exists
- Not date-sensitive — technologies are static catalog data

**SQL for list technologies with ?folder= filter**:
```sql
SELECT t.technology_key,
       COALESCE(l.loc_value, t.technology_key) AS technology_name,
       t.start_year, t.research_cost, t.folder_name
FROM technologies t
LEFT JOIN localisation l ON l.loc_key = t.technology_key
WHERE t.folder_name = $1
ORDER BY t.technology_key
LIMIT $2 OFFSET $3
```
- `$1` = `folder` (e.g. `'infantry_folder'`)
- `$2` = `limit`
- `$3` = `offset`
- Same as above but filtered by folder — note parameter positions shift

**SQL for single technology** (detail):
```sql
SELECT * FROM api_technology_tree WHERE technology_key = $1
```
- `$1` = `key` (e.g. `'infantry_weapons'`)
- Returns one row or None → 404 if None
- `SELECT *` pulls all columns including jsonb arrays — maps to `TechTreeItem` (see §6.3 in design doc for field shapes)

**SQL for country starting technologies** (date-sensitive):
```sql
SELECT technology_key, technology_name, dlc_source
FROM api_country_technologies
WHERE country_tag = $1 AND effective_date <= $2
ORDER BY technology_key
```
- `$1` = `tag.upper()` (e.g. `'GER'`)
- `$2` = `effective_date` (e.g. `date(1936, 1, 1)`)
- No pagination — countries typically have 20-80 starting techs, always return all
- `api_country_technologies` is a **view** (not a function) — the date filter goes in `WHERE`, not as a function argument
- `technology_name` comes from the view's own `LEFT JOIN localisation`
- This is the pattern for **date-sensitive views vs functions**: views expose the `effective_date` column and you filter with `<=`; functions accept the date as a parameter

### Step 3.2 — Characters

**Design ref:** §6.4

Schemas (`schemas/character.py`):
- `CharacterRole` — role_type, sub_ideology_key, skill, attack_skill, defense_skill, planning_skill, logistics_skill, maneuvering_skill, coordination_skill, dlc_source, traits[]
- `CharacterSummary` — character_id, name_key, country_tag, gender (lightweight, for list)
- `CharacterDetail` — everything in CharacterSummary + roles[] (full, for detail)

Router (`routers/characters.py`):
- `GET /api/v1/countries/{tag}/characters` — lightweight list (no roles), returns `list[CharacterSummary]`
- `GET /api/v1/characters/{character_id}` — full detail with roles, returns `CharacterDetail` or 404

**How to build the file** (copy the pattern from `technologies.py`):
1. One `APIRouter` with `prefix="/api/v1"`, `tags=["Characters"]`
2. List endpoint: `@router.get("/countries/{tag}/characters")` — uses `db.fetch()`, takes `tag`, `limit`, `offset` params, returns `list[CharacterSummary]`. The SQL only selects 4 flat columns (no `roles`), keeping it lightweight

3. Detail endpoint: `@router.get("/characters/{character_id}")` — uses `db.fetchrow()`, raises 404 if None, returns `CharacterDetail` with `roles`
4. `return [dict(row) for row in rows]` for lists, `return dict(row)` for single
5. No date logic — characters are not date-sensitive, so no `Depends(get_effective_date)`
6. Register in `main.py`: `app.include_router(characters.router)`

**SQL for list characters by country** (paginated, lightweight — no roles):
```sql
SELECT character_id, name_key, country_tag, gender
FROM api_country_characters
WHERE country_tag = $1
ORDER BY character_id
LIMIT $2 OFFSET $3
```
- `$1` = `tag.upper()`
- `$2` = `limit`
- `$3` = `offset`

**SQL for single character** (full, with roles):
```sql
SELECT character_id, name_key, country_tag, gender, roles
FROM api_country_characters
WHERE character_id = $1
```
- `$1` = `character_id` (e.g. `'GER_erwin_rommel'`)
- Returns one row or None → 404 if None

### Step 3.3 — Military (Land / Naval / Air)

**Design ref:** §6.5

Schemas (`schemas/military.py`):
- `Regiment` — unit_type_key, grid_x, grid_y
- `SupportCompany` — unit_type_key, grid_x, grid_y
- `Deployed` — location_province_id, start_experience_factor
- `DivisionDetail` — country_tag, division_template_id, template_name, oob_file, regiments[], support[], deployed_divisions[]
- `Ship` — ship_name, definition, hull_equipment_key, version_name, pride_of_the_fleet
- `TaskForce` — task_force_id, task_force_name, location_province_id, ships[]
- `NavalDetail` — country_tag, fleet_id, fleet_name, naval_base_province_id, oob_file, task_forces[]
- `AirWingItem` — country_tag, location_state_id, state_name_key, equipment_type, amount, wing_name, version_name, oob_file

Router (`routers/military.py`):
- `GET /api/v1/countries/{tag}/divisions` — date-sensitive via OOB file suffix
- `GET /api/v1/countries/{tag}/naval` — same OOB filtering
- `GET /api/v1/countries/{tag}/air` — same OOB filtering

**How to build the file:**
1. One `APIRouter` with `prefix="/api/v1"`, `tags=["Military"]`
2. Three endpoints: `@router.get("/countries/{tag}/divisions")`, `@router.get("/countries/{tag}/naval")`, `@router.get("/countries/{tag}/air")`
3. All three use `Depends(get_effective_date)` — this is the date-sensitive part
4. Before each SQL call, compute `oob_suffix` from the date. Pass it as `$2` in the SQL
5. No 404 needed — if a country has no military, you just get an empty list, which is valid
6. Register in `main.py`: `app.include_router(military.router)`

All three endpoints share the same date-to-OOB logic:
```python
oob_suffix = "1936" if effective_date.year == 1936 else "1939"
```

**SQL for divisions**:
```sql
SELECT country_tag, division_template_id, template_name, oob_file,
       regiments, support, deployed_divisions
FROM api_country_divisions
WHERE country_tag = $1
  AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
ORDER BY template_name
```
- `$1` = `tag.upper()`
- `$2` = `oob_suffix` (e.g. `'1936'`)

**SQL for naval**:
```sql
SELECT country_tag, fleet_id, fleet_name, naval_base_province_id, oob_file,
       task_forces
FROM api_country_naval
WHERE country_tag = $1
  AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
ORDER BY fleet_name
```

**SQL for air wings**:
```sql
SELECT country_tag, location_state_id, state_name_key,
       equipment_type, amount, wing_name, version_name, oob_file
FROM api_country_air
WHERE country_tag = $1
  AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
ORDER BY location_state_id
```

### Step 3.4 — Focus Trees

**Design ref:** §6.6

Schemas (`schemas/focus.py`):
- `FocusPrereq` — group (int), required_focus_id (str)
- `FocusItem` — focus_id, cost, x_pos, y_pos, icon, dlc_source, prerequisites[], mutually_exclusive[]
- `FocusTreeSummary` — focus_tree_id, country_tag (for the list endpoint)
- `FocusTreeDetail` — focus_tree_id, country_tag, focuses[]

Router (`routers/focuses.py`):
- `GET /api/v1/focus-trees` — list all trees (lightweight, no focuses array)
- `GET /api/v1/focus-trees/{focus_tree_id}` — single tree with focuses
- `GET /api/v1/countries/{tag}/focus-tree` — tree for a country

**How to build the file:**
1. One `APIRouter` with `prefix="/api/v1"`, `tags=["Focus Trees"]`
2. List endpoint (`@router.get("/focus-trees")`): uses `db.fetch()`, returns `list[FocusTreeSummary]` — note the SQL only selects `focus_tree_id, country_tag` (no `focuses` column), keeping it lightweight
3. Detail endpoint (`@router.get("/focus-trees/{focus_tree_id}")`): uses `db.fetchrow()`, returns `FocusTreeDetail` or 404
4. Country endpoint (`@router.get("/countries/{tag}/focus-tree")`): uses `db.fetchrow()`, returns `FocusTreeDetail` or 404 — same query, just filtered by country instead of tree id
5. Not date-sensitive — no `Depends(get_effective_date)` needed
6. Register in `main.py`: `app.include_router(focuses.router)`

**SQL for list focus trees** (paginated, lightweight):
```sql
SELECT focus_tree_id, country_tag
FROM api_focus_tree_detail
ORDER BY focus_tree_id
LIMIT $1 OFFSET $2
```

**SQL for single focus tree**:
```sql
SELECT focus_tree_id, country_tag, focuses
FROM api_focus_tree_detail
WHERE focus_tree_id = $1
```

**SQL for focus tree by country**:
```sql
SELECT focus_tree_id, country_tag, focuses
FROM api_focus_tree_detail
WHERE country_tag = $1
```

### Step 3.5 — Equipment

**Design ref:** §6.7

Schemas (`schemas/equipment.py`):
- `EquipmentResource` — resource_key, amount
- `EquipmentItem` — equipment_key, is_archetype, archetype_key, parent_key, year, build_cost_ic, reliability, maximum_speed, defense, breakthrough, soft_attack, hard_attack, ap_attack, air_attack, armor_value, hardness, dlc_source, resources[]

Router (`routers/equipment.py`):
- `GET /api/v1/equipment` — supports `?archetype=`, `?is_archetype=`
- `GET /api/v1/equipment/{equipment_key}` — single item or 404

**How to build the file:**
1. One `APIRouter` with `prefix="/api/v1"`, `tags=["Equipment"]`
2. List endpoint (`@router.get("/equipment")`): has **two optional query params**: `?archetype=` and `?is_archetype=`. Use `if/elif/else` to pick the right SQL string (same pattern as `technologies.py` with its `if folder:` branch). Three SQL variants = three branches
3. Detail endpoint (`@router.get("/equipment/{equipment_key}")`): `db.fetchrow()`, 404 if None, returns `EquipmentItem`
4. Not date-sensitive — equipment definitions are static catalog data
5. Register in `main.py`: `app.include_router(equipment.router)`

**SQL for list equipment** (paginated, no filters):
```sql
SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
       build_cost_ic, reliability, maximum_speed, defense, breakthrough,
       soft_attack, hard_attack, ap_attack, air_attack, armor_value,
       hardness, dlc_source, resources
FROM api_equipment_catalog
ORDER BY equipment_key
LIMIT $1 OFFSET $2
```

**SQL with ?archetype= filter**:
```sql
SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
       build_cost_ic, reliability, maximum_speed, defense, breakthrough,
       soft_attack, hard_attack, ap_attack, air_attack, armor_value,
       hardness, dlc_source, resources
FROM api_equipment_catalog
WHERE archetype_key = $1
ORDER BY equipment_key
LIMIT $2 OFFSET $3
```

**SQL with ?is_archetype= filter**:
```sql
SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
       build_cost_ic, reliability, maximum_speed, defense, breakthrough,
       soft_attack, hard_attack, ap_attack, air_attack, armor_value,
       hardness, dlc_source, resources
FROM api_equipment_catalog
WHERE is_archetype = $1
ORDER BY equipment_key
LIMIT $2 OFFSET $3
```

**SQL for single equipment item**:
```sql
SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
       build_cost_ic, reliability, maximum_speed, defense, breakthrough,
       soft_attack, hard_attack, ap_attack, air_attack, armor_value,
       hardness, dlc_source, resources
FROM api_equipment_catalog
WHERE equipment_key = $1
```

### Step 3.6 — Ideas

**Design ref:** §6.8

Schemas (`schemas/idea.py`):
- `IdeaModifier` — modifier_key, modifier_value (float)
- `IdeaDetail` — idea_key, slot, is_law, cost, removal_cost, is_default, dlc_source, modifiers[]

Router (`routers/ideas.py`):
- `GET /api/v1/ideas` — supports `?slot=`, `?is_law=`
- `GET /api/v1/ideas/{idea_key}` — single idea or 404

**How to build the file:**
1. One `APIRouter` with `prefix="/api/v1"`, `tags=["Ideas"]`
2. List endpoint (`@router.get("/ideas")`): has **two optional query params**: `?slot=` and `?is_law=`. Same `if/elif/else` branching pattern as equipment
3. Detail endpoint (`@router.get("/ideas/{idea_key}")`): `db.fetchrow()`, 404 if None, returns `IdeaDetail`
4. Not date-sensitive
5. Register in `main.py`: `app.include_router(ideas.router)`
6. This is structurally identical to equipment — if you get equipment working, copy-paste and rename

**SQL for list ideas** (paginated, no filters):
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
ORDER BY idea_key
LIMIT $1 OFFSET $2
```

**SQL with ?slot= filter**:
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
WHERE slot = $1
ORDER BY idea_key
LIMIT $2 OFFSET $3
```

**SQL with ?is_law= filter**:
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
WHERE is_law = $1
ORDER BY idea_key
LIMIT $2 OFFSET $3
```

**SQL for single idea**:
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
WHERE idea_key = $1
```

### Step 3.7 — Register all Phase 3 routers in `main.py`

### Test Gate: Phase 3

**Scope:** All Slice B endpoints return correct data. Every test file follows the same pattern established in Phase 2: GET a URL → check status code → parse JSON → assert on fields.

**Testing pattern for nested arrays:** When an endpoint returns jsonb arrays (like `roles[]`, `regiments[]`, `task_forces[]`), you need to:
1. Assert the field is a list: `assert isinstance(data["roles"], list)`
2. Assert it's not empty (if you know the test entity has data): `assert len(data["roles"]) > 0`
3. Loop through items and check their fields: `for role in data["roles"]: assert "role_type" in role`

**Testing pattern for filters:** When an endpoint has a query filter (like `?folder=`), loop through ALL results and assert the filter field matches on every item. For example, if you request `?slot=economy`, every idea in the response must have `slot == "economy"`.

#### `test_technologies.py` (8 tests)

| Test | URL | What to check |
|---|---|---|
| `test_list_technologies_200` | `GET /api/v1/technologies` | Status 200, non-empty list |
| `test_list_technologies_pagination` | `GET /api/v1/technologies?limit=5&offset=0` | Exactly 5 items |
| `test_list_technologies_folder_filter` | `GET /api/v1/technologies?folder=infantry_folder` | Non-empty list, every item has `folder_name` == `"infantry_folder"` |
| `test_list_technologies_has_name` | `GET /api/v1/technologies?limit=5` | Every item has both `technology_key` and `technology_name` |
| `test_technology_detail` | `GET /api/v1/technologies/infantry_weapons` | `technology_key` == `"infantry_weapons"`, has `prerequisites`, `categories`, `enables_equipment`, `enables_units` — all lists |
| `test_technology_detail_404` | `GET /api/v1/technologies/nonexistent_tech_xyz` | Status 404 |
| `test_country_technologies_ger` | `GET /api/v1/countries/GER/technologies` | Non-empty list, every item has `technology_key` and `technology_name` |
| `test_country_technologies_lowercase_tag` | `GET /api/v1/countries/ger/technologies` | Status 200, non-empty — proves tag uppercasing works |

#### `test_characters.py` (10 tests) — ALREADY WRITTEN

This file is already complete at `api/tests/test_characters.py`. Here's what each test verifies:

**List endpoint** (`GET /api/v1/countries/{tag}/characters`):

| Test | URL | What to check |
|---|---|---|
| `test_list_characters_200` | `GET /api/v1/countries/GER/characters` | Status 200, non-empty list (GER has ~140 characters) |
| `test_list_characters_summary_fields` | `GET /api/v1/countries/GER/characters?limit=5` | Every item has `character_id`, `name_key`, `country_tag`, `gender` — and `roles` is **NOT** present (list is lightweight, no nested data) |
| `test_list_characters_pagination` | `GET /api/v1/countries/GER/characters?limit=3&offset=0` | Exactly 3 items |
| `test_list_characters_lowercase_tag` | `GET /api/v1/countries/ger/characters` | Status 200, non-empty |
| `test_list_characters_empty_country` | `GET /api/v1/countries/ZZZ/characters` | Status 200, empty list `[]` — not 404. An empty collection is valid |

**Detail endpoint** (`GET /api/v1/characters/{character_id}`):

| Test | URL | What to check |
|---|---|---|
| `test_character_detail_rommel` | `GET /api/v1/characters/GER_erwin_rommel` | `character_id` == `"GER_erwin_rommel"`, `country_tag` == `"GER"`, `gender` == `"male"`, `roles` is a list with at least 2 items (Rommel is both corps_commander and advisor) |
| `test_character_detail_roles_have_required_fields` | `GET /api/v1/characters/GER_erwin_rommel` | Loop through each role in `roles[]` and check it has: `role_type` (string), `traits` (list), and all skill fields (`skill`, `attack_skill`, `defense_skill`, `planning_skill`, `logistics_skill`, `manuvering_skill`, `coordination_skill`). Skill values will be null but the keys must exist |
| `test_character_detail_rommel_has_corps_commander` | `GET /api/v1/characters/GER_erwin_rommel` | Filter `roles[]` to find the one where `role_type` == `"corps_commander"`. Assert exactly 1 match. Check its `traits` list contains `"armor_officer"` and `"trickster"` |
| `test_character_detail_rommel_has_advisor` | `GET /api/v1/characters/GER_erwin_rommel` | Filter `roles[]` to find `role_type` == `"advisor"`. Assert exactly 1 match. Check it has at least one trait |
| `test_character_detail_404` | `GET /api/v1/characters/ZZZ_nobody` | Status 404 |

#### `test_military.py` (9 tests)

All three military endpoints are date-sensitive and use OOB file suffix matching. They return **empty lists** (not 404) for countries with no military.

**Divisions** (`GET /api/v1/countries/{tag}/divisions`):

| Test | URL | What to check |
|---|---|---|
| `test_divisions_ger_200` | `GET /api/v1/countries/GER/divisions` | Status 200, non-empty list |
| `test_divisions_have_nested_arrays` | `GET /api/v1/countries/GER/divisions` | Each division has `template_name`, and `regiments`, `support`, `deployed_divisions` are all lists. `regiments` is non-empty (every template has at least one regiment) |
| `test_divisions_empty_country` | `GET /api/v1/countries/ZZZ/divisions` | Status 200, empty list `[]` |

**Naval** (`GET /api/v1/countries/{tag}/naval`):

| Test | URL | What to check |
|---|---|---|
| `test_naval_ger_200` | `GET /api/v1/countries/GER/naval` | Status 200, non-empty list |
| `test_naval_has_task_forces` | `GET /api/v1/countries/GER/naval` | Each fleet has `fleet_name` and `task_forces` (list). If a fleet has task forces, each task force should have `task_force_name` and `ships` (list). This tests 2 levels of nesting: fleet → task_forces[] → ships[] |
| `test_naval_empty_country` | `GET /api/v1/countries/ZZZ/naval` | Status 200, empty list `[]` |

**Air** (`GET /api/v1/countries/{tag}/air`):

| Test | URL | What to check |
|---|---|---|
| `test_air_ger_200` | `GET /api/v1/countries/GER/air` | Status 200, non-empty list |
| `test_air_has_equipment_type` | `GET /api/v1/countries/GER/air` | Each air wing has `equipment_type` and `amount` |
| `test_air_empty_country` | `GET /api/v1/countries/ZZZ/air` | Status 200, empty list `[]` |

#### `test_focuses.py` (8 tests)

Focus trees use the Summary/Detail split. The list returns `FocusTreeSummary` (no `focuses[]`), the detail returns `FocusTreeDetail` (with `focuses[]`).

**Tip for the detail test:** Since you may not know a valid `focus_tree_id` upfront, fetch the list first with `?limit=1`, grab the `focus_tree_id` from the first result, then GET the detail for that ID.

| Test | URL | What to check |
|---|---|---|
| `test_list_focus_trees_200` | `GET /api/v1/focus-trees` | Status 200, non-empty list |
| `test_list_focus_trees_pagination` | `GET /api/v1/focus-trees?limit=5&offset=0` | Exactly 5 items |
| `test_list_focus_trees_summary_only` | `GET /api/v1/focus-trees?limit=3` | Every item has `focus_tree_id` and `country_tag`, and `focuses` is **NOT** present |
| `test_focus_tree_detail` | `GET /api/v1/focus-trees/{id}` | `focus_tree_id` matches, `focuses` is a non-empty list |
| `test_focus_tree_focuses_have_fields` | `GET /api/v1/focus-trees/{id}` | Each focus in `focuses[]` has `focus_id`, `cost`, `prerequisites` (list), `mutually_exclusive` (list) |
| `test_focus_tree_detail_404` | `GET /api/v1/focus-trees/nonexistent_tree_xyz` | Status 404 |
| `test_country_focus_tree_ger` | `GET /api/v1/countries/GER/focus-tree` | `country_tag` == `"GER"`, `focuses` is a non-empty list |
| `test_country_focus_tree_404` | `GET /api/v1/countries/ZZZ/focus-tree` | Status 404 (unlike military endpoints, a missing tree IS a 404 because it returns a single object, not a collection) |

#### `test_equipment.py` (7 tests)

Equipment has two filters (`?is_archetype=` and `?archetype=`). Test each one by looping through results and asserting the filter field matches.

| Test | URL | What to check |
|---|---|---|
| `test_list_equipment_200` | `GET /api/v1/equipment` | Status 200, non-empty list |
| `test_list_equipment_pagination` | `GET /api/v1/equipment?limit=5&offset=0` | Exactly 5 items |
| `test_list_equipment_archetype_filter` | `GET /api/v1/equipment?is_archetype=true` | Non-empty, every item has `is_archetype` == `true` |
| `test_list_equipment_parent_filter` | `GET /api/v1/equipment?archetype=infantry_equipment` | Non-empty, every item has `archetype_key` == `"infantry_equipment"` |
| `test_equipment_detail` | `GET /api/v1/equipment/infantry_equipment_0` | `equipment_key` matches, `resources` is a list |
| `test_equipment_detail_has_stats` | `GET /api/v1/equipment/infantry_equipment_0` | Has `build_cost_ic`, `reliability`, `soft_attack` fields |
| `test_equipment_detail_404` | `GET /api/v1/equipment/nonexistent_equip_xyz` | Status 404 |

#### `test_ideas.py` (7 tests)

Ideas have two filters (`?slot=` and `?is_law=`). Same loop-and-assert pattern as equipment.

**Tip for the detail test:** Since you may not know a valid `idea_key` upfront, fetch the list first with `?limit=1`, grab the `idea_key`, then GET the detail.

| Test | URL | What to check |
|---|---|---|
| `test_list_ideas_200` | `GET /api/v1/ideas` | Status 200, non-empty list |
| `test_list_ideas_pagination` | `GET /api/v1/ideas?limit=5&offset=0` | Exactly 5 items |
| `test_list_ideas_slot_filter` | `GET /api/v1/ideas?slot=economy` | Non-empty, every item has `slot` == `"economy"` |
| `test_list_ideas_law_filter` | `GET /api/v1/ideas?is_law=true` | Non-empty, every item has `is_law` == `true` |
| `test_idea_detail` | `GET /api/v1/ideas/{key}` | `idea_key` matches, `modifiers` is a list |
| `test_idea_detail_modifiers_have_fields` | `GET /api/v1/ideas/{key}` | Each modifier in `modifiers[]` has `modifier_key` (string) and `modifier_value` (number) |
| `test_idea_detail_404` | `GET /api/v1/ideas/nonexistent_idea_xyz` | Status 404 |

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
- `FactionDetail` — template_key, name_loc, manifest_key, icon, goals[], rules[], member_upgrade_groups[]
- `SpecialProjectDetail` — project_key, specialization_key, project_tag, complexity, prototype_time, rewards[]

Router (`routers/dlc.py`):
- `GET /api/v1/mios` + `/{organization_key}` — 459 MIO organisations
- `GET /api/v1/operations` + `/{operation_key}` — 37 espionage operations
- `GET /api/v1/bop` + `/{bop_key}` — Balance of Power definitions
- `GET /api/v1/factions` + `/{template_key}` — 65 faction templates (DLC: Götterdämmerung)
- `GET /api/v1/special-projects` + `/{project_key}` — 48 special projects (DLC: Götterdämmerung)

None are date-sensitive.

**SQL for factions** (list, paginated):
```sql
SELECT template_key, name_loc, manifest_key, icon, can_leader_join_other,
       dlc_source, goals, rules, member_upgrade_groups
FROM api_faction_detail
ORDER BY template_key
LIMIT $1 OFFSET $2
```

**SQL for single faction:**
```sql
SELECT * FROM api_faction_detail WHERE template_key = $1
```

**SQL for special projects** (list, paginated):
```sql
SELECT project_key, specialization_key, project_tag, complexity,
       prototype_time, dlc_source, rewards
FROM api_special_project_detail
ORDER BY project_key
LIMIT $1 OFFSET $2
```

**SQL for single special project:**
```sql
SELECT * FROM api_special_project_detail WHERE project_key = $1
```

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

**Scope:** DLC-specific read endpoints and the annotations CRUD lifecycle all work correctly.

#### `test_dlc.py` (15 tests)

Five DLC subsystems, each with list + detail + 404. For the detail tests, fetch the list with `?limit=1` first to get a valid key.

**MIOs** (`/api/v1/mios`):

| Test | URL | What to check |
|---|---|---|
| `test_list_mios_200` | `GET /api/v1/mios` | Status 200, non-empty list |
| `test_mio_detail` | `GET /api/v1/mios/{key}` | `organization_key` matches, `traits` is a list |
| `test_mio_detail_404` | `GET /api/v1/mios/nonexistent_mio_xyz` | Status 404 |

**Operations** (`/api/v1/operations`):

| Test | URL | What to check |
|---|---|---|
| `test_list_operations_200` | `GET /api/v1/operations` | Status 200, non-empty list (La Résistance espionage ops) |
| `test_operation_detail` | `GET /api/v1/operations/{key}` | Has `phase_groups` (list) and `equipment_requirements` (list) |
| `test_operation_detail_404` | `GET /api/v1/operations/nonexistent_op_xyz` | Status 404 |

**Balance of Power** (`/api/v1/bop`):

| Test | URL | What to check |
|---|---|---|
| `test_list_bop_200` | `GET /api/v1/bop` | Status 200, non-empty list |
| `test_bop_detail` | `GET /api/v1/bop/{key}` | Has `sides` (list) and `ranges` (list) |
| `test_bop_detail_404` | `GET /api/v1/bop/nonexistent_bop_xyz` | Status 404 |

**Factions** (`/api/v1/factions`):

| Test | URL | What to check |
|---|---|---|
| `test_list_factions_200` | `GET /api/v1/factions` | Status 200, non-empty list |
| `test_faction_detail` | `GET /api/v1/factions/{key}` | `template_key` matches, `goals` is a list, `rules` is a list |
| `test_faction_detail_404` | `GET /api/v1/factions/nonexistent_faction_xyz` | Status 404 |

**Special Projects** (`/api/v1/special-projects`):

| Test | URL | What to check |
|---|---|---|
| `test_list_special_projects_200` | `GET /api/v1/special-projects` | Status 200, non-empty list |
| `test_special_project_detail` | `GET /api/v1/special-projects/{key}` | `project_key` matches, `rewards` is a list |
| `test_special_project_detail_404` | `GET /api/v1/special-projects/nonexistent_sp_xyz` | Status 404 |

#### `test_annotations.py` (7 tests)

Annotations are the only **write** endpoint (POST + DELETE). Tests must run as a lifecycle: create → read → list → delete → verify deletion.

**Tip:** Each test that needs an annotation should create its own first (don't rely on ordering between tests). After creating, save the returned `annotation_id` — you'll need it for GET and DELETE.

| Test | Method + URL | What to check |
|---|---|---|
| `test_create_annotation` | `POST /api/v1/annotations` with `{"entity_type": "country", "entity_key": "GER", "note": "Test annotation"}` | Status 201, response has `entity_type`, `entity_key`, `note` matching input, plus server-assigned `annotation_id` (int) and `created_at` (timestamp) |
| `test_get_annotation_by_id` | Create one via POST, then `GET /api/v1/annotations/{id}` | Status 200, `annotation_id` matches, `note` matches |
| `test_list_annotations_filter` | Create one, then `GET /api/v1/annotations?entity_type=technology&entity_key=infantry_weapons` | Status 200, your created note appears in the list |
| `test_delete_annotation` | Create one, `DELETE /api/v1/annotations/{id}`, then `GET /api/v1/annotations/{id}` | DELETE returns 204, subsequent GET returns 404 |
| `test_delete_annotation_404` | `DELETE /api/v1/annotations/999999` | Status 404 (can't delete what doesn't exist) |
| `test_get_annotation_404` | `GET /api/v1/annotations/999999` | Status 404 |
| `test_create_annotation_empty_note` | `POST /api/v1/annotations` with `{"entity_type": "country", "entity_key": "GER", "note": ""}` | Status 422 — Pydantic rejects empty string. Add `min_length=1` on the `note` field in the schema |

**Run:** `pytest tests/ -v`

**Exit criteria:** All REST endpoints implemented and tested. Full Swagger docs at `/docs` show all 16 tags with correct models. Annotations CRUD works end-to-end.

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

#### `test_graphql.py` (7 tests)

All GraphQL tests send `POST /graphql` with `{"query": "..."}`. The response is `{"data": {...}}` on success, or `{"errors": [...]}` on failure. Note: GraphQL always returns HTTP 200, even for errors — check `resp.json()["errors"]` instead of `resp.status_code`.

**Key difference from REST tests:** GraphQL uses camelCase field names (`ownedStates`, `technologyKey`) because Strawberry auto-converts. Use exactly those camelCase names in your query string.

| Test | GraphQL query (abbreviated) | What to check |
|---|---|---|
| `test_country_query` | `{ country(tag: "GER") { tag stability ownedStates { stateId } } }` | `data["country"]["tag"]` == `"GER"`, `ownedStates` is a list |
| `test_country_date_1939` | `{ country(tag: "GER", date: "1939-08-14") { tag ownedStates { stateId } } }` | Returns 200 without errors — proves date parameter works through GraphQL |
| `test_characters_query` | `{ characters(countryTag: "GER") { nameKey roles { roleType traits } } }` | Non-empty list of characters. At least one character has at least one role with a non-empty `traits` list (loop through all characters and roles to find one) |
| `test_minimal_fields` | `{ countries(limit: 5) { tag } }` | Exactly 5 items. Each has only the `tag` field (proves GraphQL field selection works — only requested fields returned) |
| `test_technologies_filter` | `{ technologies(folder: "infantry_folder") { technologyKey } }` | Non-empty list — proves query filters work through GraphQL |
| `test_annotations_roundtrip` | Create an annotation via `POST /api/v1/annotations` (REST), then query via `{ annotations(entityType: "country", entityKey: "GER") { note } }` | The note you just created appears in the GraphQL results — proves REST and GraphQL share the same data |
| `test_graphql_invalid_query` | `{ nonExistentField }` | HTTP 200, but response has `"errors"` key — proves errors are handled gracefully, not 500 |

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
Phase 4  Slice C: DLC + annotations (MIOs, ops, BoP, factions, special projects, CRUD)
   │     └─ TEST GATE: DLC reads + annotation CRUD lifecycle
   │
Phase 5  GraphQL layer (types, resolvers, schema, mount)
   │     └─ TEST GATE: all queries, field selection, date params
   │
Phase 6  Polish (CORS, docs, integration smoke test)
         └─ FINAL TEST GATE: full suite + manual smoke
```

**Estimated test count:** ~78 tests across 10 test files.

**Files created:** ~30 Python files + 2 SQL changes + 3 doc updates.
