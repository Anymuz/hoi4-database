-- HOI4 PostgreSQL Seed Load Order — All 127 Tables (FK-safe)
--
-- Every \copy uses an explicit column list so that SERIAL/BIGSERIAL PKs are
-- auto-generated and CSV column order does not need to match the schema.
-- Tables that need FK resolution from natural keys to surrogate IDs use
-- staging temp tables with INSERT ... SELECT ... JOIN.
--
-- Usage:  psql -d hoi4 -f sql/seed-load-order.sql
--         (run from the repo root so data/csv/ paths resolve)

\set ON_ERROR_STOP on
BEGIN;

-- ============================================================
-- TIER 0 — Root reference tables (32 tables, no FK dependencies)
-- ============================================================
\copy continents(continent_id, continent_key) FROM 'data/csv/continents.csv' WITH (FORMAT csv, HEADER);
\copy terrain_types(terrain_type) FROM 'data/csv/terrain_types.csv' WITH (FORMAT csv, HEADER);
\copy state_categories(state_category) FROM 'data/csv/state_categories.csv' WITH (FORMAT csv, HEADER);
\copy resource_types(resource_key, icon_frame, civilian_factory_cost_unit, convoy_cost_unit) FROM 'data/csv/resource_types.csv' WITH (FORMAT csv, HEADER);
\copy building_types(building_key, base_cost, show_on_map, state_max, province_max, shares_slots, source_file) FROM 'data/csv/building_types.csv' WITH (FORMAT csv, HEADER);
\copy ideologies(ideology_key, color_r, color_g, color_b) FROM 'data/csv/ideologies.csv' WITH (FORMAT csv, HEADER);
\copy technology_categories(category_key) FROM 'data/csv/technology_categories.csv' WITH (FORMAT csv, HEADER);
\copy character_traits(trait_key, trait_type) FROM 'data/csv/character_traits.csv' WITH (FORMAT csv, HEADER);
\copy operation_tokens(token_key, name, "desc", icon, text_icon, intel_source, intel_gain) FROM 'data/csv/operation_tokens.csv' WITH (FORMAT csv, HEADER);
\copy operation_phase_definitions(phase_key, name, "desc", icon, picture, return_on_complete, source_file) FROM 'data/csv/operation_phase_definitions.csv' WITH (FORMAT csv, HEADER);
\copy intel_agency_upgrade_branches(branch_key) FROM 'data/csv/intel_agency_upgrade_branches.csv' WITH (FORMAT csv, HEADER);
\copy compliance_modifiers(modifier_key, type, icon, small_icon, threshold, margin, dlc_source) FROM 'data/csv/compliance_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy resistance_modifiers(modifier_key, type, icon, small_icon, threshold, margin) FROM 'data/csv/resistance_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy resistance_activities(activity_key, alert_text, max_amount, duration) FROM 'data/csv/resistance_activities.csv' WITH (FORMAT csv, HEADER);
\copy mio_equipment_groups(group_key) FROM 'data/csv/mio_equipment_groups.csv' WITH (FORMAT csv, HEADER);
\copy mio_templates(template_key, icon, dlc_source, source_file) FROM 'data/csv/mio_templates.csv' WITH (FORMAT csv, HEADER);
\copy mio_policies(policy_key, icon, dlc_source, source_file) FROM 'data/csv/mio_policies.csv' WITH (FORMAT csv, HEADER);
\copy raid_categories(category_key, intel_source, faction_influence_score_on_success, free_targeting, dlc_source) FROM 'data/csv/raid_categories.csv' WITH (FORMAT csv, HEADER);
\copy medals(medal_key, name, description, frame_1, frame_2, frame_3, tracked_variable) FROM 'data/csv/medals.csv' WITH (FORMAT csv, HEADER);
\copy ribbons(ribbon_key, name, description, quote_text) FROM 'data/csv/ribbons.csv' WITH (FORMAT csv, HEADER);
\copy ace_modifiers(modifier_key, chance) FROM 'data/csv/ace_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy unit_medals(medal_key, frame, icon, cost) FROM 'data/csv/unit_medals.csv' WITH (FORMAT csv, HEADER);
\copy continuous_focus_palettes(palette_id, is_default, reset_on_civilwar, position_x, position_y, source_file) FROM 'data/csv/continuous_focus_palettes.csv' WITH (FORMAT csv, HEADER);
\copy technology_sharing_groups(group_id, name, "desc", picture, research_sharing_per_country_bonus, dlc_source, source_file) FROM 'data/csv/technology_sharing_groups.csv' WITH (FORMAT csv, HEADER);
\copy dynamic_modifiers(modifier_key, icon, attacker_modifier, source_file) FROM 'data/csv/dynamic_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy scientist_traits(trait_key, icon, dlc_source) FROM 'data/csv/scientist_traits.csv' WITH (FORMAT csv, HEADER);
\copy peace_action_categories(category_key, name, is_default) FROM 'data/csv/peace_action_categories.csv' WITH (FORMAT csv, HEADER);
\copy autonomy_states(autonomy_key, is_puppet, is_default, min_freedom_level, manpower_influence, dlc_source) FROM 'data/csv/autonomy_states.csv' WITH (FORMAT csv, HEADER);
\copy occupation_laws(occupation_law_key, icon_index, sound_effect, gui_order, main_fallback_law, fallback_law_key) FROM 'data/csv/occupation_laws.csv' WITH (FORMAT csv, HEADER);
\copy decision_categories(category_key, icon, picture_gfx, priority) FROM 'data/csv/decision_categories.csv' WITH (FORMAT csv, HEADER);
\copy balance_of_power_definitions(bop_key, initial_value, left_side, right_side, decision_category, source_file) FROM 'data/csv/balance_of_power_definitions.csv' WITH (FORMAT csv, HEADER);
\copy doctrine_folders(folder_key, name_loc, ledger, xp_type) FROM 'data/csv/doctrine_folders.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 1 — Depends only on Tier 0 (32 tables)
-- ============================================================
\copy terrain_combat_modifiers(terrain_type, unit_class, modifier_key, modifier_value) FROM 'data/csv/terrain_combat_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy terrain_building_limits(terrain_type, building_key, max_level) FROM 'data/csv/terrain_building_limits.csv' WITH (FORMAT csv, HEADER);
\copy sub_ideologies(ideology_key, sub_ideology_key) FROM 'data/csv/sub_ideologies.csv' WITH (FORMAT csv, HEADER);
\copy doctrine_tracks(track_key, folder_key, name_loc, mastery_multiplier) FROM 'data/csv/doctrine_tracks.csv' WITH (FORMAT csv, HEADER);
\copy grand_doctrines(doctrine_key, folder_key, name_loc, xp_cost, xp_type, source_file) FROM 'data/csv/grand_doctrines.csv' WITH (FORMAT csv, HEADER);
\copy technologies(technology_key, research_cost, start_year, folder_name, source_file) FROM 'data/csv/technologies.csv' WITH (FORMAT csv, HEADER);
\copy unit_types(unit_type_key, abbreviation, unit_group, combat_width, max_strength, max_organisation, default_morale, manpower, training_time, suppression, weight, supply_consumption, source_file) FROM 'data/csv/unit_types.csv' WITH (FORMAT csv, HEADER);
\copy equipment_definitions(equipment_key, is_archetype, archetype_key, parent_key, year, build_cost_ic, reliability, maximum_speed, defense, breakthrough, soft_attack, hard_attack, ap_attack, air_attack, armor_value, hardness, is_buildable, source_file) FROM 'data/csv/equipment_definitions.csv' WITH (FORMAT csv, HEADER);
\copy provinces(province_id, map_r, map_g, map_b, province_kind, is_coastal, terrain, continent_id) FROM 'data/csv/provinces.csv' WITH (FORMAT csv, HEADER);
\copy autonomy_state_modifiers(autonomy_key, modifier_key, modifier_value) FROM 'data/csv/autonomy_state_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy occupation_law_modifiers(occupation_law_key, modifier_key, modifier_value, is_suppressed) FROM 'data/csv/occupation_law_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy operation_phase_equipment(phase_key, equipment_key, amount) FROM 'data/csv/operation_phase_equipment.csv' WITH (FORMAT csv, HEADER);
\copy operations(operation_key, name, "desc", icon, priority, days, network_strength, operatives, risk_chance, experience, cost_multiplier, outcome_extra_chance, prevent_captured_operative_to_die, scale_cost_independent_of_target, dlc_source, source_file) FROM 'data/csv/operations.csv' WITH (FORMAT csv, HEADER);
\copy intel_agency_upgrades(upgrade_key, branch_key, picture, frame, sound) FROM 'data/csv/intel_agency_upgrades.csv' WITH (FORMAT csv, HEADER);
\copy compliance_modifier_effects(modifier_key, effect_key, effect_value) FROM 'data/csv/compliance_modifier_effects.csv' WITH (FORMAT csv, HEADER);
\copy resistance_modifier_effects(modifier_key, effect_key, effect_value) FROM 'data/csv/resistance_modifier_effects.csv' WITH (FORMAT csv, HEADER);
\copy mio_equipment_group_members(group_key, equipment_type) FROM 'data/csv/mio_equipment_group_members.csv' WITH (FORMAT csv, HEADER);
\copy mio_organizations(organization_key, template_key, icon, dlc_source, source_file) FROM 'data/csv/mio_organizations.csv' WITH (FORMAT csv, HEADER);
\copy mio_policy_bonuses(policy_key, bonus_category, bonus_key, bonus_value) FROM 'data/csv/mio_policy_bonuses.csv' WITH (FORMAT csv, HEADER);
\copy raids(raid_key, category_key, days_to_prepare, command_power, target_icon, launch_sound, custom_map_icon, dlc_source, source_file) FROM 'data/csv/raids.csv' WITH (FORMAT csv, HEADER);
\copy medal_tiers(medal_key, tier, variable, threshold_value, compare) FROM 'data/csv/medal_tiers.csv' WITH (FORMAT csv, HEADER);
\copy ace_modifier_effects(modifier_key, effect_key, effect_value) FROM 'data/csv/ace_modifier_effects.csv' WITH (FORMAT csv, HEADER);
\copy ace_modifier_equipment_types(modifier_key, equipment_type) FROM 'data/csv/ace_modifier_equipment_types.csv' WITH (FORMAT csv, HEADER);
\copy unit_medal_modifiers(medal_key, modifier_key, modifier_value) FROM 'data/csv/unit_medal_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy continuous_focuses(focus_id, palette_id, icon, daily_cost, available_if_capitulated, dlc_source) FROM 'data/csv/continuous_focuses.csv' WITH (FORMAT csv, HEADER);
\copy dynamic_modifier_effects(modifier_key, effect_key, effect_value_static, effect_value_variable) FROM 'data/csv/dynamic_modifier_effects.csv' WITH (FORMAT csv, HEADER);
\copy scientist_trait_modifiers(trait_key, modifier_key, modifier_value) FROM 'data/csv/scientist_trait_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy peace_cost_modifiers(modifier_key, category_key, peace_action_type, cost_multiplier, dlc_source, source_file) FROM 'data/csv/peace_cost_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy bop_sides(bop_key, side_id, side_position, icon) FROM 'data/csv/bop_sides.csv' WITH (FORMAT csv, HEADER);
\copy ideas(idea_key, slot, is_law, cost, removal_cost, is_default, source_file) FROM 'data/csv/ideas.csv' WITH (FORMAT csv, HEADER);
\copy grand_doctrine_tracks(doctrine_key, track_key, ordinal) FROM 'data/csv/grand_doctrine_tracks.csv' WITH (FORMAT csv, HEADER);
\copy subdoctrines(subdoctrine_key, track_key, name_loc, xp_cost, xp_type, reward_count, source_file) FROM 'data/csv/subdoctrines.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 2 — Depends on Tier 0 + 1 (23 tables)
-- ============================================================
\copy equipment_resources(equipment_key, resource_key, amount, source_file) FROM 'data/csv/equipment_resources.csv' WITH (FORMAT csv, HEADER);
\copy technology_categories_junction(technology_key, category_key) FROM 'data/csv/technology_categories_junction.csv' WITH (FORMAT csv, HEADER);
\copy technology_prerequisites(technology_key, prerequisite_key, source_file) FROM 'data/csv/technology_prerequisites.csv' WITH (FORMAT csv, HEADER);
\copy technology_enables_equipment(technology_key, equipment_key, source_file) FROM 'data/csv/technology_enables_equipment.csv' WITH (FORMAT csv, HEADER);
\copy technology_enables_units(technology_key, unit_type_key, source_file) FROM 'data/csv/technology_enables_units.csv' WITH (FORMAT csv, HEADER);
\copy province_building_positions(province_id, building_type, pos_x, pos_y, pos_z, rotation, linked_province_id) FROM 'data/csv/province_building_positions.csv' WITH (FORMAT csv, HEADER);
\copy strategic_regions(strategic_region_id, name_key, source_file) FROM 'data/csv/strategic_regions.csv' WITH (FORMAT csv, HEADER);
\copy supply_nodes(level, province_id) FROM 'data/csv/supply_nodes.csv' WITH (FORMAT csv, HEADER);
\copy province_adjacencies(from_province_id, to_province_id, adjacency_type, through_province_id, start_x, start_y, stop_x, stop_y, adjacency_rule_name, comment) FROM 'data/csv/province_adjacencies.csv' WITH (FORMAT csv, HEADER);
\copy province_railways(from_province_id, to_province_id, railway_level) FROM 'data/csv/province_railways.csv' WITH (FORMAT csv, HEADER);
\copy states(state_id, state_name_key, manpower, state_category, local_supplies, source_file) FROM 'data/csv/states.csv' WITH (FORMAT csv, HEADER);
\copy idea_modifiers(idea_key, modifier_key, modifier_value, source_file) FROM 'data/csv/idea_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy operation_awarded_tokens(operation_key, token_key) FROM 'data/csv/operation_awarded_tokens.csv' WITH (FORMAT csv, HEADER);
\copy operation_equipment_requirements(operation_key, equipment_key, amount) FROM 'data/csv/operation_equipment_requirements.csv' WITH (FORMAT csv, HEADER);
\copy operation_phase_groups(operation_key, sequence_index) FROM 'data/csv/operation_phase_groups.csv' WITH (FORMAT csv, HEADER);
\copy intel_agency_upgrade_levels(upgrade_key, level_index, modifier_key, modifier_value) FROM 'data/csv/intel_agency_upgrade_levels.csv' WITH (FORMAT csv, HEADER);
\copy intel_agency_upgrade_progress_modifiers(upgrade_key, modifier_key, modifier_value) FROM 'data/csv/intel_agency_upgrade_progress_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy mio_organization_equipment_types(owner_key, equipment_type) FROM 'data/csv/mio_organization_equipment_types.csv' WITH (FORMAT csv, HEADER);
\copy mio_initial_traits(owner_key, owner_type, name) FROM 'data/csv/mio_initial_traits.csv' WITH (FORMAT csv, HEADER);
\copy mio_traits(trait_token, owner_key, owner_type, trait_type, name, icon, special_trait_background, position_x, position_y, relative_position_id) FROM 'data/csv/mio_traits.csv' WITH (FORMAT csv, HEADER);
\copy raid_equipment_requirements(raid_key, requirement_group, equipment_type, amount_min, amount_max) FROM 'data/csv/raid_equipment_requirements.csv' WITH (FORMAT csv, HEADER);
\copy continuous_focus_modifiers(focus_id, modifier_key, modifier_value) FROM 'data/csv/continuous_focus_modifiers.csv' WITH (FORMAT csv, HEADER);
\copy bop_ranges(range_id, bop_key, side_id, min_value, max_value) FROM 'data/csv/bop_ranges.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 3 — Depends on Tier 0 + 1 + 2 (12 tables)
-- ============================================================
\copy strategic_region_provinces(strategic_region_id, province_id) FROM 'data/csv/strategic_region_provinces.csv' WITH (FORMAT csv, HEADER);
\copy state_provinces(state_id, province_id, source_file) FROM 'data/csv/state_provinces.csv' WITH (FORMAT csv, HEADER);
\copy state_resources(state_id, resource_key, amount, source_file) FROM 'data/csv/state_resources.csv' WITH (FORMAT csv, HEADER);
\copy state_buildings(state_id, building_key, level, effective_date, source_file) FROM 'data/csv/state_buildings.csv' WITH (FORMAT csv, HEADER);
\copy state_victory_points(state_id, province_id, victory_points, source_file) FROM 'data/csv/state_victory_points.csv' WITH (FORMAT csv, HEADER);
\copy province_buildings(province_id, state_id, building_key, effective_date, level, source_file, dlc_source) FROM 'data/csv/province_buildings.csv' WITH (FORMAT csv, HEADER);
\copy countries(tag, country_file_path, graphical_culture, graphical_culture_2d, color_r, color_g, color_b, capital_state_id, stability, war_support) FROM 'data/csv/countries.csv' WITH (FORMAT csv, HEADER);
\copy operation_phase_options(operation_key, sequence_index, phase_key, base_weight) FROM 'data/csv/operation_phase_options.csv' WITH (FORMAT csv, HEADER);
\copy mio_trait_bonuses(trait_token, bonus_category, bonus_key, bonus_value) FROM 'data/csv/mio_trait_bonuses.csv' WITH (FORMAT csv, HEADER);
\copy mio_trait_prerequisites(trait_token, parent_token, requirement_type) FROM 'data/csv/mio_trait_prerequisites.csv' WITH (FORMAT csv, HEADER);
\copy mio_trait_exclusions(trait_token_a, trait_token_b) FROM 'data/csv/mio_trait_exclusions.csv' WITH (FORMAT csv, HEADER);
\copy bop_range_modifiers(range_id, modifier_key, modifier_value) FROM 'data/csv/bop_range_modifiers.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 4 — Depends on countries / Tier 3 (15 tables)
-- ============================================================
\copy state_ownership_history(state_id, effective_date, owner_tag, controller_tag, source_file, dlc_source) FROM 'data/csv/state_ownership_history.csv' WITH (FORMAT csv, HEADER);
\copy province_controller_history(province_id, state_id, effective_date, controller_tag, source_file, dlc_source) FROM 'data/csv/province_controller_history.csv' WITH (FORMAT csv, HEADER);
\copy state_cores(state_id, country_tag, effective_date, source_file, dlc_source) FROM 'data/csv/state_cores.csv' WITH (FORMAT csv, HEADER);
\copy country_starting_technologies(country_tag, technology_key, effective_date, source_file, dlc_source) FROM 'data/csv/country_starting_technologies.csv' WITH (FORMAT csv, HEADER);
\copy country_starting_ideas(country_tag, idea_key, effective_date, source_file, dlc_source) FROM 'data/csv/country_starting_ideas.csv' WITH (FORMAT csv, HEADER);
\copy characters(character_id, name_key, gender, source_file) FROM 'data/csv/characters.csv' WITH (FORMAT csv, HEADER);
\copy division_templates(template_name, division_names_group, source_file) FROM 'data/csv/division_templates.csv' WITH (FORMAT csv, HEADER);
\copy equipment_variants(owner_tag, base_equipment_key, version_name, effective_date, source_file) FROM 'data/csv/equipment_variants.csv' WITH (FORMAT csv, HEADER);
\copy fleets(country_tag, fleet_name, naval_base_province_id, source_file) FROM 'data/csv/fleets.csv' WITH (FORMAT csv, HEADER);
\copy air_wings(country_tag, location_state_id, wing_name, equipment_type, amount, version_name, source_file) FROM 'data/csv/air_wings.csv' WITH (FORMAT csv, HEADER);
\copy focus_trees(focus_tree_id, initial_x, initial_y, source_file) FROM 'data/csv/focus_trees.csv' WITH (FORMAT csv, HEADER);
\copy country_visual_definitions(country_tag, graphical_culture, graphical_culture_2d) FROM 'data/csv/country_visual_definitions.csv' WITH (FORMAT csv, HEADER);
\copy intelligence_agencies(agency_id, picture_gfx, default_tag, available_tag, dlc_source, source_file) FROM 'data/csv/intelligence_agencies.csv' WITH (FORMAT csv, HEADER);
\copy bookmarks(bookmark_name, bookmark_date, picture_gfx, default_country_tag) FROM 'data/csv/bookmarks.csv' WITH (FORMAT csv, HEADER);
\copy country_starting_doctrines(country_tag, date, doctrine_type, doctrine_key) FROM 'data/csv/country_starting_doctrines.csv' WITH (FORMAT csv, HEADER);

