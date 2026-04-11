# app/schemas/event.py
from __future__ import annotations
from pydantic import BaseModel  # For defining data models and validation

# Pydantic schema (response models) for Events, for API responses and data validation.

# EventOption represents a single option within an event, with its name, index, AI chance factor, trigger and effect blocks.
class EventOption(BaseModel):
    event_option_id: int
    option_name: str | None = None
    option_index: int = 0
    ai_chance_factor: str | None = None
    trigger_block: str | None = None
    effect_block: str | None = None
# End of EventOption model

# Event represents a game event (country_event, news_event, etc.) with its type, title, description, picture, and nested options.
class Event(BaseModel):
    event_key: str
    event_type: str
    title_key: str | None = None
    title_text: str | None = None
    description_key: str | None = None
    picture: str | None = None
    is_triggered_only: bool | None = None
    is_major: bool | None = None
    fire_only_once: bool | None = None
    hidden: bool | None = None
    namespace: str | None = None
    source_file: str | None = None
    options: list[EventOption] = []
# End of Event model
