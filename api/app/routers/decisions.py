# app/routers/decisions.py
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.schemas.decision import Decision

router = APIRouter(prefix="/api/v1", tags=["Decisions"])

# GET /api/v1/decisions - list all decisions, optionally filtered by category
@router.get("/decisions", response_model=list[Decision])
async def list_decisions(category: str | None = None, db=Depends(get_db)):
    if category:
        rows = await db.fetch(
            "SELECT * FROM decisions WHERE category_key = $1 ORDER BY decision_key",
            category,
        )
    else:
        rows = await db.fetch(
            "SELECT * FROM decisions ORDER BY decision_key"
        )
    return [dict(r) for r in rows]
# End of decisions list endpoint

# GET /api/v1/decisions/{key} - get one decision by key
@router.get("/decisions/{key}", response_model=Decision)
async def get_decision(key: str, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM decisions WHERE decision_key = $1", key
    )
    if not row:
        raise HTTPException(404, detail="Decision not found")
    return dict(row)
# End of decision detail endpoint
