# app/routers/annotations.py
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from app.database import get_db
from app.schemas.annotation import AnnotationCreate, AnnotationOut

router = APIRouter(prefix="/api/v1", tags=["Annotations"])

# GET /api/v1/annotations - list annotations, optional filters: ?entity_type=, ?entity_key=
@router.get("/annotations", response_model=list[AnnotationOut])
async def list_annotations(
    entity_type: str | None = Query(None, description="Filter by entity type (e.g. country, technology)"),
    entity_key: str | None = Query(None, description="Filter by entity key (e.g. GER, infantry_weapons)"),
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    if entity_type and entity_key:
        rows = await db.fetch(
            """
            SELECT annotation_id, entity_type, entity_key, note, created_at
            FROM user_annotations
            WHERE entity_type = $1 AND entity_key = $2
            ORDER BY created_at DESC
            LIMIT $3 OFFSET $4
            """,
            entity_type, entity_key, limit, offset,
        )
    elif entity_type:
        rows = await db.fetch(
            """
            SELECT annotation_id, entity_type, entity_key, note, created_at
            FROM user_annotations
            WHERE entity_type = $1
            ORDER BY created_at DESC
            LIMIT $2 OFFSET $3
            """,
            entity_type, limit, offset,
        )
    else:
        rows = await db.fetch(
            """
            SELECT annotation_id, entity_type, entity_key, note, created_at
            FROM user_annotations
            ORDER BY created_at DESC
            LIMIT $1 OFFSET $2
            """,
            limit, offset,
        )
    return [dict(row) for row in rows]
# End of annotation list endpoint

# GET /api/v1/annotations/{annotation_id} - single annotation
@router.get("/annotations/{annotation_id}", response_model=AnnotationOut)
async def get_annotation(
    annotation_id: int,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT annotation_id, entity_type, entity_key, note, created_at
        FROM user_annotations
        WHERE annotation_id = $1
        """,
        annotation_id,
    )
    if not row:
        raise HTTPException(404, detail="Annotation not found")
    return dict(row)
# End of annotation detail endpoint

# POST /api/v1/annotations - create a new annotation
@router.post("/annotations", response_model=AnnotationOut, status_code=201)
async def create_annotation(
    body: AnnotationCreate,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        INSERT INTO user_annotations (entity_type, entity_key, note)
        VALUES ($1, $2, $3)
        RETURNING annotation_id, entity_type, entity_key, note, created_at
        """,
        body.entity_type, body.entity_key, body.note,
    )
    return dict(row)
# End of annotation create endpoint

# DELETE /api/v1/annotations/{annotation_id} - delete an annotation
@router.delete("/annotations/{annotation_id}", status_code=204)
async def delete_annotation(
    annotation_id: int,
    db=Depends(get_db),
):
    result = await db.execute(
        "DELETE FROM user_annotations WHERE annotation_id = $1",
        annotation_id,
    )
    if result == "DELETE 0":
        raise HTTPException(404, detail="Annotation not found")
# End of annotation delete endpoint
