# HOI4 Database — API Design Document

> **Status:** FINAL — Approved for implementation.
> **Date:** 2026-03-31
> **Decisions agreed:** Hybrid REST + GraphQL, start-date in v1, Option A directory naming.

---

## 1. Overview & Rationale

A **hybrid REST + GraphQL** API serving the 149-table HOI4 database. Game data
is read-only. A single `user_annotations` table enables user-generated metadata
(Option B scalability — extend user-facing features without touching game data).
A `localisation` table (117K English translations) provides human-readable names
for game keys in API responses.

### Why Hybrid?

| Consumer | Best served by | Reason |
|----------|---------------|--------|
| Frontend country-profile viewer | REST | Predictable endpoints, easy to cache, Swagger docs |
| AI agents / LLM tool-use | GraphQL | Request only the fields needed, reduce token waste |
| Data dump / batch export | REST | Simple paginated GET, pipe to file |
| Complex cross-entity queries | GraphQL | "Give me Germany's characters with traits AND their focus tree" in one request |

Building both is ~30% more work than REST alone. If usage patterns later favour
one interface, you can sunset the other without rewriting the database layer —
both hit the same asyncpg connection pool and the same PostgreSQL
views/functions.

### Why Start Date in V1?

HOI4 has two playable bookmarks: **1936-01-01** and **1939-08-14**. The database
already stores both (history tables have `effective_date` columns, OOB files are
per-bookmark). Shipping without date selection would serve only half the data.

**Default behaviour:** if no `?date=` param is provided, the API returns
**1936-01-01** data. This is the natural default — it's the primary campaign
start, and matches what the existing views do today. The `1939` bookmark is
opt-in via `?date=1939-08-14`.

### Tech Stack

| Component | Choice | Why this one |
|-----------|--------|--------------|
| Framework | **FastAPI** | Async-native, auto-generated OpenAPI docs at `/docs`, Pydantic-based validation, first-class dependency injection. The dominant Python API framework. |
| GraphQL | **Strawberry** | Modern Python GraphQL library. Async-native, dataclass-based type definitions (no string schemas), first-class FastAPI integration via `strawberry.fastapi.GraphQLRouter`. |
| ASGI server | **Uvicorn** | Standard ASGI server for FastAPI. `--reload` for dev, `--workers N` for production. |
| DB driver | **asyncpg** | Purpose-built async PostgreSQL driver. 2-5x faster than alternatives in benchmarks. Returns native Python types, supports connection pooling, parameterised queries (`$1, $2`). |
| Config | **pydantic-settings** | Reads `.env` files and environment variables into a typed `Settings` class. No manual parsing. |
| Validation | **Pydantic v2** | Bundled with FastAPI. Response models auto-serialise and document every field in OpenAPI. |

### Deliberate Non-Choices

| Rejected | Why |
|----------|-----|
| SQLAlchemy ORM | The 14 views already encapsulate the complex JOINs. Going ORM → model → view → JSON adds indirection for zero benefit. Raw `asyncpg` queries against views are simpler, faster, and easier to debug. |
| Alembic migrations | Schema is owned by `sql/schema.sql`. The API doesn't create or alter tables — it reads them. One less tool in the chain. |
| Auth (v1) | All game data is public reference data. Annotations are open. Auth adds complexity before there's a threat model. Add it when the API goes public. |
| Redis/caching | 220K rows, read-only. PostgreSQL is more than fast enough. Add a cache layer only if profiling shows a bottleneck. |

---

## 2. Directory Layout

Standard FastAPI convention: `routers/` for endpoint logic, `schemas/` for
Pydantic response models, `graphql/` for Strawberry type definitions and
resolvers. The folder names are different enough to avoid confusion — routers
handle HTTP, schemas define data shapes, graphql defines the graph.

```
api/
├── app/
│   ├── __init__.py              # Package marker (empty file)
│   ├── main.py                  # FastAPI app, lifespan, CORS, mount GraphQL + REST
│   ├── config.py                # Settings class (DATABASE_URL, dates, pagination)
│   ├── database.py              # asyncpg pool create/teardown + get_db dependency
│   ├── routers/                 # REST endpoints — one file per domain
│   │   ├── __init__.py
│   │   ├── countries.py         # GET /countries, /countries/{tag}
│   │   ├── states.py            # GET /states, /states/{state_id}
│   │   ├── technologies.py      # GET /technologies, /countries/{tag}/technologies
│   │   ├── characters.py        # GET /characters/{id}, /countries/{tag}/characters
│   │   ├── military.py          # GET /countries/{tag}/divisions, /naval, /air
│   │   ├── focuses.py           # GET /focus-trees, /countries/{tag}/focus-tree
│   │   ├── equipment.py         # GET /equipment
│   │   ├── ideas.py             # GET /ideas
│   │   ├── dlc.py               # GET /mios, /operations, /bop
│   │   └── annotations.py       # GET/POST/DELETE /annotations
│   ├── schemas/                 # Pydantic models — shared by REST + GraphQL
│   │   ├── __init__.py
│   │   ├── country.py           # CountrySummary, CountryDetail
│   │   ├── state.py             # StateSummary, StateDetail
│   │   ├── technology.py        # TechTreeItem, CountryTech
│   │   ├── character.py         # CharacterDetail, CharacterRole
│   │   ├── military.py          # DivisionDetail, NavalDetail, AirWingItem
│   │   ├── focus.py             # FocusTreeDetail, FocusItem
│   │   ├── equipment.py         # EquipmentItem
│   │   ├── idea.py              # IdeaDetail
│   │   ├── dlc.py               # MioDetail, OperationDetail, BopDetail
│   │   └── annotation.py        # AnnotationCreate, AnnotationOut
│   └── graphql/                 # Strawberry types + resolvers
│       ├── __init__.py
│       ├── types.py             # @strawberry.type mirrors of Pydantic schemas
│       ├── resolvers.py         # Query resolver functions (call asyncpg)
│       └── schema.py            # strawberry.Schema(query=Query)
├── requirements.txt
├── .env.example
└── README.md
```

