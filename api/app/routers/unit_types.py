# app/routers/unit_types.py
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.schemas.unit_type import UnitType

router = APIRouter(prefix="/api/v1", tags=["Unit Types"])

# GET /api/v1/unit-types, list all unit types with optional unit_group filter
@router.get("/unit-types", response_model=list[UnitType])
async def list_unit_types(
    unit_group: str | None = Query(None),
    db=Depends(get_db),
):
    if unit_group:
        rows = await db.fetch(
            "SELECT * FROM api_unit_type_detail WHERE unit_group = $1 ORDER BY unit_type_key",
            unit_group,
        )
    else:
        rows = await db.fetch(
            "SELECT * FROM api_unit_type_detail ORDER BY unit_type_key"
        )
    return [dict(r) for r in rows]
# End of unit type list endpoint.

# GET /api/v1/unit-types/{key}, get one unit type by key
@router.get("/unit-types/{key}", response_model=UnitType)
async def get_unit_type(key: str, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM api_unit_type_detail WHERE unit_type_key = $1", key
    )
    if not row:
        raise HTTPException(404, detail="Unit type not found")
    return dict(row)
# End of unit type endpoints.
