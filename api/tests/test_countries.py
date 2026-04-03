# tests/test_countries.py
# Phase 2 tests: verify country list and detail endpoints against the real database.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Country list tests:
async def test_list_countries_200(client):
    # GET /api/v1/countries should return 200 with a list
    resp = await client.get("/api/v1/countries")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0  # database has hundreds of countries
# End of country list 200 test

async def test_list_countries_has_tag(client):
    # Each country in the list should have a tag field
    resp = await client.get("/api/v1/countries?limit=5")
    data = resp.json()
    for country in data:
        assert "tag" in country
    # End loop checking tags
# End of country list tag field test

async def test_list_countries_pagination(client):
    # Limit and offset should control the result count
    resp = await client.get("/api/v1/countries?limit=3&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 3 # Should match the request limit of 3
# End of country list pagination test
# ----------------------------------------------

# Country detail tests:
async def test_country_detail_ger(client):
    # GET /api/v1/countries/GER should return Germany with nested data
    resp = await client.get("/api/v1/countries/GER")
    assert resp.status_code == 200
    data = resp.json()
    assert data["tag"] == "GER"
    assert data["capital_state_id"] is not None
    assert isinstance(data["owned_states"], list)
    assert isinstance(data["starting_technologies"], list)
    assert len(data["owned_states"]) > 0
    assert len(data["starting_technologies"]) > 0
# End of country detail GER test

async def test_country_detail_lowercase_tag(client):
    # Tags should be case-insensitive, so /countries/ger should work
    resp = await client.get("/api/v1/countries/ger")
    assert resp.status_code == 200
    assert resp.json()["tag"] == "GER"
# End of country detail lowercase tag test

async def test_country_detail_404(client):
    # A non-existent country tag should return 404
    resp = await client.get("/api/v1/countries/ZZZ")
    assert resp.status_code == 404
# End of country detail 404 test
# ----------------------------------------------

# Country date filtering tests:
async def test_country_detail_1939(client):
    # Requesting ?date=1939-08-14 should still return valid data
    resp = await client.get("/api/v1/countries/GER?date=1939-08-14")
    assert resp.status_code == 200
    assert resp.json()["tag"] == "GER"
# End of country detail date test

async def test_country_list_invalid_date(client):
    # An invalid date should return 400
    resp = await client.get("/api/v1/countries?date=2000-01-01")
    assert resp.status_code == 400
# End of country list invalid date test
# -----------------------------------------------