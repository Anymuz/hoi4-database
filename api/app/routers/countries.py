# app/routers/countries.py
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.dependencies import get_effective_date
from app.schemas.country import CountrySummary, CountryDetail

# All country endpoints live under /api/v1/countries
router = APIRouter(prefix="/api/v1/countries", tags=["Countries"])

# GET /api/v1/countries, list all countries (paginated, date-sensitive)
@router.get("", response_model=list[CountrySummary])
async def list_countries(
    effective_date: date = Depends(get_effective_date),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT tag, capital_state_id, stability, war_support
        FROM api_country_detail($1)
        ORDER BY tag
        LIMIT $2 OFFSET $3
        """,
        effective_date, limit, offset,
    )
    return [dict(row) for row in rows]
# End of country list endpoint

# GET /api/v1/countries/{tag}, full detail for one country (date-sensitive)
@router.get("/{tag}", response_model=CountryDetail)
async def get_country(
    tag: str,
    effective_date: date = Depends(get_effective_date),
    db=Depends(get_db),
):
    row = await db.fetchrow(
        "SELECT * FROM api_country_detail($1) WHERE tag = $2",
        effective_date, tag.upper(),
    )
    if not row:
        raise HTTPException(404, detail=f"Country '{tag.upper()}' not found")
    return dict(row)
# End of country detail endpoint
