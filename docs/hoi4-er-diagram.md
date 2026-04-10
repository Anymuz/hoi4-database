```mermaid
erDiagram
    %% ============================================================
    %% HOI4 Complete ER Diagram - 127 tables (66 base + 61 DLC)
    %% Phases 1-15: 66 core tables (geography, countries, techs,
    %%   characters, OOB, ideas, focuses, bookmarks, decisions)
    %% Phases 16-23: 61 DLC tables (espionage, occupation/resistance,
    %%   MIO, raids, career profile, BOP, continuous focuses, misc, doctrines)
    %% ============================================================

    %% === Phase 1: Global Reference Tables ===

    continents {
        int continent_id PK
        varchar continent_key UK
    }

    terrain_types {
        varchar terrain_type PK
        smallint color_r
        smallint color_g
        smallint color_b
        numeric movement_cost
        int combat_width
        int combat_support_width
        numeric attrition
        boolean is_water
        boolean naval_terrain
        varchar sound_type
        numeric ai_terrain_importance_factor
        numeric match_value
        numeric sickness_chance
        numeric naval_mine_hit_chance
        int minimum_seazone_dominance
        numeric enemy_army_bonus_air_superiority_factor
        numeric supply_flow_penalty_factor
        numeric truck_attrition_factor
    }

    terrain_building_limits {
        varchar terrain_type FK
        varchar building_key FK
        int max_level
    }

    terrain_combat_modifiers {
        bigint id PK
        varchar terrain_type FK
        varchar unit_class
        varchar modifier_key
        numeric modifier_value
    }

    state_categories {
        varchar state_category PK
        int local_building_slots
        smallint color_r
        smallint color_g
        smallint color_b
    }

    resource_types {
        varchar resource_key PK
        int icon_frame
        numeric cic
        numeric convoys
    }

    building_types {
        varchar building_key PK
        int base_cost
        int state_max
        int province_max
        boolean shares_slots
        varchar dlc_source
    }

    ideologies {
        varchar ideology_key PK
        smallint color_r
        smallint color_g
        smallint color_b
    }

    sub_ideologies {
        varchar sub_ideology_key PK
        varchar ideology_key FK
    }

    technology_categories {
        varchar category_key PK
    }

    technologies {
        varchar technology_key PK
        numeric research_cost
        smallint start_year
        varchar folder_name
        varchar dlc_source
    }

    unit_types {
        varchar unit_type_key PK
        varchar abbreviation
        varchar unit_group
        numeric combat_width
        int manpower
        varchar dlc_source
    }

    equipment_definitions {
        varchar equipment_key PK
        boolean is_archetype
        varchar archetype_key FK
        varchar parent_key FK
        smallint year
        numeric build_cost_ic
        varchar dlc_source
    }

    equipment_resources {
        varchar equipment_key FK
        varchar resource_key FK
        int amount
    }

    autonomy_states {
        varchar autonomy_key PK
        boolean is_puppet
        boolean is_default
        numeric min_freedom_level
        numeric manpower_influence
        varchar dlc_source
    }

    autonomy_state_modifiers {
        bigint id PK
        varchar autonomy_key FK
        varchar modifier_key
        numeric modifier_value
    }

    occupation_laws {
        varchar occupation_law_key PK
        int icon_index
        varchar sound_effect
        int gui_order
        boolean main_fallback_law
        varchar fallback_law_key FK
    }

    occupation_law_modifiers {
        bigint id PK
        varchar occupation_law_key FK
        varchar modifier_key
        numeric modifier_value
        boolean is_suppressed
    }

    %% === Phase 2: Geography ===

    provinces {
        int province_id PK
        smallint map_r
        smallint map_g
        smallint map_b
        varchar province_kind
        boolean is_coastal
        varchar terrain FK
        int continent_id FK
    }

    province_building_positions {
        bigint position_id PK
        int province_id FK
        varchar building_type
        numeric pos_x
        numeric pos_y
        numeric pos_z
        numeric rotation
        int linked_province_id
    }

    province_adjacencies {
        bigint id PK
        int from_province_id FK
        int to_province_id FK
        varchar adjacency_type
        int through_province_id FK
        numeric start_x
        numeric start_y
        numeric stop_x
        numeric stop_y
        varchar adjacency_rule_name
        varchar comment
    }

    province_railways {
        bigint id PK
        int from_province_id FK
        int to_province_id FK
        smallint railway_level
    }

    strategic_regions {
        int strategic_region_id PK
        varchar name_key
    }

    strategic_region_provinces {
        int strategic_region_id FK
        int province_id FK
    }

    supply_nodes {
        int province_id PK
        int level
    }

    states {
        int state_id PK
        varchar state_name_key
        bigint manpower
        varchar state_category FK
    }

    state_provinces {
        int state_id FK
        int province_id FK
    }

    state_resources {
        bigint id PK
        int state_id FK
        varchar resource_key FK
        numeric amount
        varchar dlc_source
    }

    state_buildings {
        bigint id PK
        int state_id FK
        varchar building_key FK
        int level
        varchar dlc_source
    }

    province_buildings {
        bigint id PK
        int province_id FK
        int state_id FK
        varchar building_key FK
        int level
        varchar dlc_source
    }

    state_victory_points {
        bigint id PK
        int state_id FK
        int province_id FK
        int victory_points
        varchar dlc_source
    }

    %% === Phase 3: Countries ===

    countries {
        char3 tag PK
        text country_file_path
        int capital_state_id FK
        numeric stability
        numeric war_support
        smallint color_r
        smallint color_g
        smallint color_b
    }

    country_visual_definitions {
        char3 country_tag PK
        varchar graphical_culture
        varchar graphical_culture_2d
    }

    state_ownership_history {
        bigint id PK
        int state_id FK
        date effective_date
        char3 owner_tag FK
        char3 controller_tag FK
        varchar dlc_source
    }

    province_controller_history {
        bigint id PK
        int province_id FK
        int state_id FK
        char3 controller_tag FK
        varchar dlc_source
    }

    state_cores {
        bigint id PK
        int state_id FK
        char3 country_tag FK
        varchar dlc_source
    }

    country_starting_technologies {
        bigint id PK
        char3 country_tag FK
        varchar technology_key FK
        varchar dlc_source
    }

    country_starting_ideas {
        char3 country_tag FK
        varchar idea_key FK
        date effective_date
        varchar dlc_source
    }

    intelligence_agencies {
        int agency_id PK
        varchar picture_gfx
        char3 default_tag FK
        char3 available_tag
        text source_file
        varchar dlc_source
    }

    %% === Phase 4: Technologies (detailed) ===

    technology_categories_junction {
        varchar technology_key FK
        varchar category_key FK
    }

    technology_prerequisites {
        varchar technology_key FK
        varchar prerequisite_key FK
    }

    technology_enables_equipment {
        varchar technology_key FK
        varchar equipment_key FK
    }

    technology_enables_units {
        varchar technology_key FK
        varchar unit_type_key FK
    }

    %% === Phase 5: Characters ===

    characters {
        varchar character_id PK
        varchar name_key
        char3 country_tag FK
        varchar gender
    }

    character_roles {
        int character_role_id PK
        varchar character_id FK
        varchar role_type
        varchar sub_ideology_key FK
        smallint skill
        smallint attack_skill
        smallint defense_skill
        varchar dlc_source
    }

    character_traits {
        varchar trait_key PK
        varchar trait_type
    }

    character_role_traits {
        int character_role_id FK
        varchar trait_key FK
    }

    %% === Phase 6: Division Templates and OOB ===

    division_templates {
        int division_template_id PK
        char3 country_tag FK
        varchar template_name
        varchar division_names_group
        varchar oob_file
    }

    division_template_regiments {
        int division_template_id FK
        varchar unit_type_key FK
        smallint grid_x
        smallint grid_y
    }

    division_template_support {
        int division_template_id FK
        varchar unit_type_key FK
        smallint grid_x
        smallint grid_y
    }

    divisions {
        int division_id PK
        char3 country_tag FK
        int division_template_id FK
        varchar template_name
        int location_province_id FK
        numeric start_experience_factor
        varchar oob_file
    }

    %% === Phase 7: Naval OOB ===

    equipment_variants {
        int equipment_variant_id PK
        char3 owner_tag FK
        varchar base_equipment_key FK
        varchar version_name
    }

    fleets {
        int fleet_id PK
        char3 country_tag FK
        varchar fleet_name
        int naval_base_province_id FK
        varchar oob_file
    }

    task_forces {
        int task_force_id PK
        int fleet_id FK
        varchar task_force_name
        int location_province_id FK
    }

    ships {
        int ship_id PK
        int task_force_id FK
        varchar ship_name
        varchar definition
        varchar hull_equipment_key FK
        varchar version_name
        char3 owner_tag FK
        boolean pride_of_the_fleet
    }

    %% === Phase 8: Air OOB ===

    air_wings {
        int air_wing_id PK
        char3 country_tag FK
        int location_state_id FK
        varchar wing_name
        varchar equipment_type
        int amount
        varchar version_name
        varchar oob_file
    }

    %% === Phase 9: Ideas and National Spirits ===

    ideas {
        varchar idea_key PK
        varchar slot
        boolean is_law
        int cost
        int removal_cost
        boolean is_default
        varchar dlc_source
    }

    idea_modifiers {
        bigint id PK
        varchar idea_key FK
        varchar modifier_key
        numeric modifier_value
    }

    %% === Phase 10: National Focus Trees ===

    focus_trees {
        varchar focus_tree_id PK
        char3 country_tag FK
        int initial_x
        int initial_y
    }

    focuses {
        varchar focus_id PK
        varchar focus_tree_id FK
        numeric cost
        int x_pos
        int y_pos
        varchar icon
        varchar dlc_source
    }

    focus_prerequisites {
        varchar focus_id FK
        smallint prerequisite_group
        varchar required_focus_id FK
    }

    focus_mutually_exclusive {
        varchar focus_a_id FK
        varchar focus_b_id FK
    }

    %% === Phase 11: Bookmarks ===

    bookmarks {
        int bookmark_id PK
        varchar bookmark_name
        date bookmark_date
        varchar picture_gfx
        char3 default_country_tag FK
    }

    bookmark_countries {
        int bookmark_id FK
        char3 country_tag FK
        varchar ideology_key FK
    }

    %% === Phase 12: Decisions ===

    decision_categories {
        varchar category_key PK
        varchar icon
        varchar picture_gfx
        int priority
    }

    decisions {
        varchar decision_key PK
        varchar category_key FK
        varchar icon
        int cost
        boolean fire_only_once
        varchar dlc_source
    }

    %% ============================================================
    %% Relationships
    %% ============================================================

    %% Phase 1 - reference table relationships
    ideologies ||--o{ sub_ideologies : has
    equipment_definitions ||--o{ equipment_definitions : "archetype/parent"
    equipment_definitions ||--o{ equipment_resources : consumes
    resource_types ||--o{ equipment_resources : "used_by"
    terrain_types ||--o{ terrain_building_limits : "limits"
    building_types ||--o{ terrain_building_limits : "limited_in"
    terrain_types ||--o{ terrain_combat_modifiers : "modifies"
    autonomy_states ||--o{ autonomy_state_modifiers : "modified_by"
    occupation_laws ||--o{ occupation_law_modifiers : "modified_by"
    occupation_laws ||--o| occupation_laws : "fallback"

    %% Phase 2 - geography relationships
    terrain_types ||--o{ provinces : "terrain_of"
    continents ||--o{ provinces : "contains"
    provinces ||--o{ province_building_positions : has
    provinces ||--o{ province_adjacencies : "from"
    provinces ||--o{ province_adjacencies : "to"
    provinces ||--o{ province_railways : "from"
    provinces ||--o{ province_railways : "to"
    strategic_regions ||--o{ strategic_region_provinces : contains
    provinces ||--o{ strategic_region_provinces : belongs_to
    provinces ||--o{ supply_nodes : is_hub
    state_categories ||--o{ states : "categorized"
    states ||--|{ state_provinces : contains
    provinces ||--o{ state_provinces : belongs_to
    states ||--o{ state_resources : has
    resource_types ||--o{ state_resources : typed
    states ||--o{ state_buildings : has
    building_types ||--o{ state_buildings : typed
    states ||--o{ province_buildings : contains
    provinces ||--o{ province_buildings : has
    building_types ||--o{ province_buildings : typed
    states ||--o{ state_victory_points : has
    provinces ||--o{ state_victory_points : at

    %% Phase 3 - country relationships
    states ||--o| countries : "capital_of"
    countries ||--|| country_visual_definitions : "visuals"
    countries ||--o{ state_ownership_history : owns
    states ||--o{ state_ownership_history : history
    countries ||--o{ state_cores : has_core
    states ||--o{ state_cores : history
    provinces ||--o{ province_controller_history : has
    states ||--o{ province_controller_history : history
    countries ||--o{ province_controller_history : controls
    countries ||--o{ country_starting_technologies : researched
    technologies ||--o{ country_starting_technologies : unlocked_by
    countries ||--o{ country_starting_ideas : starts_with
    ideas ||--o{ country_starting_ideas : activated
    countries ||--o{ intelligence_agencies : "has_agency"
    countries ||--o{ intelligence_agencies : "available_for"

    %% Phase 4 - technology relationships
    technologies ||--o{ technology_categories_junction : categorized
    technology_categories ||--o{ technology_categories_junction : groups
    technologies ||--o{ technology_prerequisites : "leads_to"
    technologies ||--o{ technology_prerequisites : "required_by"
    technologies ||--o{ technology_enables_equipment : unlocks
    equipment_definitions ||--o{ technology_enables_equipment : unlocked_by
    technologies ||--o{ technology_enables_units : unlocks
    unit_types ||--o{ technology_enables_units : unlocked_by

    %% Phase 5 - character relationships
    countries ||--o{ characters : has
    characters ||--o{ character_roles : holds
    sub_ideologies ||--o{ character_roles : "ideology_of"
    character_roles ||--o{ character_role_traits : assigned
    character_traits ||--o{ character_role_traits : applied

    %% Phase 6 - land OOB relationships
    countries ||--o{ division_templates : defines
    division_templates ||--o{ division_template_regiments : has_regiment
    unit_types ||--o{ division_template_regiments : typed
    division_templates ||--o{ division_template_support : has_support
    unit_types ||--o{ division_template_support : typed
    countries ||--o{ divisions : deploys
    division_templates ||--o{ divisions : instantiated
    provinces ||--o{ divisions : stationed

    %% Phase 7 - naval OOB relationships
    countries ||--o{ equipment_variants : designs
    equipment_definitions ||--o{ equipment_variants : based_on
    countries ||--o{ fleets : commands
    provinces ||--o{ fleets : home_port
    fleets ||--o{ task_forces : contains
    provinces ||--o{ task_forces : located
    task_forces ||--o{ ships : carries
    equipment_definitions ||--o{ ships : hull
    countries ||--o{ ships : owned_by

    %% Phase 8 - air OOB relationships
    countries ||--o{ air_wings : operates
    states ||--o{ air_wings : based_at

    %% Phase 9 - ideas relationships
    ideas ||--o{ idea_modifiers : modified_by

    %% Phase 10 - focus tree relationships
    countries ||--o{ focus_trees : has_tree
    focus_trees ||--o{ focuses : contains
    focuses ||--o{ focus_prerequisites : requires
    focuses ||--o{ focus_prerequisites : "required_by"
    focuses ||--o{ focus_mutually_exclusive : excludes

    %% Phase 11 - bookmark relationships
    countries ||--o{ bookmark_countries : "featured_in"
    bookmarks ||--o{ bookmark_countries : "includes"
    countries ||--o| bookmarks : "default_for"
    ideologies ||--o{ bookmark_countries : "starts_as"

    %% Phase 12 - decision relationships
    decision_categories ||--o{ decisions : "contains"

    %% === Phase 16: Espionage System (La Résistance) ===

    operations {
        varchar operation_key PK
        varchar name
        text desc
        varchar icon
        varchar map_icon
        int priority
        int days
        int network_strength
        int operatives
        numeric risk_chance
        int experience
        numeric cost_multiplier
        numeric outcome_extra_chance
        boolean prevent_captured_operative_to_die
        boolean scale_cost_independent_of_target
        text source_file
        varchar dlc_source
    }

    operation_awarded_tokens {
        varchar operation_key FK
        varchar token_key FK
    }

    operation_equipment_requirements {
        int id PK
        varchar operation_key FK
        varchar equipment_key
        int amount
    }

    operation_phase_groups {
        varchar operation_key FK
        smallint sequence_index
    }

    operation_phase_options {
        int id PK
        varchar operation_key FK
        smallint sequence_index FK
        varchar phase_key FK
        int base_weight
    }

    operation_phase_definitions {
        varchar phase_key PK
        varchar name
        text desc
        text outcome
        varchar icon
        varchar picture
        boolean return_on_complete
        text source_file
    }

    operation_phase_equipment {
        int id PK
        varchar phase_key FK
        varchar equipment_key
        int amount
    }

    operation_tokens {
        varchar token_key PK
        varchar name
        text desc
        varchar icon
        varchar text_icon
        varchar intel_source
        int intel_gain
    }

    intelligence_agency_names {
        int id PK
        int agency_id FK
        varchar agency_name
    }

    intel_agency_upgrade_branches {
        varchar branch_key PK
    }

    intel_agency_upgrades {
        varchar upgrade_key PK
        varchar branch_key FK
        varchar picture
        int frame
        varchar sound
    }

    intel_agency_upgrade_levels {
        int id PK
        varchar upgrade_key FK
        smallint level_index
        varchar modifier_key
        numeric modifier_value
    }

    intel_agency_upgrade_progress_modifiers {
        int id PK
        varchar upgrade_key FK
        varchar modifier_key
        numeric modifier_value
    }

    %% === Phase 17: Occupation & Resistance ===

    compliance_modifiers {
        varchar modifier_key PK
        varchar type
        varchar icon
        varchar small_icon
        int threshold
        int margin
        varchar dlc_source
    }

    compliance_modifier_effects {
        int id PK
        varchar modifier_key FK
        varchar effect_key
        numeric effect_value
    }

    resistance_modifiers {
        varchar modifier_key PK
        varchar type
        varchar icon
        varchar small_icon
        int threshold
        int margin
    }

    resistance_modifier_effects {
        int id PK
        varchar modifier_key FK
        varchar effect_key
        numeric effect_value
    }

    resistance_activities {
        varchar activity_key PK
        varchar alert_text
        int base_weight
        varchar dlc_source
    }

    %% === Phase 18: MIO System (Arms Against Tyranny) ===

    mio_equipment_groups {
        varchar group_key PK
    }

    mio_equipment_group_members {
        int id PK
        varchar group_key FK
        varchar equipment_type
    }

    mio_templates {
        varchar template_key PK
        varchar icon
        varchar dlc_source
    }

    mio_organizations {
        varchar mio_key PK
        varchar template_key FK
        char3 country_tag FK
        varchar icon
        varchar dlc_source
    }

    mio_organization_equipment_types {
        int id PK
        varchar owner_key
        varchar owner_type
        varchar equipment_type
    }

    mio_initial_traits {
        int id PK
        varchar owner_key
        varchar owner_type
        varchar equipment_bonus_key
        numeric equipment_bonus_value
        varchar production_bonus_key
        numeric production_bonus_value
        varchar organization_modifier_key
        numeric organization_modifier_value
    }

    mio_traits {
        varchar trait_token PK
        varchar owner_key
        varchar owner_type
        varchar name
        varchar icon
        smallint position_x
        smallint position_y
        varchar limit_to_equipment_type
        boolean any_parent
        boolean all_parents
    }

    mio_trait_bonuses {
        int id PK
        varchar trait_token FK
        varchar bonus_type
        varchar modifier_key
        numeric modifier_value
    }

    mio_trait_prerequisites {
        int id PK
        varchar trait_token FK
        varchar parent_trait_token FK
    }

    mio_trait_exclusions {
        int id PK
        varchar trait_token_a FK
        varchar trait_token_b FK
    }

    mio_policies {
        varchar policy_key PK
        varchar icon
        varchar dlc_source
    }

    mio_policy_bonuses {
        int id PK
        varchar policy_key FK
        varchar bonus_type
        varchar target_scope
        varchar modifier_key
        numeric modifier_value
    }

    %% === Phase 19: Raids (Götterdämmerung) ===

    raid_categories {
        varchar category_key PK
        varchar intel_source
        numeric faction_influence_score_on_success
        boolean free_targeting
        varchar dlc_source
    }

    raids {
        varchar raid_key PK
        varchar category_key FK
        int days_to_prepare
        int command_power
        varchar target_type
        varchar dlc_source
        text source_file
    }

    raid_equipment_requirements {
        int id PK
        varchar raid_key FK
        varchar equipment_key
        int amount
        boolean is_essential
    }

    %% === Phase 20: Career Profile ===

    medals {
        varchar medal_key PK
        varchar name
        varchar description
        int frame_1
        int frame_2
        int frame_3
        varchar dlc_source
    }

    medal_tiers {
        int id PK
        varchar medal_key FK
        varchar tier
        varchar tracked_variable
        int threshold_value
        varchar comparison
    }

    ribbons {
        varchar ribbon_key PK
        varchar name
        varchar description
        varchar quote_text
        varchar dlc_source
    }

    ace_modifiers {
        varchar modifier_key PK
        numeric chance
    }

    ace_modifier_effects {
        int id PK
        varchar modifier_key FK
        varchar effect_key
        numeric effect_value
    }

    ace_modifier_equipment_types {
        int id PK
        varchar modifier_key FK
        varchar equipment_type
    }

    unit_medals {
        varchar medal_key PK
        int frame
        varchar icon
        int cost
        varchar dlc_source
    }

    unit_medal_modifiers {
        int id PK
        varchar medal_key FK
        varchar modifier_key
        numeric modifier_value
    }

    %% === Phase 21: Balance of Power & Continuous Focuses ===

    balance_of_power_definitions {
        varchar bop_key PK
        char3 country_tag FK
        numeric initial_value
        varchar left_side_id
        varchar right_side_id
        varchar decision_category
    }

    bop_sides {
        int id PK
        varchar bop_key FK
        varchar side_id
        varchar icon
    }

    bop_ranges {
        int id PK
        varchar bop_key FK
        varchar side_id
        varchar range_id
        numeric min_value
        numeric max_value
    }

    bop_range_modifiers {
        int id PK
        int range_id FK
        varchar modifier_key
        numeric modifier_value
    }

    continuous_focus_palettes {
        varchar palette_id PK
        boolean is_default
        boolean reset_on_civilwar
    }

    continuous_focuses {
        varchar focus_id PK
        varchar palette_id FK
        varchar icon
        int daily_cost
        boolean available_if_capitulated
        varchar dlc_source
    }

    continuous_focus_modifiers {
        int id PK
        varchar focus_id FK
        varchar modifier_key
        numeric modifier_value
    }

    %% === Phase 22: Misc DLC Systems ===

    technology_sharing_groups {
        varchar group_id PK
        varchar name
        text desc
        varchar picture
        numeric research_sharing_per_country_bonus
        varchar dlc_source
    }

    dynamic_modifiers {
        varchar modifier_key PK
        varchar icon
        boolean attacker_modifier
        varchar dlc_source
    }

    dynamic_modifier_effects {
        int id PK
        varchar modifier_key FK
        varchar effect_key
        numeric effect_value
    }

    scientist_traits {
        varchar trait_key PK
        varchar icon
    }

    scientist_trait_modifiers {
        int id PK
        varchar trait_key FK
        varchar modifier_key
        numeric modifier_value
    }

    peace_action_categories {
        varchar category_key PK
        boolean is_default
    }

    peace_cost_modifiers {
        varchar modifier_key PK
        varchar category_key FK
        varchar peace_action_type
        numeric cost_multiplier
        varchar dlc_source
    }

    %% ============================================================
    %% Phase 16–22 Relationships
    %% ============================================================

    %% Phase 16 - espionage relationships
    operations ||--o{ operation_awarded_tokens : "awards"
    operation_tokens ||--o{ operation_awarded_tokens : "awarded_by"
    operations ||--o{ operation_equipment_requirements : "requires"
    operations ||--o{ operation_phase_groups : "has_phase_group"
    operations ||--o{ operation_phase_options : "has_phase_option"
    operation_phase_definitions ||--o{ operation_phase_options : "option_for"
    operation_phase_definitions ||--o{ operation_phase_equipment : "requires"
    intelligence_agencies ||--o{ intelligence_agency_names : "named"
    intel_agency_upgrade_branches ||--o{ intel_agency_upgrades : "contains"
    intel_agency_upgrades ||--o{ intel_agency_upgrade_levels : "has_level"
    intel_agency_upgrades ||--o{ intel_agency_upgrade_progress_modifiers : "modified_by"

    %% Phase 17 - occupation & resistance relationships
    compliance_modifiers ||--o{ compliance_modifier_effects : "applies"
    resistance_modifiers ||--o{ resistance_modifier_effects : "applies"

    %% Phase 18 - MIO relationships
    mio_equipment_groups ||--o{ mio_equipment_group_members : "contains"
    mio_templates ||--o{ mio_organizations : "instantiates"
    countries ||--o{ mio_organizations : "owns"
    mio_traits ||--o{ mio_trait_bonuses : "grants"
    mio_traits ||--o{ mio_trait_prerequisites : "requires"
    mio_traits ||--o{ mio_trait_prerequisites : "required_by"
    mio_traits ||--o{ mio_trait_exclusions : "excludes_a"
    mio_traits ||--o{ mio_trait_exclusions : "excludes_b"
    mio_policies ||--o{ mio_policy_bonuses : "grants"

    %% Phase 19 - raid relationships
    raid_categories ||--o{ raids : "contains"
    raids ||--o{ raid_equipment_requirements : "requires"

    %% Phase 20 - career profile relationships
    medals ||--o{ medal_tiers : "has_tier"
    ace_modifiers ||--o{ ace_modifier_effects : "applies"
    ace_modifiers ||--o{ ace_modifier_equipment_types : "applies_to"
    unit_medals ||--o{ unit_medal_modifiers : "modified_by"

    %% Phase 21 - BOP & continuous focus relationships
    countries ||--o{ balance_of_power_definitions : "has_bop"
    balance_of_power_definitions ||--o{ bop_sides : "has_side"
    balance_of_power_definitions ||--o{ bop_ranges : "has_range"
    bop_ranges ||--o{ bop_range_modifiers : "modified_by"
    continuous_focus_palettes ||--o{ continuous_focuses : "contains"
    continuous_focuses ||--o{ continuous_focus_modifiers : "modified_by"

    %% Phase 22 - misc DLC relationships
    dynamic_modifiers ||--o{ dynamic_modifier_effects : "applies"
    scientist_traits ||--o{ scientist_trait_modifiers : "modified_by"
    peace_action_categories ||--o{ peace_cost_modifiers : "has_modifier"

    %% ============================================================
    %% Phase 23 - Doctrines (Officer Corps)
    %% ============================================================

    doctrine_folders {
        varchar folder_key PK
        varchar name_loc
        varchar ledger
        varchar xp_type
    }

    doctrine_tracks {
        varchar track_key PK
        varchar folder_key FK
        varchar name_loc
        numeric mastery_multiplier
    }

    grand_doctrines {
        varchar doctrine_key PK
        varchar folder_key FK
        varchar name_loc
        int xp_cost
        varchar xp_type
    }

    grand_doctrine_tracks {
        varchar doctrine_key FK
        varchar track_key FK
        smallint ordinal
    }

    subdoctrines {
        varchar subdoctrine_key PK
        varchar track_key FK
        varchar name_loc
        int xp_cost
        varchar xp_type
        smallint reward_count
    }

    country_starting_doctrines {
        serial id PK
        char country_tag FK
        date date
        varchar doctrine_type
        varchar doctrine_key
    }

    %% Phase 23 relationships
    doctrine_folders ||--o{ doctrine_tracks : "has_track"
    doctrine_folders ||--o{ grand_doctrines : "has_grand_doctrine"
    grand_doctrines ||--o{ grand_doctrine_tracks : "uses_track"
    doctrine_tracks ||--o{ grand_doctrine_tracks : "used_by"
    doctrine_tracks ||--o{ subdoctrines : "has_subdoctrine"
    countries ||--o{ country_starting_doctrines : "starts_with"
```