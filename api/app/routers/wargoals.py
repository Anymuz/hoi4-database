# app/routers/wargoals.py
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.schemas.wargoal import WargoalType

router = APIRouter(prefix="/api/v1", tags=["Wargoals"])

# GET /api/v1/wargoals, list all wargoal types
@router.get("/wargoals", response_model=list[WargoalType])
async def list_wargoal_types(db=Depends(get_db)):
    rows = await db.fetch(
        "SELECT * FROM wargoal_types ORDER BY wargoal_key"
    )
    return [dict(r) for r in rows]
# End of wargoal type list endpoint.

# GET /api/v1/wargoals/{key}, get one wargoal type by key
@router.get("/wargoals/{key}", response_model=WargoalType)
async def get_wargoal_type(key: str, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM wargoal_types WHERE wargoal_key = $1", key
    )
    if not row:
        raise HTTPException(404, detail="Wargoal type not found")
    return dict(row)
# End of wargoal type endpoints.