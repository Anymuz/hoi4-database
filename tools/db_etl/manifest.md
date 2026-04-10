# HOI4 Database ETL - Module Manifest

Status: **COMPLETE** - full pipeline extracts, converts, and loads all 151 schema tables (~225K rows).

## Overview

The ETL pipeline has four stages:

1. **Extract** - `export_markdown_dump.py` reads HOI4 game files and writes markdown tables to `docs/data-dump/` (160 files, ~220K rows across 23 schema phases). The script contains ~85 parser functions covering every table in the schema.
2. **Extract localisation** - `export_localisation.py` reads 189 `*_l_english.yml` files from `localisation/english/` and writes `data/csv/localisation.csv` (117,490 English display-name translations).
3. **Transform** - `md_to_csv.py` reads those markdown tables, renames columns to match the schema, merges multi-source tables (e.g., countries), splits multi-target files (e.g., focus_links), and writes CSV files to `data/csv/`.
4. **Generate** - `gen_seed_sql.py` produces `sql/seed-load-order.sql` (native `\copy` commands); `gen_seed_docker.py` produces `sql/seed-docker.sql` (Docker `COPY` commands). Both use explicit column lists and FK staging tables.
5. **Load** - PostgreSQL loads via `psql -f sql/seed-load-order.sql` (native) or `psql -f sql/seed-docker.sql` (Docker container). Localisation is loaded separately via `COPY localisation FROM ... CSV HEADER`.

Each extraction module is a function in `export_markdown_dump.py`.

---

## Pipeline Scripts

| Script | Purpose | Input | Output |
|---|---|---|---|
| `export_markdown_dump.py` | Parse HOI4 game files | Game install directory | `docs/data-dump/` (160 .md files) |
| `export_localisation.py` | Extract English display names | `localisation/english/` (game install) | `data/csv/localisation.csv` (117,490 rows) |
| `md_to_csv.py` | Convert markdown -> CSV | `docs/data-dump/` | `data/csv/` (149 .csv files) |
| `gen_seed_sql.py` | Generate native seed SQL | `data/csv/` headers | `sql/seed-load-order.sql` |
| `gen_seed_docker.py` | Generate Docker seed SQL | `sql/seed-load-order.sql` | `sql/seed-docker.sql` |
| `validate_data.py` | FK/PK/NOT NULL checks | `docs/data-dump/` | Console report |

---

## Module Inventory

### Module 01: `parse_continents`
- **Input**: `map/continent.txt`
- **Output tables**: `continents`
- **Row estimate**: 7
- **Notes**: Simple ordered list. Assign sequential continent_id.

### Module 02: `parse_terrain`
- **Input**: `map/definition.csv` (distinct terrain column)
- **Output tables**: `terrain_types`
- **Row estimate**: ~15
- **Notes**: Extract unique terrain values before loading provinces.

### Module 03: `parse_provinces`
- **Input**: `map/definition.csv`
- **Output tables**: `provinces`
- **Row estimate**: ~13,000
- **Notes**: CSV; province_id, R, G, B, province_kind, is_coastal, terrain_key, continent_id. FK to terrain_types and continents.

### Module 04: `parse_resources`
- **Input**: `common/resources/00_resources.txt`
- **Output tables**: `resource_types`
- **Row estimate**: 6
- **Notes**: Paradox Script blocks; extract key, icon_frame, cic, convoys.

### Module 05: `parse_building_types`
- **Input**: `common/buildings/00_buildings.txt`
- **Output tables**: `building_types`
- **Row estimate**: ~18
- **Notes**: Extract level caps, base_cost, shares_slots, province vs state flag.

### Module 06: `parse_state_categories`
- **Input**: `common/state_category/*.txt`
- **Output tables**: `state_categories`
- **Row estimate**: ~10
- **Notes**: Extract category key and local_building_slots.

### Module 07: `parse_ideologies`
- **Input**: `common/ideologies/00_ideologies.txt`
- **Output tables**: `ideologies`, `sub_ideologies`
- **Row estimate**: 4 ideologies, ~18 sub-ideologies
- **Notes**: Top-level blocks -> ideologies. Nested `types` -> sub_ideologies.

### Module 08: `parse_technologies`
- **Input**: `common/technologies/*.txt`
- **Output tables**: `technologies`, `technology_categories`, `technology_categories_junction`, `technology_prerequisites`, `technology_enables_equipment`, `technology_enables_units`
- **Row estimate**: ~400 techs, ~50 categories, ~800 junction rows
- **Notes**: Complex; multiple sub-blocks per tech. DLC-gated techs have `has_dlc` guards.

### Module 09: `parse_unit_types`
- **Input**: `common/units/*.txt` (exclude `equipment/` subdirectory)
- **Output tables**: `unit_types`
- **Row estimate**: ~60
- **Notes**: One block per unit type. Air/naval types may lack combat_width.

### Module 10: `parse_equipment`
- **Input**: `common/units/equipment/*.txt`
- **Output tables**: `equipment_definitions`, `equipment_resources`
- **Row estimate**: ~350 equipment, ~500 resource rows
- **Notes**: Archetype vs variant inheritance. NULL stats on variants = inherited from archetype. DLC-gated entries.

### Module 11: `parse_country_tags`
- **Input**: `common/country_tags/00_countries.txt`
- **Output tables**: `countries` (tag, country_file_path)
- **Row estimate**: ~80
- **Notes**: `TAG = "countries/File.txt"` lines. First pass - creates country rows.

### Module 12: `parse_country_definitions`
- **Input**: `common/countries/*.txt`
- **Output tables**: `countries` (UPDATE: color_r/g/b, graphical_culture)
- **Row estimate**: ~80 updates
- **Notes**: Second pass - enriches existing country rows with color and culture.

