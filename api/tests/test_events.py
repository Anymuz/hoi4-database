# api/tests/test_events.py
# Phase 10 tests: verify event list and detail endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Events list returns 200 with data
async def test_list_events_200(client):
    resp = await client.get("/api/v1/events")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
# End of test_list_events_200

# Events filtered by type
async def test_events_by_type(client):
    resp = await client.get("/api/v1/events?event_type=country_event")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    assert all(e["event_type"] == "country_event" for e in data)
# End of test_events_by_type

# Events filtered by namespace
async def test_events_by_namespace(client):
    resp = await client.get("/api/v1/events?namespace=germany")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
# End of test_events_by_namespace

# Event detail returns the event with options
async def test_event_detail(client):
    resp = await client.get("/api/v1/events")
    key = resp.json()[0]["event_key"]
    detail = await client.get(f"/api/v1/events/{key}")
    assert detail.status_code == 200
    assert detail.json()["event_key"] == key
    assert "options" in detail.json()
# End of test_event_detail

# Event 404
async def test_event_404(client):
    resp = await client.get("/api/v1/events/nonexistent_event_xyz")
    assert resp.status_code == 404
# End of test_event_404

# GraphQL events query
async def test_graphql_events(client):
    query = '{ events { eventKey eventType titleKey options { optionName optionIndex } } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    data = resp.json()["data"]["events"]
    assert len(data) > 0
# End of test_graphql_events
