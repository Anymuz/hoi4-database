# app/dependencies.py
from datetime import date # Python date objects
from fastapi import Query, HTTPException # FastAPI query parameters and error handling
from app.config import get_settings # Import get_settings from app/config.py

# Validate and parse the '?date=' query parameter for API endpoints.
def get_effective_date (
    date_str: str | None = Query (
        None, # Default to none, will be overridden to default date from config.py
        alias = "date", # parameter name
        description = "Bookmark date: 1936-01-01 (default) or 1939-08-14",
        examples = ["1936-01-01", "1939-08-14"]
    ),
) -> date:
    settings = get_settings() # from config.py
    raw_date = date_str or settings.default_date # Use provided date or default
    
    # Block values not from allowed dates to prevent SQL injection
    if raw_date not in settings.allowed_dates: 
        raise HTTPException(status_code = 400, detail = f"Invalid date '{raw_date}'! Must use one of: {settings.allowed_dates}")
    return date.fromisoformat(raw_date) # Return python date object for API handlers.
# End of get_effective_date function.