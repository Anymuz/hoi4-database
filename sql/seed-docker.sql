-- HOI4 PostgreSQL Seed Load Order — All 127 Tables (FK-safe)
--
-- Every \copy uses an explicit column list so that SERIAL/BIGSERIAL PKs are
-- auto-generated and CSV column order does not need to match the schema.
-- Tables that need FK resolution from natural keys to surrogate IDs use
-- staging temp tables with INSERT ... SELECT ... JOIN.
--
-- Usage:  psql -d hoi4 -f sql/seed-load-order.sql
--         (run from the repo root so data/csv/ paths resolve)

BEGIN;

-- ============================================================
-- TIER 0 — Root reference tables (32 tables, no FK dependencies)
-- ============================================================
COPY continents (continent_id, continent_key) FROM '/data_csv/continents.csv' WITH (FORMAT csv, HEADER);
COPY terrain_types (terrain_type) FROM '/data_csv/terrain_types.csv' WITH (FORMAT csv, HEADER);
COPY state_categories (state_category) FROM '/data_csv/state_categories.csv' WITH (FORMAT csv, HEADER);
COPY resource_types (resource_key, icon_frame, civilian_factory_cost_unit, convoy_cost_unit) FROM '/data_csv/resource_types.csv' WITH (FORMAT csv, HEADER);
COPY building_types (building_key, base_cost, show_on_map, state_max, province_max, shares_slots, source_file) FROM '/data_csv/building_types.csv' WITH (FORMAT csv, HEADER);
COPY ideologies (ideology_key, color_r, color_g, color_b) FROM '/data_csv/ideologies.csv' WITH (FORMAT csv, HEADER);
COPY technology_categories (category_key) FROM '/data_csv/technology_categories.csv' WITH (FORMAT csv, HEADER);
COPY character_traits (trait_key, trait_type) FROM '/data_csv/character_traits.csv' WITH (FORMAT csv, HEADER);
COPY operation_tokens (token_key, name, "desc", icon, text_icon, intel_source, intel_gain) FROM '/data_csv/operation_tokens.csv' WITH (FORMAT csv, HEADER);
COPY operation_phase_definitions (phase_key, name, "desc", icon, picture, return_on_complete, source_file) FROM '/data_csv/operation_phase_definitions.csv' WITH (FORMAT csv, HEADER);
COPY intel_agency_upgrade_branches (branch_key) FROM '/data_csv/intel_agency_upgrade_branches.csv' WITH (FORMAT csv, HEADER);
COPY compliance_modifiers (modifier_key, type, icon, small_icon, threshold, margin, dlc_source) FROM '/data_csv/compliance_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY resistance_modifiers (modifier_key, type, icon, small_icon, threshold, margin) FROM '/data_csv/resistance_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY resistance_activities (activity_key, alert_text, max_amount, duration) FROM '/data_csv/resistance_activities.csv' WITH (FORMAT csv, HEADER);
COPY mio_equipment_groups (group_key) FROM '/data_csv/mio_equipment_groups.csv' WITH (FORMAT csv, HEADER);
COPY mio_templates (template_key, icon, dlc_source, source_file) FROM '/data_csv/mio_templates.csv' WITH (FORMAT csv, HEADER);
COPY mio_policies (policy_key, icon, dlc_source, source_file) FROM '/data_csv/mio_policies.csv' WITH (FORMAT csv, HEADER);
COPY raid_categories (category_key, intel_source, faction_influence_score_on_success, free_targeting, dlc_source) FROM '/data_csv/raid_categories.csv' WITH (FORMAT csv, HEADER);
COPY medals (medal_key, name, description, frame_1, frame_2, frame_3, tracked_variable) FROM '/data_csv/medals.csv' WITH (FORMAT csv, HEADER);
COPY ribbons (ribbon_key, name, description, quote_text) FROM '/data_csv/ribbons.csv' WITH (FORMAT csv, HEADER);
COPY ace_modifiers (modifier_key, chance) FROM '/data_csv/ace_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY unit_medals (medal_key, frame, icon, cost) FROM '/data_csv/unit_medals.csv' WITH (FORMAT csv, HEADER);
COPY continuous_focus_palettes (palette_id, is_default, reset_on_civilwar, position_x, position_y, source_file) FROM '/data_csv/continuous_focus_palettes.csv' WITH (FORMAT csv, HEADER);
COPY technology_sharing_groups (group_id, name, "desc", picture, research_sharing_per_country_bonus, dlc_source, source_file) FROM '/data_csv/technology_sharing_groups.csv' WITH (FORMAT csv, HEADER);
COPY dynamic_modifiers (modifier_key, icon, attacker_modifier, source_file) FROM '/data_csv/dynamic_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY scientist_traits (trait_key, icon, dlc_source) FROM '/data_csv/scientist_traits.csv' WITH (FORMAT csv, HEADER);
COPY peace_action_categories (category_key, name, is_default) FROM '/data_csv/peace_action_categories.csv' WITH (FORMAT csv, HEADER);
COPY autonomy_states (autonomy_key, is_puppet, is_default, min_freedom_level, manpower_influence, dlc_source) FROM '/data_csv/autonomy_states.csv' WITH (FORMAT csv, HEADER);
COPY occupation_laws (occupation_law_key, icon_index, sound_effect, gui_order, main_fallback_law, fallback_law_key) FROM '/data_csv/occupation_laws.csv' WITH (FORMAT csv, HEADER);
COPY decision_categories (category_key, icon, picture_gfx, priority) FROM '/data_csv/decision_categories.csv' WITH (FORMAT csv, HEADER);
COPY balance_of_power_definitions (bop_key, initial_value, left_side, right_side, decision_category, source_file) FROM '/data_csv/balance_of_power_definitions.csv' WITH (FORMAT csv, HEADER);
COPY doctrine_folders (folder_key, name_loc, ledger, xp_type) FROM '/data_csv/doctrine_folders.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 1 — Depends only on Tier 0 (32 tables)
-- ============================================================
COPY terrain_combat_modifiers (terrain_type, unit_class, modifier_key, modifier_value) FROM '/data_csv/terrain_combat_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY terrain_building_limits (terrain_type, building_key, max_level) FROM '/data_csv/terrain_building_limits.csv' WITH (FORMAT csv, HEADER);
COPY sub_ideologies (ideology_key, sub_ideology_key) FROM '/data_csv/sub_ideologies.csv' WITH (FORMAT csv, HEADER);
COPY doctrine_tracks (track_key, folder_key, name_loc, mastery_multiplier) FROM '/data_csv/doctrine_tracks.csv' WITH (FORMAT csv, HEADER);
COPY grand_doctrines (doctrine_key, folder_key, name_loc, xp_cost, xp_type, source_file) FROM '/data_csv/grand_doctrines.csv' WITH (FORMAT csv, HEADER);
COPY technologies (technology_key, research_cost, start_year, folder_name, source_file) FROM '/data_csv/technologies.csv' WITH (FORMAT csv, HEADER);
COPY unit_types (unit_type_key, abbreviation, unit_group, combat_width, max_strength, max_organisation, default_morale, manpower, training_time, suppression, weight, supply_consumption, source_file) FROM '/data_csv/unit_types.csv' WITH (FORMAT csv, HEADER);
COPY equipment_definitions (equipment_key, is_archetype, archetype_key, parent_key, year, build_cost_ic, reliability, maximum_speed, defense, breakthrough, soft_attack, hard_attack, ap_attack, air_attack, armor_value, hardness, is_buildable, source_file) FROM '/data_csv/equipment_definitions.csv' WITH (FORMAT csv, HEADER);
COPY provinces (province_id, map_r, map_g, map_b, province_kind, is_coastal, terrain, continent_id) FROM '/data_csv/provinces.csv' WITH (FORMAT csv, HEADER);
COPY autonomy_state_modifiers (autonomy_key, modifier_key, modifier_value) FROM '/data_csv/autonomy_state_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY occupation_law_modifiers (occupation_law_key, modifier_key, modifier_value, is_suppressed) FROM '/data_csv/occupation_law_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY operation_phase_equipment (phase_key, equipment_key, amount) FROM '/data_csv/operation_phase_equipment.csv' WITH (FORMAT csv, HEADER);
COPY operations (operation_key, name, "desc", icon, priority, days, network_strength, operatives, risk_chance, experience, cost_multiplier, outcome_extra_chance, prevent_captured_operative_to_die, scale_cost_independent_of_target, dlc_source, source_file) FROM '/data_csv/operations.csv' WITH (FORMAT csv, HEADER);
COPY intel_agency_upgrades (upgrade_key, branch_key, picture, frame, sound) FROM '/data_csv/intel_agency_upgrades.csv' WITH (FORMAT csv, HEADER);
COPY compliance_modifier_effects (modifier_key, effect_key, effect_value) FROM '/data_csv/compliance_modifier_effects.csv' WITH (FORMAT csv, HEADER);
COPY resistance_modifier_effects (modifier_key, effect_key, effect_value) FROM '/data_csv/resistance_modifier_effects.csv' WITH (FORMAT csv, HEADER);
COPY mio_equipment_group_members (group_key, equipment_type) FROM '/data_csv/mio_equipment_group_members.csv' WITH (FORMAT csv, HEADER);
COPY mio_organizations (organization_key, template_key, icon, dlc_source, source_file) FROM '/data_csv/mio_organizations.csv' WITH (FORMAT csv, HEADER);
COPY mio_policy_bonuses (policy_key, bonus_category, bonus_key, bonus_value) FROM '/data_csv/mio_policy_bonuses.csv' WITH (FORMAT csv, HEADER);
COPY raids (raid_key, category_key, days_to_prepare, command_power, target_icon, launch_sound, custom_map_icon, dlc_source, source_file) FROM '/data_csv/raids.csv' WITH (FORMAT csv, HEADER);
COPY medal_tiers (medal_key, tier, variable, threshold_value, compare) FROM '/data_csv/medal_tiers.csv' WITH (FORMAT csv, HEADER);
COPY ace_modifier_effects (modifier_key, effect_key, effect_value) FROM '/data_csv/ace_modifier_effects.csv' WITH (FORMAT csv, HEADER);
COPY ace_modifier_equipment_types (modifier_key, equipment_type) FROM '/data_csv/ace_modifier_equipment_types.csv' WITH (FORMAT csv, HEADER);
COPY unit_medal_modifiers (medal_key, modifier_key, modifier_value) FROM '/data_csv/unit_medal_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY continuous_focuses (focus_id, palette_id, icon, daily_cost, available_if_capitulated, dlc_source) FROM '/data_csv/continuous_focuses.csv' WITH (FORMAT csv, HEADER);
COPY dynamic_modifier_effects (modifier_key, effect_key, effect_value_static, effect_value_variable) FROM '/data_csv/dynamic_modifier_effects.csv' WITH (FORMAT csv, HEADER);
COPY scientist_trait_modifiers (trait_key, modifier_key, modifier_value) FROM '/data_csv/scientist_trait_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY peace_cost_modifiers (modifier_key, category_key, peace_action_type, cost_multiplier, dlc_source, source_file) FROM '/data_csv/peace_cost_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY bop_sides (bop_key, side_id, side_position, icon) FROM '/data_csv/bop_sides.csv' WITH (FORMAT csv, HEADER);
COPY ideas (idea_key, slot, is_law, cost, removal_cost, is_default, source_file) FROM '/data_csv/ideas.csv' WITH (FORMAT csv, HEADER);
COPY grand_doctrine_tracks (doctrine_key, track_key, ordinal) FROM '/data_csv/grand_doctrine_tracks.csv' WITH (FORMAT csv, HEADER);
COPY subdoctrines (subdoctrine_key, track_key, name_loc, xp_cost, xp_type, reward_count, source_file) FROM '/data_csv/subdoctrines.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 2 — Depends on Tier 0 + 1 (23 tables)
-- ============================================================
COPY equipment_resources (equipment_key, resource_key, amount, source_file) FROM '/data_csv/equipment_resources.csv' WITH (FORMAT csv, HEADER);
COPY technology_categories_junction (technology_key, category_key) FROM '/data_csv/technology_categories_junction.csv' WITH (FORMAT csv, HEADER);
COPY technology_prerequisites (technology_key, prerequisite_key, source_file) FROM '/data_csv/technology_prerequisites.csv' WITH (FORMAT csv, HEADER);
COPY technology_enables_equipment (technology_key, equipment_key, source_file) FROM '/data_csv/technology_enables_equipment.csv' WITH (FORMAT csv, HEADER);
COPY technology_enables_units (technology_key, unit_type_key, source_file) FROM '/data_csv/technology_enables_units.csv' WITH (FORMAT csv, HEADER);
COPY province_building_positions (province_id, building_type, pos_x, pos_y, pos_z, rotation, linked_province_id) FROM '/data_csv/province_building_positions.csv' WITH (FORMAT csv, HEADER);
COPY strategic_regions (strategic_region_id, name_key, source_file) FROM '/data_csv/strategic_regions.csv' WITH (FORMAT csv, HEADER);
COPY supply_nodes (level, province_id) FROM '/data_csv/supply_nodes.csv' WITH (FORMAT csv, HEADER);
COPY province_adjacencies (from_province_id, to_province_id, adjacency_type, through_province_id, start_x, start_y, stop_x, stop_y, adjacency_rule_name, comment) FROM '/data_csv/province_adjacencies.csv' WITH (FORMAT csv, HEADER);
COPY province_railways (from_province_id, to_province_id, railway_level) FROM '/data_csv/province_railways.csv' WITH (FORMAT csv, HEADER);
COPY states (state_id, state_name_key, manpower, state_category, local_supplies, source_file) FROM '/data_csv/states.csv' WITH (FORMAT csv, HEADER);
COPY idea_modifiers (idea_key, modifier_key, modifier_value, source_file) FROM '/data_csv/idea_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY operation_awarded_tokens (operation_key, token_key) FROM '/data_csv/operation_awarded_tokens.csv' WITH (FORMAT csv, HEADER);
COPY operation_equipment_requirements (operation_key, equipment_key, amount) FROM '/data_csv/operation_equipment_requirements.csv' WITH (FORMAT csv, HEADER);
COPY operation_phase_groups (operation_key, sequence_index) FROM '/data_csv/operation_phase_groups.csv' WITH (FORMAT csv, HEADER);
COPY intel_agency_upgrade_levels (upgrade_key, level_index, modifier_key, modifier_value) FROM '/data_csv/intel_agency_upgrade_levels.csv' WITH (FORMAT csv, HEADER);
COPY intel_agency_upgrade_progress_modifiers (upgrade_key, modifier_key, modifier_value) FROM '/data_csv/intel_agency_upgrade_progress_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY mio_organization_equipment_types (owner_key, equipment_type) FROM '/data_csv/mio_organization_equipment_types.csv' WITH (FORMAT csv, HEADER);
COPY mio_initial_traits (owner_key, owner_type, name) FROM '/data_csv/mio_initial_traits.csv' WITH (FORMAT csv, HEADER);
COPY mio_traits (trait_token, owner_key, owner_type, trait_type, name, icon, special_trait_background, position_x, position_y, relative_position_id) FROM '/data_csv/mio_traits.csv' WITH (FORMAT csv, HEADER);
COPY raid_equipment_requirements (raid_key, requirement_group, equipment_type, amount_min, amount_max) FROM '/data_csv/raid_equipment_requirements.csv' WITH (FORMAT csv, HEADER);
COPY continuous_focus_modifiers (focus_id, modifier_key, modifier_value) FROM '/data_csv/continuous_focus_modifiers.csv' WITH (FORMAT csv, HEADER);
COPY bop_ranges (range_id, bop_key, side_id, min_value, max_value) FROM '/data_csv/bop_ranges.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 3 — Depends on Tier 0 + 1 + 2 (12 tables)
-- ============================================================
COPY strategic_region_provinces (strategic_region_id, province_id) FROM '/data_csv/strategic_region_provinces.csv' WITH (FORMAT csv, HEADER);
COPY state_provinces (state_id, province_id, source_file) FROM '/data_csv/state_provinces.csv' WITH (FORMAT csv, HEADER);
COPY state_resources (state_id, resource_key, amount, source_file) FROM '/data_csv/state_resources.csv' WITH (FORMAT csv, HEADER);
COPY state_buildings (state_id, building_key, level, source_file) FROM '/data_csv/state_buildings.csv' WITH (FORMAT csv, HEADER);
COPY state_victory_points (state_id, province_id, victory_points, source_file) FROM '/data_csv/state_victory_points.csv' WITH (FORMAT csv, HEADER);
COPY province_buildings (province_id, state_id, building_key, effective_date, level, source_file, dlc_source) FROM '/data_csv/province_buildings.csv' WITH (FORMAT csv, HEADER);
COPY countries (tag, country_file_path, graphical_culture, graphical_culture_2d, color_r, color_g, color_b, capital_state_id, stability, war_support) FROM '/data_csv/countries.csv' WITH (FORMAT csv, HEADER);
COPY operation_phase_options (operation_key, sequence_index, phase_key, base_weight) FROM '/data_csv/operation_phase_options.csv' WITH (FORMAT csv, HEADER);
COPY mio_trait_bonuses (trait_token, bonus_category, bonus_key, bonus_value) FROM '/data_csv/mio_trait_bonuses.csv' WITH (FORMAT csv, HEADER);
COPY mio_trait_prerequisites (trait_token, parent_token, requirement_type) FROM '/data_csv/mio_trait_prerequisites.csv' WITH (FORMAT csv, HEADER);
COPY mio_trait_exclusions (trait_token_a, trait_token_b) FROM '/data_csv/mio_trait_exclusions.csv' WITH (FORMAT csv, HEADER);
COPY bop_range_modifiers (range_id, modifier_key, modifier_value) FROM '/data_csv/bop_range_modifiers.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 4 — Depends on countries / Tier 3 (15 tables)
-- ============================================================
COPY state_ownership_history (state_id, effective_date, owner_tag, controller_tag, source_file, dlc_source) FROM '/data_csv/state_ownership_history.csv' WITH (FORMAT csv, HEADER);
COPY province_controller_history (province_id, state_id, effective_date, controller_tag, source_file, dlc_source) FROM '/data_csv/province_controller_history.csv' WITH (FORMAT csv, HEADER);
COPY state_cores (state_id, country_tag, effective_date, source_file, dlc_source) FROM '/data_csv/state_cores.csv' WITH (FORMAT csv, HEADER);
COPY country_starting_technologies (country_tag, technology_key, source_file) FROM '/data_csv/country_starting_technologies.csv' WITH (FORMAT csv, HEADER);
COPY country_starting_ideas (country_tag, idea_key, effective_date, source_file, dlc_source) FROM '/data_csv/country_starting_ideas.csv' WITH (FORMAT csv, HEADER);
COPY characters (character_id, name_key, gender, source_file) FROM '/data_csv/characters.csv' WITH (FORMAT csv, HEADER);
COPY division_templates (template_name, division_names_group, source_file) FROM '/data_csv/division_templates.csv' WITH (FORMAT csv, HEADER);
COPY equipment_variants (owner_tag, base_equipment_key, version_name, source_file) FROM '/data_csv/equipment_variants.csv' WITH (FORMAT csv, HEADER);
COPY fleets (country_tag, fleet_name, naval_base_province_id, source_file) FROM '/data_csv/fleets.csv' WITH (FORMAT csv, HEADER);
COPY air_wings (country_tag, location_state_id, wing_name, equipment_type, amount, version_name, source_file) FROM '/data_csv/air_wings.csv' WITH (FORMAT csv, HEADER);
COPY focus_trees (focus_tree_id, initial_x, initial_y, source_file) FROM '/data_csv/focus_trees.csv' WITH (FORMAT csv, HEADER);
COPY country_visual_definitions (country_tag, graphical_culture, graphical_culture_2d) FROM '/data_csv/country_visual_definitions.csv' WITH (FORMAT csv, HEADER);
COPY intelligence_agencies (agency_id, picture_gfx, default_tag, available_tag, dlc_source, source_file) FROM '/data_csv/intelligence_agencies.csv' WITH (FORMAT csv, HEADER);
COPY bookmarks (bookmark_name, bookmark_date, picture_gfx, default_country_tag) FROM '/data_csv/bookmarks.csv' WITH (FORMAT csv, HEADER);
COPY country_starting_doctrines (country_tag, date, doctrine_type, doctrine_key) FROM '/data_csv/country_starting_doctrines.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 5 — Depends on Tier 4 (9 tables, 4 need FK staging)
-- ============================================================
COPY character_roles (character_id, role_type, sub_ideology_key, source_file) FROM '/data_csv/character_roles.csv' WITH (FORMAT csv, HEADER);
COPY divisions (template_name, location_province_id, start_experience_factor, source_file) FROM '/data_csv/divisions.csv' WITH (FORMAT csv, HEADER);
COPY focuses (focus_id, focus_tree_id, x_pos, y_pos, cost, icon, source_file) FROM '/data_csv/focuses.csv' WITH (FORMAT csv, HEADER);
COPY intelligence_agency_names (agency_id, name) FROM '/data_csv/intelligence_agency_names.csv' WITH (FORMAT csv, HEADER);
COPY decisions (decision_key, category_key, icon, cost, fire_only_once, dlc_source) FROM '/data_csv/decisions.csv' WITH (FORMAT csv, HEADER);

