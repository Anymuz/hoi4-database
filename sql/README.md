# SQL Directory - Design Rationale

This directory contains two checked-in SQL files (`schema.sql`, `views.sql`) plus two generated seed scripts (`seed-load-order.sql`, `seed-docker.sql`). The seed scripts are **not** in the repository - they are generated locally by running `gen_seed_sql.py` and `gen_seed_docker.py` (see `tools/db_etl/`). This document explains **what** each file does and **why** it is structured the way it is.

---

## File Overview

| File | Purpose | Size |
|---|---|---|
| `schema.sql` | DDL - creates all 157 tables, 4 deferred FKs, 61 indexes | ~1,910 lines |
| `views.sql` | 16 read-only API views + 2 date-parameterised functions that pre-join and aggregate related tables | ~790 lines |
| `seed-load-order.sql` | **Generated locally** - FK-safe `\copy` commands with explicit column lists across 7 tiers, plus staging tables for FK resolution, wrapped in a transaction. Run `python tools/db_etl/gen_seed_sql.py` to produce it. | ~280 lines |
| `seed-docker.sql` | **Generated locally** - server-side `COPY` variant of `seed-load-order.sql` for use inside a Docker container. Run `python tools/db_etl/gen_seed_docker.py` to produce it. | ~280 lines |

---

## schema.sql

### What it does

A single transactional DDL script (`BEGIN` … `COMMIT`) that creates the entire database in one atomic pass. If any statement fails, the whole schema rolls back cleanly.

### Why one file?

PostgreSQL supports transactional DDL - unlike MySQL, a `CREATE TABLE` inside a transaction can be rolled back. Putting everything in one file means you can run `psql -f schema.sql` and either get the complete schema or nothing. No partial state to debug.

### Organisation - Phases, not alphabetical

Tables are grouped by **game domain** (Phases 1–28 + V2), not alphabetically. This mirrors how the game data is structured:

- **Phase 1** creates root reference tables (terrain, resources, buildings, ideologies) that everything else depends on
- **Phase 2** creates geography (provinces, strategic regions, supply nodes)
- **Phase 3** creates countries and their history
- Phases 4–28 build up increasingly specific game systems
- **V2** adds wargoal types, starting diplomacy, and events

This ordering matters because PostgreSQL requires referenced tables to exist before you can create an FK pointing at them. The phase order is a topological sort of the FK dependency graph.

### Why "Slice A" appears first

The first 15 tables (`countries`, `states`, `provinces`, etc.) were built during an early prototyping phase ("Slice A") and already had working DDL. Rather than rewriting them, they were preserved at the top of the file. The remaining 142 tables follow in phase order below. The deferred `ALTER TABLE` statements at the bottom tie Slice A tables to Phase 1 reference tables that didn't exist when Slice A was written.

### Key design patterns

#### Natural keys for game entities

Game-defined identifiers are used as primary keys wherever possible:

```sql
tag CHAR(3) PRIMARY KEY           -- country tags: GER, ENG, USA
technology_key VARCHAR(120) PRIMARY KEY  -- infantry_weapons, nuclear_reactor
terrain_type VARCHAR(40) PRIMARY KEY     -- plains, forest, mountain
```

**Why:** HOI4's data files reference entities by these string keys everywhere. Using them as PKs means no mapping layer is needed - the FK values in the database match what the game files contain. This makes ETL simpler and queries more readable (`WHERE tag = 'GER'` instead of joining through an ID lookup).

#### Surrogate keys for instance/history tables

Tables that record *instances* or *historical snapshots* use auto-incrementing IDs:

```sql
state_ownership_history_id BIGSERIAL PRIMARY KEY
province_building_id       BIGSERIAL PRIMARY KEY
```

**Why:** These rows don't have a natural single-column identifier. A state can be owned by different countries at different dates, so the PK needs to be synthetic. `BIGSERIAL` is used over `SERIAL` as a safety margin - some junction tables (like province buildings across all states × dates) could theoretically exceed 2 billion rows in an extended dataset.

#### Effective dates for temporal data

History tables include an `effective_date DATE` column with a unique constraint:

```sql
UNIQUE (state_id, resource_key, effective_date)
```

**Why:** HOI4 supports two start dates (1936 and 1939). The game engine replays all history blocks where `date <= start_date`. By storing the effective date, we can query either starting state:

