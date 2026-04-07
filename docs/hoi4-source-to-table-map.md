# HOI4 Source to Table Map

Status: **COMPLETE** (all 28 phases + localisation mapped — core + DLC + doctrines + factions + special projects + infrastructure)

## Purpose
Complete mapping of every source file path to target database tables and transformation rules.

---

## Source → Table Mapping

| Source path pattern | Target table(s) | Transformation notes | DLC handling |
|---|---|---|---|
| `map/continent.txt` | continents | One row per continent in file order; assign continent_id = row index | None |
| `map/definition.csv` | provinces, terrain_types | CSV parse; col1=id, col2-4=RGB, col5=province_kind, col6=is_coastal, col7=terrain, col8=continent_id. Extract distinct terrain values for terrain_types. | None |
| `map/buildings.txt` | province_building_positions | Semicolon-delimited; one row per line: province_id;building_type;x;y;z;rotation;linked_province. Convert 0 linked_province to NULL. | None |
| `map/strategicregions/*.txt` | strategic_regions, strategic_region_provinces | Parse id, name from header; provinces from provinces list block. One row per strategic region + one row per province membership. | None |
| `map/supply_nodes.txt` | supply_nodes | Two-column whitespace-delimited: level, province_id. One row per line. | None |
| `common/resources/00_resources.txt` | resource_types | One block per resource; extract resource_key, icon_frame, cic, convoys | None |
| `common/buildings/00_buildings.txt` | building_types | One block per building type; extract key, base_cost, max_level (state/province), shares_slots, only_costal. Derive is_state_level/is_province_level from max_level presence. | dlc_source nullable |
| `common/ideologies/00_ideologies.txt` | ideologies, sub_ideologies | Top-level blocks → ideologies (key, color). types sub-block → sub_ideologies (key, parent ideology_key). | None |
| `common/technologies/*.txt` | technologies, technology_categories, technology_categories_junction, technology_prerequisites, technology_enables_equipment, technology_enables_units | Per tech block: extract key, research_cost, start_year, folder. `categories = { }` → junction rows. `leads_to_tech` → prerequisites (reverse: from=current, to=target). `enable_equipments = { }` → enables_equipment. `enable_subunits = { }` → enables_units. Collect distinct categories for technology_categories. | dlc_source from `has_dlc` guard |
| `common/units/*.txt` | unit_types | One block per unit type; extract key, abbreviation, group, combat_width, max_strength, etc. Air units may lack numeric stats. | dlc_source nullable |
| `common/units/equipment/*.txt` | equipment_definitions, equipment_resources | Archetype blocks: is_archetype=true. Variant blocks: is_archetype=false, link archetype_key/parent_key. `resources = { }` sub-block → equipment_resources rows. NULL stats in variants = inherit from archetype. | dlc_source from DLC gates |
| `common/country_tags/00_countries.txt` | countries (tag, country_file_path) | `TAG = "countries/File.txt"` → one row per entry | None |
| `common/countries/*.txt` | countries (color, graphical_culture) | Parse `color = { r g b }`, graphical_culture, graphical_culture_2d | None |
| `history/countries/*.txt` | countries (capital, stability, war_support), country_starting_technologies, country_starting_ideas | Top-level fields → countries columns. `set_technology = { key = 1 }` → country_starting_technologies. `add_ideas = { key }` → country_starting_ideas. Dated blocks (1936.1.1, etc.) may override. DLC conditionals under `if = { limit = { has_dlc } }`. | dlc_source from has_dlc guards |
| `history/states/*.txt` | states, state_provinces, state_ownership_history, state_cores, state_victory_points, state_resources, state_buildings, province_buildings | state block → states row. `provinces = { }` → state_provinces. `owner = TAG` → state_ownership_history. `add_core_of = TAG` → state_cores. `victory_points = { prov vp }` → state_victory_points. `resources = { }` → state_resources. `buildings = { key = N }` → state_buildings. `buildings = { prov_id = { key = N } }` → province_buildings. | dlc_source from DLC conditionals in dated blocks |
| `common/characters/*.txt` | characters, character_roles, character_role_traits | One block per character: id, name, gender, portraits. Role sub-blocks (country_leader, field_marshal, corps_commander, navy_leader, advisor) → character_roles. `traits = { }` within roles → character_role_traits. Country_tag derived from filename prefix. | dlc_source on roles |
| `common/ideas/*.txt` | ideas, idea_modifiers | Category blocks (economy, trade_laws, country, etc.) contain idea sub-blocks. Each idea → ideas row (key, slot=parent category, cost, removal_cost, default). `modifier = { }` → idea_modifiers rows (one per key-value pair). Law categories: economy, trade_laws, mobilization_laws, conscription_laws. | dlc_source from allowed blocks |
| `common/national_focus/*.txt` | focus_trees, focuses, focus_prerequisites, focus_mutually_exclusive | `focus_tree = { id = X }` → focus_trees. `focus = { id = X }` → focuses. `prerequisite = { focus = A focus = B }` → focus_prerequisites (same group = OR). Multiple `prerequisite` blocks → different groups (AND). `mutually_exclusive = { focus = X }` → focus_mutually_exclusive (normalize: a < b). | dlc_source from has_dlc in available blocks |
| `history/units/*.txt` (land OOB) | division_templates, division_template_regiments, division_template_support, divisions | `division_template = { name = "..." }` → division_templates. `regiments = { }` → regiments (type, x, y). `support = { }` → support (type, x, y). `units = { division = { } }` → divisions (template name, location, experience). Country derived from filename. | None |
| `history/units/*_naval_*.txt` | fleets, task_forces, ships, equipment_variants | `fleet = { name = "..." }` → fleets. `task_force = { }` → task_forces. `ship = { }` → ships (name, definition, equipment hull, version, owner). `create_equipment_variant = { }` → equipment_variants. | DLC-specific OOB files (mtg vs legacy) |
| `history/units/*_air_*.txt` | air_wings | `air_wings = { state_id = { wing = { equipment, amount, version_name } } }` → air_wings. Each equipment entry = one row. Country derived from filename. | DLC-specific OOB files (bba vs legacy) |
| `common/terrain/00_terrain.txt` | terrain_types, terrain_combat_modifiers, terrain_building_limits | Top-level blocks → terrain_types (movement_cost, attrition, is_water, etc.). `units = { }` sub-blocks → terrain_combat_modifiers per unit class. `buildings = { }` sub-block → terrain_building_limits. | None |
| `common/state_category/*.txt` | state_categories | One block per category; extract key, local_building_slots, color | None |
| `map/adjacencies.csv` | province_adjacencies | CSV parse; from_province_id, to_province_id, type, through_province_id, start/stop coords, rule, comment | None |
| `map/railways.txt` | province_railways | Level + province chain per line. Consecutive province pairs → one row each with railway_level. | None |
| `common/autonomous_states/*.txt` | autonomy_states, autonomy_state_modifiers | One block per autonomy level; extract key, is_puppet, min_freedom_level, manpower_influence. `modifier = { }` → autonomy_state_modifiers rows. | dlc_source from DLC gates |
| `common/occupation_laws/*.txt` | occupation_laws, occupation_law_modifiers | One block per law; extract key, icon, sound, gui_order, fallback_law. `state_modifier = { }` → occupation_law_modifiers (is_suppressed=false). `suppressed_state_modifier = { }` → occupation_law_modifiers (is_suppressed=true). | None |
| `common/countries/*.txt` | country_visual_definitions | Parse graphical_culture and graphical_culture_2d per country file | None |
| `common/intelligence_agencies/*.txt` | intelligence_agencies, intelligence_agency_names | `intelligence_agency = { }` blocks → intelligence_agencies (picture, default/available tags). `names = { }` list → intelligence_agency_names. | dlc_source from DLC gates |
| `common/bookmarks/*.txt` | bookmarks, bookmark_countries | `bookmark = { }` wrapper with `bookmark_date`, `name`. Nested country blocks → bookmark_countries (tag, ideology). | None |
| `common/decisions/**/*.txt` | decision_categories, decisions | Top-level block key → decision_categories. Nested `decisions = { }` → decisions (key, icon, cost, fire_only_once). | dlc_source from DLC gates |
| `common/operation_tokens/*.txt` | operation_tokens | One block per token; extract key, name, desc, icon, text_icon, intel_source, intel_gain | La Résistance |
| `common/operation_phases/*.txt` | operation_phase_definitions, operation_phase_equipment | One block per phase; extract key, name, desc, outcome, icon, return_on_complete. `equipment = { }` → operation_phase_equipment. | La Résistance |
| `common/operations/*.txt` | operations, operation_awarded_tokens, operation_equipment_requirements, operation_phase_groups, operation_phase_options | One block per operation; extract key, days, network_strength, operatives, risk_chance. `awarded_tokens = { }` → operation_awarded_tokens. `equipment = { }` → operation_equipment_requirements. `phases = { }` numbered groups with weighted phase alternatives → operation_phase_groups + operation_phase_options. | La Résistance |
| `common/intelligence_agency_upgrades/*.txt` | intel_agency_upgrade_branches, intel_agency_upgrades, intel_agency_upgrade_levels, intel_agency_upgrade_progress_modifiers | Branch wrappers → intel_agency_upgrade_branches. Upgrade blocks → intel_agency_upgrades (branch, picture). `level = { modifier = { } }` → intel_agency_upgrade_levels. `upgrade_progress_modifiers = { }` → intel_agency_upgrade_progress_modifiers. | La Résistance |
| `common/resistance_compliance_modifiers/*.txt` | compliance_modifiers, compliance_modifier_effects, resistance_modifiers, resistance_modifier_effects | Compliance blocks (type=compliance) → compliance_modifiers + effects. Resistance blocks (type=resistance) → resistance_modifiers + effects. Extract threshold, margin, icon, state_modifier key-values. | La Résistance |
| `common/resistance_activity/*.txt` | resistance_activities | One block per activity; extract key, alert_text, max_amount, duration | La Résistance |
| `common/military_industrial_organization/organizations/*.txt` | mio_templates, mio_organizations, mio_organization_equipment_types, mio_initial_traits, mio_traits, mio_trait_bonuses, mio_trait_prerequisites, mio_trait_exclusions | Template blocks (no `include`) → mio_templates. Org blocks (with country-specific `allowed`) → mio_organizations. `equipment = { }` → mio_organization_equipment_types. `initial_trait = { }` → mio_initial_traits. `add_trait = { }` / `trait = { }` → mio_traits with bonuses, prerequisites, exclusions child rows. | Arms Against Tyranny |
| `common/military_industrial_organization/policies/*.txt` | mio_policies, mio_policy_bonuses | One block per policy; extract key, icon. `equipment_bonus = { }` / `production_bonus = { }` → mio_policy_bonuses. | Arms Against Tyranny |
| `common/equipment_groups/*.txt` | mio_equipment_groups, mio_equipment_group_members | One block per group; key → mio_equipment_groups. Listed equipment types → mio_equipment_group_members. | Arms Against Tyranny |
| `common/raids/**/*.txt` | raid_categories, raids, raid_equipment_requirements | Category blocks → raid_categories (intel_source, faction_influence). Raid blocks → raids (days_to_prepare, command_power). `equipment = { }` groups → raid_equipment_requirements (group + min/max). | Götterdämmerung |
| `common/medals/*.txt` | medals, medal_tiers | One block per medal; extract key, name, frames, tracked_variable. `tier = { }` sub-blocks → medal_tiers (threshold, compare). | By Blood Alone |
| `common/ribbons/*.txt` | ribbons | One block per ribbon; extract key, name, description, quote_text, happened_trigger | By Blood Alone |
| `common/aces/*.txt` | ace_modifiers, ace_modifier_effects, ace_modifier_equipment_types | One block per modifier; extract key, chance. `modifier = { }` → ace_modifier_effects. `type = { }` → ace_modifier_equipment_types. | By Blood Alone |
| `common/unit_medals/*.txt` | unit_medals, unit_medal_modifiers | One block per medal; extract key, frame, icon, cost. `modifier = { }` → unit_medal_modifiers. Uses `@variable` substitution. | Götterdämmerung |
| `common/bop/*.txt` | balance_of_power_definitions, bop_sides, bop_ranges, bop_range_modifiers | One file per country; extract bop_key, initial_value, left/right_side, decision_category. Side blocks → bop_sides. `range = { }` within sides → bop_ranges (min/max). `modifier = { }` within ranges → bop_range_modifiers. | Various (BBA, AAT, ToA) |
| `common/continuous_focus/*.txt` | continuous_focus_palettes, continuous_focuses, continuous_focus_modifiers | Palette blocks → continuous_focus_palettes (is_default, reset_on_civilwar). Focus blocks within → continuous_focuses (icon, daily_cost). `modifier = { }` → continuous_focus_modifiers. | Various |
| `common/technology_sharing/*.txt` | technology_sharing_groups | `technology_sharing_group = { }` blocks; extract id, name, desc, picture, research_sharing_per_country_bonus | Together for Victory + others |
| `common/dynamic_modifiers/*.txt` | dynamic_modifiers, dynamic_modifier_effects | One block per modifier; extract key, icon, attacker_modifier. Modifier key-value pairs → dynamic_modifier_effects (static numeric or variable reference). | Various |
| `common/scientist_traits/*.txt` | scientist_traits, scientist_trait_modifiers | One block per trait; extract key, icon. `modifier = { }` → scientist_trait_modifiers. | Götterdämmerung |
| `common/peace_conference/**/*.txt` | peace_action_categories, peace_cost_modifiers | Category blocks → peace_action_categories (name, is_default). `cost_modifier = { }` sub-blocks → peace_cost_modifiers (category, peace_action_type, cost_multiplier). | By Blood Alone |
| `common/factions/rules/groups/*.txt` | faction_rule_groups | Parse `rule_group_xxx = { rules = { ... } }` blocks. Key from block name; child list → faction_rule_group_members. | Ride of the Valkyries |
| `common/factions/rules/*.txt` | faction_rules, faction_rule_group_members | Parse `rule_key = { type = ... }` blocks. Extract rule_key, type. Back-link to rule_group via rule_groups file. | Ride of the Valkyries |
| `common/factions/goals/faction_manifests.txt` | faction_manifests | Parse top-level blocks. Extract name, description, is_manifest, total_amount from ratio_progress. | Ride of the Valkyries |
| `common/factions/goals/faction_goals_*.txt` | faction_goals | Parse top-level blocks. Extract name, description, category (from filename: short/medium/long_term), group. | Ride of the Valkyries |
| `common/factions/templates/*.txt` | faction_templates, faction_template_goals, faction_template_rules | Parse `faction_template_xxx = { }` blocks. Extract name, manifest, icon, can_leader_join_other_factions. `goals = { ... }` → junction. `default_rules = { ... }` → junction. | Ride of the Valkyries |
| `common/factions/member_upgrades/*.txt` | faction_member_upgrades | Parse `upgrade_key = { bonus = N }` blocks. | Ride of the Valkyries |
| `common/factions/member_upgrades/member_groups/*.txt` | faction_member_upgrade_groups | Parse group blocks with name, default_upgrade, upgrade_type, icon. | Ride of the Valkyries |
| `common/special_projects/specialization/*.txt` | special_project_specializations | Parse `specialization_xxx = { }` blocks. | Götterdämmerung |
| `common/special_projects/project_tags/tags.txt` | special_project_tags | Parse `project_tags = { tag_key... }` list. | Götterdämmerung |
| `common/special_projects/projects/*.txt` | special_projects, special_project_reward_links | Parse `sp_xxx = { specialization, project_tags, complexity, prototype_time }`. `generic_prototype_rewards = { ... }` → junction. | Götterdämmerung |
| `common/special_projects/prototype_rewards/*.txt` | special_project_rewards | Parse reward blocks. Extract fire_only_once, threshold min/max. | Götterdämmerung |
| `common/collections/*.txt` | collections | Parse `collection_key = { input = ..., name = ... }` blocks. | Ride of the Valkyries |
| `common/ai_faction_theaters/*.txt` | ai_faction_theaters, ai_faction_theater_regions | Parse `theater_key = { name = ..., regions = { id... } }` blocks. Region list → junction. | Ride of the Valkyries |
| `common/timed_activities/*.txt` | timed_activities, timed_activity_equipment | Parse `activity_key = { equipment_need = { equip = N } }` blocks. | Base game |
| `localisation/english/*_l_english.yml` | localisation | YAML-like format: `key:0 "value"` per line under `l_english:` header. Regex extract `^\s+(\S+?):\d*\s+"(.+)"\s*$`. Deduplicate (later file wins). 189 files → 117,490 rows. | None (base game + all DLC) |