### Why not merge schemas/ and graphql/?

Pydantic models (schemas) are used by REST response validation **and** can be
referenced when building Strawberry types. Keeping them separate means REST
works without any GraphQL code loaded, and vice versa. If you ever drop one
interface, you delete one folder.

---

## 3. Configuration (`config.py`)

```python
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://hoi4:hoi4pass@localhost:5432/hoi4"
    app_title: str = "HOI4 Database API"
    app_version: str = "1.0.0"

    # Pagination
    default_page_size: int = 50
    max_page_size: int = 500

    # Game date defaults
    default_date: str = "1936-01-01"         # Primary bookmark
    allowed_dates: list[str] = [             # Whitelist — reject anything else
        "1936-01-01",
        "1939-08-14",
    ]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

**Key point:** `allowed_dates` is a whitelist. The API rejects any `?date=`
value not in this list with a 400 error. This prevents SQL injection via the
date parameter and avoids queries against non-existent history snapshots.

**How to use it:**

```python
from app.config import get_settings

settings = get_settings()         # cached singleton
print(settings.database_url)      # reads from .env or env var
print(settings.default_date)      # "1936-01-01"
```

---

## 4. Database Connection (`database.py`)

The connection pool lives on `app.state` and is created/destroyed via FastAPI's lifespan context manager. Every request borrows a connection from the pool via a dependency.

```python
import asyncpg
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from app.config import get_settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create the asyncpg pool on startup, close it on shutdown."""
    settings = get_settings()
    app.state.pool = await asyncpg.create_pool(
        settings.database_url,
        min_size=2,       # keep 2 connections warm
        max_size=10,      # scale up to 10 under load
    )
    yield
    await app.state.pool.close()

async def get_db(request: Request):
    """FastAPI dependency — yields one connection per request."""
    async with request.app.state.pool.acquire() as conn:
        yield conn
```

**How you'll use `get_db` in a router:**

```python
from fastapi import APIRouter, Depends
from app.database import get_db

router = APIRouter()

@router.get("/example")
async def example_endpoint(db = Depends(get_db)):
    rows = await db.fetch("SELECT * FROM some_view LIMIT 10")
    return [dict(r) for r in rows]
```

`asyncpg` returns `Record` objects. `dict(record)` converts them to
dictionaries that Pydantic can validate. jsonb columns come back as Python
dicts/lists automatically — no manual parsing needed.

---

## 5. Start Date Handling (V1)

### The Problem

Six views are date-sensitive — they filter history tables by `effective_date`:

| View | Date-sensitive tables |
|------|---------------------|
| `api_country_detail` | `state_ownership_history`, `country_starting_technologies` |
| `api_state_detail` | `state_ownership_history`, `state_resources`, `state_buildings`, `province_buildings` |
| `api_country_technologies` | `country_starting_technologies` |
| `api_country_divisions` | Indirectly — OOB files differ per bookmark |
| `api_country_naval` | Indirectly — OOB files differ per bookmark |
| `api_country_air` | Indirectly — OOB files differ per bookmark |

The current views hardcode `WHERE effective_date = DATE '1936-01-01'`. To
support both bookmarks, we replace these views with **PostgreSQL functions**
that accept a date parameter.

### The Solution: PostgreSQL Functions

**Before (hardcoded view):**
```sql
CREATE OR REPLACE VIEW api_country_detail AS
WITH ownership_1936 AS (
    SELECT ... FROM state_ownership_history
    WHERE effective_date = DATE '1936-01-01'    -- hardcoded!
) ...
```

**After (parameterised function):**
```sql
CREATE OR REPLACE FUNCTION api_country_detail(p_date DATE DEFAULT '1936-01-01')
RETURNS TABLE ( ... same columns ... )
LANGUAGE sql STABLE AS $$
    WITH ownership AS (
        SELECT ... FROM state_ownership_history
        WHERE effective_date <= p_date           -- parameterised!
    ) ...
$$;
```

**How the API calls it:**
```python
# In routers/countries.py
rows = await db.fetch(
    "SELECT * FROM api_country_detail($1)",
    date_param    # e.g. datetime.date(1936, 1, 1)
)
```

The `DEFAULT '1936-01-01'` in the function signature means plain
`SELECT * FROM api_country_detail()` still works in psql without arguments.

### Date Parameter Validation Helper

Every date-sensitive router needs to validate the `?date=` query parameter.
Write this once in a shared module:

```python
# app/dependencies.py
from datetime import date
from fastapi import Query, HTTPException
from app.config import get_settings

def get_effective_date(
    date_str: str | None = Query(
        None,
        alias="date",
        description="Bookmark date: 1936-01-01 (default) or 1939-08-14",
        examples=["1936-01-01", "1939-08-14"],
    ),
) -> date:
    """Validate and parse the ?date= query parameter."""
    settings = get_settings()
    raw = date_str or settings.default_date

    if raw not in settings.allowed_dates:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid date '{raw}'. Allowed: {settings.allowed_dates}",
        )
    return date.fromisoformat(raw)
```

**Usage in a router:**

```python
from fastapi import Depends
from app.dependencies import get_effective_date

@router.get("/countries/{tag}")
async def get_country(
    tag: str,
    effective_date: date = Depends(get_effective_date),
    db = Depends(get_db),
):
    row = await db.fetchrow(
        "SELECT * FROM api_country_detail($1) WHERE tag = $2",
        effective_date,
        tag.upper(),
    )
    ...
```

**The eight non-date-sensitive views** (`api_technology_tree`,
`api_country_characters`, `api_focus_tree_detail`, `api_equipment_catalog`,
`api_ideas_detail`, `api_mio_organization_detail`, `api_operation_detail`,
`api_bop_detail`) stay as plain views — no date parameter needed. Tech trees,
equipment stats, and focus trees are the same regardless of start date.

---

## 6. REST Endpoint Specification

All game data endpoints are **GET-only**. Annotations are **GET/POST/DELETE**.

### 6.1 Conventions

| Convention | Detail |
|------------|--------|
| Base path | `/api/v1` |
| Pagination | `?limit=50&offset=0` on all list endpoints |
| Date filtering | `?date=1936-01-01` (default) or `?date=1939-08-14` on date-sensitive endpoints |
| Response format | JSON, Pydantic-validated |
| Error format | `{"detail": "message"}` (FastAPI default) |
| 404 behaviour | Single-entity endpoints return 404 if not found |

### 6.2 Country & State (Slice A) — Date-Sensitive

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/countries` | `api_country_detail(date)` | List all countries (paginated) |
| GET | `/api/v1/countries/{tag}` | `api_country_detail(date)` | Full country detail |
| GET | `/api/v1/states` | `api_state_detail(date)` | List all states (paginated) |
| GET | `/api/v1/states/{state_id}` | `api_state_detail(date)` | Full state detail |

**Query params:** `?date=1936-01-01&limit=50&offset=0`, states also accept `?owner_tag=GER`

**How to implement the countries list endpoint:**

```python
# api/app/routers/countries.py
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.dependencies import get_effective_date
from app.schemas.country import CountrySummary, CountryDetail

router = APIRouter(prefix="/api/v1/countries", tags=["Countries"])

@router.get("", response_model=list[CountrySummary])
async def list_countries(
    effective_date: date = Depends(get_effective_date),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT tag, capital_state_id, stability, war_support
        FROM api_country_detail($1)
        ORDER BY tag
        LIMIT $2 OFFSET $3
        """,
        effective_date, limit, offset,
    )
    return [dict(r) for r in rows]

