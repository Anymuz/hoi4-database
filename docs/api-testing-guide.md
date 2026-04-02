# HOI4 Database — API Testing Guide

> Quick-reference for writing and running tests against the FastAPI API.
> Uses **pytest** + **httpx** (async test client) against the real Docker database.

---

## Setup

```bash
cd /mnt/c/Users/joshu/hoi4-database/api
pip install -r requirements.txt      # installs pytest, httpx, etc.
```

Make sure the Docker database is running:

```bash
docker start hoi4-db
```

---

## Running Tests

```bash
pytest tests/ -v              # all tests, verbose
pytest tests/test_health.py   # one file only
pytest tests/ -k "country"    # only tests with "country" in the name
pytest tests/ -x              # stop on first failure
```

---

## Project Structure

```
api/
├── app/                      # the actual API code
│   ├── main.py
│   └── ...
└── tests/
    ├── conftest.py           # shared setup (runs once, reused by all tests)
    ├── test_health.py
    ├── test_countries.py
    └── ...
```

---

## conftest.py — Shared Setup

This file creates a test HTTP client that talks directly to the FastAPI app
without needing to start a server. Every test function that has `client` as
a parameter automatically receives this client.

```python
# tests/conftest.py
import asyncio
import pytest
import asyncpg
import httpx
from httpx import ASGITransport

from app.main import app
from app.database import get_db


@pytest.fixture(scope="session")
def event_loop():
    """One event loop for the whole test session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def pool():
    """Real database connection pool — tests run against actual data."""
    p = await asyncpg.create_pool(
        "postgresql://hoi4:hoi4pass@localhost:5432/hoi4"
    )
    yield p
    await p.close()


@pytest.fixture(scope="session")
async def client(pool):
    """Async HTTP client wired to the FastAPI app."""

    async def _override_get_db():
        async with pool.acquire() as conn:
            yield conn

    app.dependency_overrides[get_db] = _override_get_db

    transport = ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        yield c

    app.dependency_overrides.clear()
```

**What this does:**
- `pool` — opens a connection to the Docker database once, shares it across all tests
- `client` — creates a fake HTTP client that calls the API in-process (no server needed)
- `_override_get_db` — swaps the API's normal database connection for the test one

---

## Writing Tests — The Pattern

Every test is just a Python function that starts with `test_`. It receives
the `client` fixture and makes HTTP requests. Use `assert` to check results.

### Example 1: Simple Health Check

```python
# tests/test_health.py
import pytest

@pytest.mark.asyncio
async def test_health_returns_ok(client):
    response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

### Example 2: List Endpoint with Count

```python
# tests/test_countries.py
import pytest

@pytest.mark.asyncio
async def test_list_countries(client):
    response = await client.get("/api/v1/countries", params={"limit": 500})

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 400  # we have ~428 countries in the DB
```

### Example 3: Detail Endpoint — Check Specific Fields

```python
@pytest.mark.asyncio
async def test_get_germany(client):
    response = await client.get("/api/v1/countries/GER")

    assert response.status_code == 200
    germany = response.json()
    assert germany["tag"] == "GER"
    assert "owned_states" in germany         # has the nested array
    assert "starting_technologies" in germany
    assert germany["stability"] is not None
```

### Example 4: 404 for Missing Entity

```python
@pytest.mark.asyncio
async def test_country_not_found(client):
    response = await client.get("/api/v1/countries/ZZZ")

    assert response.status_code == 404
```

### Example 5: Query Parameter Filtering

```python
@pytest.mark.asyncio
async def test_states_filter_by_owner(client):
    response = await client.get("/api/v1/states", params={"owner_tag": "GER"})

    assert response.status_code == 200
    states = response.json()
    assert len(states) > 0
    # every returned state should belong to Germany
    for state in states:
        assert state["owner_tag"] == "GER"
