# app/schemas/focus.py
from pydantic import BaseModel


class FocusPrereq(BaseModel):
    group: int | None = None
    required_focus_id: str


class FocusItem(BaseModel):
    focus_id: str
    cost: float | None = None
    x_pos: int | None = None
    y_pos: int | None = None
    icon: str | None = None
    dlc_source: str | None = None
    completion_reward: str | None = None
    prerequisites: list[FocusPrereq] = []
    mutually_exclusive: list[str] = []


class FocusTreeSummary(BaseModel):
    focus_tree_id: str
    country_tag: str | None = None


class FocusTreeDetail(BaseModel):
    focus_tree_id: str
    country_tag: str | None = None
    focuses: list[FocusItem] = []
