# app/schemas/wargoal.py
from pydantic import BaseModel # For defining data models and validation

# Pydantic schema (response models) for a wargoal, for API responses and data validation.

# Wargoal type, used for defining wargoal types in the game and their properties.
class WargoalType(BaseModel):
    wargoal_key: str
    war_name_key: str | None = None
    generate_base_cost: int | None = None
    generate_per_state_cost: int | None = None
    take_states_limit: int | None = None
    take_states_cost: int | None = None
    puppet_cost: int | None = None
    force_government_cost: int | None = None
    expire: int | None = None
    threat: float | None = None
    take_states_threat_factor: float | None = None
    allowed_block: str | None = None
    available_block: str | None = None
    source_file: str | None = None
# End of WargoalType model