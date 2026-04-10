# app/schemas/annotation.py
from datetime import datetime
from pydantic import BaseModel, Field


class AnnotationCreate(BaseModel):
    entity_type: str = Field(..., max_length=50, examples=["country"])
    entity_key: str = Field(..., max_length=200, examples=["GER"])
    note: str = Field(..., min_length=1, examples=["Good for beginners"])


class AnnotationOut(BaseModel):
    annotation_id: int
    entity_type: str
    entity_key: str
    note: str
    created_at: datetime
