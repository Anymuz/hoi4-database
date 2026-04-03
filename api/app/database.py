# app/database.py
import json  # For JSON encoding/decoding
import asyncpg # PostgreSQL client library for Python
from contextlib import asynccontextmanager # For creating async context managers
from fastapi import FastAPI, Request # FastAPI framework for building APIs
from app.config import get_settings # Import the get_settings function from app/config.py

# asyncpg returns JSONB columns as raw strings by default.
# This callback registers a codec on every new connection so that
# JSONB values are automatically decoded to Python dicts/lists.
async def _init_connection(conn):
    await conn.set_type_codec(
        'jsonb',
        encoder=json.dumps,
        decoder=json.loads,
        schema='pg_catalog',
    )

# Define an async context manager for DB connection lifecycle
@asynccontextmanager 
async def lifespan(app: FastAPI):
    settings = get_settings()  # From config.py

    # Create a connection pool to the database using the settings from config.py
    app.state.db_pool = await asyncpg.create_pool(
        settings.database_url,
        min_size = 2, # Minimum 2 connections ready
        max_size = 10, # Maximum scale to 10
        init = _init_connection, # Register JSONB codec on each connection
    ) 

    yield # API now serves requests with the connection pool.
    await app.state.db_pool.close() # Close the connection pool on shutdown
# End of lifespan context manager.

# Get a database connection from the pool for a given request.
async def get_db(request: Request): # FastAPI dependency
    async with request.app.state.db_pool.acquire() as conn: 
        yield conn # Yeild connection to requeset handler.
    # Release connection back to the pool after request
# End of get_db function.