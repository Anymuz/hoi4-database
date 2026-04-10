# app/routers/states.py
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.dependencies import get_effective_date
from app.schemas.state import StateSummary, StateDetail

router = APIRouter(prefix="/api/v1", tags=["States"])

# GET /api/v1/states, list all states (paginated, date-sensitive)
# Optional ?owner_tag=GER to filter by owning country
@router.get("/states", response_model=list[StateSummary])
async def list_states(
    effective_date: date = Depends(get_effective_date),
    owner_tag: str | None = Query(None, description="Filter by owner country tag (e.g. GER)"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    if owner_tag:
        rows = await db.fetch(
            """
            SELECT state_id, state_name_key, state_name, state_category, manpower, owner_tag
            FROM api_state_detail($1)
            WHERE owner_tag = $2
            ORDER BY state_id
            LIMIT $3 OFFSET $4
            """,
            effective_date, owner_tag.upper(), limit, offset,
        )
    else:
        rows = await db.fetch(
            """
            SELECT state_id, state_name_key, state_name, state_category, manpower, owner_tag
            FROM api_state_detail($1)
            ORDER BY state_id
            LIMIT $2 OFFSET $3
            """,
            effective_date, limit, offset,
        )
    return [dict(row) for row in rows]
# End of state list endpoint

# GET /api/v1/states/{state_id}, full detail for one state (date-sensitive)
@router.get("/states/{state_id}", response_model=StateDetail)
async def get_state(
    state_id: int,
    effective_date: date = Depends(get_effective_date),
    db=Depends(get_db),
):
    row = await db.fetchrow(
        "SELECT * FROM api_state_detail($1) WHERE state_id = $2",
        effective_date, state_id,
    )
    if not row:
        raise HTTPException(404, detail=f"State {state_id} not found")
    return dict(row)
# End of state detail endpoint