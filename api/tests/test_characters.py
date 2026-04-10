# tests/test_characters.py
# Phase 3 tests: verify character list and detail endpoints.

import pytest

# Mark every test in this file as async so pytest-asyncio will run them.
pytestmark = pytest.mark.asyncio(loop_scope="session")

# Character list tests (GET /api/v1/countries/{tag}/characters):
async def test_list_characters_200(client):
    # GET /api/v1/countries/GER/characters should return 200 with a list
    resp = await client.get("/api/v1/countries/GER/characters")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0  # GER has ~140 characters
# End of character list 200 test

async def test_list_characters_summary_fields(client):
    # Each item in the list should have exactly the 4 summary fields and NO roles
    resp = await client.get("/api/v1/countries/GER/characters?limit=5")
    assert resp.status_code == 200
    data = resp.json()
    for char in data:
        assert "character_id" in char
        assert "name_key" in char
        assert "country_tag" in char
        assert "gender" in char
        assert "roles" not in char  # list endpoint is lightweight - no roles
# End of character list summary fields test

async def test_list_characters_pagination(client):
    # Limit and offset should control the result count
    resp = await client.get("/api/v1/countries/GER/characters?limit=3&offset=0")
    assert resp.status_code == 200
    assert len(resp.json()) == 3
# End of character list pagination test

async def test_list_characters_lowercase_tag(client):
    # Tags should be case-insensitive - /countries/ger/characters should work
    resp = await client.get("/api/v1/countries/ger/characters")
    assert resp.status_code == 200
    assert len(resp.json()) > 0
# End of character list lowercase tag test

async def test_list_characters_empty_country(client):
    # A country with no characters should return 200 with an empty list (not 404)
    resp = await client.get("/api/v1/countries/ZZZ/characters")
    assert resp.status_code == 200
    assert resp.json() == []
# End of character list empty country test
# ----------------------------------------------

# Character detail tests (GET /api/v1/characters/{character_id}):
async def test_character_detail_rommel(client):
    # GET /api/v1/characters/GER_erwin_rommel should return Rommel with his roles
    resp = await client.get("/api/v1/characters/GER_erwin_rommel")
    assert resp.status_code == 200
    data = resp.json()
    # Check the top-level summary fields are present
    assert data["character_id"] == "GER_erwin_rommel"
    assert data["name_key"] == "GER_erwin_rommel"
    assert data["country_tag"] == "GER"
    assert data["gender"] == "male"
    # Check that roles is a list and not empty
    assert isinstance(data["roles"], list)
    assert len(data["roles"]) >= 2  # Rommel is both corps_commander and advisor
# End of character detail Rommel test

async def test_character_detail_roles_have_required_fields(client):
    # Each role object should have role_type, traits list, and skill fields
    resp = await client.get("/api/v1/characters/GER_erwin_rommel")
    data = resp.json()
    for role in data["roles"]:
        # role_type is always present (e.g. "advisor", "corps_commander")
        assert "role_type" in role
        assert isinstance(role["role_type"], str)
        # traits is always a list (may be empty for some roles)
        assert "traits" in role
        assert isinstance(role["traits"], list)
        # skill fields exist (they may be null - that's OK)
        assert "skill" in role
        assert "attack_skill" in role
        assert "defense_skill" in role
        assert "planning_skill" in role
        assert "logistics_skill" in role
        assert "maneuvering_skill" in role  
        assert "coordination_skill" in role
# End of character detail roles fields test

async def test_character_detail_rommel_has_corps_commander(client):
    # Rommel should have a corps_commander role with specific known traits
    resp = await client.get("/api/v1/characters/GER_erwin_rommel")
    data = resp.json()
    # Find the corps_commander role
    commander_roles = [r for r in data["roles"] if r["role_type"] == "corps_commander"]
    assert len(commander_roles) == 1, "Rommel should have exactly one corps_commander role"
    commander = commander_roles[0]
    # Rommel's known traits include armor_officer and trickster
    assert "armor_officer" in commander["traits"]
    assert "trickster" in commander["traits"]
# End of character detail Rommel corps_commander test

async def test_character_detail_rommel_has_advisor(client):
    # Rommel should also have an advisor role
    resp = await client.get("/api/v1/characters/GER_erwin_rommel")
    data = resp.json()
    advisor_roles = [r for r in data["roles"] if r["role_type"] == "advisor"]
    assert len(advisor_roles) == 1, "Rommel should have exactly one advisor role"
    # Advisor role should have at least one trait
    assert len(advisor_roles[0]["traits"]) > 0
# End of character detail Rommel advisor test

async def test_character_detail_404(client):
    # A non-existent character ID should return 404
    resp = await client.get("/api/v1/characters/ZZZ_nobody")
    assert resp.status_code == 404
# End of character detail 404 test
# -----------------------------------------------
