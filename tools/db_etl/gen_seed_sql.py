#!/usr/bin/env python3
"""Generate seed-load-order.sql with explicit column lists from CSV headers."""

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CSV_DIR = REPO / "data" / "csv"
OUT = REPO / "sql" / "seed-load-order.sql"

# Read all CSV headers
def get_headers():
    h = {}
    for f in sorted(CSV_DIR.glob("*.csv")):
        with open(f, encoding="utf-8") as fh:
            h[f.stem] = next(csv.reader(fh))
    return h

HEADERS = get_headers()

# PostgreSQL reserved words that need quoting in column lists
_RESERVED = {"desc", "order", "group", "limit", "offset", "user", "table", "column", "check", "default"}

def _quote_col(c):
    return f'"{c}"' if c.lower() in _RESERVED else c

def copy_cmd(table):
    cols = ", ".join(_quote_col(c) for c in HEADERS[table])
    return f"\\copy {table}({cols}) FROM 'data/csv/{table}.csv' WITH (FORMAT csv, HEADER);"

# -- Tier ordering (from FK dependency analysis) --
TIER0 = [
    "continents", "terrain_types", "state_categories", "resource_types",
    "building_types", "ideologies", "technology_categories", "character_traits",
    "operation_tokens", "operation_phase_definitions", "intel_agency_upgrade_branches",
    "compliance_modifiers", "resistance_modifiers", "resistance_activities",
    "mio_equipment_groups", "mio_templates", "mio_policies", "raid_categories",
    "medals", "ribbons", "ace_modifiers", "unit_medals",
    "continuous_focus_palettes", "technology_sharing_groups", "dynamic_modifiers",
    "scientist_traits", "peace_action_categories", "autonomy_states",
    "occupation_laws", "decision_categories", "balance_of_power_definitions",
    "doctrine_folders",
    "ai_faction_theaters", "collections", "faction_goals", "faction_manifests",
    "faction_member_upgrade_groups", "faction_rule_groups", "localisation",
    "special_project_specializations", "special_project_tags", "timed_activities",
    "wargoal_types",
]

TIER1 = [
    "terrain_combat_modifiers", "terrain_building_limits", "sub_ideologies",
    "doctrine_tracks", "grand_doctrines",
    "technologies", "unit_types", "equipment_definitions", "provinces",
    "autonomy_state_modifiers", "occupation_law_modifiers",
    "operation_phase_equipment", "operations", "intel_agency_upgrades",
    "compliance_modifier_effects", "resistance_modifier_effects",
    "mio_equipment_group_members", "mio_organizations", "mio_policy_bonuses",
    "raids", "medal_tiers", "ace_modifier_effects", "ace_modifier_equipment_types",
    "unit_medal_modifiers", "continuous_focuses", "dynamic_modifier_effects",
    "scientist_trait_modifiers", "peace_cost_modifiers", "bop_sides",
    "ideas", "grand_doctrine_tracks", "subdoctrines",
    "faction_member_upgrades", "faction_rules", "faction_templates",
    "special_projects", "special_project_rewards", "timed_activity_equipment",
]

TIER2 = [
    "equipment_resources", "technology_categories_junction",
    "technology_prerequisites", "technology_enables_equipment",
    "technology_enables_units", "province_building_positions",
    "strategic_regions", "supply_nodes", "province_adjacencies",
    "province_railways", "states", "idea_modifiers",
    "operation_awarded_tokens", "operation_equipment_requirements",
    "operation_phase_groups", "intel_agency_upgrade_levels",
    "intel_agency_upgrade_progress_modifiers",
    "mio_organization_equipment_types", "mio_initial_traits", "mio_traits",
    "raid_equipment_requirements", "continuous_focus_modifiers", "bop_ranges",
    "faction_rule_group_members", "faction_template_goals",
    "faction_template_rules", "special_project_reward_links",
]

TIER3 = [
    "strategic_region_provinces", "state_provinces", "state_resources",
    "state_buildings", "state_victory_points", "province_buildings",
    "countries", "operation_phase_options",
    "mio_trait_bonuses", "mio_trait_prerequisites", "mio_trait_exclusions",
    "bop_range_modifiers",
    "ai_faction_theater_regions",
]

TIER4 = [
    "state_ownership_history", "province_controller_history", "state_cores",
    "country_starting_technologies", "country_starting_ideas",
    "characters", "division_templates", "equipment_variants",
    "fleets", "air_wings", "focus_trees", "country_visual_definitions",
    "intelligence_agencies", "bookmarks", "country_starting_doctrines",
]

TIER5_SIMPLE = [
    "character_roles", "divisions", "focuses",
    "intelligence_agency_names", "decisions",
]

TIER6_SIMPLE = ["focus_prerequisites", "focus_mutually_exclusive"]

# -- Build the SQL --
lines = []

