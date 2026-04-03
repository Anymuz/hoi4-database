# tests/test_states.py
# Phase 2 tests: verify state list and detail endpoints against the real database.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# State list tests:
async def test_list_states_200(client):
    # GET /api/v1/states should return 200 with a list
    resp = await client.get("/api/v1/states")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of state list 200 test

async def test_list_states_pagination(client):
    # Limit and offset should control the result count
    resp = await client.get("/api/v1/states?limit=5&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 5
# End of state list pagination test

async def test_list_states_filter_by_owner(client):
    # ?owner_tag=GER should return only German-owned states
    resp = await client.get("/api/v1/states?owner_tag=GER")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for state in data:
        assert state["owner_tag"] == "GER"
# End of state list filter by owner test
# ----------------------------------------------

# State detail tests:
async def test_state_detail_64(client):
    # GET /api/v1/states/64 (Brandenburg) should return full nested data
    resp = await client.get("/api/v1/states/64")
    assert resp.status_code == 200
    data = resp.json()
    assert data["state_id"] == 64
    assert isinstance(data["resources"], list)
    assert isinstance(data["state_buildings"], list)
    assert isinstance(data["provinces"], list)
    assert len(data["provinces"]) > 0  # states always have provinces
# End of state detail 64 test

async def test_state_detail_provinces_have_terrain(client):
    # Each province inside a state should have terrain info
    resp = await client.get("/api/v1/states/64")
    data = resp.json()
    for prov in data["provinces"]:
        assert "province_id" in prov
        assert "terrain" in prov
# End of state detail provinces have terrain test

async def test_state_detail_404(client):
    # A non-existent state ID should return 404
    resp = await client.get("/api/v1/states/99999")
    assert resp.status_code == 404
# End of state detail 404 test
# ----------------------------------------------

# State date filtering tests:
async def test_state_detail_1939(client):
    # Requesting ?date=1939-08-14 should still return valid data
    resp = await client.get("/api/v1/states/64?date=1939-08-14")
    assert resp.status_code == 200
    assert resp.json()["state_id"] == 64
# End of state detail date test

async def test_state_list_invalid_date(client):
    # An invalid date should return 400
    resp = await client.get("/api/v1/states?date=2000-01-01")
    assert resp.status_code == 400
# End of state list invalid date test
# -----------------------------------------------