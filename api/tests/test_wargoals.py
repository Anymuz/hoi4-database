# api/tests/test_wargoals.py
# Phase 7 tests: verify wargoal list and detail endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Wargoal list tests:
async def test_list_wargoals_200(client):
    resp = await client.get("/api/v1/wargoals")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
# End of wargoal list 200 test

# Wargoal detail tests:
async def test_wargoal_detail(client):
    resp = await client.get("/api/v1/wargoals")
    key = resp.json()[0]["wargoal_key"]
    detail = await client.get(f"/api/v1/wargoals/{key}")
    assert detail.status_code == 200
    assert detail.json()["wargoal_key"] == key
# End of wargoal detail test

# Test that requesting a non-existent wargoal returns 404
async def test_wargoal_404(client):
    resp = await client.get("/api/v1/wargoals/nonexistent_xyz")
    assert resp.status_code == 404
# End of wargoal 404 test