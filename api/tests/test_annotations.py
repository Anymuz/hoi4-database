# tests/test_annotations.py
import pytest
# Phase 4 tests: verify annotation CRUD lifecycle.

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Helper — create an annotation and return the response JSON.
async def _create(client, entity_type="country", entity_key="GER", note="Test annotation"):
    resp = await client.post(
        "/api/v1/annotations",
        json={"entity_type": entity_type, "entity_key": entity_key, "note": note},
    )
    return resp
# End of _create helper

# Create tests:
async def test_create_annotation(client):
    resp = await _create(client)
    assert resp.status_code == 201
    data = resp.json()
    assert data["entity_type"] == "country"
    assert data["entity_key"] == "GER"
    assert data["note"] == "Test annotation"
    assert isinstance(data["annotation_id"], int)
    assert "created_at" in data
# End of test_create_annotation

# Get by ID tests:
async def test_get_annotation_by_id(client):
    created = (await _create(client, note="Get by ID test")).json()
    aid = created["annotation_id"]

    resp = await client.get(f"/api/v1/annotations/{aid}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["annotation_id"] == aid
    assert data["note"] == "Get by ID test"
# End of test_get_annotation_by_id

# List with filter tests:
async def test_list_annotations_filter(client):
    await _create(client, entity_type="technology", entity_key="infantry_weapons", note="Filter test")

    resp = await client.get("/api/v1/annotations?entity_type=technology&entity_key=infantry_weapons")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    notes = [a["note"] for a in data]
    assert "Filter test" in notes
# End of test_list_annotations_filter

# Delete tests:
async def test_delete_annotation(client):
    created = (await _create(client, note="To be deleted")).json()
    aid = created["annotation_id"]

    del_resp = await client.delete(f"/api/v1/annotations/{aid}")
    assert del_resp.status_code == 204

    get_resp = await client.get(f"/api/v1/annotations/{aid}")
    assert get_resp.status_code == 404
# End of test_delete_annotation

async def test_delete_annotation_404(client):
    resp = await client.delete("/api/v1/annotations/999999")
    assert resp.status_code == 404
# End of test_delete_annotation_404

# 404 tests:
async def test_get_annotation_404(client):
    resp = await client.get("/api/v1/annotations/999999")
    assert resp.status_code == 404
# End of test_get_annotation_404

# Validation tests:
async def test_create_annotation_empty_note(client):
    resp = await _create(client, note="")
    assert resp.status_code == 422
# End of test_create_annotation_empty_note
# ----------------------------------------------
