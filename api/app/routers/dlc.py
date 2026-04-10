# app/routers/dlc.py
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.schemas.dlc import (
    MIOSummary, MIODetail,
    OperationSummary, OperationDetail,
    BOPSummary, BOPDetail,
    FactionSummary, FactionDetail,
    SpecialProjectSummary, SpecialProjectDetail,
)

router = APIRouter(prefix="/api/v1", tags=["DLC"]) 

# GET api/v1/mios, list all MIOS with summary info (date-sensitive)
@router.get("/mios", response_model=list[MIOSummary], tags=["MIOs"])
async def list_mios(
    limit: int = Query(50, ge=1, le=500), # Pagination limit
    offset: int = Query(0, ge=0), # Pagination offset
    db=Depends(get_db), # Get database connection
):
    rows = await db.fetch(
        """
        SELECT organization_key, template_icon, template_key, icon, dlc_source,
        equipment_types
        FROM api_mio_organization_detail
        ORDER BY organization_key
        LIMIT $1 OFFSET $2
        """,
        limit, offset,
    )
    return [dict(row) for row in rows]
# End of MIO list endpoint

# GET api/v1/mios/{organization_key}, full detail for one MIO
@router.get("/mios/{organization_key}", response_model=MIODetail, tags=["MIOs"])
async def get_mio(
    organization_key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT * FROM api_mio_organization_detail 
        WHERE organization_key = $1
        """,
        organization_key,
    )
    if not row:
        raise HTTPException(404, detail=f"MIO '{organization_key}' not found")
    return dict(row)
# End of MIO detail endpoint

# GET /api/v1/operations — list all operations (summary)
@router.get("/operations", response_model=list[OperationSummary], tags=["Operations"])
async def list_operations(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT operation_key, name, days, network_strength, operatives,
               risk_chance, experience, dlc_source
        FROM api_operation_detail
        ORDER BY operation_key
        LIMIT $1 OFFSET $2
        """,
        limit, offset,
    )
    return [dict(row) for row in rows]
# End of operation list endpoint

# GET /api/v1/operations/{operation_key} — single operation with phases & equipment
@router.get("/operations/{operation_key}", response_model=OperationDetail, tags=["Operations"])
async def get_operation(
    operation_key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT * FROM api_operation_detail
        WHERE operation_key = $1
        """,
        operation_key,
    )
    if not row:
        raise HTTPException(404, detail=f"Operation '{operation_key}' not found")
    return dict(row)
# End of operation detail endpoint

# GET /api/v1/bop — list all BoP definitions (summary)
@router.get("/bop", response_model=list[BOPSummary], tags=["Balance of Power"])
async def list_bop(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT bop_key, initial_value, left_side, right_side, decision_category
        FROM api_bop_detail
        ORDER BY bop_key
        LIMIT $1 OFFSET $2
        """,
        limit, offset,
    )
    return [dict(row) for row in rows]
# End of BoP list endpoint

# GET /api/v1/bop/{bop_key} — single BoP with sides, ranges, modifiers
@router.get("/bop/{bop_key}", response_model=BOPDetail, tags=["Balance of Power"])
async def get_bop(
    bop_key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT * FROM api_bop_detail
        WHERE bop_key = $1
        """,
        bop_key,
    )
    if not row:
        raise HTTPException(404, detail=f"Balance of power '{bop_key}' not found")
    return dict(row)
# End of BoP detail endpoint

# GET /api/v1/factions — list all faction templates (summary)
@router.get("/factions", response_model=list[FactionSummary], tags=["Factions"])
async def list_factions(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT template_key, name_loc, manifest_key, icon,
               can_leader_join_other, dlc_source
        FROM api_faction_detail
        ORDER BY template_key
        LIMIT $1 OFFSET $2
        """,
        limit, offset,
    )
    return [dict(row) for row in rows]

# GET /api/v1/factions/{template_key} — single faction with goals, rules, upgrades
@router.get("/factions/{template_key}", response_model=FactionDetail, tags=["Factions"])
async def get_faction(
    template_key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT * FROM api_faction_detail
        WHERE template_key = $1
        """,
        template_key,
    )
    if not row:
        raise HTTPException(404, detail=f"Faction '{template_key}' not found")
    return dict(row)
# End of faction detail endpoint

# GET /api/v1/special-projects — list all special projects (summary)
@router.get("/special-projects", response_model=list[SpecialProjectSummary], tags=["Special Projects"])
async def list_special_projects(
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT project_key, specialization_key, project_tag, complexity,
               prototype_time, dlc_source
        FROM api_special_project_detail
        ORDER BY project_key
        LIMIT $1 OFFSET $2
        """,
        limit, offset,
    )
    return [dict(row) for row in rows]
# End of special project list endpoint

# GET /api/v1/special-projects/{project_key} — single project with rewards
@router.get("/special-projects/{project_key}", response_model=SpecialProjectDetail, tags=["Special Projects"])
async def get_special_project(
    project_key: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT * FROM api_special_project_detail
        WHERE project_key = $1
        """,
        project_key,
    )
    if not row:
        raise HTTPException(404, detail=f"Special project '{project_key}' not found")
    return dict(row)
# End of special project detail endpoint