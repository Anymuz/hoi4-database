# app/routers/diplomacy.py
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.schemas.diplomacy import DiplomaticRelation, StartingFaction, FactionMember
import json

router = APIRouter(prefix="/api/v1", tags=["Diplomacy"])

# GET /api/v1/diplomacy - list all diplomatic relations
@router.get("/diplomacy", response_model=list[DiplomaticRelation])
async def list_diplomatic_relations(country_tag: str | None = None, db=Depends(get_db)):
    if country_tag:
        rows = await db.fetch(
            "SELECT * FROM diplomatic_relations WHERE country_tag = $1 ORDER BY target_tag",
            country_tag.upper(),
        )
    else:
        rows = await db.fetch(
            "SELECT * FROM diplomatic_relations ORDER BY country_tag, target_tag"
        )
    return [dict(r) for r in rows]
# End of diplomatic relations list endpoint

# GET /api/v1/diplomacy/{id} - get one diplomatic relation
@router.get("/diplomacy/{relation_id}", response_model=DiplomaticRelation)
async def get_diplomatic_relation(relation_id: int, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM diplomatic_relations WHERE diplomatic_relation_id = $1",
        relation_id,
    )
    if not row:
        raise HTTPException(404, detail="Diplomatic relation not found")
    return dict(row)
# End of diplomatic relation detail endpoint

# GET /api/v1/factions/starting - list all starting factions with members
@router.get("/factions/starting", response_model=list[StartingFaction])
async def list_starting_factions(db=Depends(get_db)):
    rows = await db.fetch(
        "SELECT * FROM api_starting_factions ORDER BY faction_template_key"
    )
    results = []
    for r in rows:
        d = dict(r)
        members_raw = d.pop("members", [])
        if isinstance(members_raw, str):
            members_raw = json.loads(members_raw)
        d["members"] = [FactionMember(**m) for m in members_raw]
        results.append(d)
    return results
# End of starting factions list endpoint

# GET /api/v1/factions/starting/{id} - get one starting faction
@router.get("/factions/starting/{faction_id}", response_model=StartingFaction)
async def get_starting_faction(faction_id: int, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM api_starting_factions WHERE starting_faction_id = $1",
        faction_id,
    )
    if not row:
        raise HTTPException(404, detail="Starting faction not found")
    d = dict(row)
    members_raw = d.pop("members", [])
    if isinstance(members_raw, str):
        members_raw = json.loads(members_raw)
    d["members"] = [FactionMember(**m) for m in members_raw]
    return d
# End of starting faction detail endpoint