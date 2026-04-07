# tests/test_ideas.py
import pytest
# Phase 3 tests: verify idea list and detail endpoints.

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# List ideas tests:
async def test_list_ideas_200(client):
    resp = await client.get("/api/v1/ideas")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of test_list_ideas_200

async def test_list_ideas_pagination(client):
    resp = await client.get("/api/v1/ideas?limit=5&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 5
# End of test_list_ideas_pagination

async def test_list_ideas_slot_filter(client):
    resp = await client.get("/api/v1/ideas?slot=economy")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for item in data:
        assert item["slot"] == "economy"
# End of test_list_ideas_slot_filter

async def test_list_ideas_law_filter(client):
    resp = await client.get("/api/v1/ideas?is_law=true")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for item in data:
        assert item["is_law"] is True
# End of test_list_ideas_law_filter
# ----------------------------------------------

# Idea detail tests:
async def test_idea_detail(client):
    resp = await client.get("/api/v1/ideas?limit=1")
    assert resp.status_code == 200
    first = resp.json()[0]
    idea_key = first["idea_key"]

    resp2 = await client.get(f"/api/v1/ideas/{idea_key}")
    assert resp2.status_code == 200
    detail = resp2.json()
    assert detail["idea_key"] == idea_key
    assert isinstance(detail["modifiers"], list)
# End of test_idea_detail

async def test_idea_detail_modifiers_have_fields(client):
    resp = await client.get("/api/v1/ideas?limit=1")
    first = resp.json()[0]
    idea_key = first["idea_key"]

    resp2 = await client.get(f"/api/v1/ideas/{idea_key}")
    detail = resp2.json()
    for mod in detail["modifiers"]:
        assert isinstance(mod["modifier_key"], str)
        assert isinstance(mod["modifier_value"], (int, float))
# End of test_idea_detail_modifiers_have_fields

async def test_idea_detail_404(client):
    resp = await client.get("/api/v1/ideas/nonexistent_idea_xyz")
    assert resp.status_code == 404
# End of test_idea_detail_404
# ----------------------------------------------