@router.get("/{tag}", response_model=CountryDetail)
async def get_country(
    tag: str,
    effective_date: date = Depends(get_effective_date),
    db=Depends(get_db),
):
    row = await db.fetchrow(
        "SELECT * FROM api_country_detail($1) WHERE tag = $2",
        effective_date, tag.upper(),
    )
    if not row:
        raise HTTPException(404, detail=f"Country '{tag}' not found")
    return dict(row)
```

**The Pydantic schemas:**

```python
# api/app/schemas/country.py
from pydantic import BaseModel

class OwnedState(BaseModel):
    state_id: int
    state_name_key: str
    state_name: str | None = None
    controller_tag: str | None = None

class StartingTech(BaseModel):
    technology_key: str
    technology_name: str | None = None
    dlc_source: str | None = None

class ColorRGB(BaseModel):
    r: int
    g: int
    b: int

class CountrySummary(BaseModel):
    """Used in list endpoints — lightweight."""
    tag: str
    capital_state_id: int | None = None
    stability: float | None = None
    war_support: float | None = None

class CountryDetail(BaseModel):
    """Used in detail endpoints — full data."""
    tag: str
    capital_state_id: int | None = None
    stability: float | None = None
    war_support: float | None = None
    graphical_culture: str | None = None
    graphical_culture_2d: str | None = None
    color_rgb: ColorRGB | None = None
    owned_states: list[OwnedState] = []
    starting_technologies: list[StartingTech] = []
```

**Response model fields** come directly from the view columns. `asyncpg`
returns jsonb columns as Python dicts/lists, and Pydantic validates them
against the nested models automatically.

### 6.3 Technologies (Slice B)

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/technologies` | `technologies` table | List all techs (lightweight) |
| GET | `/api/v1/technologies/{key}` | `api_technology_tree` view | Single tech (full detail) |
| GET | `/api/v1/countries/{tag}/technologies` | `api_country_technologies` view | Country starting techs |

**Query params:** `?folder=infantry&limit=50&offset=0`

The list endpoint queries the `technologies` table directly (no jsonb
subqueries), returning a lightweight `TechSummary`. The detail endpoint hits
`api_technology_tree` which runs 4 correlated jsonb subqueries — acceptable
for a single row, too expensive for 574. This mirrors the
`CountrySummary`/`CountryDetail` split in §6.2.

Country techs are date-sensitive (uses `effective_date` column in the view):
```python
rows = await db.fetch(
    """
    SELECT * FROM api_country_technologies
    WHERE country_tag = $1 AND effective_date <= $2
    ORDER BY technology_key
    """,
    tag.upper(), effective_date,
)
```

**Response models:**

`TechSummary` (list endpoint — lightweight):
```
technology_key: str
technology_name: str | None
start_year: int | None
research_cost: float | None
folder_name: str | None
```