```sql
-- Get Germany's 1936 technologies
SELECT * FROM country_starting_technologies
WHERE country_tag = 'GER' AND effective_date <= '1936-01-01';

-- Get Germany's 1939 technologies (includes 1936 + 1939 additions)
SELECT * FROM country_starting_technologies
WHERE country_tag = 'GER' AND effective_date <= '1939-01-01';
```

#### The DLC guard column

Most tables include a nullable `dlc_source VARCHAR(50)`:

```sql
dlc_source VARCHAR(50)  -- NULL = base game, 'La Résistance' = DLC-gated
```

**Why:** HOI4 has 37 DLCs. Many game entities only exist when a specific DLC is active, guarded by `has_dlc = "DLC Name"` checks in the source files. Storing this allows API consumers to filter results by owned DLCs, or to see base-game-only content.

#### Deferred FK constraints (ALTER TABLE)

Four foreign keys are added via `ALTER TABLE` at the bottom of the file instead of inline:

1. `countries.capital_state_id -> states` - countries are defined before states in game files, but reference them
2. `provinces.continent_id -> continents` - provinces were in Slice A, continents were added in Phase 1
3. `provinces.terrain -> terrain_types` - same reason
4. `states.state_category -> state_categories` - same reason

**Why:** These are circular or cross-phase dependencies. The referenced table doesn't exist yet when the referencing table is created. PostgreSQL's `ALTER TABLE ADD CONSTRAINT` resolves this cleanly.

#### Self-referential FKs

Several tables reference themselves:

- **`equipment_definitions`** - `archetype_key` and `parent_key` both point back to `equipment_definitions`. Equipment forms an inheritance chain (e.g., `infantry_equipment_1` -> `infantry_equipment_0` -> `infantry_equipment` archetype). Both FKs are declared `DEFERRABLE INITIALLY DEFERRED` so that bulk-loading equipment rows in any order succeeds - PostgreSQL defers constraint checking until `COMMIT`.
- **`occupation_laws`** - `fallback_law_key` references another occupation law as a fallback.
- **`focus_prerequisites` / `focus_mutually_exclusive`** - focuses reference other focuses.
- **`mio_trait_prerequisites` / `mio_trait_exclusions`** - MIO traits form prerequisite trees and exclusion pairs.

**Why:** These mirror actual game mechanics where entities form trees, chains, or peer relationships.

#### Schema refinements after initial load

The schema was originally designed from game file structures before full data extraction. Loading real data revealed mismatches that required refinements. All fixes were applied to the extraction script (`export_markdown_dump.py`) so the pipeline now produces clean data, but the schema also absorbed changes:

| Category | Count | Examples |
|---|---|---|
| Column types widened | 5 | `operations.experience` INT -> NUMERIC(5,2); `mio_*.owner_type` VARCHAR(10) -> VARCHAR(15) |
| NOT NULL relaxed | 8 | `medal_tiers.variable`, `province_adjacencies.adjacency_type`, `equipment_variants.version_name` |
| Self-referential FKs made deferrable | 2 | `equipment_definitions.archetype_key`, `equipment_definitions.parent_key` |
| FK intentionally omitted | 1 | `country_starting_ideas.idea_key` - character-advisor names are used as idea keys but don't exist as rows in `ideas` |

All other FK constraints (126 total) are fully enforced. DLC data loads successfully - the extraction script now captures DLC equipment, sub-ideologies, focus trees, and technologies that were originally missing.

### Index strategy

61 indexes (2 UNIQUE + 59 regular B-tree) are defined after all table definitions. They are grouped by phase, matching the table ordering, and follow the naming convention `ix_<table>_<column_description>` (or `uq_` for unique constraints).

#### Why indexes are placed at the end of schema.sql

All 63 `CREATE INDEX` statements live after the final `ALTER TABLE`. This lets PostgreSQL build each index on the fully populated table in a single pass during initial load, rather than maintaining the index row-by-row across thousands of `COPY` inserts. For the seed workflow (load via `seed-load-order.sql`, then `\i schema.sql` to add indexes), this ordering gives the fastest possible bulk load.

#### Category 1 - UNIQUE indexes (3)

These enforce business rules that the table's primary key alone cannot guarantee:

| Index | Table | Columns | Why |
|---|---|---|---|
| `uq_state_ownership_history` | state_ownership_history | `(state_id, effective_date)` | A state can only change ownership once per date. Without this, duplicate history rows could silently appear. |
| `uq_country_starting_technologies` | country_starting_technologies | `(country_tag, technology_key, effective_date, COALESCE(dlc_source, ''))` | A country can research a technology once per date per DLC context. The `COALESCE` wrapper is necessary because PostgreSQL treats NULLs as distinct in unique indexes - without it, two rows with `dlc_source = NULL` would both be allowed. |

