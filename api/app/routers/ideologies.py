# app/routers/ideologies.py
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.schemas.ideology import Ideology, ColorRGB, SubIdeology

router = APIRouter(prefix="/api/v1", tags=["Ideologies"])

# Helper to convert a database row into an Ideology response dict.
def _row_to_ideology(row) -> dict:
    d = dict(row)
    d["color_rgb"] = {"r": d.pop("color_r"), "g": d.pop("color_g"), "b": d.pop("color_b")}
    d["sub_ideologies"] = [dict(s) for s in (d.get("sub_ideologies") or [])]
    return d
# End of _row_to_ideology helper.

# GET /api/v1/ideologies, list all ideologies with nested sub-ideologies
@router.get("/ideologies", response_model=list[Ideology])
async def list_ideologies(db=Depends(get_db)):
    rows = await db.fetch(
        "SELECT * FROM api_ideology_detail ORDER BY ideology_key"
    )
    return [_row_to_ideology(r) for r in rows]
# End of ideology list endpoint.

# GET /api/v1/ideologies/{key}, get one ideology by key with nested sub-ideologies
@router.get("/ideologies/{key}", response_model=Ideology)
async def get_ideology(key: str, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM api_ideology_detail WHERE ideology_key = $1", key
    )
    if not row:
        raise HTTPException(404, detail="Ideology not found")
    return _row_to_ideology(row)
# End of ideology endpoints.