lines.append("-- HOI4 PostgreSQL Seed Load Order - All 127 Tables (FK-safe)")
lines.append("--")
lines.append("-- Every \\copy uses an explicit column list so that SERIAL/BIGSERIAL PKs are")
lines.append("-- auto-generated and CSV column order does not need to match the schema.")
lines.append("-- Tables that need FK resolution from natural keys to surrogate IDs use")
lines.append("-- staging temp tables with INSERT ... SELECT ... JOIN.")
lines.append("--")
lines.append("-- Usage:  psql -d hoi4 -f sql/seed-load-order.sql")
lines.append("--         (run from the repo root so data/csv/ paths resolve)")
lines.append("")
lines.append("\\set ON_ERROR_STOP on")
lines.append("BEGIN;")
lines.append("")

def add_tier(label, tables):
    lines.append(f"-- ============================================================")
    lines.append(f"-- {label}")
    lines.append(f"-- ============================================================")
    for t in tables:
        lines.append(copy_cmd(t))
    lines.append("")

add_tier("TIER 0 - Root reference tables (32 tables, no FK dependencies)", TIER0)
add_tier("TIER 1 - Depends only on Tier 0 (32 tables)", TIER1)
add_tier("TIER 2 - Depends on Tier 0 + 1 (23 tables)", TIER2)
add_tier("TIER 3 - Depends on Tier 0 + 1 + 2 (12 tables)", TIER3)
add_tier("TIER 4 - Depends on countries / Tier 3 (15 tables)", TIER4)

# -- Tier 5 (5 simple + 4 FK staging) --
lines.append("-- ============================================================")
lines.append("-- TIER 5 - Depends on Tier 4 (9 tables, 4 need FK staging)")
lines.append("-- ============================================================")
for t in TIER5_SIMPLE:
    lines.append(copy_cmd(t))

lines.append("")
lines.append("-- division_template_regiments: resolve template_name -> division_template_id")
lines.append("CREATE TEMP TABLE _stage_dtr (template_name TEXT, unit_type_key TEXT, grid_x TEXT, grid_y TEXT);")
lines.append("\\copy _stage_dtr FROM 'data/csv/division_template_regiments.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO division_template_regiments (division_template_id, unit_type_key, grid_x, grid_y)")
lines.append("  SELECT dt.division_template_id, s.unit_type_key, s.grid_x::smallint, s.grid_y::smallint")
lines.append("  FROM _stage_dtr s")
lines.append("  JOIN division_templates dt ON dt.template_name = s.template_name;")
lines.append("DROP TABLE _stage_dtr;")

lines.append("")
lines.append("-- division_template_support: resolve template_name -> division_template_id")
lines.append("CREATE TEMP TABLE _stage_dts (template_name TEXT, unit_type_key TEXT, grid_x TEXT, grid_y TEXT);")
lines.append("\\copy _stage_dts FROM 'data/csv/division_template_support.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO division_template_support (division_template_id, unit_type_key, grid_x, grid_y)")
lines.append("  SELECT dt.division_template_id, s.unit_type_key, s.grid_x::smallint, s.grid_y::smallint")
lines.append("  FROM _stage_dts s")
lines.append("  JOIN division_templates dt ON dt.template_name = s.template_name;")
lines.append("DROP TABLE _stage_dts;")

lines.append("")
lines.append("-- task_forces: resolve (country_tag, fleet_name) -> fleet_id")
lines.append("CREATE TEMP TABLE _stage_tf (country_tag TEXT, fleet_name TEXT, task_force_name TEXT, location_province_id TEXT, source_file TEXT);")
lines.append("\\copy _stage_tf FROM 'data/csv/task_forces.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO task_forces (fleet_id, task_force_name, location_province_id)")
lines.append("  SELECT f.fleet_id, s.task_force_name, NULLIF(s.location_province_id, '')::int")
lines.append("  FROM _stage_tf s")
lines.append("  JOIN fleets f ON f.country_tag = s.country_tag AND f.fleet_name = s.fleet_name;")
lines.append("DROP TABLE _stage_tf;")

lines.append("")
lines.append("-- bookmark_countries: resolve bookmark_name -> bookmark_id")
lines.append("CREATE TEMP TABLE _stage_bc (bookmark_name TEXT, country_tag TEXT, ideology_key TEXT);")
lines.append("\\copy _stage_bc FROM 'data/csv/bookmark_countries.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO bookmark_countries (bookmark_id, country_tag, ideology_key)")
lines.append("  SELECT b.bookmark_id, s.country_tag, s.ideology_key")
lines.append("  FROM _stage_bc s")
lines.append("  JOIN bookmarks b ON b.bookmark_name = s.bookmark_name;")
lines.append("DROP TABLE _stage_bc;")

