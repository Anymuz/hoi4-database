# app/schemas/country.py
from pydantic import BaseModel  # For defining data models and validation 

# Pydantic schema (response models) for a Country, for API responses and data validation.

# Colors as RGB values, can be used for UI elements
class ColorRGB(BaseModel):
    r: int      # Red component (0-255)
    g: int      # Green component (0-255)
    b: int      # Blue component (0-255)
# End of ColorRGB model

# State owned by a country
class OwnedState(BaseModel):
    state_id: int                          # Unique ID of the state
    state_name_key: str                    # Localisation key (e.g. "STATE_64")
    state_name: str | None = None          # Human-readable name (e.g. "Brandenburg")
    controller_tag: str | None = None      # State controller (different from owner if occupied)
# End of OwnedState model

# Starting technology for a country
class StartingTech(BaseModel):
    technology_key: str                    # Tech key (e.g. "infantry_weapons")
    technology_name: str | None = None     # Human-readable name (e.g. "Infantry Weapons")
    dlc_source: str | None = None          # DLC source, null if base game
# End of StartingTech model

# Summary of a country (lightweight for lists)
class CountrySummary(BaseModel):
    tag: str                            # 3-letter country tag (e.g. GER, ENG)
    capital_state_id: int | None = None # ID of the capital state
    stability: float | None = None      # Country stability (0-1)
    war_support: float | None = None    # Country war support (0-1)
# End of CountrySummary model

# Full details of a country, includes all data including states and tech.
class CountryDetail(BaseModel):
    tag: str                                # 3-letter country tag (e.g. GER, ENG)
    capital_state_id: int | None = None     # ID of the capital state
    stability: float | None = None          # Country stability (0-1)
    war_support: float | None = None        # Country war support (0-1)
    graphical_culture: str | None = None    # Graphical culture for unit appearances
    graphical_culture_2d: str | None = None # Graphical culture for 2D UI elements
    color_rgb: ColorRGB | None = None       # Country color for UI elements
    owned_states: list[OwnedState] = []              # List of states owned by the country
    starting_technologies: list[StartingTech] = []   # List of starting technologies for the country
# End of CountryDetail model