-- ============================================================
-- TIER 5 — Depends on Tier 4 (9 tables, 4 need FK staging)
-- ============================================================
\copy character_roles(character_id, role_type, sub_ideology_key, source_file) FROM 'data/csv/character_roles.csv' WITH (FORMAT csv, HEADER);
\copy divisions(template_name, location_province_id, start_experience_factor, source_file) FROM 'data/csv/divisions.csv' WITH (FORMAT csv, HEADER);
\copy focuses(focus_id, focus_tree_id, x_pos, y_pos, cost, icon, source_file) FROM 'data/csv/focuses.csv' WITH (FORMAT csv, HEADER);
\copy intelligence_agency_names(agency_id, name) FROM 'data/csv/intelligence_agency_names.csv' WITH (FORMAT csv, HEADER);
\copy decisions(decision_key, category_key, icon, cost, fire_only_once, dlc_source) FROM 'data/csv/decisions.csv' WITH (FORMAT csv, HEADER);

-- division_template_regiments: resolve template_name → division_template_id
CREATE TEMP TABLE _stage_dtr (template_name TEXT, unit_type_key TEXT, grid_x TEXT, grid_y TEXT);
\copy _stage_dtr FROM 'data/csv/division_template_regiments.csv' WITH (FORMAT csv, HEADER);
INSERT INTO division_template_regiments (division_template_id, unit_type_key, grid_x, grid_y)
  SELECT dt.division_template_id, s.unit_type_key, s.grid_x::smallint, s.grid_y::smallint
  FROM _stage_dtr s
  JOIN division_templates dt ON dt.template_name = s.template_name;
