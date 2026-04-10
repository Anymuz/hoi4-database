# app/schemas/diplomacy.py
from pydantic import BaseModel  # For defining data models and validation 
from datetime import date as Date # For representing effective dates in diplomatic relations and factions
# app/schemas/country.py

# Pydantic schema (response models) for a Country, for API responses and data validation.

# DiplomaticRelation represents a diplomatic relation between two countries, with its type, autonomy level, freedom level, effective date, and other details.
class DiplomaticRelation(BaseModel):
    diplomatic_relation_id: int
    country_tag: str
    target_tag: str
    relation_type: str
    autonomy_type: str | None = None
    freedom_level: float | None = None
    effective_date: Date | None = None
    dlc_source: str | None = None
    source_file: str | None = None
# End of DiplomaticRelation model

# FactionMember represents a member of a starting faction, with their tag and name. Nested within the StartingFaction type.
class FactionMember(BaseModel):
    member_tag: str
    member_name: str | None = None
# End of FactionMember model

# StartingFaction represents a faction that exists at the start of the game, with its ID, template key, leader, effective date, and members.
class StartingFaction(BaseModel):
    starting_faction_id: int
    faction_template_key: str
    leader_tag: str
    leader_name: str | None = None
    effective_date: Date | None = None
    members: list[FactionMember] = []
# End of StartingFaction model