`TechTreeItem` (detail endpoint — full, inherits TechSummary):
```
technology_key: str
technology_name: str | None
start_year: int | None
research_cost: float | None
folder_name: str | None
prerequisites: list[str]          # jsonb array from view
categories: list[str]
enables_equipment: list[str]
enables_units: list[str]
```

`StartingTech` (country techs endpoint):
```
technology_key: str
technology_name: str | None
dlc_source: str | None          # only populated here (from country_starting_technologies)
```

### 6.4 Characters (Slice B)

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/countries/{tag}/characters` | `api_country_characters` view | List characters (lightweight, no roles) |
| GET | `/api/v1/characters/{character_id}` | `api_country_characters` view | Single character (full, with roles) |

Not date-sensitive — characters don't change between bookmarks.

**SQL Queries:**

List characters for a country (paginated, lightweight — omit roles):
```sql
SELECT character_id, name_key, country_tag, gender
FROM api_country_characters
WHERE country_tag = $1
ORDER BY character_id
LIMIT $2 OFFSET $3
```

Single character by ID (full, with roles):
```sql
SELECT character_id, name_key, country_tag, gender, roles
FROM api_country_characters
WHERE character_id = $1
```

**Response model (`CharacterSummary` — for the list endpoint):**
```
character_id: str
name_key: str
country_tag: str
gender: str | None
```

**Response model (`CharacterDetail` — for the detail endpoint):**
```
character_id: str
name_key: str
country_tag: str
gender: str | None
roles: list[CharacterRole]        # nested jsonb from view

# Where CharacterRole is:
role_type: str
sub_ideology_key: str | None
skill: int | None
attack_skill: int | None
defense_skill: int | None
planning_skill: int | None
logistics_skill: int | None
maneuvering_skill: int | None
coordination_skill: int | None
dlc_source: str | None
traits: list[str]
```

### 6.5 Military — Land / Naval / Air (Slice B) — Date-Sensitive

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/countries/{tag}/divisions` | `api_country_divisions` | Division templates + deployed units |
| GET | `/api/v1/countries/{tag}/naval` | `api_country_naval` | Fleets, task forces, ships |
| GET | `/api/v1/countries/{tag}/air` | `api_country_air` | Air wings |

Date-sensitive indirectly — the OOB data in the database has an `oob_file`
column (e.g. `GER_1936.txt` vs `GER_1939.txt`). Filter by matching the
oob_file suffix to the requested date:

```python
# Determine which OOB file suffix matches the requested date
oob_suffix = "1936" if effective_date.year == 1936 else "1939"
```

**SQL Queries:**

Divisions for a country (date-filtered via OOB file):
```sql
SELECT country_tag, division_template_id, template_name, oob_file,
       regiments, support, deployed_divisions
FROM api_country_divisions
WHERE country_tag = $1
  AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
ORDER BY template_name
```
- `$1` = country tag (e.g. `'GER'`)
- `$2` = OOB year suffix (e.g. `'1936'` or `'1939'`)

Naval forces for a country (date-filtered via OOB file):
```sql
SELECT country_tag, fleet_id, fleet_name, naval_base_province_id, oob_file,
       task_forces
FROM api_country_naval
WHERE country_tag = $1
  AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
ORDER BY fleet_name
```

Air wings for a country (date-filtered via OOB file):
```sql
SELECT country_tag, location_state_id, state_name_key,
       equipment_type, amount, wing_name, version_name, oob_file
FROM api_country_air
WHERE country_tag = $1
  AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
ORDER BY location_state_id
```

**Division response model:**
```
country_tag: str
division_template_id: int
template_name: str
oob_file: str | None
regiments: list[Regiment]           # [{unit_type_key, grid_x, grid_y}]
support: list[SupportCompany]       # [{unit_type_key, grid_x, grid_y}]
deployed_divisions: list[Deployed]  # [{location_province_id, start_experience_factor}]
```

**Naval response model (`NavalDetail`):**
```
country_tag: str
fleet_id: int
fleet_name: str
naval_base_province_id: int | None
oob_file: str | None
task_forces: list[TaskForce]

# Where TaskForce is:
task_force_id: int
task_force_name: str
location_province_id: int | None
ships: list[Ship]

# Where Ship is:
ship_name: str
definition: str
hull_equipment_key: str
version_name: str | None
pride_of_the_fleet: bool | None
```

**Air response model (`AirWingItem`):**
```
country_tag: str
location_state_id: int
state_name_key: str
equipment_type: str
amount: int
wing_name: str | None
version_name: str | None
oob_file: str | None
```

### 6.6 Focus Trees (Slice B)

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/focus-trees` | `api_focus_tree_detail` view | List all trees |
| GET | `/api/v1/focus-trees/{focus_tree_id}` | `api_focus_tree_detail` view | Single tree + focuses |
| GET | `/api/v1/countries/{tag}/focus-tree` | `api_focus_tree_detail` view | Tree for a country |

Not date-sensitive. Focus trees are static.

**SQL Queries:**

List all focus trees (paginated, lightweight — omit the focuses array):
```sql
SELECT focus_tree_id, country_tag
FROM api_focus_tree_detail
ORDER BY focus_tree_id
LIMIT $1 OFFSET $2
```

Single focus tree with all focuses:
```sql
SELECT focus_tree_id, country_tag, focuses
FROM api_focus_tree_detail
WHERE focus_tree_id = $1
```

Focus tree for a country:
```sql
SELECT focus_tree_id, country_tag, focuses
FROM api_focus_tree_detail
WHERE country_tag = $1
```

**Response model (`FocusTreeSummary` — for the list endpoint):**
```
focus_tree_id: str
country_tag: str | None
```

**Response model (`FocusTreeDetail` — for single tree / country endpoints):**
```
focus_tree_id: str
country_tag: str | None
focuses: list[FocusItem]

