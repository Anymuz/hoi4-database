# HOI4 Database API

REST + GraphQL API for the Hearts of Iron IV relational database.

## Stack

- **FastAPI** — REST endpoints + OpenAPI docs
- **Strawberry GraphQL** — GraphQL layer mounted at `/graphql`
- **asyncpg** — async PostgreSQL driver
- **Pydantic v2** — request/response validation
- **pytest + httpx** — async test suite

## Prerequisites

- Python 3.11+
- PostgreSQL 16 running (see root `docker-compose.yml`)
- Database loaded with schema + seed data (see `tools/db_etl/runbook.md`)

## Quick Start

```bash
cd api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # edit if your DB creds differ
uvicorn app.main:app --reload
```

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
| `/api/v1/ideas` | Ideas & national spirits |
| `/api/v1/mios` | Military-industrial orgs (AAT DLC) |
| `/api/v1/operations` | Espionage operations (LaR DLC) |
| `/api/v1/bop` | Balance of power (BBA DLC) |
| `/api/v1/annotations` | User annotations (CRUD) |

## Date Filtering

Country and state endpoints accept `?date=` with two valid values:

- `1936-01-01` (default) — pre-war start
- `1939-08-14` — late start

## Running Tests

```bash
cd api
pytest tests/ -v
```

## Project Structure

```
api/
├── app/
│   ├── main.py          # FastAPI app, lifespan, router mounts
│   ├── config.py        # pydantic-settings config
│   ├── database.py      # asyncpg pool + get_db dependency
│   ├── dependencies.py  # shared deps (date validation)
│   ├── routers/         # one file per endpoint group
│   ├── schemas/         # Pydantic models
│   └── graphql/         # Strawberry types, resolvers, schema
├── tests/               # pytest suite
├── requirements.txt
├── .env.example
└── README.md
```