```

### Example 6: Date Parameter (1936 vs 1939)

```python
@pytest.mark.asyncio
async def test_country_date_changes_data(client):
    r1936 = await client.get("/api/v1/countries/GER", params={"date": "1936-01-01"})
    r1939 = await client.get("/api/v1/countries/GER", params={"date": "1939-08-14"})

    assert r1936.status_code == 200
    assert r1939.status_code == 200
    # Germany should own different states in 1939 (annexed Austria, Czechia, etc.)
    states_1936 = r1936.json()["owned_states"]
    states_1939 = r1939.json()["owned_states"]
    assert states_1936 != states_1939
```

### Example 7: Invalid Date Returns 400

```python
@pytest.mark.asyncio
async def test_invalid_date_rejected(client):
    response = await client.get("/api/v1/countries/GER", params={"date": "2000-01-01"})

    assert response.status_code == 400
```

### Example 8: Pagination

```python
@pytest.mark.asyncio
async def test_pagination(client):
    page1 = await client.get("/api/v1/equipment", params={"limit": 10, "offset": 0})
    page2 = await client.get("/api/v1/equipment", params={"limit": 10, "offset": 10})

    assert page1.status_code == 200
    assert page2.status_code == 200
    # pages should have different items
    keys1 = {item["equipment_key"] for item in page1.json()}
    keys2 = {item["equipment_key"] for item in page2.json()}
    assert keys1.isdisjoint(keys2)  # no overlap
```

### Example 9: POST + DELETE (Annotations CRUD)

```python
@pytest.mark.asyncio
async def test_annotation_lifecycle(client):
    # Create
    payload = {"entity_type": "country", "entity_key": "GER", "note": "Test note"}
    create_resp = await client.post("/api/v1/annotations", json=payload)
    assert create_resp.status_code == 201
    annotation_id = create_resp.json()["annotation_id"]

    # Read it back
    get_resp = await client.get(f"/api/v1/annotations/{annotation_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["note"] == "Test note"

    # Delete it
    del_resp = await client.delete(f"/api/v1/annotations/{annotation_id}")
    assert del_resp.status_code == 204

    # Confirm it's gone
    gone_resp = await client.get(f"/api/v1/annotations/{annotation_id}")
    assert gone_resp.status_code == 404
```

### Example 10: GraphQL Query

```python
@pytest.mark.asyncio
async def test_graphql_country(client):
    query = """
    {
        country(tag: "GER") {
            tag
            stability
            ownedStates { stateId }
        }
    }
    """
    response = await client.post("/graphql", json={"query": query})

    assert response.status_code == 200
    data = response.json()["data"]["country"]
    assert data["tag"] == "GER"
    assert len(data["ownedStates"]) > 0
```

---

## Reading Test Output

When you run `pytest tests/ -v`, you'll see something like:

```
tests/test_health.py::test_health_returns_ok PASSED
tests/test_countries.py::test_list_countries PASSED
tests/test_countries.py::test_get_germany PASSED
tests/test_countries.py::test_country_not_found PASSED
tests/test_countries.py::test_invalid_date_rejected PASSED

5 passed in 1.8s
```

If something fails:

```
tests/test_countries.py::test_get_germany FAILED

    assert germany["stability"] == 0.5
E   AssertionError: assert 0.6 == 0.5

FAILED tests/test_countries.py::test_get_germany - AssertionError
1 failed, 4 passed in 1.6s
```

pytest tells you **which line** failed, **what the actual value was**, and **what you expected**. Fix the code (or the test) and re-run.

---

## Quick Reference

| What you want | How to write it |
|---|---|
| Check status code | `assert response.status_code == 200` |
| Check JSON body | `assert response.json()["key"] == "value"` |
| Check list length | `assert len(response.json()) >= 10` |
| Check field exists | `assert "field_name" in response.json()` |
| Check field is not null | `assert response.json()["field"] is not None` |
| Check every item in list | `for item in data: assert item["x"] == "y"` |
| Check two responses differ | `assert resp1.json() != resp2.json()` |
| Send query params | `client.get("/path", params={"key": "val"})` |
| Send JSON body (POST) | `client.post("/path", json={"key": "val"})` |
| Send GraphQL query | `client.post("/graphql", json={"query": "{ ... }"})` |
