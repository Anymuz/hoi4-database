# tests/test_graphql.py
import pytest
# Phase 5 tests: verify GraphQL layer returns correct data.
# All queries POST to /graphql with {"query": "..."}. GraphQL always returns HTTP 200 so we use check resp.json()["errors"] for failures.

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Test the country query with a valid tag, should return correct country data.
async def test_country_query(client):
    query = '{ country(tag: "GER") { tag stability ownedStates { stateId } } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    body = resp.json()
    assert "errors" not in body
    data = body["data"]["country"]
    assert data["tag"] == "GER"
    assert isinstance(data["ownedStates"], list)
# End of test_country_query

# Test the country query with the 1939 bookmark date returns valid data.
async def test_country_date_1939(client):
    query = '{ country(tag: "GER", date: "1939-08-14") { tag ownedStates { stateId } } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    body = resp.json()
    assert "errors" not in body
    assert body["data"]["country"]["tag"] == "GER"
# End of test_country_date_1939

# Test the characters query returns characters with roles and traits.
async def test_characters_query(client):
    query = '{ characters(countryTag: "GER") { nameKey roles { roleType traits } } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    body = resp.json()
    assert "errors" not in body
    characters = body["data"]["characters"]
    assert len(characters) > 0
    # At least one character should have a role with a non-empty traits list
    found_traits = False
    for ch in characters:
        for role in ch["roles"]:
            if len(role["traits"]) > 0:
                found_traits = True
                break
        if found_traits:
            break
    assert found_traits, "Expected at least one character with non-empty traits"
# End of test_characters_query

# Test that requesting minimal fields (tag only) returns exactly 5 countries.
async def test_minimal_fields(client):
    query = "{ countries(limit: 5) { tag } }"
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    body = resp.json()
    assert "errors" not in body
    items = body["data"]["countries"]
    assert len(items) == 5
    for item in items:
        assert "tag" in item
# End of test_minimal_fields

# Test that filtering technologies by folder returns results.
async def test_technologies_filter(client):
    query = '{ technologies(folder: "infantry_folder") { technologyKey } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    body = resp.json()
    assert "errors" not in body
    techs = body["data"]["technologies"]
    assert len(techs) > 0
# End of test_technologies_filter

# Test creating an annotation via REST and reading it back via GraphQL.
async def test_annotations_roundtrip(client):
    # Create via REST
    resp = await client.post(
        "/api/v1/annotations",
        json={"entity_type": "country", "entity_key": "GER", "note": "GraphQL roundtrip test"},
    )
    assert resp.status_code == 201

    # Query via GraphQL
    query = '{ annotations(entityType: "country", entityKey: "GER") { note } }'
    resp = await client.post("/graphql", json={"query": query})
    assert resp.status_code == 200
    body = resp.json()
    assert "errors" not in body
    notes = [a["note"] for a in body["data"]["annotations"]]
    assert "GraphQL roundtrip test" in notes
# End of test_annotations_roundtrip

# Test that an invalid GraphQL query returns errors in the response.
async def test_graphql_invalid_query(client):
    resp = await client.post("/graphql", json={"query": "{ nonExistentField }"})
    assert resp.status_code == 200
    body = resp.json()
    assert "errors" in body
# End of test_graphql_invalid_query
