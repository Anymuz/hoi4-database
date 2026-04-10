# tests/test_health.py
# Phase 1 test gate: verify the API boots and core infrastructure works.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Health endpoint:
async def test_health_200(client):
    # GET /health should return 200 with {"status": "ok"}
    resp = await client.get("/health")
    assert resp.status_code == 200  # Assert that the response status code is 200 OK (successful test if true)
    assert resp.json() == {"status": "ok"} # Response body should be exactly {"status": "ok"}
# End of health endpoint test

#  OpenAPI schema:
async def test_openapi_schema(client):
    # GET /openapi.json should return 200 and include the correct app title
    resp = await client.get("/openapi.json")
    assert resp.status_code == 200  # Response status code should be 200 OK
    assert "HOI4" in resp.json()["info"]["title"]  # Response body should include "HOI4" in the title
# End of OpenAPI schema test