-- division_template_regiments: resolve template_name → division_template_id
CREATE TEMP TABLE _stage_dtr (template_name TEXT, unit_type_key TEXT, grid_x TEXT, grid_y TEXT);
COPY _stage_dtr FROM '/data_csv/division_template_regiments.csv' WITH (FORMAT csv, HEADER);
INSERT INTO division_template_regiments (division_template_id, unit_type_key, grid_x, grid_y)
  SELECT dt.division_template_id, s.unit_type_key, s.grid_x::smallint, s.grid_y::smallint
  FROM _stage_dtr s
  JOIN division_templates dt ON dt.template_name = s.template_name;
DROP TABLE _stage_dtr;

-- division_template_support: resolve template_name → division_template_id
CREATE TEMP TABLE _stage_dts (template_name TEXT, unit_type_key TEXT, grid_x TEXT, grid_y TEXT);
COPY _stage_dts FROM '/data_csv/division_template_support.csv' WITH (FORMAT csv, HEADER);
INSERT INTO division_template_support (division_template_id, unit_type_key, grid_x, grid_y)
  SELECT dt.division_template_id, s.unit_type_key, s.grid_x::smallint, s.grid_y::smallint
  FROM _stage_dts s
  JOIN division_templates dt ON dt.template_name = s.template_name;
