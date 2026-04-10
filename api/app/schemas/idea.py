# app/schemas/idea.py
from pydantic import BaseModel


class IdeaModifier(BaseModel):
    modifier_key: str
    modifier_value: float | None = None


class IdeaDetail(BaseModel):
    idea_key: str
    slot: str | None = None
    is_law: bool
    cost: float | None = None
    removal_cost: float | None = None
    is_default: bool
    dlc_source: str | None = None
    on_add_effect: str | None = None
    on_remove_effect: str | None = None
    allowed_condition: str | None = None
    modifiers: list[IdeaModifier] = []
