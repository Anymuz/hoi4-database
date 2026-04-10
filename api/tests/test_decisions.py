# api/tests/test_decisions.py
# Phase 11 tests: verify decision list and detail endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Decisions list returns 200 with data
async def test_list_decisions_200(client):
    resp = await client.get("/api/v1/decisions")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
# End of test_list_decisions_200

# Decisions filtered by category
async def test_decisions_by_category(client):
    resp = await client.get("/api/v1/decisions")
    cat = resp.json()[0]["category_key"]
    filtered = await client.get(f"/api/v1/decisions?category={cat}")
    assert filtered.status_code == 200
    assert len(filtered.json()) > 0
    assert all(d["category_key"] == cat for d in filtered.json())
# End of test_decisions_by_category

# Decision detail returns the decision with effect blocks
async def test_decision_detail(client):
    resp = await client.get("/api/v1/decisions")
    key = resp.json()[0]["decision_key"]
    detail = await client.get(f"/api/v1/decisions/{key}")
    assert detail.status_code == 200
    assert detail.json()["decision_key"] == key
# End of test_decision_detail

# Decision 404
async def test_decision_404(client):
    resp = await client.get("/api/v1/decisions/nonexistent_decision_xyz")
    assert resp.status_code == 404
# End of test_decision_404

# GraphQL decisions query
async def test_graphql_decisions(client):
    query = '{ decisions { decisionKey categoryKey allowed available completeEffect } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    data = resp.json()["data"]["decisions"]
    assert len(data) > 0
# End of test_graphql_decisions
