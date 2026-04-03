# tests/conftest.py
# Shared test fixtures used by every test file in this directory.
# pytest automatically discovers conftest.py and makes its fixtures available.

import asyncio
import asyncpg
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.database import get_db
from app.config import get_settings

settings = get_settings()

# One pytest loop for all tests, using a single event loop to avoid DOSsing the API with loop creation overhead.
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop # Loop opens to connection pool
    loop.close()
# Endd of event_loop fixture.

# Create a seperate asyncpg connection pool testing, this connects to the database the same way as our API
@pytest_asyncio.fixture(scope="session")
async def db_pool():
    pool = await asyncpg.create_pool(settings.database_url, min_size=1, max_size=3)
    yield pool # Pool opens to connections
    await pool.close()
# End of db_pool fixture.

# Override the app's get_db dependency to use our test pool, so tests operate on the real database but through our own controlled pool.
@pytest_asyncio.fixture(scope="session")
async def client(db_pool):
    # Hands over a connection from our test pool to the API handlers for each test request.
    async def _test_get_db():
        async with db_pool.acquire() as conn:
            yield conn # Connection opens to API handlers
    # End of _test_get_db function.

    # Override the get_db dependency in the app.
    app.dependency_overrides[get_db] = _test_get_db 

    # Use ASGITransport to simulate real HTTP requests without network overhead.
    transport = ASGITransport(app=app) 

    # Create an AsyncClient that sends requests to our FastAPI app directly
    async with AsyncClient(transport=transport, base_url="http://test") as ac: 
        yield ac # Client is yeilded to simulate HTTP requests to the API handlers

    # Restore original dependencies after tests to avoid side effects and contamination between tests.
    app.dependency_overrides.clear() 
# End of client fixture.