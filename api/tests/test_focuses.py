# tests/test_focuses.py
# Phase 3 tests: verify focus tree list, detail, and country focus tree endpoints.
import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# List focus trees tests:
async def test_list_focus_trees_200(client):
    resp = await client.get("/api/v1/focus-trees")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of test_list_focus_trees_200

async def test_list_focus_trees_pagination(client):
    resp = await client.get("/api/v1/focus-trees?limit=5&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 5
# End of test_list_focus_trees_pagination

async def test_list_focus_trees_summary_only(client):
    resp = await client.get("/api/v1/focus-trees?limit=3")
    assert resp.status_code == 200
    for tree in resp.json():
        assert "focus_tree_id" in tree
        assert "country_tag" in tree
        assert "focuses" not in tree
# End of test_list_focus_trees_summary_only
# ----------------------------------------------

# Focus tree detail tests:
async def test_focus_tree_detail(client):
    # Grab a valid focus_tree_id from the list
    list_resp = await client.get("/api/v1/focus-trees?limit=1")
    tree_id = list_resp.json()[0]["focus_tree_id"]

    resp = await client.get(f"/api/v1/focus-trees/{tree_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["focus_tree_id"] == tree_id
    assert isinstance(data["focuses"], list)
    assert len(data["focuses"]) > 0
# End of test_focus_tree_detail

async def test_focus_tree_focuses_have_fields(client):
    list_resp = await client.get("/api/v1/focus-trees?limit=1")
    tree_id = list_resp.json()[0]["focus_tree_id"]

    resp = await client.get(f"/api/v1/focus-trees/{tree_id}")
    assert resp.status_code == 200
    for focus in resp.json()["focuses"]:
        assert "focus_id" in focus
        assert "cost" in focus
        assert isinstance(focus["prerequisites"], list)
        assert isinstance(focus["mutually_exclusive"], list)
# End of test_focus_tree_focuses_have_fields

async def test_focus_tree_detail_404(client):
    resp = await client.get("/api/v1/focus-trees/nonexistent_tree_xyz")
    assert resp.status_code == 404
# End of test_focus_tree_detail_404
# ----------------------------------------------

# Country focus tree tests:
async def test_country_focus_tree_ger(client):
    resp = await client.get("/api/v1/countries/GER/focus-tree")
    assert resp.status_code == 200
    data = resp.json()
    assert data["country_tag"] == "GER"
    assert isinstance(data["focuses"], list)
    assert len(data["focuses"]) > 0
# End of test_country_focus_tree_ger

async def test_country_focus_tree_404(client):
    resp = await client.get("/api/v1/countries/ZZZ/focus-tree")
    assert resp.status_code == 404
# End of test_country_focus_tree_404
# ----------------------------------------------