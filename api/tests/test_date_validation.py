# tests/test_date_validation.py
# Tests for the ?date= query parameter validation logic.

import pytest
from datetime import date
from fastapi import HTTPException
from app.dependencies import get_effective_date

# Tests for get_effective_date function in app/dependencies.py:
def test_default_date():
    # Test that no date provided returns the default 1936-01-01
    result = get_effective_date(None)
    assert result == date(1936, 1, 1) # Shuld return the default date of January 1, 1936
# End of default date test

def test_valid_date_1939():
    # 1939-08-14 is in the allowed list so should return that date
    result = get_effective_date("1939-08-14")
    assert result == date(1939, 8, 14) # Should return the provided date of August 14, 1939
# End of valid date test

def test_invalid_date_400():
    # A date not in the allowed list should raise HTTPException with 400
    with pytest.raises(HTTPException) as exc_info: # with is used to assert that an exception is raised
        get_effective_date("2000-01-01")
    assert exc_info.value.status_code == 400 # Raised exception should be 400 for an invalid date
# End of invalid date test
# -----------------------------------------------