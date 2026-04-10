# tessts/test_dlc.py
import pytest
# Phase 4 tests: verify DLC-related endpoints.

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# List MIOS tests:
async def test_list_mios_200(client):
    # Test that the MIO list endpoint returns a 200 status and a non-empty list of MIOs.
    resp = await client.get("/api/v1/mios")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of test_list_mios_200

async def test_list_mios_pagination(client):
    # Test that the MIO list endpoint respects pagination parameters.
    resp = await client.get("/api/v1/mios?limit=5&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 5
# End of test_list_mios_pagination

async def test_get_mio_detail(client):
    resp = await client.get("/api/v1/mios?limit=1")
    assert resp.status_code == 200
    first = resp.json()[0]
    key = first["organization_key"]

    detail = await client.get(f"/api/v1/mios/{key}")
    assert detail.status_code == 200
    data = detail.json()
    assert data["organization_key"] == key
    assert isinstance(data["traits"], list)

async def test_mio_detail_404(client):
    resp = await client.get("/api/v1/mios/nonexistent_mio_xyz")
    assert resp.status_code == 404
# --------------------------------

# Operations tests:
async def test_list_operations_200(client):
    resp = await client.get("/api/v1/operations")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

async def test_operation_detail(client):
    resp = await client.get("/api/v1/operations?limit=1")
    assert resp.status_code == 200
    key = resp.json()[0]["operation_key"]

    detail = await client.get(f"/api/v1/operations/{key}")
    assert detail.status_code == 200
    data = detail.json()
    assert data["operation_key"] == key
    assert isinstance(data["phase_groups"], list)
    assert isinstance(data["equipment_requirements"], list)

async def test_operation_detail_404(client):
    resp = await client.get("/api/v1/operations/nonexistent_op_xyz")
    assert resp.status_code == 404
# --------------------------------

# Balance of Power tests:
async def test_list_bop_200(client):
    resp = await client.get("/api/v1/bop")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

async def test_bop_detail(client):
    resp = await client.get("/api/v1/bop?limit=1")
    assert resp.status_code == 200
    key = resp.json()[0]["bop_key"]

    detail = await client.get(f"/api/v1/bop/{key}")
    assert detail.status_code == 200
    data = detail.json()
    assert data["bop_key"] == key
    assert isinstance(data["sides"], list)

async def test_bop_detail_404(client):
    resp = await client.get("/api/v1/bop/nonexistent_bop_xyz")
    assert resp.status_code == 404
# --------------------------------

# Factions tests:
async def test_list_factions_200(client):
    resp = await client.get("/api/v1/factions")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

async def test_faction_detail(client):
    resp = await client.get("/api/v1/factions?limit=1")
    assert resp.status_code == 200
    key = resp.json()[0]["template_key"]

    detail = await client.get(f"/api/v1/factions/{key}")
    assert detail.status_code == 200
    data = detail.json()
    assert data["template_key"] == key
    assert isinstance(data["goals"], list)
    assert isinstance(data["rules"], list)

async def test_faction_detail_404(client):
    resp = await client.get("/api/v1/factions/nonexistent_faction_xyz")
    assert resp.status_code == 404
# --------------------------------

# Special Projects tests:
async def test_list_special_projects_200(client):
    resp = await client.get("/api/v1/special-projects")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

async def test_special_project_detail(client):
    resp = await client.get("/api/v1/special-projects?limit=1")
    assert resp.status_code == 200
    key = resp.json()[0]["project_key"]

    detail = await client.get(f"/api/v1/special-projects/{key}")
    assert detail.status_code == 200
    data = detail.json()
    assert data["project_key"] == key
    assert isinstance(data["rewards"], list)

async def test_special_project_detail_404(client):
    resp = await client.get("/api/v1/special-projects/nonexistent_sp_xyz")
    assert resp.status_code == 404
# --------------------------------