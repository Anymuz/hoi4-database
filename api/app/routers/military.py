# app/routers/military.py
from datetime import date
from fastapi import APIRouter, Depends, Query
from app.database import get_db
from app.dependencies import get_effective_date
from app.schemas.military import DivisionDetail, NavalDetail, AirWingItem

router = APIRouter(prefix="/api/v1", tags=["Military"])

# GET /api/v1/countries/{tag}/divisions, division templates + deployed units (date-sensitive)
@router.get("/countries/{tag}/divisions", response_model=list[DivisionDetail], tags=["Land Forces"])
async def list_divisions(
    tag: str,
    effective_date: date = Depends(get_effective_date),
    db=Depends(get_db),
):
    oob_suffix = "1936" if effective_date.year == 1936 else "1939"
    rows = await db.fetch(
        """
        SELECT country_tag, division_template_id, template_name, oob_file,
               regiments, support, deployed_divisions
        FROM api_country_divisions
        WHERE country_tag = $1
          AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
        ORDER BY template_name
        """,
        tag.upper(), oob_suffix,
    )
    return [dict(row) for row in rows]
# End of divisions endpoint

# GET /api/v1/countries/{tag}/naval, fleets + task forces + ships (date-sensitive)
@router.get("/countries/{tag}/naval", response_model=list[NavalDetail], tags=["Naval Forces"])
async def list_naval(
    tag: str,
    effective_date: date = Depends(get_effective_date),
    db=Depends(get_db),
):
    oob_suffix = "1936" if effective_date.year == 1936 else "1939"
    rows = await db.fetch(
        """
        SELECT country_tag, fleet_id, fleet_name, naval_base_province_id, oob_file,
               task_forces
        FROM api_country_naval
        WHERE country_tag = $1
          AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
        ORDER BY fleet_name
        """,
        tag.upper(), oob_suffix,
    )
    return [dict(row) for row in rows]
# End of naval endpoint

# GET /api/v1/countries/{tag}/air, air wings (date-sensitive)
@router.get("/countries/{tag}/air", response_model=list[AirWingItem], tags=["Air Forces"])
async def list_air(
    tag: str,
    effective_date: date = Depends(get_effective_date),
    db=Depends(get_db),
):
    oob_suffix = "1936" if effective_date.year == 1936 else "1939"
    rows = await db.fetch(
        """
        SELECT country_tag, location_state_id, state_name_key,
               equipment_type, amount, wing_name, version_name, oob_file
        FROM api_country_air
        WHERE country_tag = $1
          AND (oob_file LIKE '%_' || $2 || '%' OR oob_file IS NULL OR oob_file = '')
        ORDER BY location_state_id
        """,
        tag.upper(), oob_suffix,
    )
    return [dict(row) for row in rows]
# End of air endpoint