# Where FocusItem is:
focus_id: str
cost: float | None
x_pos: int | None
y_pos: int | None
icon: str | None
dlc_source: str | None
prerequisites: list[FocusPrereq]        # [{group, required_focus_id}]
mutually_exclusive: list[str]            # [focus_id, ...]
```

### 6.7 Equipment Catalog (Slice B)

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/equipment` | `api_equipment_catalog` view | All equipment |
| GET | `/api/v1/equipment/{equipment_key}` | `api_equipment_catalog` view | Single item |

**Query params:** `?archetype=infantry_equipment&is_archetype=true`

Not date-sensitive. Equipment definitions don't change between bookmarks.

**SQL Queries:**

List all equipment (paginated):
```sql
SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
       build_cost_ic, reliability, maximum_speed, defense, breakthrough,
       soft_attack, hard_attack, ap_attack, air_attack, armor_value,
       hardness, dlc_source, resources
FROM api_equipment_catalog
ORDER BY equipment_key
LIMIT $1 OFFSET $2
```

Filter by archetype:
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

Filter by is_archetype flag:
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

Single equipment item:
```sql
SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
       build_cost_ic, reliability, maximum_speed, defense, breakthrough,
       soft_attack, hard_attack, ap_attack, air_attack, armor_value,
       hardness, dlc_source, resources
FROM api_equipment_catalog
WHERE equipment_key = $1
```

**Response model (`EquipmentItem`):**
```
equipment_key: str
is_archetype: bool
archetype_key: str | None
parent_key: str | None
year: int | None
build_cost_ic: float | None
reliability: float | None
maximum_speed: float | None
defense: float | None
breakthrough: float | None
soft_attack: float | None
hard_attack: float | None
ap_attack: float | None
air_attack: float | None
armor_value: float | None
hardness: float | None
dlc_source: str | None
resources: list[EquipmentResource]   # [{resource_key, amount}]
```

### 6.8 Ideas & National Spirits (Slice B)

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/ideas` | `api_ideas_detail` view | All ideas |
| GET | `/api/v1/ideas/{idea_key}` | `api_ideas_detail` view | Single idea |

**Query params:** `?slot=economy&is_law=true`

Not date-sensitive. Ideas and laws are static definitions.

**SQL Queries:**

List all ideas (paginated):
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
ORDER BY idea_key
LIMIT $1 OFFSET $2
```

Filter by slot:
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
WHERE slot = $1
ORDER BY idea_key
LIMIT $2 OFFSET $3
```

Filter by is_law:
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
WHERE is_law = $1
ORDER BY idea_key
LIMIT $2 OFFSET $3
```

Single idea:
```sql
SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
       dlc_source, modifiers
FROM api_ideas_detail
WHERE idea_key = $1
```

**Response model (`IdeaDetail`):**
```
idea_key: str
slot: str | None
is_law: bool
cost: float | None
removal_cost: float | None
is_default: bool
dlc_source: str | None
modifiers: list[IdeaModifier]      # [{modifier_key, modifier_value}]
```

### 6.9 DLC Systems (Slice C)

| Method | Path | SQL Source | Description |
|--------|------|------------|-------------|
| GET | `/api/v1/mios` | `api_mio_organization_detail` view | MIO organisations |
| GET | `/api/v1/mios/{organization_key}` | `api_mio_organization_detail` view | Single MIO |
| GET | `/api/v1/operations` | `api_operation_detail` view | Espionage operations |
| GET | `/api/v1/operations/{operation_key}` | `api_operation_detail` view | Single operation |
| GET | `/api/v1/bop` | `api_bop_detail` view | Balance of Power definitions |
| GET | `/api/v1/bop/{bop_key}` | `api_bop_detail` view | Single BOP |
| GET | `/api/v1/factions` | `api_faction_detail` view | Faction templates (DLC: Götterdämmerung) |
| GET | `/api/v1/factions/{template_key}` | `api_faction_detail` view | Single faction template with goals & rules |
| GET | `/api/v1/special-projects` | `api_special_project_detail` view | Special projects (DLC: Götterdämmerung) |
| GET | `/api/v1/special-projects/{project_key}` | `api_special_project_detail` view | Single project with rewards |

None are date-sensitive.

**Faction response model (`FactionDetail`):**
```
template_key: str
name_loc: str | None
manifest_key: str | None
icon: str | None
can_leader_join_other: bool | None
dlc_source: str | None
goals: list[FactionGoal]              # [{goal_key, name_loc, category, goal_group}]
rules: list[FactionRule]               # [{rule_key, rule_type, rule_group_key}]
member_upgrade_groups: list[UpgradeGroup]  # [{group_key, name_loc, upgrades: [{upgrade_key, bonus}]}]
```

**Special project response model (`SpecialProjectDetail`):**
```
project_key: str
specialization_key: str
project_tag: str | None
complexity: str | None
prototype_time: str | None
dlc_source: str | None
rewards: list[ProjectReward]           # [{reward_key, fire_only_once, threshold_min, threshold_max}]
```

