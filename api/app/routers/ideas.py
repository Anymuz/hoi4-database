# app/routers/ideas.py
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.schemas.idea import IdeaDetail

router = APIRouter(prefix="/api/v1", tags=["Ideas"])

# GET /api/v1/ideas — list ideas, optional filters: ?slot=, ?is_law=
@router.get("/ideas", response_model=list[IdeaDetail])
async def list_ideas(
    slot: str | None = Query(None, description="Filter by slot (e.g. economy, trade_laws)"),
    is_law: bool | None = Query(None, description="Filter laws only (true) or non-laws only (false)"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    if slot:
        rows = await db.fetch(
            """
            SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
                   dlc_source, modifiers
            FROM api_ideas_detail
            WHERE slot = $1
            ORDER BY idea_key
            LIMIT $2 OFFSET $3
            """,
            slot, limit, offset,
        )
    elif is_law is not None:
        rows = await db.fetch(
            """
            SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
                   dlc_source, modifiers
            FROM api_ideas_detail
            WHERE is_law = $1
            ORDER BY idea_key
            LIMIT $2 OFFSET $3
            """,
            is_law, limit, offset,
        )
    else:
        rows = await db.fetch(
            """
            SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
                   dlc_source, modifiers
            FROM api_ideas_detail
            ORDER BY idea_key
            LIMIT $1 OFFSET $2
            """,
            limit, offset,
        )
    return [dict(row) for row in rows]
# End of idea list endpoint

# GET /api/v1/ideas/{idea_key} — single idea
@router.get("/ideas/{idea_key}", response_model=IdeaDetail)
async def get_idea(
    idea_key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT idea_key, slot, is_law, cost, removal_cost, is_default,
               dlc_source, modifiers
        FROM api_ideas_detail
        WHERE idea_key = $1
        """,
        idea_key,
    )
    if not row:
        raise HTTPException(404, detail=f"Idea '{idea_key}' not found")
    return dict(row)
# End of idea detail endpoint