# api/tests/test_unit_types.py
# Phase 14 tests: verify unit type list, detail, filter, 404, and GraphQL endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Unit type list tests:
async def test_list_unit_types_200(client):
    resp = await client.get("/api/v1/unit-types")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) >= 50
# End of unit type list 200 test

# Unit type filter by unit_group tests:
async def test_unit_types_by_group(client):
    resp = await client.get("/api/v1/unit-types?unit_group=infantry")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    assert all(d["unit_group"] == "infantry" for d in data)
# End of unit type group filter test

# Unit type detail tests:
async def test_unit_type_detail(client):
    resp = await client.get("/api/v1/unit-types/infantry")
    assert resp.status_code == 200
    data = resp.json()
    assert data["unit_type_key"] == "infantry"
    assert data["combat_width"] is not None
    assert data["manpower"] is not None
# End of unit type detail test

# Test that requesting a non-existent unit type returns 404
async def test_unit_type_404(client):
    resp = await client.get("/api/v1/unit-types/nonexistent_xyz")
    assert resp.status_code == 404
# End of unit type 404 test

# GraphQL: query unit types
async def test_graphql_unit_types(client):
    query = """
    {
        unitTypes {
            unitTypeKey
            unitTypeName
            unitGroup
            combatWidth
            manpower
        }
    }
    """
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    data = resp.json()["data"]["unitTypes"]
    assert len(data) >= 50
    assert any(u["unitTypeKey"] == "infantry" for u in data)
# End of GraphQL unit types test
