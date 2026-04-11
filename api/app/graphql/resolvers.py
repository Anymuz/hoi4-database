# app/graphql/resolvers.py
# GraphQL Query resolvers, async functions that fetch data from PostgreSQL.

import strawberry
from datetime import date as date_type
from typing import Optional
from strawberry.types import Info

# Import the GraphQL types that correspond to  database views and tables.
from app.graphql.types import (
    Country, State, Technology, Character, Division,
    FocusTree, Equipment, EquipmentVariant, EquipmentVariantModule,
    EquipmentVariantUpgrade, Idea, Mio, Operation, Bop,
    Faction, SpecialProject, Annotation, Wargoal,
    DiplomaticRelation, StartingFaction, Event, Decision,
    Ideology,
)

# Helper function to get the asyncpg pool from the FastAPI app context.
async def get_pool(info: Info):
    # Each resolver acquires a connection from the app's pool (same fastAPI async pool used by REST) and uses the same SQL views/functions.
    return info.context["request"].app.state.db_pool
# End of get_pool function.

# Helper function to parse date strings, defaulting to 1936-01-01 if not provided.
def _parse_date(date_str: str | None) -> date_type:
    # Convert an ISO date string to a date object, defaulting to 1936-01-01
    return date_type.fromisoformat(date_str) if date_str else date_type(1936, 1, 1)
# End of _parse_date function.

