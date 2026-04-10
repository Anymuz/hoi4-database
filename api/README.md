# HOI4 Database API

REST + GraphQL API for the Hearts of Iron IV relational database.

## Stack

- **FastAPI** - REST endpoints + OpenAPI docs
- **Strawberry GraphQL** - GraphQL layer mounted at `/graphql`
- **asyncpg** - async PostgreSQL driver
- **Pydantic v2** - request/response validation
- **pytest + httpx** - async test suite

## Prerequisites

- Python 3.11+
- PostgreSQL 16 running (see root `docker-compose.yml`)
- Database loaded with schema + seed data (see `tools/db_etl/runbook.md`)

## Quick Start

```bash
bash tools/setup-api.sh    # creates venv, installs deps, copies .env, runs tests
```

Or manually:

```bash
cd api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # edit if your DB creds differ
uvicorn app.main:app --reload
```

## Utility Scripts

All scripts are in `tools/` at the repo root. Run from WSL with `bash tools/<script>`.

| Script | Purpose |
|--------|---------|
| `setup-api.sh` | Create venv, install deps, copy .env, run tests || `start-api.sh` | Start FastAPI (Uvicorn, port 8000) |
| `stop-api.sh` | Stop the FastAPI server |
| `restart-api.sh` | Restart FastAPI |
| `run-tests.sh` | Run pytest (no setup) |
| `start-db.sh` | Start (or create) the Docker PostgreSQL container |
| `stop-db.sh` | Stop the container, preserve data volume |
| `reload-db.sh` | Nuke and reload the database from scratch |

## Endpoints

| URL | Description |
|-----|-------------|
| `/health` | Health check |
| `/docs` | Swagger UI |
| `/redoc` | ReDoc |
| `/graphql` | GraphiQL IDE |
| `/api/v1/countries` | Countries (date-sensitive) |
| `/api/v1/states` | States (date-sensitive) |
| `/api/v1/technologies` | Technology tree |
| `/api/v1/characters/{id}` | Characters |
| `/api/v1/countries/{tag}/divisions` | Land OOB |
| `/api/v1/countries/{tag}/naval` | Naval OOB |
| `/api/v1/countries/{tag}/air` | Air OOB |
| `/api/v1/focus-trees` | National focus trees |
| `/api/v1/equipment` | Equipment catalog |
| `/api/v1/equipment-variants` | Equipment variants (modules, upgrades) |
| `/api/v1/ideas` | Ideas & national spirits |
| `/api/v1/mios` | Military-industrial orgs (AAT DLC) |
| `/api/v1/operations` | Espionage operations (LaR DLC) |
| `/api/v1/bop` | Balance of power (BBA DLC) |
| `/api/v1/factions` | Faction templates (DLC: Götterdämmerung) |
| `/api/v1/special-projects` | Special R&D projects (DLC: Götterdämmerung) |
| `/api/v1/annotations` | User annotations (CRUD) |

## Running Tests

```bash
cd api
pytest tests/ -v
```

105 tests across 13 test files.

## Project Structure

```
api/
├-- app/
│   ├-- main.py          # FastAPI app, lifespan, router mounts
│   ├-- config.py        # pydantic-settings config
│   ├-- database.py      # asyncpg pool + get_db dependency
│   ├-- dependencies.py  # shared deps (date validation)
│   ├-- routers/         # one file per endpoint group
│   ├-- schemas/         # Pydantic models
│   └-- graphql/         # Strawberry types, resolvers, schema
├-- tests/               # pytest suite
├-- requirements.txt
├-- .env.example
└-- README.md
```
