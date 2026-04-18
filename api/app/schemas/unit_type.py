# app/schemas/unit_type.py
from pydantic import BaseModel # For defining data models and validation

# Pydantic schema (response model) for unit types, for API responses and data validation.

# UnitType represents a military unit type with combat stats, manpower, and training data.
class UnitType(BaseModel):
    unit_type_key: str
    unit_type_name: str | None = None
    abbreviation: str | None = None
    unit_group: str | None = None
    combat_width: float | None = None
    max_strength: float | None = None
    max_organisation: float | None = None
    default_morale: float | None = None
    manpower: int | None = None
    training_time: int | None = None
    suppression: float | None = None
    weight: float | None = None
    supply_consumption: float | None = None
    source_file: str | None = None
    dlc_source: str | None = None
# End of UnitType model