### 6.10 Annotations (User Data — Read/Write)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/annotations` | List annotations |
| GET | `/api/v1/annotations/{id}` | Single annotation |
| POST | `/api/v1/annotations` | Create annotation |
| DELETE | `/api/v1/annotations/{id}` | Delete annotation |

**Query params for list:** `?entity_type=country&entity_key=GER&limit=50&offset=0`

**Pydantic schemas:**

```python
# api/app/schemas/annotation.py
from datetime import datetime
from pydantic import BaseModel, Field

class AnnotationCreate(BaseModel):
    """Request body for POST /annotations."""
    entity_type: str = Field(..., max_length=50, examples=["country"])
    entity_key: str = Field(..., max_length=200, examples=["GER"])
    note: str = Field(..., min_length=1, examples=["Good for beginners"])

class AnnotationOut(BaseModel):
    """Response model for annotation endpoints."""
    annotation_id: int
    entity_type: str
    entity_key: str
    note: str
    created_at: datetime
```

**How to implement:**

```python
# api/app/routers/annotations.py
@router.post("", response_model=AnnotationOut, status_code=201)
async def create_annotation(body: AnnotationCreate, db=Depends(get_db)):
    row = await db.fetchrow(
        """
        INSERT INTO user_annotations (entity_type, entity_key, note)
        VALUES ($1, $2, $3)
        RETURNING annotation_id, entity_type, entity_key, note, created_at
        """,
        body.entity_type, body.entity_key, body.note,
    )
    return dict(row)

@router.delete("/{annotation_id}", status_code=204)
async def delete_annotation(annotation_id: int, db=Depends(get_db)):
    result = await db.execute(
        "DELETE FROM user_annotations WHERE annotation_id = $1",
        annotation_id,
    )
    if result == "DELETE 0":
        raise HTTPException(404, detail="Annotation not found")
```

**DDL (added to schema.sql):**
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

---

## 7. GraphQL Layer (Strawberry)

### Why Strawberry?

Strawberry uses Python dataclasses with decorators — no schema-definition
language (SDL) strings, no separate `.graphql` files. Types are Python code,
checked by your IDE and type-checker. It integrates with FastAPI via
`GraphQLRouter` and shares the same asyncpg pool.

### Mounting on FastAPI

```python
# api/app/main.py (relevant excerpt)
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema

graphql_app = GraphQLRouter(schema)

app = FastAPI(title=settings.app_title, lifespan=lifespan)
app.include_router(graphql_app, prefix="/graphql")
# ... include REST routers ...
```

After this, GraphQL is available at:
- **`/graphql`** — GraphQL endpoint (POST queries here)
- **`/graphql`** in browser — GraphiQL IDE (interactive explorer, like Swagger for GraphQL)

### Defining Types

Strawberry types mirror the Pydantic schemas but use `@strawberry.type`:

```python
# api/app/graphql/types.py
import strawberry
from typing import Optional

@strawberry.type
class OwnedState:
    state_id: int
    state_name_key: str
    state_name: Optional[str] = None
    controller_tag: Optional[str] = None

@strawberry.type
class StartingTech:
    technology_key: str
    technology_name: Optional[str] = None
    dlc_source: Optional[str] = None

@strawberry.type
class Country:
    tag: str
    capital_state_id: Optional[int] = None
    stability: Optional[float] = None
    war_support: Optional[float] = None
    graphical_culture: Optional[str] = None
    graphical_culture_2d: Optional[str] = None
    owned_states: list[OwnedState]
    starting_technologies: list[StartingTech]

@strawberry.type
class CharacterRole:
    role_type: str
    sub_ideology_key: Optional[str] = None
    skill: Optional[int] = None
    attack_skill: Optional[int] = None
    defense_skill: Optional[int] = None
    traits: list[str]

@strawberry.type
class Character:
    character_id: str
    name_key: str
    country_tag: str
    gender: Optional[str] = None
    roles: list[CharacterRole]
```

**Pattern:** one `@strawberry.type` per entity. Fields match the view columns.
Nested jsonb arrays map to `list[NestedType]`.

### Writing Resolvers

Resolvers are async functions that fetch data from the database. Use
`strawberry.types.Info` to access the FastAPI request (and thus the pool):

```python
# api/app/graphql/resolvers.py
import strawberry
from datetime import date
from typing import Optional
from strawberry.types import Info
from app.graphql.types import Country, Character

async def get_pool(info: Info):
    """Extract the asyncpg pool from the FastAPI app state."""
    return info.context["request"].app.state.pool

@strawberry.type
class Query:
    @strawberry.field
    async def country(
        self,
        info: Info,
        tag: str,
        date: Optional[str] = "1936-01-01",
    ) -> Optional[Country]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM api_country_detail($1) WHERE tag = $2",
                date_obj, tag.upper(),
            )
            if not row:
                return None
            return Country(**dict(row))

    @strawberry.field
    async def countries(
        self,
        info: Info,
        date: Optional[str] = "1936-01-01",
        limit: int = 50,
        offset: int = 0,
    ) -> list[Country]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """SELECT * FROM api_country_detail($1)
                   ORDER BY tag LIMIT $2 OFFSET $3""",
                date_obj, limit, offset,
            )
            return [Country(**dict(r)) for r in rows]

    @strawberry.field
    async def characters(
        self,
        info: Info,
        country_tag: Optional[str] = None,
    ) -> list[Character]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if country_tag:
                rows = await conn.fetch(
                    "SELECT * FROM api_country_characters WHERE country_tag = $1",
                    country_tag.upper(),
                )
            else:
                rows = await conn.fetch("SELECT * FROM api_country_characters")
            return [Character(**dict(r)) for r in rows]
```

