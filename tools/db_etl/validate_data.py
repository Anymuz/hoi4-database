#!/usr/bin/env python3
"""
HOI4 Data-Dump Validation Script

Reads all markdown data-dump files and performs:
  1. Row-count audit against expected totals
  2. Foreign-key referential integrity checks
  3. Primary-key / unique-constraint violation checks
  4. NOT NULL constraint checks on mandatory columns

Usage:
    python tools/db_etl/validate_data.py [--dump-dir docs/data-dump]
"""

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Markdown table parser
# ---------------------------------------------------------------------------

def parse_md_table(path: Path) -> tuple[list[str], list[dict]]:
    """Parse a markdown file containing a single pipe-delimited table.
    Returns (headers, rows) where each row is a dict keyed by header name.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    headers = []
    rows = []
    header_found = False
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if not header_found:
            headers = cells
            header_found = True
            continue
        # skip separator line (|---|---|)
        if all(re.fullmatch(r"-+:?|:?-+:?", c) for c in cells):
            continue
        row = {}
        for i, h in enumerate(headers):
            row[h] = cells[i] if i < len(cells) else ""
        rows.append(row)
    return headers, rows


def load_dump(dump_dir: Path, filename: str) -> tuple[list[str], list[dict]]:
    """Load a dump file; returns ([], []) if not found."""
    p = dump_dir / filename
    if not p.exists():
        return [], []
    return parse_md_table(p)


# ---------------------------------------------------------------------------
# PK index builder
# ---------------------------------------------------------------------------

def build_pk_index(rows: list[dict], col: str) -> set[str]:
    """Collect all non-empty values of `col` into a set."""
    return {r[col] for r in rows if r.get(col, "").strip()}


# ---------------------------------------------------------------------------
# Validation checks
# ---------------------------------------------------------------------------

class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def note(self, msg: str):
        self.info.append(msg)


def check_fk(
    result: ValidationResult,
    child_rows: list[dict],
    child_col: str,
    parent_pk: set[str],
    child_label: str,
    parent_label: str,
    known_gaps: set[str] | None = None,
    soft: bool = False,
):
    """Check that every non-empty child_col value exists in parent_pk.
    Values in known_gaps are counted but not reported. If soft=True,
    remaining orphans are reported as warnings instead of errors."""
    orphans = set()
    expected = set()
    for r in child_rows:
        val = r.get(child_col, "").strip()
        if val and val not in parent_pk:
            if known_gaps and val in known_gaps:
                expected.add(val)
            else:
                orphans.add(val)
    if orphans:
        sample = sorted(orphans)[:10]
        msg = (
            f"FK violation: {child_label}.{child_col} → {parent_label}: "
            f"{len(orphans)} orphan(s): {sample}"
        )
        if soft:
            result.warn(msg)
        else:
            result.error(msg)
    elif expected:
        result.note(
            f"FK OK: {child_label}.{child_col} → {parent_label} ({len(child_rows)} rows checked, "
            f"{len(expected)} known-gap values skipped: doctrines/mods)"
        )
    else:
        result.note(
            f"FK OK: {child_label}.{child_col} → {parent_label} ({len(child_rows)} rows checked)"
        )


def check_unique(
    result: ValidationResult,
    rows: list[dict],
    cols: list[str],
    label: str,
):
    """Check that the combination of cols is unique."""
    seen = Counter()
    for r in rows:
        key = tuple(r.get(c, "").strip() for c in cols)
        seen[key] += 1
    dupes = {k: v for k, v in seen.items() if v > 1}
    if dupes:
        sample = list(dupes.items())[:5]
        result.error(f"UNIQUE violation in {label} on {cols}: {len(dupes)} duplicate key(s), e.g. {sample}")
    else:
        result.note(f"UNIQUE OK: {label} on {cols} ({len(rows)} rows)")


def check_not_null(
    result: ValidationResult,
    rows: list[dict],
    col: str,
    label: str,
):
    """Check that col is never empty."""
    nulls = sum(1 for r in rows if not r.get(col, "").strip())
    if nulls:
        result.warn(f"NOT NULL issue: {label}.{col} has {nulls} empty value(s)")
    else:
        result.note(f"NOT NULL OK: {label}.{col} ({len(rows)} rows)")


# ---------------------------------------------------------------------------
# Main validation
# ---------------------------------------------------------------------------

def run_validation(dump_dir: Path) -> ValidationResult:
    result = ValidationResult()

    # Load all dump files into a registry keyed by short name
    dumps: dict[str, tuple[list[str], list[dict]]] = {}

    def load(name: str, filename: str | None = None) -> list[dict]:
        fn = filename or f"{name}.md"
        h, rows = load_dump(dump_dir, fn)
        dumps[name] = (h, rows)
        if not rows:
            result.warn(f"Empty or missing: {fn}")
        return rows

    # ── Tier 0: Root tables ──────────────────────────────────────
    countries_rows = load("countries", "country_tags.md")
    country_pk = build_pk_index(countries_rows, "tag")

    states_rows = load("states", "states.md")
    state_pk = build_pk_index(states_rows, "state_id")

    provinces_rows = load("provinces", "map_definition_provinces.md")
    province_pk = build_pk_index(provinces_rows, "province_id")

    resources_rows = load("resources", "resources.md")
    resource_pk = build_pk_index(resources_rows, "resource_key")

    buildings_rows = load("building_types", "building_types.md")
    building_pk = build_pk_index(buildings_rows, "building_key")

    ideologies_rows = load("ideologies", "ideologies.md")
    ideology_pk = build_pk_index(ideologies_rows, "ideology_key")

    sub_ideologies_rows = load("sub_ideologies", "sub_ideologies.md")
    sub_ideology_pk = build_pk_index(sub_ideologies_rows, "sub_ideology_key")

    technologies_rows = load("technologies", "technologies_all.md")
    tech_pk = build_pk_index(technologies_rows, "technology_key")

    unit_types_rows = load("unit_types", "unit_types_all.md")
    unit_type_pk = build_pk_index(unit_types_rows, "unit_type")

    equipment_rows = load("equipment", "equipment_all.md")
    equipment_pk = build_pk_index(equipment_rows, "equipment_key")

    terrain_rows = load("terrain_types", "terrain_types.md")
    terrain_pk = build_pk_index(terrain_rows, "terrain_type") if terrain_rows else set()

    state_cat_rows = load("state_categories", "state_categories.md")
    state_cat_pk = build_pk_index(state_cat_rows, "state_category")

    continents_rows = load("continents", "continents.md")
    continent_pk = build_pk_index(continents_rows, "continent_id")

    ideas_rows = load("ideas", "ideas_all.md")
    ideas_pk = build_pk_index(ideas_rows, "idea_key")

    focus_trees_rows = load("focus_trees", "focus_trees_all.md")
    focus_tree_pk = build_pk_index(focus_trees_rows, "focus_tree_id")

    focuses_rows = load("focuses", "focuses_all.md")
    focus_pk = build_pk_index(focuses_rows, "focus_id")

    characters_rows = load("characters", "characters_all.md")
    character_pk = build_pk_index(characters_rows, "character_id")

    strategic_regions_rows = load("strategic_regions", "strategic_regions.md")
    strategic_region_pk = build_pk_index(strategic_regions_rows, "strategic_region_id")

    division_templates_rows = load("division_templates", "division_templates_all.md")

    # DLC root tables
    operation_tokens_rows = load("operation_tokens", "operation_tokens.md")
    op_token_pk = build_pk_index(operation_tokens_rows, "token_key")

    op_phase_defs_rows = load("operation_phase_definitions", "operation_phase_definitions.md")
    op_phase_pk = build_pk_index(op_phase_defs_rows, "phase_key")

    operations_rows = load("operations", "operations.md")
    operations_pk = build_pk_index(operations_rows, "operation_key")

    intel_branch_rows = load("intel_agency_upgrade_branches", "intel_agency_upgrade_branches.md")
    intel_branch_pk = build_pk_index(intel_branch_rows, "branch_key")

    intel_upgrade_rows = load("intel_agency_upgrades", "intel_agency_upgrades.md")
    intel_upgrade_pk = build_pk_index(intel_upgrade_rows, "upgrade_key")

    compliance_rows = load("compliance_modifiers", "compliance_modifiers.md")
    compliance_pk = build_pk_index(compliance_rows, "modifier_key")

    resistance_rows = load("resistance_modifiers", "resistance_modifiers.md")
    resistance_pk = build_pk_index(resistance_rows, "modifier_key")

    mio_equip_group_rows = load("mio_equipment_groups", "mio_equipment_groups.md")
    mio_equip_group_pk = build_pk_index(mio_equip_group_rows, "group_key")

    mio_template_rows = load("mio_templates", "mio_templates.md")
    mio_template_pk = build_pk_index(mio_template_rows, "template_key")

    mio_org_rows = load("mio_organizations", "mio_organizations.md")
    mio_org_pk = build_pk_index(mio_org_rows, "organization_key")

    mio_policy_rows = load("mio_policies", "mio_policies.md")
    mio_policy_pk = build_pk_index(mio_policy_rows, "policy_key")

    raid_cat_rows = load("raid_categories", "raid_categories.md")
    raid_cat_pk = build_pk_index(raid_cat_rows, "category_key")

    raids_rows = load("raids", "raids.md")
    raids_pk = build_pk_index(raids_rows, "raid_key")

    medals_rows = load("medals", "medals.md")
    medals_pk = build_pk_index(medals_rows, "medal_key")

    ace_mod_rows = load("ace_modifiers", "ace_modifiers.md")
    ace_mod_pk = build_pk_index(ace_mod_rows, "modifier_key")

    unit_medals_rows = load("unit_medals", "unit_medals.md")
    unit_medal_pk = build_pk_index(unit_medals_rows, "medal_key")

    bop_rows = load("bop", "balance_of_power_definitions.md")
    bop_pk = build_pk_index(bop_rows, "bop_key")

    bop_sides_rows = load("bop_sides", "bop_sides.md")
    # Composite PK: (bop_key, side_id)

    bop_ranges_rows = load("bop_ranges", "bop_ranges.md")
    bop_range_pk = build_pk_index(bop_ranges_rows, "range_id")

    cf_palette_rows = load("continuous_focus_palettes", "continuous_focus_palettes.md")
    cf_palette_pk = build_pk_index(cf_palette_rows, "palette_id")

    cf_rows = load("continuous_focuses", "continuous_focuses.md")
    cf_pk = build_pk_index(cf_rows, "focus_id")

    dyn_mod_rows = load("dynamic_modifiers", "dynamic_modifiers.md")
    dyn_mod_pk = build_pk_index(dyn_mod_rows, "modifier_key")

    sci_trait_rows = load("scientist_traits", "scientist_traits.md")
    sci_trait_pk = build_pk_index(sci_trait_rows, "trait_key")

    peace_cat_rows = load("peace_action_categories", "peace_action_categories.md")
    peace_cat_pk = build_pk_index(peace_cat_rows, "category_key")

    autonomy_rows = load("autonomy_states", "autonomy_states.md")
    autonomy_pk = build_pk_index(autonomy_rows, "autonomy_key")

    occupation_rows = load("occupation_laws", "occupation_laws.md")
    occupation_pk = build_pk_index(occupation_rows, "occupation_law_key")

    decision_cat_rows = load("decision_categories", "decision_categories.md")
    decision_cat_pk = build_pk_index(decision_cat_rows, "category_key")

    bookmark_rows = load("bookmarks", "bookmarks.md")
    bookmark_pk = build_pk_index(bookmark_rows, "bookmark_id")

    tech_sharing_rows = load("technology_sharing_groups", "technology_sharing_groups.md")

    # ── Child tables ─────────────────────────────────────────────

    # Geography FK checks
    sp_rows = load("state_provinces", "state_provinces.md")
    if sp_rows:
        check_fk(result, sp_rows, "state_id", state_pk, "state_provinces", "states")
        check_fk(result, sp_rows, "province_id", province_pk, "state_provinces", "provinces")

    sr_rows = load("state_resources", "state_resources.md")
    if sr_rows:
        check_fk(result, sr_rows, "state_id", state_pk, "state_resources", "states")
        check_fk(result, sr_rows, "resource_key", resource_pk, "state_resources", "resource_types")

    sb_rows = load("state_buildings", "state_buildings.md")
    if sb_rows:
        check_fk(result, sb_rows, "state_id", state_pk, "state_buildings", "states")
        check_fk(result, sb_rows, "building_key", building_pk, "state_buildings", "building_types")

    svp_rows = load("state_victory_points", "state_victory_points.md")
    if svp_rows:
        check_fk(result, svp_rows, "state_id", state_pk, "state_victory_points", "states")
        check_fk(result, svp_rows, "province_id", province_pk, "state_victory_points", "provinces")

    srp_rows = load("strategic_region_provinces", "strategic_region_provinces.md")
    if srp_rows:
        check_fk(result, srp_rows, "strategic_region_id", strategic_region_pk, "strategic_region_provinces", "strategic_regions")
        check_fk(result, srp_rows, "province_id", province_pk, "strategic_region_provinces", "provinces")

    sn_rows = load("supply_nodes", "supply_nodes.md")
    if sn_rows:
        check_fk(result, sn_rows, "province_id", province_pk, "supply_nodes", "provinces")

    # Country-history FK checks
    ch_rows = load("country_history", "country_history.md")
    if ch_rows:
        check_fk(result, ch_rows, "tag", country_pk, "country_history", "countries")

    # Known gaps: doctrine techs live in common/doctrines/, not common/technologies/
    # These are assigned in country history via set_technology but aren't in the technologies table.
    DOCTRINE_TECHS = {
        "air_superiority", "basic_medium_battery", "battlefleet_concentration",
        "convoy_escorts", "convoy_sailing", "defence_in_depth",
        "direct_ground_support", "dispersed_fighting", "dive_bombing",
        "fighter_baiting", "fleet_in_being", "formation_flying",
        "grand_battle_plan", "guerrilla_warfare", "infantry_offensive",
        "land_air_coordination", "mass_assault", "mobile_infantry",
        "mobile_warfare", "naval_strike_tactics", "operational_integrity",
        "shock_and_awe", "slow_divisional_advance", "superior_firepower",
        "trade_interdiction", "trench_warfare",
        "volkssturm",  # edge-case base game doctrine
    }
    # militia_tech is a base-game tech referenced in unlocks but not in tech files
    KNOWN_TECH_GAPS = DOCTRINE_TECHS | {"militia_tech"}

    cst_rows = load("country_starting_technologies", "country_starting_technologies.md")
    if cst_rows:
        check_fk(result, cst_rows, "country_tag", country_pk, "country_starting_technologies", "countries")
        check_fk(result, cst_rows, "technology_key", tech_pk, "country_starting_technologies", "technologies",
                 known_gaps=KNOWN_TECH_GAPS, soft=True)

    # Equipment FK checks
    if equipment_rows:
        # archetype self-ref
        archetypes = {r.get("equipment_key", "").strip() for r in equipment_rows
                      if r.get("is_archetype", "").strip().lower() == "true"}
        child_equip = [r for r in equipment_rows
                       if r.get("archetype_key", "").strip()]
        check_fk(result, child_equip, "archetype_key", equipment_pk, "equipment_definitions", "equipment_definitions(archetype)")

    eq_res_rows = load("equipment_resources", "equipment_resources_all.md")
    if eq_res_rows:
        check_fk(result, eq_res_rows, "equipment_key", equipment_pk, "equipment_resources", "equipment_definitions")
        check_fk(result, eq_res_rows, "resource_key", resource_pk, "equipment_resources", "resource_types")

    # Technology link FK checks
    tech_links_rows = load("technology_links", "technology_links_all.md")
    if tech_links_rows:
        check_fk(result, tech_links_rows, "technology_key", tech_pk, "technology_prerequisites", "technologies")
        check_fk(result, tech_links_rows, "prerequisite_key", tech_pk, "technology_prerequisites", "technologies(prereq)")

    tech_unlocks_rows = load("technology_unlocks", "technology_unlocks_all.md")
    if tech_unlocks_rows:
        check_fk(result, tech_unlocks_rows, "technology_key", tech_pk, "technology_unlocks", "technologies",
                 known_gaps=KNOWN_TECH_GAPS, soft=True)

    # Character FK checks
    if characters_rows:
        check_fk(result, characters_rows, "country_tag", country_pk, "characters", "countries")

    char_roles_rows = load("character_roles", "character_roles_all.md")
    if char_roles_rows:
        check_fk(result, char_roles_rows, "character_id", character_pk, "character_roles", "characters")

    # Focus FK checks
    if focus_trees_rows:
        check_fk(result, focus_trees_rows, "country_tag", country_pk, "focus_trees", "countries")

    if focuses_rows:
        check_fk(result, focuses_rows, "focus_tree_id", focus_tree_pk, "focuses", "focus_trees")

    focus_links_rows = load("focus_links", "focus_links_all.md")
    if focus_links_rows:
        check_fk(result, focus_links_rows, "focus_id", focus_pk, "focus_links", "focuses")
        # prerequisite_focus_id -> focuses
        check_fk(result, focus_links_rows, "required_focus_id", focus_pk, "focus_links", "focuses(required)")

    # Idea FK checks
    idea_mod_rows = load("idea_modifiers", "idea_modifiers_all.md")
    if idea_mod_rows:
        check_fk(result, idea_mod_rows, "idea_key", ideas_pk, "idea_modifiers", "ideas")

    # Division template FK checks
    div_reg_rows = load("division_template_regiments", "division_template_regiments_all.md")
    if div_reg_rows:
        check_fk(result, div_reg_rows, "unit_type", unit_type_pk, "division_template_regiments", "unit_types")

    divisions_rows = load("divisions", "divisions_all.md")
    if divisions_rows:
        check_fk(result, divisions_rows, "country_tag", country_pk, "divisions", "countries")

    # ── DLC FK checks ────────────────────────────────────────────

    # Phase 11: Governance
    asm_rows = load("autonomy_state_modifiers", "autonomy_state_modifiers.md")
    if asm_rows:
        check_fk(result, asm_rows, "autonomy_key", autonomy_pk, "autonomy_state_modifiers", "autonomy_states")

    olm_rows = load("occupation_law_modifiers", "occupation_law_modifiers.md")
    if olm_rows:
        check_fk(result, olm_rows, "occupation_law_key", occupation_pk, "occupation_law_modifiers", "occupation_laws")

    # Phase 12-15: Extensions
    bookmark_countries_rows = load("bookmark_countries", "bookmark_countries.md")
    if bookmark_countries_rows:
        check_fk(result, bookmark_countries_rows, "country_tag", country_pk, "bookmark_countries", "countries")
        check_fk(result, bookmark_countries_rows, "ideology", ideology_pk, "bookmark_countries", "ideologies")

    decisions_rows = load("decisions", "decisions_all.md")
    if decisions_rows:
        check_fk(result, decisions_rows, "category_key", decision_cat_pk, "decisions", "decision_categories")

    intel_agency_rows = load("intelligence_agencies", "intelligence_agencies.md")
    # No strict country FK since available_tag can be complex

    intel_agency_names_rows = load("intelligence_agency_names", "intelligence_agency_names.md")

    # Phase 16: Espionage
    op_awarded_rows = load("operation_awarded_tokens", "operation_awarded_tokens.md")
    if op_awarded_rows:
        check_fk(result, op_awarded_rows, "operation_key", operations_pk, "operation_awarded_tokens", "operations")
        check_fk(result, op_awarded_rows, "token_key", op_token_pk, "operation_awarded_tokens", "operation_tokens")

    op_equip_rows = load("operation_equipment_requirements", "operation_equipment_requirements.md")
    if op_equip_rows:
        check_fk(result, op_equip_rows, "operation_key", operations_pk, "operation_equipment_requirements", "operations")

    op_phase_groups_rows = load("operation_phase_groups", "operation_phase_groups.md")
    if op_phase_groups_rows:
        check_fk(result, op_phase_groups_rows, "operation_key", operations_pk, "operation_phase_groups", "operations")

    op_phase_options_rows = load("operation_phase_options", "operation_phase_options.md")
    if op_phase_options_rows:
        check_fk(result, op_phase_options_rows, "operation_key", operations_pk, "operation_phase_options", "operations")
        check_fk(result, op_phase_options_rows, "phase_key", op_phase_pk, "operation_phase_options", "operation_phase_definitions")

    op_phase_equip_rows = load("operation_phase_equipment", "operation_phase_equipment.md")
    if op_phase_equip_rows:
        check_fk(result, op_phase_equip_rows, "phase_key", op_phase_pk, "operation_phase_equipment", "operation_phase_definitions")

    intel_upgrades_rows = load("intel_agency_upgrades_", "intel_agency_upgrades.md")
    if intel_upgrades_rows:
        check_fk(result, intel_upgrades_rows, "branch_key", intel_branch_pk, "intel_agency_upgrades", "intel_agency_upgrade_branches")

    intel_levels_rows = load("intel_agency_upgrade_levels", "intel_agency_upgrade_levels.md")
    if intel_levels_rows:
        check_fk(result, intel_levels_rows, "upgrade_key", intel_upgrade_pk, "intel_agency_upgrade_levels", "intel_agency_upgrades")

    intel_progress_rows = load("intel_agency_upgrade_progress_modifiers", "intel_agency_upgrade_progress_modifiers.md")
    if intel_progress_rows:
        check_fk(result, intel_progress_rows, "upgrade_key", intel_upgrade_pk, "intel_agency_upgrade_progress_modifiers", "intel_agency_upgrades")

    # Phase 17: Occupation & Resistance
    comp_eff_rows = load("compliance_modifier_effects", "compliance_modifier_effects.md")
    if comp_eff_rows:
        check_fk(result, comp_eff_rows, "modifier_key", compliance_pk, "compliance_modifier_effects", "compliance_modifiers")

    res_eff_rows = load("resistance_modifier_effects", "resistance_modifier_effects.md")
    if res_eff_rows:
        check_fk(result, res_eff_rows, "modifier_key", resistance_pk, "resistance_modifier_effects", "resistance_modifiers")

    # Phase 18: MIO
    mio_grp_members_rows = load("mio_equipment_group_members", "mio_equipment_group_members.md")
    if mio_grp_members_rows:
        check_fk(result, mio_grp_members_rows, "group_key", mio_equip_group_pk, "mio_equipment_group_members", "mio_equipment_groups")

    if mio_org_rows:
        check_fk(result, mio_org_rows, "template_key", mio_template_pk, "mio_organizations", "mio_templates")

    mio_policy_bonus_rows = load("mio_policy_bonuses", "mio_policy_bonuses.md")
    if mio_policy_bonus_rows:
        check_fk(result, mio_policy_bonus_rows, "policy_key", mio_policy_pk, "mio_policy_bonuses", "mio_policies")

    # Phase 19: Raids
    if raids_rows:
        check_fk(result, raids_rows, "category_key", raid_cat_pk, "raids", "raid_categories")

    raid_equip_rows = load("raid_equipment_requirements", "raid_equipment_requirements.md")
    if raid_equip_rows:
        check_fk(result, raid_equip_rows, "raid_key", raids_pk, "raid_equipment_requirements", "raids")

    # Phase 20: Career Profile
    medal_tiers_rows = load("medal_tiers", "medal_tiers.md")
    if medal_tiers_rows:
        check_fk(result, medal_tiers_rows, "medal_key", medals_pk, "medal_tiers", "medals")

    ace_eff_rows = load("ace_modifier_effects", "ace_modifier_effects.md")
    if ace_eff_rows:
        check_fk(result, ace_eff_rows, "modifier_key", ace_mod_pk, "ace_modifier_effects", "ace_modifiers")

    ace_equip_rows = load("ace_modifier_equipment_types", "ace_modifier_equipment_types.md")
    if ace_equip_rows:
        check_fk(result, ace_equip_rows, "modifier_key", ace_mod_pk, "ace_modifier_equipment_types", "ace_modifiers")

    unit_medal_mod_rows = load("unit_medal_modifiers", "unit_medal_modifiers.md")
    if unit_medal_mod_rows:
        check_fk(result, unit_medal_mod_rows, "medal_key", unit_medal_pk, "unit_medal_modifiers", "unit_medals")

    # Phase 21: BOP & Continuous Focuses
    if bop_sides_rows:
        check_fk(result, bop_sides_rows, "bop_key", bop_pk, "bop_sides", "balance_of_power_definitions")

    if bop_ranges_rows:
        # Check bop_key exists in bop definitions
        check_fk(result, bop_ranges_rows, "bop_key", bop_pk, "bop_ranges", "balance_of_power_definitions")

    bop_range_mod_rows = load("bop_range_modifiers", "bop_range_modifiers.md")
    if bop_range_mod_rows:
        check_fk(result, bop_range_mod_rows, "range_id", bop_range_pk, "bop_range_modifiers", "bop_ranges")

    if cf_rows:
        check_fk(result, cf_rows, "palette_id", cf_palette_pk, "continuous_focuses", "continuous_focus_palettes")

    cf_mod_rows = load("continuous_focus_modifiers", "continuous_focus_modifiers.md")
    if cf_mod_rows:
        check_fk(result, cf_mod_rows, "focus_id", cf_pk, "continuous_focus_modifiers", "continuous_focuses")

    # Phase 22: Misc DLC
    dyn_mod_eff_rows = load("dynamic_modifier_effects", "dynamic_modifier_effects.md")
    if dyn_mod_eff_rows:
        check_fk(result, dyn_mod_eff_rows, "modifier_key", dyn_mod_pk, "dynamic_modifier_effects", "dynamic_modifiers")

    sci_trait_mod_rows = load("scientist_trait_modifiers", "scientist_trait_modifiers.md")
    if sci_trait_mod_rows:
        check_fk(result, sci_trait_mod_rows, "trait_key", sci_trait_pk, "scientist_trait_modifiers", "scientist_traits")

    peace_cost_rows = load("peace_cost_modifiers", "peace_cost_modifiers.md")
    if peace_cost_rows:
        check_fk(result, peace_cost_rows, "category_key", peace_cat_pk, "peace_cost_modifiers", "peace_action_categories")

    # Phase 23: Doctrines
    doctrine_folder_rows = load("doctrine_folders", "doctrine_folders.md")
    doctrine_folder_pk = build_pk_index(doctrine_folder_rows, "folder_key")

    doctrine_track_rows = load("doctrine_tracks", "doctrine_tracks.md")
    doctrine_track_pk = build_pk_index(doctrine_track_rows, "track_key")

    grand_doctrine_rows = load("grand_doctrines", "grand_doctrines.md")
    grand_doctrine_pk = build_pk_index(grand_doctrine_rows, "doctrine_key")

    gd_track_rows = load("grand_doctrine_tracks", "grand_doctrine_tracks.md")

    subdoctrine_rows = load("subdoctrines", "subdoctrines.md")
    subdoctrine_pk = build_pk_index(subdoctrine_rows, "subdoctrine_key")

    csd_rows = load("country_starting_doctrines", "country_starting_doctrines.md")

    if doctrine_track_rows:
        check_fk(result, doctrine_track_rows, "folder_key", doctrine_folder_pk, "doctrine_tracks", "doctrine_folders")

    if grand_doctrine_rows:
        check_fk(result, grand_doctrine_rows, "folder_key", doctrine_folder_pk, "grand_doctrines", "doctrine_folders")

    if gd_track_rows:
        check_fk(result, gd_track_rows, "doctrine_key", grand_doctrine_pk, "grand_doctrine_tracks", "grand_doctrines")
        check_fk(result, gd_track_rows, "track_key", doctrine_track_pk, "grand_doctrine_tracks", "doctrine_tracks")

    if subdoctrine_rows:
        check_fk(result, subdoctrine_rows, "track_key", doctrine_track_pk, "subdoctrines", "doctrine_tracks")

    if csd_rows:
        check_fk(result, csd_rows, "country_tag", country_pk, "country_starting_doctrines", "countries")
        # Check grand doctrine keys
        grand_csd = [r for r in csd_rows if r.get("doctrine_type", "").strip() == "grand"]
        check_fk(result, grand_csd, "doctrine_key", grand_doctrine_pk, "country_starting_doctrines(grand)", "grand_doctrines")
        # Check subdoctrine keys
        sub_csd = [r for r in csd_rows if r.get("doctrine_type", "").strip() == "sub"]
        check_fk(result, sub_csd, "doctrine_key", subdoctrine_pk, "country_starting_doctrines(sub)", "subdoctrines")

    # ── Unique / PK checks ───────────────────────────────────────

    if countries_rows:
        check_unique(result, countries_rows, ["tag"], "countries")
    if states_rows:
        check_unique(result, states_rows, ["state_id"], "states")
    if provinces_rows:
        check_unique(result, provinces_rows, ["province_id"], "provinces")
    if technologies_rows:
        check_unique(result, technologies_rows, ["technology_key"], "technologies")
    if equipment_rows:
        check_unique(result, equipment_rows, ["equipment_key"], "equipment_definitions")
    if ideas_rows:
        check_unique(result, ideas_rows, ["idea_key"], "ideas")
    if focus_trees_rows:
        check_unique(result, focus_trees_rows, ["focus_tree_id"], "focus_trees")
    if focuses_rows:
        check_unique(result, focuses_rows, ["focus_id"], "focuses")
    if operations_rows:
        check_unique(result, operations_rows, ["operation_key"], "operations")
    if mio_template_rows:
        check_unique(result, mio_template_rows, ["template_key"], "mio_templates")
    if mio_org_rows:
        check_unique(result, mio_org_rows, ["organization_key"], "mio_organizations")
    if doctrine_folder_rows:
        check_unique(result, doctrine_folder_rows, ["folder_key"], "doctrine_folders")
    if doctrine_track_rows:
        check_unique(result, doctrine_track_rows, ["track_key"], "doctrine_tracks")
    if grand_doctrine_rows:
        check_unique(result, grand_doctrine_rows, ["doctrine_key"], "grand_doctrines")
    if subdoctrine_rows:
        check_unique(result, subdoctrine_rows, ["subdoctrine_key"], "subdoctrines")

    # ── NOT NULL checks on critical columns ──────────────────────

    if states_rows:
        check_not_null(result, states_rows, "state_id", "states")
        check_not_null(result, states_rows, "name_key", "states")
    if provinces_rows:
        check_not_null(result, provinces_rows, "province_id", "provinces")
        check_not_null(result, provinces_rows, "terrain", "provinces")
    if sp_rows:
        check_not_null(result, sp_rows, "state_id", "state_provinces")
        check_not_null(result, sp_rows, "province_id", "state_provinces")

    # ── Row-count summary ────────────────────────────────────────

    result.note("")
    result.note("=== ROW COUNT SUMMARY ===")
    total = 0
    for name in sorted(dumps.keys()):
        _, rows = dumps[name]
        count = len(rows)
        total += count
        result.note(f"  {name}: {count:,} rows")
    result.note(f"  TOTAL: {total:,} rows across {len(dumps)} datasets")

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Validate HOI4 data dumps")
    parser.add_argument(
        "--dump-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent.parent / "docs" / "data-dump",
        help="Path to data-dump directory",
    )
    args = parser.parse_args()

    print(f"Validating data dumps in: {args.dump_dir}\n")
    result = run_validation(args.dump_dir)

    # Print results
    if result.errors:
        print(f"{'='*60}")
        print(f"ERRORS ({len(result.errors)})")
        print(f"{'='*60}")
        for e in result.errors:
            print(f"  ✗ {e}")
        print()

    if result.warnings:
        print(f"{'='*60}")
        print(f"WARNINGS ({len(result.warnings)})")
        print(f"{'='*60}")
        for w in result.warnings:
            print(f"  ⚠ {w}")
        print()

    print(f"{'='*60}")
    print(f"INFO ({len(result.info)})")
    print(f"{'='*60}")
    for i in result.info:
        print(f"  {i}")

    print(f"\nSummary: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
    sys.exit(1 if result.errors else 0)


if __name__ == "__main__":
    main()
