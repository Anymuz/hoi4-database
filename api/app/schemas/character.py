# app/schemas/character.py
from pydantic import BaseModel  # For defining data models and validation

# Pydantic schema (response models) for a Character, for API responses and data validation.

# Roles are seperate  due to the one-to-many relationship (one character can have multiple roles, e.g. country_leader + advisor).
class CharacterRole(BaseModel):
    role_type: str                          # Type of role (e.g. "country_leader", "advisor")
    sub_ideology_key: str | None = None     # For country_leader role, the ideology they lead (e.g. "fascism"), null for advisors.
    skill: int | None = None                # Skill level (1-5), only for advisors, null for country leaders.
    attack_skill: int | None = None         # Attack skill level (1-5), only for advisors, null for country leaders.
    defense_skill: int | None = None        # Defense skill level (1-5), only for advisors, null for country leaders.
    planning_skill: int | None = None       # Planning skill level (1-5), only for advisors, null for country leaders.
    logistics_skill: int | None = None      # Logistics skill level (1-5), only for advisors, null for country leaders.
    maneuvering_skill: int | None = None    # Maneuvering skill level (1-5), only for advisors, null for country leaders.
    coordination_skill: int | None = None   # Coordination skill level (1-5), only for advisors, null for country leaders.
    dlc_source: str | None = None           # DLC source, null if base game
    traits: list[str] = []                  # List of traits this character has (e.g. "charismatic", "strategist")
# End of CharacterRole model

# Details of a character, icludes all data including country tag and gender for filtering.
class CharacterSummary(BaseModel):
    character_id: str                     # Unique character ID (e.g. GER_erwin_rommel)
    name_key: str | None = None           # Localisation key for the character's name
    country_tag: str | None = None        # Country tag derived from character_id prefix
    gender: str | None = None             # Gender of the character
# End of CharacterSummary model

# Full details of a character, includes all data including roles and traits.
class CharacterDetail(CharacterSummary):
    roles: list[CharacterRole] = []       # List of roles this character has (e.g. country_leader, advisor)
# End of CharacterDetail model