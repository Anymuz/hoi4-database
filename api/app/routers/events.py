# app/routers/events.py
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.schemas.event import Event, EventOption
import json

router = APIRouter(prefix="/api/v1", tags=["Events"])

# GET /api/v1/events - list all events (uses the api_event_detail view)
@router.get("/events", response_model=list[Event])
async def list_events(
    event_type: str | None = None,
    namespace: str | None = None,
    db=Depends(get_db),
):
    if event_type and namespace:
        rows = await db.fetch(
            "SELECT * FROM api_event_detail WHERE event_type = $1 AND namespace LIKE '%' || $2 || '%' ORDER BY event_key",
            event_type, namespace,
        )
    elif event_type:
        rows = await db.fetch(
            "SELECT * FROM api_event_detail WHERE event_type = $1 ORDER BY event_key",
            event_type,
        )
    elif namespace:
        rows = await db.fetch(
            "SELECT * FROM api_event_detail WHERE namespace LIKE '%' || $1 || '%' ORDER BY event_key",
            namespace,
        )
    else:
        rows = await db.fetch(
            "SELECT * FROM api_event_detail ORDER BY event_key"
        )
    results = []
    for r in rows:
        d = dict(r)
        opts_raw = d.pop("options", [])
        if isinstance(opts_raw, str):
            opts_raw = json.loads(opts_raw)
        d["options"] = [EventOption(**o) for o in opts_raw]
        results.append(d)
    return results
# End of events list endpoint

# GET /api/v1/events/{key} - get one event by key
@router.get("/events/{key}", response_model=Event)
async def get_event(key: str, db=Depends(get_db)):
    row = await db.fetchrow(
        "SELECT * FROM api_event_detail WHERE event_key = $1", key
    )
    if not row:
        raise HTTPException(404, detail="Event not found")
    d = dict(row)
    opts_raw = d.pop("options", [])
    if isinstance(opts_raw, str):
        opts_raw = json.loads(opts_raw)
    d["options"] = [EventOption(**o) for o in opts_raw]
    return d
# End of event detail endpoint
