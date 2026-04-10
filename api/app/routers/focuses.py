# app/routers/focuses.py
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.schemas.focus import FocusTreeSummary, FocusTreeDetail

router = APIRouter(prefix="/api/v1", tags=["Focus Trees"])

# GET /api/v1/focus-trees - list all focus trees (lightweight, no focuses array)
@router.get("/focus-trees", response_model=list[FocusTreeSummary])
async def list_focus_trees(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT focus_tree_id, country_tag
        FROM api_focus_tree_detail
        ORDER BY focus_tree_id
        LIMIT $1 OFFSET $2
        """,
        limit, offset,
    )
    return [dict(row) for row in rows]
# End of focus tree list endpoint

# GET /api/v1/focus-trees/{focus_tree_id} - single tree with all focuses
@router.get("/focus-trees/{focus_tree_id}", response_model=FocusTreeDetail)
async def get_focus_tree(
    focus_tree_id: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT focus_tree_id, country_tag, focuses
        FROM api_focus_tree_detail
        WHERE focus_tree_id = $1
        """,
        focus_tree_id,
    )
    if not row:
        raise HTTPException(404, detail=f"Focus tree '{focus_tree_id}' not found")
    return dict(row)
# End of focus tree detail endpoint

# GET /api/v1/countries/{tag}/focus-tree - tree for a country
@router.get("/countries/{tag}/focus-tree", response_model=FocusTreeDetail)
async def get_country_focus_tree(
    tag: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT focus_tree_id, country_tag, focuses
        FROM api_focus_tree_detail
        WHERE country_tag = $1
        """,
        tag.upper(),
    )
    if not row:
        raise HTTPException(404, detail=f"No focus tree for country '{tag.upper()}'")
    return dict(row)
# End of country focus tree endpoint