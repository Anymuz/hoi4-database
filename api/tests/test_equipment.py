# tests/test_equipment.py
import pytest

pytestmark = pytest.mark.asyncio(loop_scope="session")

# ---
# List equipment
# ---

async def test_list_equipment_200(client):
    resp = await client.get("/api/v1/equipment")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of test_list_equipment_200

async def test_list_equipment_pagination(client):
    resp = await client.get("/api/v1/equipment?limit=5&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 5
# End of test_list_equipment_pagination

async def test_list_equipment_archetype_filter(client):
    resp = await client.get("/api/v1/equipment?is_archetype=true")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for item in data:
        assert item["is_archetype"] is True
# End of test_list_equipment_archetype_filter

async def test_list_equipment_parent_filter(client):
    resp = await client.get("/api/v1/equipment?archetype=infantry_equipment")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for item in data:
        assert item["archetype_key"] == "infantry_equipment"
# End of test_list_equipment_parent_filter

# ---
# Equipment detail
# ---

async def test_equipment_detail(client):
    resp = await client.get("/api/v1/equipment/infantry_equipment_0")
    assert resp.status_code == 200
    data = resp.json()
    assert data["equipment_key"] == "infantry_equipment_0"
    assert isinstance(data["resources"], list)
# End of test_equipment_detail

async def test_equipment_detail_has_stats(client):
    resp = await client.get("/api/v1/equipment/infantry_equipment_0")
    assert resp.status_code == 200
    data = resp.json()
    assert "build_cost_ic" in data
    assert "reliability" in data
    assert "soft_attack" in data
# End of test_equipment_detail_has_stats

async def test_equipment_detail_404(client):
    resp = await client.get("/api/v1/equipment/nonexistent_equip_xyz")
    assert resp.status_code == 404
# End of test_equipment_detail_404