DROP TABLE _stage_dts;

-- task_forces: resolve (country_tag, fleet_name) → fleet_id
CREATE TEMP TABLE _stage_tf (country_tag TEXT, fleet_name TEXT, task_force_name TEXT, location_province_id TEXT, source_file TEXT);
COPY _stage_tf FROM '/data_csv/task_forces.csv' WITH (FORMAT csv, HEADER);
INSERT INTO task_forces (fleet_id, task_force_name, location_province_id)
  SELECT f.fleet_id, s.task_force_name, NULLIF(s.location_province_id, '')::int
  FROM _stage_tf s
  JOIN fleets f ON f.country_tag = s.country_tag AND f.fleet_name = s.fleet_name;
DROP TABLE _stage_tf;

-- bookmark_countries: resolve bookmark_name → bookmark_id
CREATE TEMP TABLE _stage_bc (bookmark_name TEXT, country_tag TEXT, ideology_key TEXT);
COPY _stage_bc FROM '/data_csv/bookmark_countries.csv' WITH (FORMAT csv, HEADER);
INSERT INTO bookmark_countries (bookmark_id, country_tag, ideology_key)
  SELECT b.bookmark_id, s.country_tag, s.ideology_key
  FROM _stage_bc s
  JOIN bookmarks b ON b.bookmark_name = s.bookmark_name;
