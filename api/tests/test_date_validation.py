# tests/test_date_validation.py
# Tests for the ?date= query parameter validation logic.

import pytest
from datetime import date
from fastapi import HTTPException
from app.dependencies import get_effective_date

def test_default_date():
    """No date provided → returns the default 1936-01-01."""
    result = get_effective_date(None)
    assert result == date(1936, 1, 1)

def test_valid_date_1939():
    """1939-08-14 is in the allowed list → returns that date."""
    result = get_effective_date("1939-08-14")
    assert result == date(1939, 8, 14)

def test_invalid_date_400():
    """A date not in the allowed list → raises HTTPException with 400."""
    with pytest.raises(HTTPException) as exc_info:
        get_effective_date("2000-01-01")
    assert exc_info.value.status_code == 400