**Note:** The third unique-named index `uq_state_ownership_history` also doubles as a covering index for the most common history query pattern: `WHERE state_id = $1 AND effective_date <= $2 ORDER BY effective_date DESC LIMIT 1`.

#### Category 2 - History date-range indexes (6)

History tables store time-series data with `effective_date` columns. The game engine replays all events up to a bookmark date, so the dominant query pattern is:

```sql
WHERE <parent_id> = $1 AND effective_date <= $2
ORDER BY effective_date DESC LIMIT 1
```

These composite indexes put the parent FK first (equality filter) and date second (range scan):

| Index | Table | Columns |
|---|---|---|
| `ix_province_controller_history_state_date` | province_controller_history | `(state_id, effective_date)` |
| `ix_state_resources_state_date` | state_resources | `(state_id, effective_date)` |
| `ix_state_buildings_state_date` | state_buildings | `(state_id, effective_date)` |
| `ix_province_buildings_state_date` | province_buildings | `(state_id, effective_date)` |
| `ix_state_ownership_history_owner` | state_ownership_history | `(owner_tag, effective_date)` |
| `ix_state_ownership_history_controller` | state_ownership_history | `(controller_tag, effective_date)` |

**Column order matters.** `(state_id, effective_date)` supports equality on `state_id` + range on `effective_date`. Reversing the order would require a full index scan for a specific state - PostgreSQL can only use leading columns for equality.

#### Category 3 - Country/owner FK indexes (10)

The API views' most common join pattern is "fetch everything for a given country." These indexes turn those joins from sequential scans into index lookups:

| Index | Table | Column | Used by view |
|---|---|---|---|
| `ix_characters_country` | characters | `country_tag` | `api_country_characters` |
| `ix_division_templates_country` | division_templates | `country_tag` | `api_country_divisions` |
| `ix_divisions_country` | divisions | `country_tag` | `api_country_divisions` |
| `ix_air_wings_country` | air_wings | `country_tag` | `api_country_air` |
| `ix_country_starting_ideas_country` | country_starting_ideas | `country_tag` | `api_country_detail` |
| `ix_country_starting_technologies_country_date` | country_starting_technologies | `(country_tag, effective_date)` | `api_country_technologies` |
| `ix_equipment_variants_owner` | equipment_variants | `owner_tag` | `api_country_naval` |
| `ix_country_starting_doctrines_country` | country_starting_doctrines | `country_tag` | - (future doctrine view) |

Plus 2 name/slot lookups that filter within a domain:

| Index | Table | Column | Purpose |
|---|---|---|---|
| `ix_states_name` | states | `state_name_key` | Text search for states by name |
| `ix_ideas_slot` | ideas | `slot` | Filter ideas by slot (political_advisor, theorist, etc.) |

#### Category 4 - Parent->child FK indexes (19)

These index the FK column on the "many" side of one-to-many relationships, enabling efficient joins from parent to children:

| Index | Table | Column | Parent table |
|---|---|---|---|
| `ix_equipment_definitions_archetype` | equipment_definitions | `archetype_key` | equipment_definitions (self) |
| `ix_equipment_resources_equipment` | equipment_resources | `equipment_key` | equipment_definitions |
| `ix_character_roles_character` | character_roles | `character_id` | characters |
| `ix_divisions_template` | divisions | `division_template_id` | division_templates |
| `ix_ships_task_force` | ships | `task_force_id` | task_forces |
| `ix_idea_modifiers_idea` | idea_modifiers | `idea_key` | ideas |
| `ix_focuses_tree` | focuses | `focus_tree_id` | focus_trees |
| `ix_focus_prerequisites_focus` | focus_prerequisites | `focus_id` | focuses |
| `ix_technology_prerequisites_prereq` | technology_prerequisites | `prerequisite_key` | technologies |
| `ix_technology_enables_equipment_equip` | technology_enables_equipment | `equipment_key` | equipment_definitions |
| `ix_mio_organizations_template` | mio_organizations | `template_key` | mio_templates |
| `ix_mio_traits_owner` | mio_traits | `(owner_key, owner_type)` | mio_templates / mio_organizations |
| `ix_mio_trait_bonuses_token` | mio_trait_bonuses | `trait_token` | mio_traits |
| `ix_raids_category` | raids | `category_key` | raid_categories |
| `ix_unit_medal_modifiers_medal` | unit_medals | `medal_key` | medals |
| `ix_bop_ranges_side` | bop_ranges | `(bop_key, side_id)` | balance_of_power / bop_sides |
| `ix_bop_range_modifiers_range` | bop_range_modifiers | `range_id` | bop_ranges |
| `ix_continuous_focuses_palette` | continuous_focuses | `palette_id` | continuous_focus_palettes |
| `ix_dynamic_modifier_effects_modifier` | dynamic_modifier_effects | `modifier_key` | dynamic_modifiers |