### Building the Schema

```python
# api/app/graphql/schema.py
import strawberry
from app.graphql.resolvers import Query

schema = strawberry.Schema(query=Query)
```

That's it. One line. Strawberry introspects the `Query` class and builds the
full GraphQL schema from the type annotations.

### Example GraphQL Queries

**Get Germany with only the fields you need:**
```graphql
query {
  country(tag: "GER", date: "1936-01-01") {
    tag
    stability
    warSupport
    ownedStates {
      stateId
      stateNameKey
    }
  }
}
```

Note: Strawberry auto-converts Python `snake_case` to GraphQL `camelCase`.

**Get all characters for a country with their traits:**
```graphql
query {
  characters(countryTag: "GER") {
    characterId
    nameKey
    roles {
      roleType
      skill
      traits
    }
  }
}
```

**An AI agent requesting minimal data:**
```graphql
query {
  countries(date: "1939-08-14", limit: 200) {
    tag
    stability
  }
}
```

This returns just 2 fields per country — no nested states, no technologies,
no wasted tokens.

---

## 8. OpenAPI Tags & Metadata

```python
tags_metadata = [
    {"name": "Countries",        "description": "Country tags, starting stats, owned states, technologies"},
    {"name": "States",           "description": "States, buildings, resources, provinces"},
    {"name": "Technologies",     "description": "Tech trees, prerequisites, unlocks"},
    {"name": "Characters",       "description": "Leaders, generals, admirals, advisors, traits"},
    {"name": "Land Forces",      "description": "Division templates, regiments, deployed divisions"},
    {"name": "Naval Forces",     "description": "Fleets, task forces, ships"},
    {"name": "Air Forces",       "description": "Air wings"},
    {"name": "Focus Trees",      "description": "National focus trees, prerequisites, mutual exclusions"},
    {"name": "Equipment",        "description": "Equipment definitions, stats, resource costs"},
    {"name": "Ideas",            "description": "Ideas, national spirits, laws, modifiers"},
    {"name": "MIOs",             "description": "Military-Industrial Organizations (DLC: Arms Against Tyranny)"},
    {"name": "Operations",       "description": "Espionage operations (DLC: La Résistance)"},
    {"name": "Balance of Power", "description": "Balance of power mechanics (DLC: various)"},
    {"name": "Factions",         "description": "AI faction templates, goals, rules (DLC: Götterdämmerung)"},
    {"name": "Special Projects", "description": "Special projects: nuclear, rocket, science (DLC: Götterdämmerung)"},
    {"name": "Annotations",      "description": "User-created notes on game entities"},
]
```

Available at:
- **`/docs`** — Swagger UI (interactive REST explorer)
- **`/redoc`** — ReDoc (readable API reference)
- **`/graphql`** — GraphiQL (interactive GraphQL explorer)

---

## 9. CORS

Open for v1 — any frontend or AI agent can call both REST and GraphQL:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)
```

Lock down `allow_origins` to specific domains if/when the API goes public.

---

## 10. Assembling `main.py`

This is where everything comes together. Here's the full file structure:

```python
# api/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from app.config import get_settings
from app.database import lifespan
from app.graphql.schema import schema
from app.routers import (
    countries, states, technologies, characters,
    military, focuses, equipment, ideas, dlc, annotations,
)

settings = get_settings()

app = FastAPI(
    title=settings.app_title,
    version=settings.app_version,
    lifespan=lifespan,
    openapi_tags=tags_metadata,       # from section 8
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)

# GraphQL
app.include_router(GraphQLRouter(schema), prefix="/graphql")

# REST routers
app.include_router(countries.router)
app.include_router(states.router)
app.include_router(technologies.router)
app.include_router(characters.router)
app.include_router(military.router)
app.include_router(focuses.router)
app.include_router(equipment.router)
app.include_router(ideas.router)
app.include_router(dlc.router)
app.include_router(annotations.router)
```

---

## 11. Startup & Run

```bash
# 1. Set up the virtual environment
cd api
python -m venv .venv
.venv\Scripts\activate              # Windows
# source .venv/bin/activate         # Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure database URL
cp .env.example .env
# Edit .env if your PostgreSQL isn't at localhost:5432/hoi4

# 4. Run in development (auto-reload on file changes)
uvicorn app.main:app --reload --port 8000

# 5. Open in browser
#    REST Swagger:  http://localhost:8000/docs
#    GraphiQL:      http://localhost:8000/graphql
```

**Production:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 12. requirements.txt

```
fastapi>=0.115,<1.0
uvicorn[standard]>=0.30,<1.0
asyncpg>=0.30,<1.0
pydantic-settings>=2.0,<3.0
strawberry-graphql[fastapi]>=0.250,<1.0
```

Five packages. No ORM, no migration tool, no cache layer.

---

## 13. SQL Changes Required

Before the API can run, the database needs two changes:

### 13a. Convert Date-Sensitive Views to Functions

Six views need to become functions. The pattern for each:

```sql
-- Drop the old view
DROP VIEW IF EXISTS api_country_detail;

