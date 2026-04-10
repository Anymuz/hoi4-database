# app/routers/characters.py
from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import get_db
from app.schemas.character import CharacterSummary, CharacterDetail, CharacterRole

router = APIRouter(prefix="/api/v1", tags=["Characters"]) # Router for character-related endpoints.

# GET /api/v1/countries/{tag}/characters, list all characters (paginated)
@router.get("/countries/{tag}/characters", response_model=list[CharacterSummary])
async def list_characters_by_country(
    tag: str,
    limit: int = Query(50, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db=Depends(get_db),
):
    rows = await db.fetch(
        """
        SELECT character_id, name_key, country_tag, gender
        FROM api_country_characters
        WHERE country_tag = $1
        ORDER BY character_id
        LIMIT $2 OFFSET $3
        """,
        tag.upper(), limit, offset,
    )
    return [dict(row) for row in rows]  
# End of characters by country endpoint  

# GET /api/v1/characters/{character_id}, full detail for one character.
@router.get("/characters/{character_id}", response_model=CharacterDetail)
async def get_character(
    character_id: str,
    db=Depends(get_db),
):
    row = await db.fetchrow(
        """
        SELECT character_id, name_key, country_tag, gender, roles
        FROM api_country_characters
        WHERE character_id = $1
        """,
        character_id,
    )
    if not row:
        raise HTTPException(404, detail=f"Character '{character_id}' not found")
    return dict(row)
# End of character detail endpoint