#### Category 5 - Graph/adjacency indexes (4)

Province connectivity tables have two FK columns forming edges. Both sides are indexed so traversal works in either direction:

| Index | Table | Column |
|---|---|---|
| `ix_province_adjacencies_from` | province_adjacencies | `from_province_id` |
| `ix_province_adjacencies_to` | province_adjacencies | `to_province_id` |
| `ix_province_railways_from` | province_railways | `from_province_id` |
| `ix_province_railways_to` | province_railways | `to_province_id` |

#### Category 6 - Composite lookup indexes (4)

These combine multiple columns for DLC-specific or sequence-based lookups:

| Index | Table | Columns | Purpose |
|---|---|---|---|
| `ix_operations_dlc` | operations | `dlc_source` | Filter espionage operations by DLC origin |
| `ix_operation_phase_options_group` | operation_phase_options | `(operation_key, sequence_index)` | Retrieve phase options in order |
| `ix_intel_agency_upgrade_levels_upgrade` | intel_agency_upgrade_levels | `(upgrade_key, level_index)` | Retrieve upgrade tiers in order |
| `ix_peace_cost_modifiers_category` | peace_cost_modifiers | `category_key` | Filter peace actions by category |

#### Category 7 - Doctrine hierarchy indexes (4)

The Phase 23 doctrine system forms a 4-level tree (folders -> tracks -> grand doctrines -> subdoctrines). Each level is indexed on its parent FK:

| Index | Table | Column |
|---|---|---|
| `ix_doctrine_tracks_folder` | doctrine_tracks | `folder_key` |
| `ix_grand_doctrines_folder` | grand_doctrines | `folder_key` |
| `ix_subdoctrines_track` | subdoctrines | `track_key` |
| `ix_country_starting_doctrines_country` | country_starting_doctrines | `country_tag` |

#### What is NOT indexed (and why)

Not every FK column has an index. Indexes are omitted when:

1. **The table is small enough for a sequential scan.** Reference tables like `terrain_types` (15 rows), `resources` (6 rows), `ideologies` (4 rows), and `building_types` (~20 rows) are always fully cached in PostgreSQL's buffer pool. An index lookup would actually be slower than a sequential scan on these.

2. **The FK is on the "one" side of a relationship.** Columns like `states.continent_id` or `provinces.terrain_type_key` reference small parent tables. The join direction is parent->child (fetch terrain name for a province), which uses the parent's PK index, not a child FK index.

3. **No API view currently joins on that column.** For instance, `strategic_region_provinces.strategic_region_id` isn't indexed because no view currently queries "all provinces in a strategic region" - the `api_state_detail` view joins provinces through states instead. Indexes can always be added later if new views need them.

4. **The column is already the leading column of the PK.** Tables with composite PKs like `(focus_id, prerequisite_focus_id)` already have an index on the leading column via the PK's B-tree. A separate index on `focus_id` alone would be redundant.

---

## views.sql

### What it does

Defines 16 `CREATE OR REPLACE VIEW` statements plus 2 date-parameterised functions that pre-join related tables and aggregate child rows into JSONB arrays. These are the intended read interface for the REST + GraphQL API.

### Why views instead of direct queries?

1. **Encapsulation** - API endpoints map 1:1 to views. The FastAPI layer just does `SELECT * FROM api_country_detail WHERE tag = $1`.
2. **Complex joins are defined once** - a country detail involves 5+ tables. Writing that join in every API handler is error-prone.
3. **The views are not materialised** - they're regular views, so they always reflect current data. Materialisation would only help if the data were large and rarely updated, which doesn't apply to a game database that's loaded once.

### The five slices

Views are grouped by access pattern:

| Slice | Views | Use Case |
|---|---|---|
| **A** - Country & State | `api_country_detail`, `api_state_detail` | "Show me Germany" or "Show me State 64" - the most common queries |
| **B** - Domain catalogs | `api_country_technologies`, `api_technology_tree`, `api_country_characters`, `api_country_divisions`, `api_country_naval`, `api_country_air`, `api_focus_tree_detail`, `api_equipment_catalog`, `api_ideas_detail` | Browse a specific game system across all countries or drill into one country's data |
| **C** - DLC systems | `api_mio_organization_detail`, `api_operation_detail`, `api_bop_detail`, `api_faction_detail`, `api_special_project_detail` | DLC-specific queries - only relevant when the DLC is owned |
| **D** - Diplomacy & Factions | `api_starting_factions` | Pre-war alliance structures |
| **E** - Events | `api_event_detail` | Event catalogue with response options |

**Why this grouping?** It matches how a strategy guide generator or game assistant would query the data. You'd ask "What does Germany start with?" (Slice A), then drill into "What's in Germany's focus tree?" (Slice B), then optionally "What MIOs does Germany have?" (Slice C), then "Who are Germany's allies?" (Slice D) or "What events can fire?" (Slice E).

### The JSONB aggregation pattern

Most views follow the same structure:

```sql
SELECT
    parent.columns,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object('key1', child.col1, 'key2', child.col2)
            ORDER BY child.sort_col
        )
        FROM child_table child
        WHERE child.parent_id = parent.id
    ), '[]'::jsonb) AS children
FROM parent_table parent;
```

**Why JSONB?**
- A REST API returns JSON. Building it in SQL means the API layer just serialises the row - no ORM needed.
- `COALESCE(..., '[]'::jsonb)` ensures empty arrays instead of NULLs - cleaner for API consumers.
- Correlated subqueries with `jsonb_agg` avoid the row-multiplication problem that `LEFT JOIN` + `GROUP BY` causes with multiple child tables.

### The 1936 date filter

Slice A views hardcode `WHERE effective_date = DATE '1936-01-01'`:

```sql
WITH ownership_1936 AS (
    SELECT ... FROM state_ownership_history
    WHERE soh.effective_date = DATE '1936-01-01'
)
```

**Why hardcoded?** Regular views can't accept parameters. When the API is built, these will likely become functions or the date filter will be applied in the API layer. For now, 1936 is the default start date and covers the most common use case.

---

## seed-load-order.sql

### What it does

An executable psql script that loads all 157 tables in FK-safe order across 7 tiers. Every `\copy` command uses an explicit column list so SERIAL/BIGSERIAL primary keys are auto-generated and CSV column order does not need to match the schema. Six tables that need FK resolution from natural keys to surrogate IDs use staging temp tables with `INSERT ... SELECT ... JOIN`. The entire load is wrapped in `BEGIN`/`COMMIT` with `\set ON_ERROR_STOP on`, so any failure rolls back cleanly.

This file is generated by `tools/db_etl/gen_seed_sql.py`, which reads CSV headers and produces the column lists automatically. Re-run the generator after any schema or CSV column changes.

### Why does it exist?

When loading data into the database, you can't insert a row that references a foreign key target that doesn't exist yet. For example, you can't insert a `state_provinces` row before both `states` and `provinces` are loaded. The seed-load-order solves this by defining a safe sequence.

### The tier system

Tables are grouped into 7 tiers based on their FK dependencies:

| Tier | Count | Rule | Example |
|---|---|---|---|
| 0 | 32 | No FK dependencies at all | `continents`, `terrain_types`, `ideologies`, `doctrine_folders` |
| 1 | 32 | Depends only on Tier 0 tables | `provinces` -> terrains + continents, `doctrine_tracks` -> doctrine_folders |
| 2 | 23 | Depends on Tier 0 + 1 | `equipment_resources` -> equipment_definitions + resource_types |
| 3 | 12 | Depends on Tier 0–2 | `countries` -> states (which depends on state_categories) |
| 4 | 15 | Depends on `countries` (Tier 3) | `characters`, `division_templates`, `focus_trees` |
| 5 | 9 | Depends on Tier 4 entities | `character_roles` -> characters, `focuses` -> focus_trees |
| 6 | 4 | Leaf tables - deepest FK chains | `ships` -> task_forces -> fleets -> countries |

**Why tiers instead of a flat list?** Within a tier, order doesn't matter and tables can be loaded in parallel. This is useful for ETL performance - you can batch-load all 32 Tier 0 tables simultaneously.

