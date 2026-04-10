# app/main.py
from fastapi import FastAPI # FastAPI framework for building APIs
from fastapi.middleware.cors import CORSMiddleware # Middleware to handle Cross-Origin Resource Sharing (CORS)
from app.config import get_settings # Import get_settings from app/config.py to access configuration 
from app.database import lifespan # Import the DB connection pool lifespan context manager from app/database.py

settings = get_settings() # From config.py, loads settings from .env or defaults (cached for efficiency)

# OpenAPI tag list - controls how endpoints are grouped in Swagger UI (/docs).
# Each tag maps to a router, defined here so the categories appear in order.
tags_metadata = [
    {"name": "Countries",        "description": "Country tags, starting stats, owned states, technologies"},
    {"name": "States",           "description": "States, buildings, resources, provinces"},
    {"name": "Technologies",     "description": "Tech trees, prerequisites, unlocks"},
    {"name": "Characters",       "description": "Leaders, generals, admirals, advisors, traits"},
    {"name": "Land Forces",      "description": "Division templates, regiments, deployed divisions"},
    {"name": "Naval Forces",     "description": "Fleets, task forces, ships"},
    {"name": "Air Forces",       "description": "Air wings"},
    {"name": "Focus Trees",      "description": "National focus trees, prerequisites, mutual exclusions"},
    {"name": "Equipment",        "description": "Equipment definitions, stats, resource costs"},
    {"name": "Ideas",            "description": "Ideas, national spirits, laws, modifiers"},
    {"name": "MIOs",             "description": "Military-Industrial Organizations (DLC: Arms Against Tyranny)"},
    {"name": "Operations",       "description": "Espionage operations (DLC: La Résistance)"},
    {"name": "Balance of Power", "description": "Balance of power mechanics (DLC: various)"},
    {"name": "Factions",         "description": "Faction templates, goals, rules (DLC: Götterdämmerung)"},
    {"name": "Special Projects", "description": "Special R&D projects (DLC: Götterdämmerung)"},
    {"name": "Wargoals",         "description": "Wargoal type definitions (casus belli)"},
    {"name": "Diplomacy",        "description": "Starting diplomatic relations, autonomy, factions"},
    {"name": "Events",           "description": "Country events, news events, and other game events"},
    {"name": "Decisions",        "description": "Political and military decisions with scripted effects"},
    {"name": "Annotations",      "description": "User-created notes on game entities"},
]

# Create the FastAPI application.
app = FastAPI(
    # shown in Swagger UI header and OpenAPI schema
    title=settings.app_title,
    version=settings.app_version,
    lifespan=lifespan, # from database.py, manages the connection pool lifecycle
    openapi_tags=tags_metadata # groups endpoints by category in Swagger UI
)

# Cross-Origin Resource Sharing (CORS) middleware, sets protocols for calling the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # "*" means no domain restrictions, restrict this for public release API
    allow_methods=["GET", "POST", "DELETE"], # Inly these three HTTP methods are needed (secure by design)
    allow_headers=["*"], # "*" means allow all headers, restrict this for public release API
)

# Health check endpoint to 'ping' and verify the API is running, returns 200 to confirm up status.
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
# End of health_check endpoint.

# Mount REST routers - each handles one domain under /api/v1/
from app.routers import characters, countries, equipment, focuses, ideas, military, states, technologies, dlc, annotations, wargoals, diplomacy, events, decisions

app.include_router(countries.router)
app.include_router(states.router)
app.include_router(technologies.router)
app.include_router(characters.router)
app.include_router(military.router)
app.include_router(focuses.router)
app.include_router(equipment.router)
app.include_router(ideas.router)
app.include_router(diplomacy.router)
app.include_router(dlc.router)
app.include_router(annotations.router)
app.include_router(wargoals.router)
app.include_router(events.router)
app.include_router(decisions.router)

# Mount GraphQL endpoint - shares the same asyncpg pool as REST.
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")