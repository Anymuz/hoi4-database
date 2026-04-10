# app/schemas/decision.py
from pydantic import BaseModel  # For defining data models and validation

# Pydantic schema (response models) for Decisions, for API responses and data validation.

# Decision represents a political/military decision in the game, with its category, cost, scripted effect blocks, and metadata.
class Decision(BaseModel):
    decision_key: str
    category_key: str
    icon: str | None = None
    cost: int | None = None
    allowed: str | None = None
    available: str | None = None
    visible: str | None = None
    complete_effect: str | None = None
    remove_effect: str | None = None
    fire_only_once: bool | None = None
    dlc_source: str | None = None
# End of Decision model