### Explicit column lists

Every `\copy` command specifies its column list explicitly:

```sql
\copy technologies(technology_key, research_cost, start_year, folder_name, source_file) FROM 'data/csv/technologies.csv' WITH (FORMAT csv, HEADER);
```

**Why explicit columns?** Tables with `SERIAL` or `BIGSERIAL` primary keys auto-generate their IDs during load. Without a column list, PostgreSQL would expect the CSV to provide the auto-generated column. Explicit column lists also make the load resilient to CSV column reordering.

### FK staging tables

Six tables need FK resolution from natural keys (present in CSVs) to surrogate IDs (generated during load). These use temporary staging tables:

1. `division_template_regiments` - resolves `template_name` -> `division_template_id`
2. `division_template_support` - same approach
3. `task_forces` - resolves `(country_tag, fleet_name)` -> `fleet_id`
4. `ships` - resolves `(country_tag, fleet_name, task_force_name)` -> `task_force_id`
5. `bookmark_countries` - resolves `bookmark_name` -> `bookmark_id`
6. `character_role_traits` - resolves `(character_id, role_type)` -> `character_role_id`

The pattern is: load CSV into a temp table with all-TEXT columns, then `INSERT INTO ... SELECT ... JOIN` to resolve the natural keys, then drop the temp table.

### `\copy` vs `COPY`

`\copy` is a psql client-side command that reads from the local filesystem. `COPY` is a server-side command that reads from the server's filesystem. `seed-load-order.sql` uses `\copy` for native installs where the CSV files are on your machine. `seed-docker.sql` uses `COPY` because the CSVs are copied into the container filesystem (see below).

### Reloading data

To reload all data from scratch, drop and recreate the database:

```bash
dropdb hoi4 && createdb hoi4
psql -d hoi4 -f sql/schema.sql
psql -d hoi4 -f sql/seed-load-order.sql
```

Alternatively, truncate all tables in reverse tier order before reloading:

```sql
TRUNCATE focus_mutually_exclusive, focus_prerequisites, ships, character_role_traits CASCADE;
-- ... working backwards to Tier 0
TRUNCATE continents, terrain_types, ... doctrine_folders CASCADE;
```

---

## seed-docker.sql

### What it does

A Docker-compatible variant of `seed-load-order.sql`. It is **generated** by `tools/db_etl/gen_seed_docker.py`, which performs two mechanical transformations:

1. `\copy table(cols) FROM 'data/csv/file.csv'` -> `COPY table (cols) FROM '/data_csv/file.csv'` - switches from client-side `\copy` to server-side `COPY` and remaps paths from the local `data/csv/` to the container mount `/data_csv/`.
2. Removes the `\set ON_ERROR_STOP on` psql directive (not valid in plain SQL).

The file retains the same `BEGIN`/`COMMIT` transaction wrapper, tier ordering, and staging-table logic as the native version.

### Why a separate file?

Inside a Docker container, psql runs as a server process. Server-side `COPY` reads from the container's filesystem, so CSVs must be copied into the container first (`docker cp data/csv/ hoi4-db:/data_csv/`). The client-side `\copy` command doesn't work when psql is executed via `docker exec`.

See `tools/db_etl/runbook.md` -> **Step 3 Option A** for the full Docker deployment workflow.

---

## How the four files work together

```
1. schema.sql           ->  Creates empty tables with all constraints
2. seed-load-order.sql  ->  Loads data (native PostgreSQL, uses \copy)
   seed-docker.sql      ->  Loads data (Docker container, uses COPY)
3. views.sql            ->  Creates the read interface on top of filled tables
```

### Native PostgreSQL workflow
```bash
psql -d hoi4 -f sql/schema.sql
psql -d hoi4 -f sql/seed-load-order.sql   # reads data/csv/ from local filesystem
psql -d hoi4 -f sql/views.sql
```

### Docker workflow
```bash
docker exec -i hoi4-db psql -U hoi4 -d hoi4 < sql/schema.sql
docker cp data/csv/. hoi4-db:/data_csv/
docker cp sql/seed-docker.sql hoi4-db:/tmp/seed.sql
docker exec -i hoi4-db psql -U hoi4 -d hoi4 -f /tmp/seed.sql
docker exec -i hoi4-db psql -U hoi4 -d hoi4 < sql/views.sql
```

Then query via views: `SELECT * FROM api_country_detail WHERE tag = 'GER'`