lines.append("")
lines.append("-- equipment_variant_modules: resolve natural key -> equipment_variant_id")
lines.append("CREATE TEMP TABLE _stage_evm (owner_tag TEXT, base_equipment_key TEXT, version_name TEXT, effective_date TEXT, slot_name TEXT, module_key TEXT);")
lines.append("\\copy _stage_evm FROM 'data/csv/equipment_variant_modules.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO equipment_variant_modules (equipment_variant_id, slot_name, module_key)")
lines.append("  SELECT ev.equipment_variant_id, s.slot_name, s.module_key")
lines.append("  FROM _stage_evm s")
lines.append("  JOIN equipment_variants ev ON ev.owner_tag = s.owner_tag")
lines.append("    AND ev.base_equipment_key = s.base_equipment_key")
lines.append("    AND COALESCE(ev.version_name, '') = COALESCE(s.version_name, '')")
lines.append("    AND ev.effective_date = s.effective_date::date;")
lines.append("DROP TABLE _stage_evm;")

lines.append("")
lines.append("-- equipment_variant_upgrades: resolve natural key -> equipment_variant_id")
lines.append("CREATE TEMP TABLE _stage_evu (owner_tag TEXT, base_equipment_key TEXT, version_name TEXT, effective_date TEXT, upgrade_key TEXT, upgrade_level TEXT);")
lines.append("\\copy _stage_evu FROM 'data/csv/equipment_variant_upgrades.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO equipment_variant_upgrades (equipment_variant_id, upgrade_key, upgrade_level)")
lines.append("  SELECT ev.equipment_variant_id, s.upgrade_key, s.upgrade_level::int")
lines.append("  FROM _stage_evu s")
lines.append("  JOIN equipment_variants ev ON ev.owner_tag = s.owner_tag")
lines.append("    AND ev.base_equipment_key = s.base_equipment_key")
lines.append("    AND COALESCE(ev.version_name, '') = COALESCE(s.version_name, '')")
lines.append("    AND ev.effective_date = s.effective_date::date;")
lines.append("DROP TABLE _stage_evu;")

lines.append("")

# -- Tier 6 (2 simple + 2 FK staging) --
lines.append("-- ============================================================")
lines.append("-- TIER 6 - Leaf tables (4 tables, 2 need FK staging)")
lines.append("-- ============================================================")
for t in TIER6_SIMPLE:
    lines.append(copy_cmd(t))

lines.append("")
lines.append("-- character_role_traits: resolve (character_id, role_type) -> character_role_id")
lines.append("CREATE TEMP TABLE _stage_crt (character_id TEXT, role_type TEXT, trait_key TEXT, source_file TEXT);")
lines.append("\\copy _stage_crt FROM 'data/csv/character_role_traits.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO character_role_traits (character_role_id, trait_key)")
lines.append("  SELECT cr.character_role_id, s.trait_key")
lines.append("  FROM _stage_crt s")
lines.append("  JOIN character_roles cr ON cr.character_id = s.character_id AND cr.role_type = s.role_type;")
lines.append("DROP TABLE _stage_crt;")

lines.append("")
lines.append("-- ships: resolve (country_tag, fleet_name, task_force_name) -> task_force_id")
lines.append("CREATE TEMP TABLE _stage_ships (")
lines.append("  country_tag TEXT, fleet_name TEXT, task_force_name TEXT, ship_name TEXT,")
lines.append("  definition TEXT, hull_equipment_key TEXT, owner_tag TEXT, version_name TEXT,")
lines.append("  pride_of_the_fleet TEXT, source_file TEXT")
lines.append(");")
lines.append("\\copy _stage_ships FROM 'data/csv/ships.csv' WITH (FORMAT csv, HEADER);")
lines.append("INSERT INTO ships (task_force_id, ship_name, definition, hull_equipment_key,")
lines.append("                   version_name, owner_tag, pride_of_the_fleet, source_file)")
lines.append("  SELECT tf.task_force_id, s.ship_name, s.definition, s.hull_equipment_key,")
lines.append("         NULLIF(s.version_name, ''), s.owner_tag,")
lines.append("         CASE WHEN s.pride_of_the_fleet = 'true' THEN true ELSE NULL END,")
lines.append("         s.source_file")
lines.append("  FROM _stage_ships s")
lines.append("  JOIN fleets f ON f.country_tag = s.country_tag AND f.fleet_name = s.fleet_name")
lines.append("  JOIN task_forces tf ON tf.fleet_id = f.fleet_id AND tf.task_force_name = s.task_force_name;")
lines.append("DROP TABLE _stage_ships;")

lines.append("")
lines.append("COMMIT;")

# Write output
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Written {len(lines)} lines to {OUT}")

# Verify table count
copy_count = sum(1 for l in lines if l.startswith("\\copy "))
insert_count = sum(1 for l in lines if l.startswith("INSERT INTO "))
print(f"  \\copy commands: {copy_count}")
print(f"  INSERT INTO (staging): {insert_count}")
print(f"  Total tables loaded: {copy_count + insert_count}")