-- Create the function with the same output columns
CREATE OR REPLACE FUNCTION api_country_detail(p_date DATE DEFAULT '1936-01-01')
RETURNS TABLE (
    tag              CHAR(3),
    capital_state_id INTEGER,
    stability        NUMERIC,
    war_support      NUMERIC,
    graphical_culture     VARCHAR,
    graphical_culture_2d  VARCHAR,
    color_rgb             JSONB,
    owned_states          JSONB,
    starting_technologies JSONB
)
LANGUAGE sql STABLE
AS $$
    -- Same query as the old view, but replace
    -- DATE '1936-01-01' with p_date everywhere
    WITH ownership AS (
        SELECT soh.state_id, soh.owner_tag,
               COALESCE(soh.controller_tag, soh.owner_tag) AS controller_tag
        FROM state_ownership_history soh
        WHERE soh.effective_date = p_date
    ),
    tech AS (
        SELECT cst.country_tag, cst.technology_key, cst.dlc_source
        FROM country_starting_technologies cst
        WHERE cst.effective_date = p_date
    )
    SELECT ... ;  -- rest of the original query unchanged
$$;
```

**Do this for all six date-sensitive views:**
1. `api_country_detail`
2. `api_state_detail`
3. `api_country_technologies` (filter on `effective_date <= p_date`)
4. `api_country_divisions` (filter on `oob_file` suffix)
5. `api_country_naval` (filter on `oob_file` suffix)
6. `api_country_air` (filter on `oob_file` suffix)

The eight non-date-sensitive views stay as views unchanged.

### 13b. Add Annotations Table

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

### 13c. Add Localisation Table & Join to Functions

The `localisation` table stores 117,490 English display names extracted from
HOI4's `localisation/english/*_l_english.yml` files. API functions LEFT JOIN
to it so responses include human-readable names alongside raw game keys.

```sql
CREATE TABLE localisation (
    loc_key    VARCHAR(250) PRIMARY KEY,
    loc_value  TEXT         NOT NULL,
    source_file TEXT
);
```

**How it's used in functions:**

`api_country_detail` builds jsonb objects for `owned_states` and
`starting_technologies` that now include `state_name` and `technology_name`
via `LEFT JOIN localisation` + `COALESCE(loc_value, raw_key)`.

`api_state_detail` returns a `state_name TEXT` column via the same pattern.

Coverage: 96% of states, 72% of technologies. COALESCE fallback means the raw
key is returned when no translation exists — nothing breaks.

---

## 14. Implementation Order

| Step | What to build | Files to create/edit | Proves |
|------|--------------|---------------------|--------|
| 1 | **PostgreSQL setup** — load schema, seed data | Run `schema.sql`, `seed-load-order.sql`, `views.sql` | Database works |
| 2 | **Convert 6 views → functions** | Edit `sql/views.sql` | Date parameter works in psql |
| 3 | **Add `user_annotations` table** | Edit `sql/schema.sql` | Annotations table exists |
| 4 | **Scaffold API directory** — config, database, main | `api/app/__init__.py`, `config.py`, `database.py`, `main.py`, `requirements.txt`, `.env.example` | `uvicorn app.main:app` starts without errors |
| 5 | **Countries router + schemas** | `routers/countries.py`, `schemas/country.py` | Full REST stack works end-to-end with date param |
| 6 | **GraphQL types + resolvers + schema for countries** | `graphql/types.py`, `resolvers.py`, `schema.py` | GraphQL works end-to-end at `/graphql` |
| 7 | **States router** | `routers/states.py`, `schemas/state.py` | Second date-sensitive endpoint |
| 8 | **Technologies router** | `routers/technologies.py`, `schemas/technology.py` | Mixed: tech tree (view) + country techs (date) |
| 9 | **Characters router** | `routers/characters.py`, `schemas/character.py` | Non-date-sensitive endpoint |
| 10 | **Military routers** | `routers/military.py`, `schemas/military.py` | OOB file suffix filtering |
| 11 | **Focus trees, equipment, ideas routers** | 3 router files + 3 schema files | Batch of simple view-backed endpoints |
| 12 | **DLC routers** | `routers/dlc.py`, `schemas/dlc.py` | MIOs, operations, BOP, factions, special projects |
| 13 | **Annotations router** | `routers/annotations.py`, `schemas/annotation.py` | POST/DELETE (first write endpoint) |
| 14 | **Expand GraphQL** — add remaining types/resolvers | `graphql/types.py`, `graphql/resolvers.py` | Full GraphQL coverage |
| 15 | **README + .env.example + OpenAPI polish** | `api/README.md` | Documentation |

**Tip:** Steps 5-6 are the critical ones. Once countries work via both REST and
GraphQL with the date parameter, every subsequent router follows the same
pattern — you'll be copy-pasting and adjusting field names.

---

## 15. Future Considerations (not in v1)

| Feature | When | Notes |
|---------|------|-------|
| **Auth** | When API goes public | API keys or OAuth2 for annotations; game data stays open |
| **Rate limiting** | When API goes public | `slowapi` or reverse proxy |
| **Full-text search** | v2 | `?q=panzer` across entities; PostgreSQL `tsvector` |
| **Docker Compose** | v2 | API + PostgreSQL in one `docker-compose.yml` |
| **Scripted collections endpoint** | v2 | `scripted_collections` table — internal engine plumbing, low consumer value |
| **AI faction theaters endpoint** | v2 | `ai_faction_theaters` + `ai_faction_theater_regions` — AI behavior tuning, niche |
| **Timed activities endpoint** | v2 | `timed_activities` + `timed_activity_modifiers` — only 1 entry currently |
| **WebSocket** | Unlikely | No real-time use case for static game data |
| **GraphQL subscriptions** | Unlikely | Same reason — data doesn't change at runtime |