DROP TABLE _stage_dtr;

-- division_template_support: resolve template_name → division_template_id
CREATE TEMP TABLE _stage_dts (template_name TEXT, unit_type_key TEXT, grid_x TEXT, grid_y TEXT);
\copy _stage_dts FROM 'data/csv/division_template_support.csv' WITH (FORMAT csv, HEADER);
INSERT INTO division_template_support (division_template_id, unit_type_key, grid_x, grid_y)
  SELECT dt.division_template_id, s.unit_type_key, s.grid_x::smallint, s.grid_y::smallint
  FROM _stage_dts s
  JOIN division_templates dt ON dt.template_name = s.template_name;
DROP TABLE _stage_dts;

-- task_forces: resolve (country_tag, fleet_name) → fleet_id
CREATE TEMP TABLE _stage_tf (country_tag TEXT, fleet_name TEXT, task_force_name TEXT, location_province_id TEXT, source_file TEXT);
\copy _stage_tf FROM 'data/csv/task_forces.csv' WITH (FORMAT csv, HEADER);
INSERT INTO task_forces (fleet_id, task_force_name, location_province_id)
  SELECT f.fleet_id, s.task_force_name, NULLIF(s.location_province_id, '')::int
  FROM _stage_tf s
  JOIN fleets f ON f.country_tag = s.country_tag AND f.fleet_name = s.fleet_name;