### Module 13: `parse_country_history`
- **Input**: `history/countries/*.txt`
- **Output tables**: `countries` (UPDATE: capital, stability, war_support, convoys, ruling_party, last_election), `country_starting_technologies`, `country_starting_ideas`
- **Row estimate**: ~80 country updates, ~4000 tech rows, ~300 idea rows
- **Notes**: Third pass for countries. Complex: dated blocks, DLC conditionals, set_technology, add_ideas, set_politics.

### Module 14: `parse_states`
- **Input**: `history/states/*.txt`
- **Output tables**: `states`, `state_provinces`, `state_ownership_history`, `state_cores`, `state_victory_points`, `state_resources`, `state_buildings`, `province_buildings`
- **Row estimate**: ~800 states, ~13000 province links, ~1000 cores, ~2000 VP, ~3000 resources, ~4000 buildings
- **Notes**: Most complex single module. Nested blocks, dated blocks, DLC conditionals.

### Module 15: `parse_characters`
- **Input**: `common/characters/*.txt`
- **Output tables**: `characters`, `character_roles`, `character_role_traits`
- **Row estimate**: ~3000 characters, ~4500 roles, ~8000 traits
- **Notes**: Country tag derived from filename. Multiple role sub-blocks per character.

### Module 16: `parse_ideas`
- **Input**: `common/ideas/*.txt`
- **Output tables**: `ideas`, `idea_modifiers`
- **Row estimate**: ~500 ideas, ~3000 modifier rows
- **Notes**: Nested under category blocks. Modifier key-value pairs flattened to rows.

### Module 17: `parse_focuses`
- **Input**: `common/national_focus/*.txt`
- **Output tables**: `focus_trees`, `focuses`, `focus_prerequisites`, `focus_mutually_exclusive`
- **Row estimate**: ~30 trees, ~1500 focuses, ~2000 prereqs, ~300 exclusions
- **Notes**: AND/OR prerequisite modeling: each `prerequisite = { }` block is a group (AND between groups, OR within group). Mutually exclusive pairs normalised (a < b).

### Module 18: `parse_division_templates`
- **Input**: `history/units/*.txt` (land OOB files)
- **Output tables**: `division_templates`, `division_template_regiments`, `division_template_support`
- **Row estimate**: ~600 templates, ~4000 regiments, ~1500 support
- **Notes**: Country from filename. Grid positions (x, y) for regiments.

### Module 19: `parse_divisions`
- **Input**: `history/units/*.txt` (land OOB files)
- **Output tables**: `divisions`
- **Row estimate**: ~3000
- **Notes**: Same files as Module 18. `division` blocks under `units`.

### Module 20: `parse_naval_oob`
- **Input**: `history/units/*_naval_*.txt`
- **Output tables**: `fleets`, `task_forces`, `ships`, `equipment_variants`
- **Row estimate**: ~200 fleets, ~400 task forces, ~2000 ships, ~500 variants
- **Notes**: Hierarchical: fleet -> task_force -> ship. Equipment variants from `create_equipment_variant`. DLC-specific files (MTG vs legacy).

### Module 21: `parse_air_oob`
- **Input**: `history/units/*_air_*.txt`
- **Output tables**: `air_wings`
- **Row estimate**: ~500
- **Notes**: `air_wings = { state_id = { } }` blocks. DLC-specific files (BBA vs legacy).

### Module 22: `parse_strategic_regions`
- **Input**: `map/strategicregions/*.txt`
- **Output tables**: `strategic_regions`, `strategic_region_provinces`
- **Row estimate**: ~200 regions, ~13000 province links
- **Notes**: One file per region. Provinces list inside each file.

### Module 23: `parse_supply_nodes`
- **Input**: `map/supply_nodes.txt`
- **Output tables**: `supply_nodes`
- **Row estimate**: ~200
- **Notes**: Two-column whitespace-delimited file.

### Module 24: `parse_building_positions`
- **Input**: `map/buildings.txt`
- **Output tables**: `province_building_positions`
- **Row estimate**: ~150,000
- **Notes**: Semicolon-delimited. One row per building-instance per province. Convert linked_province=0 to NULL.

---

## Dependency Order (FK-safe load sequence)

```
01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08 -> 09 -> 10
-> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17
-> 18 -> 19 -> 20 -> 21
-> 22 -> 23 -> 24
```

Modules 11–12–13 must run in order (three-pass country loading).
Modules 18–19 read the same files but produce different tables.
All other modules are independent of each other within their FK tier.

---

## Shared Utilities

These are internal helper functions within `export_markdown_dump.py`:

| Utility | Purpose |
|---|---|
| `extract_block()` | Recursive Paradox Script tokenizer - extracts brace-matched `{ }` blocks |
| `find_top_level_blocks()` | Finds all top-level named blocks in a file |
| `find_game_blocks()` | Recursively unwraps DLC-guarded `if = { limit = { has_dlc } }` blocks |
| `dedup_rows()` | Deduplicates row lists by specified key columns (first occurrence wins) |
| `_pdx_date_to_iso()` | Converts Paradox `YYYY.M.D` dates to ISO `YYYY-MM-DD` |
| `_extract_equipment_tokens()` | Extracts equipment keys from `enable_equipments` blocks, filtering Paradox keywords |
| `write_md_table()` | Writes a list of dicts as a markdown table to the output directory |
| `auto_detect_hoi4()` | Finds the HOI4 install via `--hoi4-root`, `HOI4_ROOT` env var, or default Steam paths |