# The Query class defines GraphQL query resolvers. Each corresponds to the GraphQL schema and is used for fetching the data using asyncpg.
@strawberry.type
class Query:
   # Country resolvers use the same api_country_detail view as the REST endpoint, so they automatically support the same ?date= parameter for 1936 vs 1939 data. 
   # This also means they benefit from the same SQL-level protections against invalid dates and SQL injection.
    @strawberry.field
    async def country(
        self,
        info: Info,
        tag: str,
        date: Optional[str] = None,
    ) -> Optional[Country]:
        pool = await get_pool(info)
        date_obj = _parse_date(date)
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM api_country_detail($1) WHERE tag = $2",
                date_obj, tag.upper(),
            )
            if not row:
                return None
            return Country.from_row(row)
    # End of country resolver.

    # Countries list resolver, also supports ?date= for 1936 vs 1939 data, and pagination with limit/offset.
    @strawberry.field
    async def countries(
        self,
        info: Info,
        date: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[Country]:
        pool = await get_pool(info)
        date_obj = _parse_date(date)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """SELECT * FROM api_country_detail($1)
                   ORDER BY tag LIMIT $2 OFFSET $3""",
                date_obj, limit, offset,
            )
            return [Country.from_row(r) for r in rows]
    # End of countries resolver.

    # State and states resolvers also use the same api_state_detail view as the REST endpoint, so they also support ?date= and the same protections.
    @strawberry.field
    async def state(
        self,
        info: Info,
        state_id: int,
        date: Optional[str] = None,
    ) -> Optional[State]:
        pool = await get_pool(info)
        date_obj = _parse_date(date)
        async with pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM api_state_detail($1) WHERE state_id = $2",
                date_obj, state_id,
            )
            if not row:
                return None
            return State.from_row(row)
    # End of state resolver.

    # States list resolver, supports ?date= and pagination, and also optional filtering by owner_tag (country that owns the state).
    @strawberry.field
    async def states(
        self,
        info: Info,
        date: Optional[str] = None,
        owner_tag: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[State]:
        pool = await get_pool(info)
        date_obj = _parse_date(date)
        async with pool.acquire() as conn:
            if owner_tag:
                rows = await conn.fetch(
                    """SELECT * FROM api_state_detail($1)
                       WHERE owner_tag = $2
                       ORDER BY state_id LIMIT $3 OFFSET $4""",
                    date_obj, owner_tag.upper(), limit, offset,
                )
            else:
                rows = await conn.fetch(
                    """SELECT * FROM api_state_detail($1)
                       ORDER BY state_id LIMIT $2 OFFSET $3""",
                    date_obj, limit, offset,
                )
            return [State.from_row(r) for r in rows]
    # End of states resolver.

    # Technologies resolvers use the api_technology_tree view, supporting optional folder filtering and pagination.
    @strawberry.field
    async def technologies(
        self,
        info: Info,
        folder: Optional[str] = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[Technology]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if folder:
                rows = await conn.fetch(
                    """SELECT * FROM api_technology_tree
                       WHERE folder_name = $1
                       ORDER BY technology_key LIMIT $2 OFFSET $3""",
                    folder, limit, offset,
                )
            else:
                rows = await conn.fetch(
                    """SELECT * FROM api_technology_tree
                       ORDER BY technology_key LIMIT $1 OFFSET $2""",
                    limit, offset,
                )
            return [Technology.from_row(r) for r in rows]
    # End of technologies resolver.
    
    # Characters are historical generals/leaders associated with countries. Uses the api_country_characters view, which supports filtering by country_tag and pagination.
    @strawberry.field
    async def characters(
        self,
        info: Info,
        country_tag: Optional[str] = None,
    ) -> list[Character]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if country_tag:
                rows = await conn.fetch(
                    """SELECT * FROM api_country_characters
                       WHERE country_tag = $1""",
                    country_tag.upper(),
                )
            else:
                rows = await conn.fetch("SELECT * FROM api_country_characters")
            return [Character.from_row(r) for r in rows]
    # End of characters resolver.

    # Divisions are military templates used by countries. Uses the api_country_divisions view, which supports filtering by country_tag and also by oob_file for 1936 vs 1939 templates (defaulting to 1936 if not provided).
    @strawberry.field
    async def divisions(
        self,
        info: Info,
        country_tag: str,
        date: Optional[str] = None,
    ) -> list[Division]:
        pool = await get_pool(info)
        date_obj = _parse_date(date)
        oob_suffix = "1936" if date_obj.year == 1936 else "1939"
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                """SELECT * FROM api_country_divisions
                   WHERE country_tag = $1
                     AND (oob_file LIKE '%_' || $2 || '%'
                          OR oob_file IS NULL OR oob_file = '')
                   ORDER BY template_name""",
                country_tag.upper(), oob_suffix,
            )
            return [Division.from_row(r) for r in rows]
    # End of divisions resolver.

    # Focus trees are national focus trees associated with countries. Uses the api_focus_tree_detail view, which supports filtering by country_tag.
    @strawberry.field
    async def focus_trees(
        self,
        info: Info,
        country_tag: Optional[str] = None,
    ) -> list[FocusTree]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if country_tag:
                rows = await conn.fetch(
                    """SELECT * FROM api_focus_tree_detail
                       WHERE country_tag = $1""",
                    country_tag.upper(),
                )
            else:
                rows = await conn.fetch("SELECT * FROM api_focus_tree_detail")
            return [FocusTree.from_row(r) for r in rows]
    # End of focus trees resolver.
  
    # Equipment resolvers use the api_equipment_catalog view, which supports filtering by archetype_key or is_archetype boolean, as well as pagination.
    @strawberry.field
    async def equipment(
        self,
        info: Info,
        archetype: Optional[str] = None,
        is_archetype: Optional[bool] = None,
    ) -> list[Equipment]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if archetype:
                rows = await conn.fetch(
                    """SELECT * FROM api_equipment_catalog
                       WHERE archetype_key = $1
                       ORDER BY equipment_key""",
                    archetype,
                )
            elif is_archetype is not None:
                rows = await conn.fetch(
                    """SELECT * FROM api_equipment_catalog
                       WHERE is_archetype = $1
                       ORDER BY equipment_key""",
                    is_archetype,
                )
            else:
                rows = await conn.fetch(
                    "SELECT * FROM api_equipment_catalog ORDER BY equipment_key",
                )
            return [Equipment.from_row(r) for r in rows]
    # End of equipment resolver.

    # Ideas are national spirits, laws, and modifiers that provide bonuses or penalties to countries. Uses the api_ideas_detail view, which supports filtering by slot (national spirit, law, etc) or by is_law boolean.
    @strawberry.field
    async def ideas(
        self,
        info: Info,
        slot: Optional[str] = None,
        is_law: Optional[bool] = None,
    ) -> list[Idea]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if slot:
                rows = await conn.fetch(
                    """SELECT * FROM api_ideas_detail
                       WHERE slot = $1 ORDER BY idea_key""",
                    slot,
                )
            elif is_law is not None:
                rows = await conn.fetch(
                    """SELECT * FROM api_ideas_detail
                       WHERE is_law = $1 ORDER BY idea_key""",
                    is_law,
                )
            else:
                rows = await conn.fetch(
                    "SELECT * FROM api_ideas_detail ORDER BY idea_key",
                )
            return [Idea.from_row(r) for r in rows]
    # End of ideas resolver.

    # MIOs are military intelligence organizations. Uses the api_mio_organization_detail view. (DLC)
    @strawberry.field
    async def mios(self, info: Info) -> list[Mio]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM api_mio_organization_detail ORDER BY organization_key",
            )
            return [Mio.from_row(r) for r in rows]

    # Operations are special missions or tasks that can be performed by countries. Uses the api_operation_detail view. (DLC)
    @strawberry.field
    async def operations(self, info: Info) -> list[Operation]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM api_operation_detail ORDER BY operation_key",
            )
            return [Operation.from_row(r) for r in rows]

    # Balance of Power (BoP) is a DLC feature that provides additional gameplay mechanics. Uses the api_bop_detail view. (DLC)
    @strawberry.field
    async def bop(self, info: Info) -> list[Bop]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM api_bop_detail ORDER BY bop_key",
            )
            return [Bop.from_row(r) for r in rows]
    # End of BoP resolver.

    # Factions are groups of countries with shared goals and rules. Uses the api_faction_detail view. (DLC)
    @strawberry.field
    async def factions(self, info: Info) -> list[Faction]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM api_faction_detail ORDER BY template_key",
            )
            return [Faction.from_row(r) for r in rows]
    # End of factions resolver.
    
    # Special projects are unique R&D projects that provide powerful bonuses. Uses the api_special_project_detail view. (DLC)
    @strawberry.field
    async def special_projects(self, info: Info) -> list[SpecialProject]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM api_special_project_detail ORDER BY project_key",
            )
            return [SpecialProject.from_row(r) for r in rows]
    # End of special projects resolver.

    #  Equipment variants are specific versions of equipment with different modules or upgrades.
    @strawberry.field
    async def equipment_variants(
        self,
        info: Info,
        owner_tag: Optional[str] = None,
    ) -> list[EquipmentVariant]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if owner_tag:
                rows = await conn.fetch(
                    """SELECT equipment_variant_id, owner_tag, base_equipment_key,
                              version_name, effective_date::text
                       FROM equipment_variants
                       WHERE owner_tag = $1
                       ORDER BY base_equipment_key""",
                    owner_tag.upper(),
                )
            else:
                rows = await conn.fetch(
                    """SELECT equipment_variant_id, owner_tag, base_equipment_key,
                              version_name, effective_date::text
                       FROM equipment_variants
                       ORDER BY owner_tag, base_equipment_key""",
                )
            variant_ids = [r["equipment_variant_id"] for r in rows]
            if variant_ids:
                mod_rows = await conn.fetch(
                    """SELECT equipment_variant_id, slot_name, module_key
                       FROM equipment_variant_modules
                       WHERE equipment_variant_id = ANY($1)""",
                    variant_ids,
                )
                upg_rows = await conn.fetch(
                    """SELECT equipment_variant_id, upgrade_key, upgrade_level
                       FROM equipment_variant_upgrades
                       WHERE equipment_variant_id = ANY($1)""",
                    variant_ids,
                )
            else:
                mod_rows, upg_rows = [], []
            mods_by_id: dict[int, list] = {}
            for mr in mod_rows:
                mods_by_id.setdefault(mr["equipment_variant_id"], []).append(
                    EquipmentVariantModule(slot_name=mr["slot_name"], module_key=mr["module_key"])
                )
            upgs_by_id: dict[int, list] = {}
            for ur in upg_rows:
                upgs_by_id.setdefault(ur["equipment_variant_id"], []).append(
                    EquipmentVariantUpgrade(upgrade_key=ur["upgrade_key"], upgrade_level=ur["upgrade_level"])
                )
            return [
                EquipmentVariant(
                    **dict(r),
                    modules=mods_by_id.get(r["equipment_variant_id"], []),
                    upgrades=upgs_by_id.get(r["equipment_variant_id"], []),
                )
                for r in rows
            ]
    # End of equipment variants resolver.

    # Annotations are user-generated notes attached to various entities (countries, states, etc). Stored in a separate user_annotations table, supports filtering by entity_type and entity_key.
    @strawberry.field
    async def annotations(
        self,
        info: Info,
        entity_type: Optional[str] = None,
        entity_key: Optional[str] = None,
    ) -> list[Annotation]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if entity_type and entity_key:
                rows = await conn.fetch(
                    """SELECT annotation_id, entity_type, entity_key, note, created_at
                       FROM user_annotations
                       WHERE entity_type = $1 AND entity_key = $2
                       ORDER BY created_at DESC""",
                    entity_type, entity_key,
                )
            elif entity_type:
                rows = await conn.fetch(
                    """SELECT annotation_id, entity_type, entity_key, note, created_at
                       FROM user_annotations
                       WHERE entity_type = $1
                       ORDER BY created_at DESC""",
                    entity_type,
                )
            else:
                rows = await conn.fetch(
                    """SELECT annotation_id, entity_type, entity_key, note, created_at
                       FROM user_annotations
                       ORDER BY created_at DESC""",
                )
            return [Annotation(**dict(r)) for r in rows]
    # End of annotations resolver.

    # Wargoals are the objectives that countries can have in wars. Uses the wargoal_types table.
    @strawberry.field
    async def wargoals(self, info: Info) -> list[Wargoal]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM wargoal_types ORDER BY wargoal_key"
            )
            return [Wargoal.from_row(r) for r in rows]
    # End of wargoals resolver.

    # Diplomatic relations from country history files.
    @strawberry.field
    async def diplomatic_relations(self, info: Info, country_tag: Optional[str] = None) -> list[DiplomaticRelation]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if country_tag:
                rows = await conn.fetch(
                    "SELECT * FROM diplomatic_relations WHERE country_tag = $1 ORDER BY target_tag",
                    country_tag.upper(),
                )
            else:
                rows = await conn.fetch(
                    "SELECT * FROM diplomatic_relations ORDER BY country_tag, target_tag"
                )
            return [DiplomaticRelation.from_row(r) for r in rows]
    # End of diplomatic_relations resolver.

    # Starting factions with their members.
    @strawberry.field
    async def starting_factions(self, info: Info) -> list[StartingFaction]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM api_starting_factions ORDER BY faction_template_key"
            )
            return [StartingFaction.from_row(r) for r in rows]
    # End of starting_factions resolver.

    # Events with nested options from the api_event_detail view.
    @strawberry.field
    async def events(self, info: Info, event_type: Optional[str] = None, namespace: Optional[str] = None) -> list[Event]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if event_type and namespace:
                rows = await conn.fetch(
                    "SELECT * FROM api_event_detail WHERE event_type = $1 AND namespace LIKE '%' || $2 || '%' ORDER BY event_key",
                    event_type, namespace,
                )
            elif event_type:
                rows = await conn.fetch(
                    "SELECT * FROM api_event_detail WHERE event_type = $1 ORDER BY event_key",
                    event_type,
                )
            elif namespace:
                rows = await conn.fetch(
                    "SELECT * FROM api_event_detail WHERE namespace LIKE '%' || $1 || '%' ORDER BY event_key",
                    namespace,
                )
            else:
                rows = await conn.fetch(
                    "SELECT * FROM api_event_detail ORDER BY event_key"
                )
            return [Event.from_row(r) for r in rows]
    # End of events resolver.

    # Decisions with scripted effect blocks.
    @strawberry.field
    async def decisions(self, info: Info, category: Optional[str] = None) -> list[Decision]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            if category:
                rows = await conn.fetch(
                    "SELECT * FROM decisions WHERE category_key = $1 ORDER BY decision_key",
                    category,
                )
            else:
                rows = await conn.fetch(
                    "SELECT * FROM decisions ORDER BY decision_key"
                )
            return [Decision.from_row(r) for r in rows]
    # End of decisions resolver.

    # Ideologies - political ideology tree with sub-ideologies.
    @strawberry.field
    async def ideologies(self, info: Info) -> list[Ideology]:
        pool = await get_pool(info)
        async with pool.acquire() as conn:
            rows = await conn.fetch(
                "SELECT * FROM api_ideology_detail ORDER BY ideology_key"
            )
            return [Ideology.from_row(r) for r in rows]
    # End of ideologies resolver.
# End of Query class.