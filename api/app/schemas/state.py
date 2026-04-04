# app/schemas/state.py
from pydantic import BaseModel  # For defining data models and validation

# Pydantic schema (response models) for a State, for API responses and data validation.
# The api_state_detail() function returns jsonb columns for nested data.
# asyncpg automatically converts jsonb → Python list[dict].
# Pydantic validates each dict against the nested model below.

# Resource entry inside a state (e.g. {"resource_key": "steel", "amount": 24})
class StateResource(BaseModel):
    resource_key: str       # e.g. "steel", "oil", "aluminium"
    amount: int             # How much of this resource the state has
# End of StateResource model

# Building entry at the state level (e.g. {"building_key": "arms_factory", "level": 3})
class StateBuilding(BaseModel):
    building_key: str       # e.g. "arms_factory", "industrial_complex"
    level: int              # Building level/count
# End of StateBuilding model

# Building entry at the province level (specific province within a state)
class ProvinceBuilding(BaseModel):
    province_id: int        # Which province has this building
    building_key: str       # e.g. "naval_base", "bunker"
    level: int              # Building level
# End of ProvinceBuilding model

# Province belonging to a state
class Province(BaseModel):
    province_id: int                 # Unique province ID from map/definition.csv
    terrain: str | None = None       # e.g. "plains", "forest", "mountain"
    is_coastal: bool | None = None   # Whether the province touches the sea
    continent_id: int | None = None  # Which continent (1=Europe, etc.)
# End of Province model

# Summary of a state (lightweight for list endpoints)
class StateSummary(BaseModel):
    state_id: int                           # Unique state ID
    state_name_key: str                     # Localisation key (e.g. "STATE_64")
    state_name: str | None = None           # Human-readable name (e.g. "Brandenburg")
    state_category: str | None = None       # e.g. "large_city", "rural"
    manpower: int | None = None             # Base manpower
    owner_tag: str | None = None            # Country that owns this state (e.g. "GER")
# End of StateSummary model

# Full details of a state, includes all nested data
class StateDetail(StateSummary):
    local_supplies: float | None = None                 # Supply value (decimal)
    controller_tag: str | None = None                   # Controlling country tag (differs if occupied)
    resources: list[StateResource] = []                 # Steel, oil, etc.
    state_buildings: list[StateBuilding] = []           # Arms factories, civs, etc.
    province_buildings: list[ProvinceBuilding] = []     # Naval bases, bunkers per province
    provinces: list[Province] = []                      # All provinces in this state
# End of StateDetail model