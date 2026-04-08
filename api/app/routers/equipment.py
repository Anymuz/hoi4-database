# app/routers/equipment.py
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.schemas.equipment import EquipmentItem

router = APIRouter(prefix="/api/v1", tags=["Equipment"])

# GET /api/v1/equipment — list equipment, optional filters: ?archetype=, ?is_archetype=
@router.get("/equipment", response_model=list[EquipmentItem])
async def list_equipment(
    archetype: str | None = Query(None, description="Filter by archetype_key"),
    is_archetype: bool | None = Query(None, description="Filter archetypes only (true) or variants only (false)"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    if archetype:
        rows = await db.fetch(
            """
            SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
                   build_cost_ic, reliability, maximum_speed, defense, breakthrough,
                   soft_attack, hard_attack, ap_attack, air_attack, armor_value,
                   hardness, dlc_source, resources
            FROM api_equipment_catalog
            WHERE archetype_key = $1
            ORDER BY equipment_key
            LIMIT $2 OFFSET $3
            """,
            archetype, limit, offset,
        )
    elif is_archetype is not None:
        rows = await db.fetch(
            """
            SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
                   build_cost_ic, reliability, maximum_speed, defense, breakthrough,
                   soft_attack, hard_attack, ap_attack, air_attack, armor_value,
                   hardness, dlc_source, resources
            FROM api_equipment_catalog
            WHERE is_archetype = $1
            ORDER BY equipment_key
            LIMIT $2 OFFSET $3
            """,
            is_archetype, limit, offset,
        )
    else:
        rows = await db.fetch(
            """
            SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
                   build_cost_ic, reliability, maximum_speed, defense, breakthrough,
                   soft_attack, hard_attack, ap_attack, air_attack, armor_value,
                   hardness, dlc_source, resources
            FROM api_equipment_catalog
            ORDER BY equipment_key
            LIMIT $1 OFFSET $2
            """,
            limit, offset,
        )
    return [dict(row) for row in rows]
# End of equipment list endpoint

# GET /api/v1/equipment/{equipment_key} — single equipment item
@router.get("/equipment/{equipment_key}", response_model=EquipmentItem)
async def get_equipment(
    equipment_key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT equipment_key, is_archetype, archetype_key, parent_key, year,
               build_cost_ic, reliability, maximum_speed, defense, breakthrough,
               soft_attack, hard_attack, ap_attack, air_attack, armor_value,
               hardness, dlc_source, resources
        FROM api_equipment_catalog
        WHERE equipment_key = $1
        """,
        equipment_key,
    )
    if not row:
        raise HTTPException(404, detail=f"Equipment '{equipment_key}' not found")
    return dict(row)
# End of equipment detail endpoint