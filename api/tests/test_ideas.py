# tests/test_ideas.py
import pytest
# Phase 3 tests: verify idea list and detail endpoints.

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# List ideas tests:
async def test_list_ideas_200(client):
    # Test that the idea list endpoint returns a 200 status and a non-empty list of ideas.
    resp = await client.get("/api/v1/ideas")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of test_list_ideas_200

async def test_list_ideas_pagination(client):
    # Test that the idea list endpoint respects pagination parameters.
    resp = await client.get("/api/v1/ideas?limit=5&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 5
# End of test_list_ideas_pagination

async def test_list_ideas_slot_filter(client):
    # Test that filtering ideas by slot works correctly.
    resp = await client.get("/api/v1/ideas?slot=economy")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for item in data:
        assert item["slot"] == "economy"
# End of test_list_ideas_slot_filter

async def test_list_ideas_law_filter(client):
    # Test that filtering ideas by is_law works correctly.
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
    # Test that the idea detail endpoint returns correct data for a known idea.
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
    # Test that each modifier in the idea detail has the expected fields.
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
    # Test that requesting a non-existent idea returns a 404 status.
    resp = await client.get("/api/v1/ideas/nonexistent_idea_xyz")
    assert resp.status_code == 404
# End of test_idea_detail_404
# ----------------------------------------------

# Phase 7: Idea scripted effect tests:
async def test_idea_has_on_add_effect(client):
    """At least one idea has an on_add_effect."""
    resp = await client.get("/api/v1/ideas?slot=country&limit=500")
    assert resp.status_code == 200
    ideas = resp.json()
    with_effects = [i for i in ideas if i.get("on_add_effect")]
    assert len(with_effects) > 0
# End of test_idea_has_on_add_effect

async def test_idea_effect_fields_present(client):
    """Idea detail includes the three new effect fields."""
    resp = await client.get("/api/v1/ideas?limit=1")
    first = resp.json()[0]
    assert "on_add_effect" in first
    assert "on_remove_effect" in first
    assert "allowed_condition" in first
# End of test_idea_effect_fields_present
# ----------------------------------------------