DROP TABLE _stage_tf;

-- bookmark_countries: resolve bookmark_name → bookmark_id
CREATE TEMP TABLE _stage_bc (bookmark_name TEXT, country_tag TEXT, ideology_key TEXT);
\copy _stage_bc FROM 'data/csv/bookmark_countries.csv' WITH (FORMAT csv, HEADER);
INSERT INTO bookmark_countries (bookmark_id, country_tag, ideology_key)
  SELECT b.bookmark_id, s.country_tag, s.ideology_key
  FROM _stage_bc s
  JOIN bookmarks b ON b.bookmark_name = s.bookmark_name;
DROP TABLE _stage_bc;

-- ============================================================
-- TIER 6 — Leaf tables (4 tables, 2 need FK staging)
-- ============================================================
\copy focus_prerequisites(focus_id, required_focus_id) FROM 'data/csv/focus_prerequisites.csv' WITH (FORMAT csv, HEADER);
\copy focus_mutually_exclusive(focus_a_id, focus_b_id) FROM 'data/csv/focus_mutually_exclusive.csv' WITH (FORMAT csv, HEADER);

-- character_role_traits: resolve (character_id, role_type) → character_role_id
CREATE TEMP TABLE _stage_crt (character_id TEXT, role_type TEXT, trait_key TEXT, source_file TEXT);
\copy _stage_crt FROM 'data/csv/character_role_traits.csv' WITH (FORMAT csv, HEADER);
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
\copy _stage_ships FROM 'data/csv/ships.csv' WITH (FORMAT csv, HEADER);
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
