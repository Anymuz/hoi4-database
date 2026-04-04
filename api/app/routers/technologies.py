# app/routers/technologies.py
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.dependencies import get_effective_date
from app.schemas.technology import TechSummary, TechTreeItem, StartingTech

# Tech-list and tech-detail endpoints live under /api/v1/technologies
router = APIRouter(prefix="/api/v1/technologies", tags=["Technologies"])

# Country starting-tech endpoint lives under /api/v1/countries/{tag}/technologies
country_tech_router = APIRouter(prefix="/api/v1/countries", tags=["Technologies"])

# GET /api/v1/technologies, list all techs (lightweight, paginated)
# Optional ?folder= to filter by tech tree folder (e.g. infantry_folder)
@router.get("", response_model=list[TechSummary])
async def list_technologies(
    folder: str | None = Query(None, description="Filter by folder (e.g. infantry_folder)"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    if folder:
        rows = await db.fetch(
            """
            SELECT t.technology_key,
                   COALESCE(l.loc_value, t.technology_key) AS technology_name,
                   t.start_year, t.research_cost, t.folder_name
            FROM technologies t
            LEFT JOIN localisation l ON l.loc_key = t.technology_key
            WHERE t.folder_name = $1
            ORDER BY t.technology_key
            LIMIT $2 OFFSET $3
            """,
            folder, limit, offset,
        )
    else:
        rows = await db.fetch(
            """
            SELECT t.technology_key,
                   COALESCE(l.loc_value, t.technology_key) AS technology_name,
                   t.start_year, t.research_cost, t.folder_name
            FROM technologies t
            LEFT JOIN localisation l ON l.loc_key = t.technology_key
            ORDER BY t.technology_key
            LIMIT $1 OFFSET $2
            """,
            limit, offset,
        )
    return [dict(row) for row in rows]
# End of technology list endpoint

# GET /api/v1/technologies/{key}, full detail for one technology
@router.get("/{key}", response_model=TechTreeItem)
async def get_technology(
    key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        "SELECT * FROM api_technology_tree WHERE technology_key = $1",
        key,
    )
    if not row:
        raise HTTPException(404, detail=f"Technology '{key}' not found")
    return dict(row)
# End of technology detail endpoint

# GET /api/v1/countries/{tag}/technologies, starting techs for a country (date-sensitive)
@country_tech_router.get("/{tag}/technologies", response_model=list[StartingTech])
async def list_country_technologies(
    tag: str,
    effective_date: date = Depends(get_effective_date),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT technology_key, technology_name, dlc_source
        FROM api_country_technologies
        WHERE country_tag = $1 AND effective_date <= $2
        ORDER BY technology_key
        """,
        tag.upper(), effective_date,
    )
    return [dict(row) for row in rows]
# End of country technologies endpoint
