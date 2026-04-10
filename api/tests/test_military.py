# tests/test_military.py
# Phase 3 tests: verify divisions, naval, and air endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Divisions tests (GET /api/v1/countries/{tag}/divisions):
async def test_divisions_ger_200(client):
    # GER should have divisions in the default 1936 start
    resp = await client.get("/api/v1/countries/GER/divisions")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of divisions GER 200 test

async def test_divisions_have_nested_arrays(client):
    # Each division should have regiments[], support[], and deployed_divisions[]
    resp = await client.get("/api/v1/countries/GER/divisions")
    assert resp.status_code == 200
    for div in resp.json():
        assert "template_name" in div
        assert isinstance(div["regiments"], list)
        assert isinstance(div["support"], list)
        assert isinstance(div["deployed_divisions"], list)
        assert len(div["regiments"]) > 0  # every template has at least 1 regiment
# End of divisions nested arrays test

async def test_divisions_empty_country(client):
    # A non-existent country returns 200 with an empty list (not 404)
    resp = await client.get("/api/v1/countries/ZZZ/divisions")
    assert resp.status_code == 200
    assert resp.json() == []
# End of divisions empty country test
# ----------------------------------------------

# Naval tests (GET /api/v1/countries/{tag}/naval):
async def test_naval_ger_200(client):
    # GER should have fleets in 1936
    resp = await client.get("/api/v1/countries/GER/naval")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of naval GER 200 test

async def test_naval_has_task_forces(client):
    # Each fleet should have task_forces[]; task forces contain ships[]
    resp = await client.get("/api/v1/countries/GER/naval")
    assert resp.status_code == 200
    for fleet in resp.json():
        assert "fleet_name" in fleet
        assert isinstance(fleet["task_forces"], list)
        if len(fleet["task_forces"]) > 0:
            tf = fleet["task_forces"][0]
            assert "task_force_name" in tf
            assert isinstance(tf["ships"], list)
# End of naval task forces test

async def test_naval_empty_country(client):
    # A non-existent country returns 200 with an empty list
    resp = await client.get("/api/v1/countries/ZZZ/naval")
    assert resp.status_code == 200
    assert resp.json() == []
# End of naval empty country test
# ----------------------------------------------

# Air tests (GET /api/v1/countries/{tag}/air):
async def test_air_ger_200(client):
    # GER should have air wings in 1936
    resp = await client.get("/api/v1/countries/GER/air")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of air GER 200 test

async def test_air_has_equipment_type(client):
    # Each air wing should have equipment_type and amount
    resp = await client.get("/api/v1/countries/GER/air")
    assert resp.status_code == 200
    for wing in resp.json():
        assert "equipment_type" in wing
        assert "amount" in wing
# End of air equipment type test

async def test_air_empty_country(client):
    # A non-existent country returns 200 with an empty list
    resp = await client.get("/api/v1/countries/ZZZ/air")
    assert resp.status_code == 200
    assert resp.json() == []
# End of air empty country test
# ----------------------------------------------