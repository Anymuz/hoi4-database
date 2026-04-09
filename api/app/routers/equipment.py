# app/routers/equipment.py
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.schemas.equipment import EquipmentItem, EquipmentVariantSummary, EquipmentVariantDetail, VariantModule, VariantUpgrade

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


# GET /api/v1/equipment-variants — list equipment variants, optional owner_tag filter
@router.get("/equipment-variants", response_model=list[EquipmentVariantSummary], tags=["Equipment Variants"])
async def list_equipment_variants(
    owner_tag: str | None = Query(None, description="Filter by country tag (e.g. GER)"),
    base_equipment_key: str | None = Query(None, description="Filter by base equipment key"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    if owner_tag and base_equipment_key:
        rows = await db.fetch(
            """SELECT equipment_variant_id, owner_tag, base_equipment_key,
                      version_name, effective_date::text
               FROM equipment_variants
               WHERE owner_tag = $1 AND base_equipment_key = $2
               ORDER BY version_name
               LIMIT $3 OFFSET $4""",
            owner_tag.upper(), base_equipment_key, limit, offset,
        )
    elif owner_tag:
        rows = await db.fetch(
            """SELECT equipment_variant_id, owner_tag, base_equipment_key,
                      version_name, effective_date::text
               FROM equipment_variants
               WHERE owner_tag = $1
               ORDER BY base_equipment_key, version_name
               LIMIT $2 OFFSET $3""",
            owner_tag.upper(), limit, offset,
        )
    elif base_equipment_key:
        rows = await db.fetch(
            """SELECT equipment_variant_id, owner_tag, base_equipment_key,
                      version_name, effective_date::text
               FROM equipment_variants
               WHERE base_equipment_key = $1
               ORDER BY owner_tag, version_name
               LIMIT $2 OFFSET $3""",
            base_equipment_key, limit, offset,
        )
    else:
        rows = await db.fetch(
            """SELECT equipment_variant_id, owner_tag, base_equipment_key,
                      version_name, effective_date::text
               FROM equipment_variants
               ORDER BY owner_tag, base_equipment_key
               LIMIT $1 OFFSET $2""",
            limit, offset,
        )
    return [dict(row) for row in rows]


# GET /api/v1/equipment-variants/{variant_id} — detail with modules and upgrades
@router.get("/equipment-variants/{variant_id}", response_model=EquipmentVariantDetail, tags=["Equipment Variants"])
async def get_equipment_variant(
    variant_id: int,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """SELECT equipment_variant_id, owner_tag, base_equipment_key,
                  version_name, effective_date::text
           FROM equipment_variants
           WHERE equipment_variant_id = $1""",
        variant_id,
    )
    if not row:
        raise HTTPException(404, detail=f"Equipment variant {variant_id} not found")
    mod_rows = await db.fetch(
        """SELECT slot_name, module_key
           FROM equipment_variant_modules
           WHERE equipment_variant_id = $1
           ORDER BY slot_name""",
        variant_id,
    )
    upg_rows = await db.fetch(
        """SELECT upgrade_key, upgrade_level
           FROM equipment_variant_upgrades
           WHERE equipment_variant_id = $1
           ORDER BY upgrade_key""",
        variant_id,
    )
    result = dict(row)
    result["modules"] = [VariantModule(**dict(m)) for m in mod_rows]
    result["upgrades"] = [VariantUpgrade(**dict(u)) for u in upg_rows]
    return result