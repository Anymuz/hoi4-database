# app/shemas/technology.py
from pydantic import BaseModel # For defining data models and validation

# Pydantic schema (response models) for a Technology, for API responses and data validation.

# Tech summary for list endpoint. Full details list would require 4 sub-queries for all 574 rows.
class TechSummary(BaseModel):
    technology_key: str                    # Tech key (e.g. "infantry_weapons")
    technology_name: str | None = None     # Human-readable name (e.g. "Infantry Weapons")
    start_year: int | None = None          # Year this tech becomes available (e.g. 1936)
    research_cost: float | None = None     # Base research cost for this technology
    folder_name: str | None = None         # Folder name for this tech (e.g. "infantry_weapons")
# End of TechSummary model

# Technology details for a single technology, includes all data including which countries start with it.
class TechTreeItem(TechSummary):
    prerequisites: list[str] = []          # List of prerequisite tech keys
    categories: list[str] = []             # List of categories this tech belongs to
    enables_equipment: list[str] = []      # List of equipment this tech enables
    enables_units: list[str] = []          # List of units this tech enables
# End of TechTreeItem model

# Starting technology for a country
class StartingTech(BaseModel):
    technology_key: str                    # Tech key (e.g. "infantry_weapons")
    technology_name: str | None = None     # Human-readable name (e.g. "Infantry Weapons")
    dlc_source: str | None = None          # DLC source, null if base game
# End of StartingTech model