# api/tests/test_diplomacy.py
# Phase 8 tests: verify diplomacy endpoints for diplomatic relations and starting factions.
import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session") 

# Diplomatic relations list
async def test_list_diplomatic_relations_200(client):
    resp = await client.get("/api/v1/diplomacy")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
# End of test_list_diplomatic_relations_200

# Diplomatic relations filtered by country
async def test_diplomatic_relations_by_country(client):
    resp = await client.get("/api/v1/diplomacy?country_tag=ENG")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    assert all(r["country_tag"] == "ENG" for r in data)
# End of test_diplomatic_relations_by_country

# Diplomatic relation detail
async def test_diplomatic_relation_detail(client):
    resp = await client.get("/api/v1/diplomacy")
    rid = resp.json()[0]["diplomatic_relation_id"]
    detail = await client.get(f"/api/v1/diplomacy/{rid}")
    assert detail.status_code == 200
    assert detail.json()["diplomatic_relation_id"] == rid
# End of test_diplomatic_relation_detail

# Diplomatic relation 404
async def test_diplomatic_relation_404(client):
    resp = await client.get("/api/v1/diplomacy/999999")
    assert resp.status_code == 404
# End of test_diplomatic_relation_404

# Starting factions list
async def test_list_starting_factions_200(client):
    resp = await client.get("/api/v1/factions/starting")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) >= 5
    assert any(f["faction_template_key"] == "faction_template_allies" for f in data)
# End of test_list_starting_factions_200

# Starting faction detail
async def test_starting_faction_detail(client):
    resp = await client.get("/api/v1/factions/starting")
    fid = resp.json()[0]["starting_faction_id"]
    detail = await client.get(f"/api/v1/factions/starting/{fid}")
    assert detail.status_code == 200
    assert "members" in detail.json()
# End of test_starting_faction_detail

# Starting faction 404
async def test_starting_faction_404(client):
    resp = await client.get("/api/v1/factions/starting/999999")
    assert resp.status_code == 404
# End of test_starting_faction_404
