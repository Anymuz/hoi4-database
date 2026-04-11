# api/tests/test_ideologies.py
# Phase 13 tests: verify ideology list, detail, 404, color, and GraphQL endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Ideology list tests:
async def test_list_ideologies_200(client):
    resp = await client.get("/api/v1/ideologies")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 4
# End of ideology list 200 test

# Ideology detail tests:
async def test_ideology_detail(client):
    resp = await client.get("/api/v1/ideologies/fascism")
    assert resp.status_code == 200
    data = resp.json()
    assert data["ideology_key"] == "fascism"
    subs = data["sub_ideologies"]
    assert len(subs) >= 3
# End of ideology detail test

# Test that requesting a non-existent ideology returns 404
async def test_ideology_404(client):
    resp = await client.get("/api/v1/ideologies/nonexistent_xyz")
    assert resp.status_code == 404
# End of ideology 404 test

# Test that ideology detail includes color_rgb fields
async def test_ideology_has_color(client):
    resp = await client.get("/api/v1/ideologies/fascism")
    assert resp.status_code == 200
    color = resp.json()["color_rgb"]
    assert "r" in color and "g" in color and "b" in color
    assert all(isinstance(color[k], int) for k in ("r", "g", "b"))
# End of ideology color test

# GraphQL: query ideologies
async def test_graphql_ideologies(client):
    query = """
    {
        ideologies {
            ideologyKey
            colorRgb { r g b }
            subIdeologies { subIdeologyKey }
        }
    }
    """
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    data = resp.json()["data"]["ideologies"]
    assert len(data) == 4
    assert any(i["ideologyKey"] == "fascism" for i in data)
# End of GraphQL ideologies test