---

## Coverage Checklist

- [x] `common/countries/*.txt`
- [x] `common/country_tags/*.txt`
- [x] `history/countries/*.txt`
- [x] `history/states/*.txt`
- [x] `map/definition.csv`
- [x] `map/buildings.txt`
- [x] `map/continent.txt`
- [x] `common/technologies/*.txt`
- [x] `common/ideologies/*.txt`
- [x] `common/characters/*.txt`
- [x] `common/ideas/*.txt`
- [x] `common/national_focus/*.txt`
- [x] `common/units/*.txt`
- [x] `common/units/equipment/*.txt`
- [x] `common/resources/00_resources.txt`
- [x] `common/buildings/00_buildings.txt`
- [x] `history/units/*.txt` (land OOB)
- [x] `history/units/*_naval_*.txt`
- [x] `history/units/*_air_*.txt`
- [x] `map/strategicregions/*.txt`
- [x] `map/supply_nodes.txt`
- [x] `common/terrain/00_terrain.txt`
- [x] `common/state_category/*.txt`
- [x] `map/adjacencies.csv`
- [x] `map/railways.txt`
- [x] `common/autonomous_states/*.txt`
- [x] `common/occupation_laws/*.txt`
- [x] `common/intelligence_agencies/*.txt`
- [x] `common/bookmarks/*.txt`
- [x] `common/decisions/**/*.txt`
- [x] `common/operation_tokens/*.txt`
- [x] `common/operation_phases/*.txt`
- [x] `common/operations/*.txt`
- [x] `common/intelligence_agency_upgrades/*.txt`
- [x] `common/resistance_compliance_modifiers/*.txt`
- [x] `common/resistance_activity/*.txt`
- [x] `common/military_industrial_organization/organizations/*.txt`
- [x] `common/military_industrial_organization/policies/*.txt`
- [x] `common/equipment_groups/*.txt`
- [x] `common/raids/**/*.txt`
- [x] `common/medals/*.txt`
- [x] `common/ribbons/*.txt`
- [x] `common/aces/*.txt`
- [x] `common/unit_medals/*.txt`
- [x] `common/bop/*.txt`
- [x] `common/continuous_focus/*.txt`
- [x] `common/technology_sharing/*.txt`
- [x] `common/dynamic_modifiers/*.txt`
- [x] `common/scientist_traits/*.txt`
- [x] `common/peace_conference/**/*.txt`
- [x] `common/factions/rules/**/*.txt`
- [x] `common/factions/goals/*.txt`
- [x] `common/factions/templates/*.txt`
- [x] `common/factions/member_upgrades/**/*.txt`
- [x] `common/special_projects/specialization/*.txt`
- [x] `common/special_projects/project_tags/*.txt`
- [x] `common/special_projects/projects/*.txt`
- [x] `common/special_projects/prototype_rewards/*.txt`
- [x] `common/collections/*.txt`
- [x] `common/ai_faction_theaters/*.txt`
- [x] `common/timed_activities/*.txt`
- [x] `localisation/english/*_l_english.yml`

---

## Unmapped Source Files (Out of Scope)

These source paths exist but are **not modeled** in the starting-state database (they contain runtime or dynamic data):

| Path | Reason for exclusion |
|---|---|
| `common/on_actions/*.txt` | Event triggers, not data |
| `events/*.txt` | Event scripts, not starting state |
| `common/ai_strategy/*.txt` | AI behavior, not game data |
| `common/names/*.txt` | Name generation lists, not starting state |
