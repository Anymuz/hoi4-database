# tests/test_technologies.py
# Phase 3 tests: verify technology list, detail, and country-tech endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Technology list tests:
async def test_list_technologies_200(client):
    # GET /api/v1/technologies should return 200 with a list
    resp = await client.get("/api/v1/technologies")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
# End of technology list 200 test

async def test_list_technologies_pagination(client):
    # Limit and offset should control the result count
    resp = await client.get("/api/v1/technologies?limit=5&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 5
# End of technology list pagination test

async def test_list_technologies_folder_filter(client):
    # ?folder=infantry_folder should return only infantry techs
    resp = await client.get("/api/v1/technologies?folder=infantry_folder")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    for tech in data:
        assert tech["folder_name"] == "infantry_folder"
# End of technology folder filter test

async def test_list_technologies_has_name(client):
    # Every tech in the list should have technology_key and technology_name
    resp = await client.get("/api/v1/technologies?limit=5")
    assert resp.status_code == 200
    for tech in resp.json():
        assert "technology_key" in tech
        assert "technology_name" in tech
# End of technology list name test
# ----------------------------------------------

# Technology detail tests:
async def test_technology_detail(client):
    # GET /api/v1/technologies/infantry_weapons should return full detail
    resp = await client.get("/api/v1/technologies/infantry_weapons")
    assert resp.status_code == 200
    data = resp.json()
    assert data["technology_key"] == "infantry_weapons"
    assert isinstance(data["prerequisites"], list)
    assert isinstance(data["categories"], list)
    assert isinstance(data["enables_equipment"], list)
    assert isinstance(data["enables_units"], list)
# End of technology detail test

async def test_technology_detail_404(client):
    # Non-existent technology should return 404
    resp = await client.get("/api/v1/technologies/nonexistent_tech_xyz")
    assert resp.status_code == 404
# End of technology 404 test
# ----------------------------------------------

# Country starting technologies tests:
async def test_country_technologies_ger(client):
    # GET /api/v1/countries/GER/technologies should return Germany's starting techs
    resp = await client.get("/api/v1/countries/GER/technologies")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for tech in data:
        assert "technology_key" in tech
        assert "technology_name" in tech
# End of country technologies test

async def test_country_technologies_lowercase_tag(client):
    # Lowercase tag should be normalised to uppercase
    resp = await client.get("/api/v1/countries/ger/technologies")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
# End of country technologies lowercase test
