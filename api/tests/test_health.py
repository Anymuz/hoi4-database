# tests/test_health.py
# Phase 1 test gate: verify the API boots and core infrastructure works.

import pytest

# Mark every test in this file as async — pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio

# --- Health endpoint ---
async def test_health_200(client):
    """GET /health should return 200 with {"status": "ok"}."""
    resp = await client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

# --- OpenAPI schema ---
async def test_openapi_schema(client):
    # GET /openapi.json should return 200 and include the correct app title.
    resp = await client.get("/openapi.json")
    assert resp.status_code == 200
    assert "HOI4" in resp.json()["info"]["title"]