DROP TABLE _stage_bc;

-- ============================================================
-- TIER 6 — Leaf tables (4 tables, 2 need FK staging)
-- ============================================================
COPY focus_prerequisites (focus_id, required_focus_id) FROM '/data_csv/focus_prerequisites.csv' WITH (FORMAT csv, HEADER);
COPY focus_mutually_exclusive (focus_a_id, focus_b_id) FROM '/data_csv/focus_mutually_exclusive.csv' WITH (FORMAT csv, HEADER);

-- character_role_traits: resolve (character_id, role_type) → character_role_id
CREATE TEMP TABLE _stage_crt (character_id TEXT, role_type TEXT, trait_key TEXT, source_file TEXT);
COPY _stage_crt FROM '/data_csv/character_role_traits.csv' WITH (FORMAT csv, HEADER);
INSERT INTO character_role_traits (character_role_id, trait_key)
  SELECT cr.character_role_id, s.trait_key
  FROM _stage_crt s
  JOIN character_roles cr ON cr.character_id = s.character_id AND cr.role_type = s.role_type;
DROP TABLE _stage_crt;

-- ships: resolve (country_tag, fleet_name, task_force_name) → task_force_id
CREATE TEMP TABLE _stage_ships (
  country_tag TEXT, fleet_name TEXT, task_force_name TEXT, ship_name TEXT,
  definition TEXT, hull_equipment_key TEXT, owner_tag TEXT, version_name TEXT,
  pride_of_the_fleet TEXT, source_file TEXT
);
COPY _stage_ships FROM '/data_csv/ships.csv' WITH (FORMAT csv, HEADER);
INSERT INTO ships (task_force_id, ship_name, definition, hull_equipment_key,
                   version_name, owner_tag, pride_of_the_fleet, source_file)
  SELECT tf.task_force_id, s.ship_name, s.definition, s.hull_equipment_key,
         NULLIF(s.version_name, ''), s.owner_tag,
         CASE WHEN s.pride_of_the_fleet = 'true' THEN true ELSE NULL END,
         s.source_file
  FROM _stage_ships s
  JOIN fleets f ON f.country_tag = s.country_tag AND f.fleet_name = s.fleet_name
  JOIN task_forces tf ON tf.fleet_id = f.fleet_id AND tf.task_force_name = s.task_force_name;
DROP TABLE _stage_ships;

COMMIT;
