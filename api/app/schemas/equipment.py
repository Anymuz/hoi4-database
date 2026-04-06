# app/schemas/equipment.py
from pydantic import BaseModel


class EquipmentResource(BaseModel):
    resource_key: str
    amount: float | None = None


class EquipmentItem(BaseModel):
    equipment_key: str
    is_archetype: bool
    archetype_key: str | None = None
    parent_key: str | None = None
    year: int | None = None
    build_cost_ic: float | None = None
    reliability: float | None = None
    maximum_speed: float | None = None
    defense: float | None = None
    breakthrough: float | None = None
    soft_attack: float | None = None
    hard_attack: float | None = None
    ap_attack: float | None = None
    air_attack: float | None = None
    armor_value: float | None = None
    hardness: float | None = None
    dlc_source: str | None = None
    resources: list[EquipmentResource] = []
