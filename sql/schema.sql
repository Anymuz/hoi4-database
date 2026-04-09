-- HOI4 PostgreSQL Schema — Complete (149 tables, 28 phases)
-- Source: docs/hoi4-table-catalog.md (authoritative column spec)
-- Build order: docs/hoi4-database-design.md (123-step FK dependency order)
--
-- Existing Slice A tables (15): countries, technologies, resource_types, building_types,
--   states, provinces, state_provinces, state_ownership_history, province_controller_history,
--   state_cores, state_victory_points, state_resources, state_buildings, province_buildings,
--   country_starting_technologies
-- New tables (106): Phases 1–22 remaining tables

BEGIN;

-- ============================================================
-- SLICE A — Original 15 Tables (preserved)
-- ============================================================

-- 1) Root reference tables
CREATE TABLE countries (
    tag                         CHAR(3) PRIMARY KEY,
    country_file_path           TEXT,
    history_file_path           TEXT,
    graphical_culture           VARCHAR(80),
    graphical_culture_2d        VARCHAR(80),
    color_r                     SMALLINT CHECK (color_r BETWEEN 0 AND 255),
    color_g                     SMALLINT CHECK (color_g BETWEEN 0 AND 255),
    color_b                     SMALLINT CHECK (color_b BETWEEN 0 AND 255),
    capital_state_id            INT,
    stability                   NUMERIC(5,4),
    war_support                 NUMERIC(5,4),
    source_tag_file             TEXT,
    source_country_file         TEXT,
    source_history_file         TEXT,
    created_at                  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON COLUMN countries.country_file_path IS 'From common/country_tags/*.txt value, e.g. countries/Germany.txt';
COMMENT ON COLUMN countries.capital_state_id IS 'From history/countries/*.txt: capital = <state_id>';
COMMENT ON COLUMN countries.stability IS 'From history/countries/*.txt: set_stability';
COMMENT ON COLUMN countries.war_support IS 'From history/countries/*.txt: set_war_support';

CREATE TABLE technologies (
    technology_key              VARCHAR(120) PRIMARY KEY,
    technology_file             TEXT,
    start_year                  SMALLINT,
    research_cost               NUMERIC(6,3),
    folder_name                 VARCHAR(80),
    source_file                 TEXT NOT NULL
);

COMMENT ON COLUMN technologies.technology_key IS 'Paradox key inside technologies = { ... } blocks';

CREATE TABLE resource_types (
    resource_key                VARCHAR(40) PRIMARY KEY,
    icon_frame                  INT,
    civilian_factory_cost_unit  NUMERIC(8,3),
    convoy_cost_unit            NUMERIC(8,3),
    source_file                 TEXT
);

COMMENT ON COLUMN resource_types.civilian_factory_cost_unit IS 'From common/resources/00_resources.txt: cic';
COMMENT ON COLUMN resource_types.convoy_cost_unit IS 'From common/resources/00_resources.txt: convoys';

CREATE TABLE building_types (
    building_key                VARCHAR(80) PRIMARY KEY,
    base_cost                   INT,
    per_level_extra_cost        INT,
    base_cost_conversion        INT,
    icon_frame                  INT,
    show_on_map                 INT,
    shares_slots                BOOLEAN,
    state_max                   INT,
    province_max                INT,
    is_state_level              BOOLEAN NOT NULL DEFAULT false,
    is_province_level           BOOLEAN NOT NULL DEFAULT false,
    only_coastal                BOOLEAN,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN building_types.only_coastal IS 'From 00_buildings.txt field only_costal (source typo retained there)';
COMMENT ON COLUMN building_types.dlc_source IS 'Set when a building has dlc_allowed / DLC gate';

-- 2) Geography
CREATE TABLE states (
    state_id                    INT PRIMARY KEY,
    state_name_key              VARCHAR(80) NOT NULL,
    manpower                    BIGINT,
    state_category              VARCHAR(60),
    local_supplies              NUMERIC(8,3),
    source_file                 TEXT NOT NULL
);

COMMENT ON COLUMN states.state_name_key IS 'From state block name, e.g. STATE_4';

CREATE TABLE provinces (
    province_id                 INT PRIMARY KEY,
    map_r                       SMALLINT CHECK (map_r BETWEEN 0 AND 255),
    map_g                       SMALLINT CHECK (map_g BETWEEN 0 AND 255),
    map_b                       SMALLINT CHECK (map_b BETWEEN 0 AND 255),
    province_kind               VARCHAR(20) NOT NULL,
    is_coastal                  BOOLEAN NOT NULL,
    terrain                     VARCHAR(40) NOT NULL,
    continent_id                INT NOT NULL,
    source_file                 TEXT
);

COMMENT ON COLUMN provinces.province_kind IS 'From map/definition.csv column 5 (land/sea/lake)';
COMMENT ON COLUMN provinces.continent_id IS 'From map/definition.csv final column';

CREATE TABLE state_provinces (
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    province_id                 INT NOT NULL REFERENCES provinces(province_id),
    source_file                 TEXT NOT NULL,
    PRIMARY KEY (state_id, province_id)
);

-- 3) State history atoms
CREATE TABLE state_ownership_history (
    state_ownership_history_id  BIGSERIAL PRIMARY KEY,
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    effective_date              DATE NOT NULL,
    owner_tag                   CHAR(3) NOT NULL REFERENCES countries(tag),
    controller_tag              CHAR(3) REFERENCES countries(tag),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN state_ownership_history.controller_tag IS 'From controller = TAG in dated history blocks when present';

CREATE UNIQUE INDEX uq_state_ownership_history
    ON state_ownership_history (state_id, effective_date);

CREATE TABLE province_controller_history (
    province_controller_history_id BIGSERIAL PRIMARY KEY,
    province_id                 INT REFERENCES provinces(province_id),
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    effective_date              DATE NOT NULL,
    controller_tag              CHAR(3) NOT NULL REFERENCES countries(tag),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

CREATE INDEX ix_province_controller_history_state_date
    ON province_controller_history (state_id, effective_date);

CREATE TABLE state_cores (
    state_core_id               BIGSERIAL PRIMARY KEY,
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    country_tag                 CHAR(3) NOT NULL REFERENCES countries(tag),
    effective_date              DATE NOT NULL,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50),
    UNIQUE (state_id, country_tag, effective_date)
);

CREATE TABLE state_victory_points (
    state_victory_point_id      BIGSERIAL PRIMARY KEY,
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    province_id                 INT NOT NULL REFERENCES provinces(province_id),
    effective_date              DATE NOT NULL DEFAULT '1936-01-01',
    victory_points              INT NOT NULL,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50),
    UNIQUE (state_id, province_id, effective_date)
);

CREATE TABLE state_resources (
    state_resource_id           BIGSERIAL PRIMARY KEY,
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    resource_key                VARCHAR(40) NOT NULL REFERENCES resource_types(resource_key),
    effective_date              DATE NOT NULL DEFAULT '1936-01-01',
    amount                      NUMERIC(12,3) NOT NULL,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50),
    UNIQUE (state_id, resource_key, effective_date)
);

CREATE TABLE state_buildings (
    state_building_id           BIGSERIAL PRIMARY KEY,
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    building_key                VARCHAR(80) NOT NULL REFERENCES building_types(building_key),
    effective_date              DATE NOT NULL DEFAULT '1936-01-01',
    level                       INT NOT NULL,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50),
    UNIQUE (state_id, building_key, effective_date)
);

CREATE TABLE province_buildings (
    province_building_id        BIGSERIAL PRIMARY KEY,
    province_id                 INT NOT NULL REFERENCES provinces(province_id),
    state_id                    INT NOT NULL REFERENCES states(state_id) ON DELETE CASCADE,
    building_key                VARCHAR(80) NOT NULL REFERENCES building_types(building_key),
    effective_date              DATE NOT NULL,
    level                       INT NOT NULL,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50),
    UNIQUE (province_id, building_key, effective_date)
);

-- 4) Country starting technologies linkage
CREATE TABLE country_starting_technologies (
    country_starting_technology_id BIGSERIAL PRIMARY KEY,
    country_tag                 CHAR(3) NOT NULL REFERENCES countries(tag),
    technology_key              VARCHAR(120) NOT NULL REFERENCES technologies(technology_key),
    effective_date              DATE NOT NULL DEFAULT '1936-01-01',
    source_file                 TEXT NOT NULL,
    source_condition            TEXT,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN country_starting_technologies.source_condition IS 'Original gate expression context (if/limit) from country history';
COMMENT ON COLUMN country_starting_technologies.dlc_source IS 'DLC guard name when set_technology was under has_dlc condition';

CREATE UNIQUE INDEX uq_country_starting_technologies
    ON country_starting_technologies (country_tag, technology_key, effective_date, COALESCE(dlc_source, ''));

-- 5) Deferred FK after states exists
ALTER TABLE countries
    ADD CONSTRAINT fk_countries_capital_state
    FOREIGN KEY (capital_state_id) REFERENCES states(state_id);

-- API and ETL focused indexes
CREATE INDEX ix_states_name ON states (state_name_key);
CREATE INDEX ix_state_ownership_history_owner ON state_ownership_history (owner_tag, effective_date);
CREATE INDEX ix_state_ownership_history_controller ON state_ownership_history (controller_tag, effective_date);
CREATE INDEX ix_state_resources_state_date ON state_resources (state_id, effective_date);
CREATE INDEX ix_state_buildings_state_date ON state_buildings (state_id, effective_date);
CREATE INDEX ix_province_buildings_state_date ON province_buildings (state_id, effective_date);
CREATE INDEX ix_country_starting_technologies_country_date ON country_starting_technologies (country_tag, effective_date);

-- ============================================================
-- PHASE 1 — New Global Reference Tables
-- ============================================================

-- FK build order #1
CREATE TABLE continents (
    continent_id                INT PRIMARY KEY,
    continent_key               VARCHAR(40) NOT NULL UNIQUE
);

-- FK build order #2
CREATE TABLE terrain_types (
    terrain_type                VARCHAR(40) PRIMARY KEY,
    color_r                     SMALLINT,
    color_g                     SMALLINT,
    color_b                     SMALLINT,
    movement_cost               NUMERIC(4,2),
    combat_width                INT,
    combat_support_width        INT,
    attrition                   NUMERIC(4,2),
    is_water                    BOOLEAN,
    naval_terrain               BOOLEAN,
    sound_type                  VARCHAR(40),
    ai_terrain_importance_factor NUMERIC(6,2),
    match_value                 NUMERIC(6,2),
    sickness_chance             NUMERIC(4,2),
    naval_mine_hit_chance       NUMERIC(6,2),
    minimum_seazone_dominance   INT,
    enemy_army_bonus_air_superiority_factor NUMERIC(4,2),
    supply_flow_penalty_factor  NUMERIC(5,3),
    truck_attrition_factor      NUMERIC(5,2)
);

-- FK build order #2a (child of terrain_types)
CREATE TABLE terrain_combat_modifiers (
    id                          BIGSERIAL PRIMARY KEY,
    terrain_type                VARCHAR(40) NOT NULL REFERENCES terrain_types(terrain_type),
    unit_class                  VARCHAR(40),
    modifier_key                VARCHAR(80) NOT NULL,
    modifier_value              NUMERIC(6,3) NOT NULL
);

-- FK build order #3
CREATE TABLE state_categories (
    state_category              VARCHAR(40) PRIMARY KEY,
    local_building_slots        INT,
    color_r                     SMALLINT,
    color_g                     SMALLINT,
    color_b                     SMALLINT
);

-- FK build order #6
CREATE TABLE ideologies (
    ideology_key                VARCHAR(40) PRIMARY KEY,
    color_r                     SMALLINT NOT NULL,
    color_g                     SMALLINT NOT NULL,
    color_b                     SMALLINT NOT NULL
);

-- FK build order #7 → ideologies
CREATE TABLE sub_ideologies (
    sub_ideology_key            VARCHAR(60) PRIMARY KEY,
    ideology_key                VARCHAR(40) NOT NULL REFERENCES ideologies(ideology_key)
);

-- FK build order #8
CREATE TABLE technology_categories (
    category_key                VARCHAR(60) PRIMARY KEY
);

-- FK build order #10
CREATE TABLE unit_types (
    unit_type_key               VARCHAR(80) PRIMARY KEY,
    abbreviation                VARCHAR(10),
    unit_group                  VARCHAR(40),
    combat_width                NUMERIC(5,2),
    max_strength                NUMERIC(8,2),
    max_organisation            NUMERIC(8,2),
    default_morale              NUMERIC(5,2),
    manpower                    INT,
    training_time               INT,
    suppression                 NUMERIC(5,2),
    weight                      NUMERIC(5,2),
    supply_consumption          NUMERIC(5,3),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #11 → self (archetype, parent)
CREATE TABLE equipment_definitions (
    equipment_key               VARCHAR(120) PRIMARY KEY,
    is_archetype                BOOLEAN NOT NULL,
    archetype_key               VARCHAR(120) REFERENCES equipment_definitions(equipment_key) DEFERRABLE INITIALLY DEFERRED,
    parent_key                  VARCHAR(120) REFERENCES equipment_definitions(equipment_key) DEFERRABLE INITIALLY DEFERRED,
    year                        SMALLINT,
    build_cost_ic               NUMERIC(8,2),
    reliability                 NUMERIC(5,2),
    maximum_speed               NUMERIC(8,2),
    defense                     NUMERIC(8,2),
    breakthrough                NUMERIC(8,2),
    soft_attack                 NUMERIC(8,2),
    hard_attack                 NUMERIC(8,2),
    ap_attack                   NUMERIC(8,2),
    air_attack                  NUMERIC(8,2),
    armor_value                 NUMERIC(8,2),
    hardness                    NUMERIC(5,2),
    is_buildable                BOOLEAN,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN equipment_definitions.archetype_key IS 'NULL for archetypes; references parent archetype for derived equipment';
COMMENT ON COLUMN equipment_definitions.parent_key IS 'Previous entry in upgrade chain (self-ref)';

-- FK build order #12 → equipment_definitions, resource_types
CREATE TABLE equipment_resources (
    equipment_key               VARCHAR(120) NOT NULL REFERENCES equipment_definitions(equipment_key),
    resource_key                VARCHAR(40) NOT NULL REFERENCES resource_types(resource_key),
    amount                      INT NOT NULL,
    source_file                 TEXT NOT NULL,
    PRIMARY KEY (equipment_key, resource_key)
);

-- FK build order #7a → terrain_types, building_types
CREATE TABLE terrain_building_limits (
    terrain_type                VARCHAR(40) NOT NULL REFERENCES terrain_types(terrain_type),
    building_key                VARCHAR(80) NOT NULL REFERENCES building_types(building_key),
    max_level                   INT NOT NULL,
    PRIMARY KEY (terrain_type, building_key)
);

-- ============================================================
-- PHASE 2 — New Geography Tables
-- ============================================================

-- FK build order #14 → provinces
CREATE TABLE province_building_positions (
    position_id                 BIGSERIAL PRIMARY KEY,
    province_id                 INT NOT NULL REFERENCES provinces(province_id),
    building_type               VARCHAR(80) NOT NULL,
    pos_x                       NUMERIC(10,2) NOT NULL,
    pos_y                       NUMERIC(10,2) NOT NULL,
    pos_z                       NUMERIC(10,2) NOT NULL,
    rotation                    NUMERIC(6,2) NOT NULL,
    linked_province_id          INT
);

COMMENT ON COLUMN province_building_positions.linked_province_id IS 'NULL when source is 0; naval_base_spawn link to another province';

-- FK build order #15
CREATE TABLE strategic_regions (
    strategic_region_id         INT PRIMARY KEY,
    name_key                    VARCHAR(80) NOT NULL,
    source_file                 TEXT NOT NULL
);

-- FK build order #16 → strategic_regions, provinces
CREATE TABLE strategic_region_provinces (
    strategic_region_id         INT NOT NULL REFERENCES strategic_regions(strategic_region_id),
    province_id                 INT NOT NULL REFERENCES provinces(province_id),
    PRIMARY KEY (strategic_region_id, province_id)
);

-- FK build order #17 → provinces
CREATE TABLE supply_nodes (
    province_id                 INT PRIMARY KEY REFERENCES provinces(province_id),
    level                       INT NOT NULL
);

-- Province adjacencies (map/adjacencies.csv) → provinces
CREATE TABLE province_adjacencies (
    id                          BIGSERIAL PRIMARY KEY,
    from_province_id            INT NOT NULL REFERENCES provinces(province_id),
    to_province_id              INT NOT NULL REFERENCES provinces(province_id),
    adjacency_type              VARCHAR(20),
    through_province_id         INT REFERENCES provinces(province_id),
    start_x                     NUMERIC(8,1),
    start_y                     NUMERIC(8,1),
    stop_x                      NUMERIC(8,1),
    stop_y                      NUMERIC(8,1),
    adjacency_rule_name         VARCHAR(80),
    comment                     VARCHAR(200)
);

-- Province railways (map/railways.txt) → provinces
CREATE TABLE province_railways (
    id                          BIGSERIAL PRIMARY KEY,
    from_province_id            INT NOT NULL REFERENCES provinces(province_id),
    to_province_id              INT NOT NULL REFERENCES provinces(province_id),
    railway_level               SMALLINT NOT NULL
);

-- ============================================================
-- PHASE 4 — Technologies
-- ============================================================

-- FK build order #29 → technologies, technology_categories
CREATE TABLE technology_categories_junction (
    technology_key              VARCHAR(120) NOT NULL REFERENCES technologies(technology_key),
    category_key                VARCHAR(60) NOT NULL REFERENCES technology_categories(category_key),
    PRIMARY KEY (technology_key, category_key)
);

-- FK build order #30 → technologies (self-ref)
CREATE TABLE technology_prerequisites (
    technology_key              VARCHAR(120) NOT NULL REFERENCES technologies(technology_key),
    prerequisite_key            VARCHAR(120) NOT NULL REFERENCES technologies(technology_key),
    source_file                 TEXT NOT NULL,
    PRIMARY KEY (technology_key, prerequisite_key)
);

-- FK build order #31 → technologies, equipment_definitions
CREATE TABLE technology_enables_equipment (
    technology_key              VARCHAR(120) NOT NULL REFERENCES technologies(technology_key),
    equipment_key               VARCHAR(120) NOT NULL REFERENCES equipment_definitions(equipment_key),
    source_file                 TEXT NOT NULL,
    PRIMARY KEY (technology_key, equipment_key)
);

-- FK build order #32 → technologies, unit_types
CREATE TABLE technology_enables_units (
    technology_key              VARCHAR(120) NOT NULL REFERENCES technologies(technology_key),
    unit_type_key               VARCHAR(80) NOT NULL REFERENCES unit_types(unit_type_key),
    source_file                 TEXT NOT NULL,
    PRIMARY KEY (technology_key, unit_type_key)
);

-- ============================================================
-- PHASE 5 — Characters
-- ============================================================

-- FK build order #33
CREATE TABLE character_traits (
    trait_key                   VARCHAR(80) PRIMARY KEY,
    trait_type                  VARCHAR(30)
);

-- FK build order #34 → countries
CREATE TABLE characters (
    character_id                VARCHAR(120) PRIMARY KEY,
    name_key                    VARCHAR(120),
    country_tag                 CHAR(3) REFERENCES countries(tag),
    gender                      VARCHAR(10),
    portrait_civilian           VARCHAR(200),
    portrait_army               VARCHAR(200),
    portrait_navy               VARCHAR(200),
    source_file                 TEXT NOT NULL
);

-- FK build order #35 → characters, sub_ideologies
CREATE TABLE character_roles (
    character_role_id           SERIAL PRIMARY KEY,
    character_id                VARCHAR(120) NOT NULL REFERENCES characters(character_id),
    role_type                   VARCHAR(30) NOT NULL,
    sub_ideology_key            VARCHAR(60) REFERENCES sub_ideologies(sub_ideology_key),
    skill                       SMALLINT,
    attack_skill                SMALLINT,
    defense_skill               SMALLINT,
    planning_skill              SMALLINT,
    logistics_skill             SMALLINT,
    maneuvering_skill           SMALLINT,
    coordination_skill          SMALLINT,
    legacy_id                   INT,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN character_roles.role_type IS 'country_leader, field_marshal, corps_commander, navy_leader, advisor, operative';
COMMENT ON COLUMN character_roles.sub_ideology_key IS 'Only for country_leader roles';
COMMENT ON COLUMN character_roles.maneuvering_skill IS 'Admiral roles only (maneuvering)';
COMMENT ON COLUMN character_roles.coordination_skill IS 'Admiral roles only (coordination)';

-- FK build order #36 → character_roles, character_traits
CREATE TABLE character_role_traits (
    character_role_id           INT NOT NULL REFERENCES character_roles(character_role_id),
    trait_key                   VARCHAR(80) NOT NULL REFERENCES character_traits(trait_key),
    PRIMARY KEY (character_role_id, trait_key)
);

-- ============================================================
-- PHASE 9 — Ideas & National Spirits
-- (Created here because country_starting_ideas depends on ideas)
-- ============================================================

-- FK build order #37
CREATE TABLE ideas (
    idea_key                    VARCHAR(120) PRIMARY KEY,
    slot                        VARCHAR(60) NOT NULL,
    is_law                      BOOLEAN NOT NULL,
    cost                        INT,
    removal_cost                INT,
    is_default                  BOOLEAN,
    picture                     VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN ideas.slot IS 'economy, trade_laws, country, hidden_ideas, etc.';
COMMENT ON COLUMN ideas.removal_cost IS '-1 = cannot remove';

-- FK build order #38 → ideas
CREATE TABLE idea_modifiers (
    idea_modifier_id            BIGSERIAL PRIMARY KEY,
    idea_key                    VARCHAR(120) NOT NULL REFERENCES ideas(idea_key),
    modifier_key                VARCHAR(120) NOT NULL,
    modifier_value              NUMERIC(12,4) NOT NULL,
    source_file                 TEXT NOT NULL
);

-- ============================================================
-- PHASE 3 (continued) — Country Starting Ideas
-- ============================================================

-- FK build order #39 → countries, ideas
-- NOTE: idea_key is polymorphic — add_ideas can reference ideas, laws, or character advisors
CREATE TABLE country_starting_ideas (
    country_tag                 CHAR(3) NOT NULL REFERENCES countries(tag),
    idea_key                    VARCHAR(120) NOT NULL,
    effective_date              DATE NOT NULL,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50),
    PRIMARY KEY (country_tag, idea_key, effective_date)
);

-- ============================================================
-- PHASE 6 — Division Templates & Land OOB
-- ============================================================

-- FK build order #44 → countries
CREATE TABLE division_templates (
    division_template_id        SERIAL PRIMARY KEY,
    country_tag                 CHAR(3) REFERENCES countries(tag),
    template_name               VARCHAR(120) NOT NULL,
    division_names_group        VARCHAR(80),
    oob_file                    VARCHAR(120),
    source_file                 TEXT NOT NULL,
    UNIQUE (country_tag, template_name, oob_file)
);

-- FK build order #45 → division_templates, unit_types
CREATE TABLE division_template_regiments (
    division_template_id        INT NOT NULL REFERENCES division_templates(division_template_id),
    unit_type_key               VARCHAR(80) NOT NULL REFERENCES unit_types(unit_type_key),
    grid_x                      SMALLINT NOT NULL,
    grid_y                      SMALLINT NOT NULL,
    PRIMARY KEY (division_template_id, grid_x, grid_y)
);

-- FK build order #46 → division_templates, unit_types
CREATE TABLE division_template_support (
    division_template_id        INT NOT NULL REFERENCES division_templates(division_template_id),
    unit_type_key               VARCHAR(80) NOT NULL REFERENCES unit_types(unit_type_key),
    grid_x                      SMALLINT NOT NULL,
    grid_y                      SMALLINT NOT NULL,
    PRIMARY KEY (division_template_id, grid_x, grid_y)
);

-- FK build order #47 → division_templates, countries, provinces
CREATE TABLE divisions (
    division_id                 SERIAL PRIMARY KEY,
    country_tag                 CHAR(3) REFERENCES countries(tag),
    division_template_id        INT REFERENCES division_templates(division_template_id),
    template_name               VARCHAR(120),
    location_province_id        INT REFERENCES provinces(province_id),
    start_experience_factor     NUMERIC(4,2),
    oob_file                    VARCHAR(120),
    source_file                 TEXT NOT NULL
);

COMMENT ON COLUMN divisions.division_template_id IS 'Resolved by matching template_name; nullable until ETL resolves';
COMMENT ON COLUMN divisions.template_name IS 'Raw template name from division_template field in OOB file';

-- ============================================================
-- PHASE 7 — Naval OOB
-- ============================================================

-- FK build order #48 → countries, equipment_definitions
CREATE TABLE equipment_variants (
    equipment_variant_id        SERIAL PRIMARY KEY,
    owner_tag                   CHAR(3) NOT NULL REFERENCES countries(tag),
    base_equipment_key          VARCHAR(120) NOT NULL REFERENCES equipment_definitions(equipment_key),
    version_name                VARCHAR(120),
    effective_date              DATE NOT NULL DEFAULT '1936-01-01',
    source_file                 TEXT NOT NULL,
    UNIQUE (owner_tag, base_equipment_key, version_name, effective_date)
);

-- FK build order #48b → equipment_variants
CREATE TABLE equipment_variant_modules (
    equipment_variant_id        INT NOT NULL REFERENCES equipment_variants(equipment_variant_id),
    slot_name                   VARCHAR(120) NOT NULL,
    module_key                  VARCHAR(120) NOT NULL,
    PRIMARY KEY (equipment_variant_id, slot_name)
);

-- FK build order #48c → equipment_variants
CREATE TABLE equipment_variant_upgrades (
    equipment_variant_id        INT NOT NULL REFERENCES equipment_variants(equipment_variant_id),
    upgrade_key                 VARCHAR(120) NOT NULL,
    upgrade_level               INT NOT NULL DEFAULT 0,
    PRIMARY KEY (equipment_variant_id, upgrade_key)
);

-- FK build order #49 → countries, provinces
CREATE TABLE fleets (
    fleet_id                    SERIAL PRIMARY KEY,
    country_tag                 CHAR(3) NOT NULL REFERENCES countries(tag),
    fleet_name                  VARCHAR(200) NOT NULL,
    naval_base_province_id      INT REFERENCES provinces(province_id),
    oob_file                    VARCHAR(120),
    source_file                 TEXT NOT NULL
);

-- FK build order #50 → fleets, provinces
CREATE TABLE task_forces (
    task_force_id               SERIAL PRIMARY KEY,
    fleet_id                    INT NOT NULL REFERENCES fleets(fleet_id),
    task_force_name             VARCHAR(200) NOT NULL,
    location_province_id        INT REFERENCES provinces(province_id)
);

-- FK build order #51 → task_forces, equipment_definitions, countries
CREATE TABLE ships (
    ship_id                     SERIAL PRIMARY KEY,
    task_force_id               INT NOT NULL REFERENCES task_forces(task_force_id),
    ship_name                   VARCHAR(200) NOT NULL,
    definition                  VARCHAR(60) NOT NULL,
    hull_equipment_key          VARCHAR(120) NOT NULL REFERENCES equipment_definitions(equipment_key),
    version_name                VARCHAR(120),
    owner_tag                   CHAR(3) NOT NULL REFERENCES countries(tag),
    pride_of_the_fleet          BOOLEAN,
    start_experience_factor     NUMERIC(4,2),
    source_file                 TEXT NOT NULL
);

COMMENT ON COLUMN ships.definition IS 'Role type: destroyer, submarine, light_cruiser, heavy_cruiser, battle_cruiser, battleship, carrier';

-- ============================================================
-- PHASE 8 — Air OOB
-- ============================================================

-- FK build order #52 → countries, states
CREATE TABLE air_wings (
    air_wing_id                 SERIAL PRIMARY KEY,
    country_tag                 CHAR(3) NOT NULL REFERENCES countries(tag),
    location_state_id           INT NOT NULL REFERENCES states(state_id),
    wing_name                   VARCHAR(200),
    equipment_type              VARCHAR(120) NOT NULL,
    amount                      INT NOT NULL,
    version_name                VARCHAR(120),
    oob_file                    VARCHAR(120),
    source_file                 TEXT NOT NULL
);

-- ============================================================
-- PHASE 10 — National Focus Trees
-- ============================================================

-- FK build order #40 → countries (nullable)
CREATE TABLE focus_trees (
    focus_tree_id               VARCHAR(120) PRIMARY KEY,
    country_tag                 CHAR(3) REFERENCES countries(tag),
    initial_x                   INT,
    initial_y                   INT,
    source_file                 TEXT NOT NULL
);

-- FK build order #41 → focus_trees
CREATE TABLE focuses (
    focus_id                    VARCHAR(120) PRIMARY KEY,
    focus_tree_id               VARCHAR(120) NOT NULL REFERENCES focus_trees(focus_tree_id),
    cost                        NUMERIC(5,1),
    x_pos                       INT,
    y_pos                       INT,
    icon                        VARCHAR(200),
    cancel_if_invalid           BOOLEAN,
    continue_if_invalid         BOOLEAN,
    available_if_capitulated    BOOLEAN,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #42 → focuses (self-ref)
CREATE TABLE focus_prerequisites (
    focus_id                    VARCHAR(120) NOT NULL REFERENCES focuses(focus_id),
    prerequisite_group          SMALLINT NOT NULL DEFAULT 1,
    required_focus_id           VARCHAR(120) NOT NULL REFERENCES focuses(focus_id),
    PRIMARY KEY (focus_id, prerequisite_group, required_focus_id)
);

COMMENT ON COLUMN focus_prerequisites.prerequisite_group IS 'Same group = OR alternatives; all groups must be satisfied (AND)';

-- FK build order #43 → focuses (self-ref)
CREATE TABLE focus_mutually_exclusive (
    focus_a_id                  VARCHAR(120) NOT NULL REFERENCES focuses(focus_id),
    focus_b_id                  VARCHAR(120) NOT NULL REFERENCES focuses(focus_id),
    PRIMARY KEY (focus_a_id, focus_b_id),
    CHECK (focus_a_id < focus_b_id)
);

-- ============================================================
-- PHASE 11 — Governance
-- ============================================================

-- FK build order #53
CREATE TABLE autonomy_states (
    autonomy_key                VARCHAR(80) PRIMARY KEY,
    is_puppet                   BOOLEAN,
    is_default                  BOOLEAN,
    min_freedom_level           NUMERIC(4,2),
    manpower_influence          NUMERIC(4,2),
    dlc_source                  VARCHAR(80)
);

-- FK build order #54 → autonomy_states
CREATE TABLE autonomy_state_modifiers (
    id                          BIGSERIAL PRIMARY KEY,
    autonomy_key                VARCHAR(80) NOT NULL REFERENCES autonomy_states(autonomy_key),
    modifier_key                VARCHAR(120) NOT NULL,
    modifier_value              NUMERIC(8,4) NOT NULL
);

-- FK build order #55 → self (fallback_law_key)
CREATE TABLE occupation_laws (
    occupation_law_key          VARCHAR(80) PRIMARY KEY,
    icon_index                  INT,
    sound_effect                VARCHAR(120),
    gui_order                   INT,
    main_fallback_law           BOOLEAN,
    fallback_law_key            VARCHAR(80) REFERENCES occupation_laws(occupation_law_key)
);

-- FK build order #56 → occupation_laws
CREATE TABLE occupation_law_modifiers (
    id                          BIGSERIAL PRIMARY KEY,
    occupation_law_key          VARCHAR(80) NOT NULL REFERENCES occupation_laws(occupation_law_key),
    modifier_key                VARCHAR(120) NOT NULL,
    modifier_value              NUMERIC(8,4) NOT NULL,
    is_suppressed               BOOLEAN NOT NULL
);

COMMENT ON COLUMN occupation_law_modifiers.is_suppressed IS 'false = state_modifier block, true = suppressed_state_modifier block';

-- ============================================================
-- PHASE 12–15 — Extensions
-- ============================================================

-- FK build order #57 → countries
CREATE TABLE country_visual_definitions (
    country_tag                 CHAR(3) PRIMARY KEY REFERENCES countries(tag),
    graphical_culture           VARCHAR(80),
    graphical_culture_2d        VARCHAR(80)
);

-- FK build order #58 → countries (REVISED from Phase 16)
CREATE TABLE intelligence_agencies (
    agency_id                   SERIAL PRIMARY KEY,
    picture_gfx                 VARCHAR(120) NOT NULL,
    default_tag                 CHAR(3) REFERENCES countries(tag),
    available_tag               CHAR(3) REFERENCES countries(tag),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN intelligence_agencies.default_tag IS 'Country this agency is the default for';
COMMENT ON COLUMN intelligence_agencies.available_tag IS 'Restricts which country can use this agency (original_tag check)';

-- FK build order #59 → intelligence_agencies
CREATE TABLE intelligence_agency_names (
    id                          SERIAL PRIMARY KEY,
    agency_id                   INT NOT NULL REFERENCES intelligence_agencies(agency_id),
    name                        VARCHAR(200) NOT NULL
);

-- FK build order #60 → countries
CREATE TABLE bookmarks (
    bookmark_id                 SERIAL PRIMARY KEY,
    bookmark_name               VARCHAR(120) NOT NULL,
    bookmark_date               DATE NOT NULL,
    picture_gfx                 VARCHAR(120),
    default_country_tag         CHAR(3) REFERENCES countries(tag)
);

-- FK build order #61 → bookmarks, countries, ideologies
CREATE TABLE bookmark_countries (
    bookmark_id                 INT NOT NULL REFERENCES bookmarks(bookmark_id),
    country_tag                 CHAR(3) NOT NULL REFERENCES countries(tag),
    ideology_key                VARCHAR(40) REFERENCES ideologies(ideology_key),
    PRIMARY KEY (bookmark_id, country_tag)
);

-- FK build order #62
CREATE TABLE decision_categories (
    category_key                VARCHAR(80) PRIMARY KEY,
    icon                        VARCHAR(120),
    picture_gfx                 VARCHAR(120),
    priority                    INT
);

-- FK build order #63 → decision_categories
CREATE TABLE decisions (
    decision_key                VARCHAR(120) PRIMARY KEY,
    category_key                VARCHAR(80) NOT NULL REFERENCES decision_categories(category_key),
    icon                        VARCHAR(120),
    cost                        INT,
    fire_only_once              BOOLEAN,
    dlc_source                  VARCHAR(80)
);

-- ============================================================
-- PHASE 16 — Espionage System (La Résistance)
-- ============================================================

-- FK build order #64
CREATE TABLE operation_tokens (
    token_key                   VARCHAR(60) PRIMARY KEY,
    name                        VARCHAR(120),
    "desc"                        VARCHAR(200),
    icon                        VARCHAR(120),
    text_icon                   VARCHAR(120),
    intel_source                VARCHAR(30),
    intel_gain                  INT
);

-- FK build order #65
CREATE TABLE operation_phase_definitions (
    phase_key                   VARCHAR(120) PRIMARY KEY,
    name                        VARCHAR(120),
    "desc"                        VARCHAR(200),
    outcome                     VARCHAR(120),
    icon                        VARCHAR(120),
    picture                     VARCHAR(120),
    return_on_complete          BOOLEAN,
    source_file                 TEXT NOT NULL
);

-- FK build order #66 → operation_phase_definitions
CREATE TABLE operation_phase_equipment (
    id                          SERIAL PRIMARY KEY,
    phase_key                   VARCHAR(120) NOT NULL REFERENCES operation_phase_definitions(phase_key),
    equipment_key               VARCHAR(120) NOT NULL,
    amount                      INT,
    days                        INT
);

-- FK build order #67
CREATE TABLE operations (
    operation_key               VARCHAR(120) PRIMARY KEY,
    name                        VARCHAR(120),
    "desc"                        VARCHAR(120),
    icon                        VARCHAR(120),
    map_icon                    VARCHAR(120),
    priority                    INT,
    days                        INT,
    network_strength            INT,
    operatives                  INT,
    risk_chance                 NUMERIC(4,3),
    experience                  NUMERIC(5,2),
    cost_multiplier             NUMERIC(5,3),
    outcome_extra_chance        NUMERIC(4,3),
    prevent_captured_operative_to_die BOOLEAN,
    scale_cost_independent_of_target BOOLEAN,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #68 → operations, operation_tokens
CREATE TABLE operation_awarded_tokens (
    operation_key               VARCHAR(120) NOT NULL REFERENCES operations(operation_key),
    token_key                   VARCHAR(60) NOT NULL REFERENCES operation_tokens(token_key),
    PRIMARY KEY (operation_key, token_key)
);

-- FK build order #69 → operations
CREATE TABLE operation_equipment_requirements (
    id                          SERIAL PRIMARY KEY,
    operation_key               VARCHAR(120) NOT NULL REFERENCES operations(operation_key),
    equipment_key               VARCHAR(120) NOT NULL,
    amount                      INT NOT NULL
);

-- FK build order #70 → operations
CREATE TABLE operation_phase_groups (
    operation_key               VARCHAR(120) NOT NULL REFERENCES operations(operation_key),
    sequence_index              SMALLINT NOT NULL,
    PRIMARY KEY (operation_key, sequence_index)
);

-- FK build order #71 → operation_phase_groups, operation_phase_definitions
CREATE TABLE operation_phase_options (
    id                          SERIAL PRIMARY KEY,
    operation_key               VARCHAR(120) NOT NULL,
    sequence_index              SMALLINT NOT NULL,
    phase_key                   VARCHAR(120) NOT NULL REFERENCES operation_phase_definitions(phase_key),
    base_weight                 INT NOT NULL,
    FOREIGN KEY (operation_key, sequence_index) REFERENCES operation_phase_groups(operation_key, sequence_index)
);

-- FK build order #72
CREATE TABLE intel_agency_upgrade_branches (
    branch_key                  VARCHAR(60) PRIMARY KEY
);

-- FK build order #73 → intel_agency_upgrade_branches
CREATE TABLE intel_agency_upgrades (
    upgrade_key                 VARCHAR(80) PRIMARY KEY,
    branch_key                  VARCHAR(60) NOT NULL REFERENCES intel_agency_upgrade_branches(branch_key),
    picture                     VARCHAR(120),
    frame                       VARCHAR(120),
    sound                       VARCHAR(120)
);

-- FK build order #74 → intel_agency_upgrades
CREATE TABLE intel_agency_upgrade_levels (
    id                          SERIAL PRIMARY KEY,
    upgrade_key                 VARCHAR(80) NOT NULL REFERENCES intel_agency_upgrades(upgrade_key),
    level_index                 SMALLINT NOT NULL,
    modifier_key                VARCHAR(80) NOT NULL,
    modifier_value              NUMERIC(8,4) NOT NULL
);

-- FK build order #75 → intel_agency_upgrades
CREATE TABLE intel_agency_upgrade_progress_modifiers (
    id                          SERIAL PRIMARY KEY,
    upgrade_key                 VARCHAR(80) NOT NULL REFERENCES intel_agency_upgrades(upgrade_key),
    modifier_key                VARCHAR(80) NOT NULL,
    modifier_value              NUMERIC(8,4) NOT NULL
);

-- ============================================================
-- PHASE 17 — Occupation & Resistance (La Résistance)
-- ============================================================

-- FK build order #76
CREATE TABLE compliance_modifiers (
    modifier_key                VARCHAR(60) PRIMARY KEY,
    type                        VARCHAR(40) NOT NULL,
    icon                        VARCHAR(120),
    small_icon                  VARCHAR(120),
    threshold                   INT NOT NULL,
    margin                      INT,
    dlc_source                  VARCHAR(50),
    source_file                 TEXT
);

-- FK build order #77 → compliance_modifiers
CREATE TABLE compliance_modifier_effects (
    id                          SERIAL PRIMARY KEY,
    modifier_key                VARCHAR(60) NOT NULL REFERENCES compliance_modifiers(modifier_key),
    effect_key                  VARCHAR(80) NOT NULL,
    effect_value                NUMERIC(10,4) NOT NULL
);

-- FK build order #78
CREATE TABLE resistance_modifiers (
    modifier_key                VARCHAR(60) PRIMARY KEY,
    type                        VARCHAR(40) NOT NULL,
    icon                        VARCHAR(120),
    small_icon                  VARCHAR(120),
    threshold                   INT NOT NULL,
    margin                      INT,
    source_file                 TEXT
);

-- FK build order #79 → resistance_modifiers
CREATE TABLE resistance_modifier_effects (
    id                          SERIAL PRIMARY KEY,
    modifier_key                VARCHAR(60) NOT NULL REFERENCES resistance_modifiers(modifier_key),
    effect_key                  VARCHAR(80) NOT NULL,
    effect_value                NUMERIC(10,4) NOT NULL
);

-- FK build order #80
CREATE TABLE resistance_activities (
    activity_key                VARCHAR(80) PRIMARY KEY,
    alert_text                  VARCHAR(120),
    max_amount                  INT,
    duration                    INT,
    source_file                 TEXT
);

-- ============================================================
-- PHASE 18 — Military-Industrial Organizations (Arms Against Tyranny)
-- ============================================================

-- FK build order #81
CREATE TABLE mio_equipment_groups (
    group_key                   VARCHAR(80) PRIMARY KEY
);

-- FK build order #82 → mio_equipment_groups
CREATE TABLE mio_equipment_group_members (
    group_key                   VARCHAR(80) NOT NULL REFERENCES mio_equipment_groups(group_key),
    equipment_type              VARCHAR(120) NOT NULL,
    PRIMARY KEY (group_key, equipment_type)
);

-- FK build order #83
CREATE TABLE mio_templates (
    template_key                VARCHAR(120) PRIMARY KEY,
    icon                        VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #84 → mio_templates
CREATE TABLE mio_organizations (
    organization_key            VARCHAR(120) PRIMARY KEY,
    template_key                VARCHAR(120) REFERENCES mio_templates(template_key),
    icon                        VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN mio_organizations.template_key IS 'FK to generic template via include; NULL if standalone org';

-- FK build order #85 — polymorphic (mio_templates or mio_organizations)
CREATE TABLE mio_organization_equipment_types (
    id                          SERIAL PRIMARY KEY,
    owner_key                   VARCHAR(120) NOT NULL,
    owner_type                  VARCHAR(15),
    equipment_type              VARCHAR(120) NOT NULL
);

COMMENT ON COLUMN mio_organization_equipment_types.owner_type IS '''template'' or ''organization''';

-- FK build order #86 — polymorphic
CREATE TABLE mio_initial_traits (
    id                          SERIAL PRIMARY KEY,
    owner_key                   VARCHAR(120) NOT NULL,
    owner_type                  VARCHAR(15) NOT NULL,
    name                        VARCHAR(120)
);

COMMENT ON COLUMN mio_initial_traits.owner_type IS '''template'' or ''organization''';

-- FK build order #87 — polymorphic (mio_templates or mio_organizations)
CREATE TABLE mio_traits (
    trait_token                 VARCHAR(120) PRIMARY KEY,
    owner_key                   VARCHAR(120) NOT NULL,
    owner_type                  VARCHAR(15) NOT NULL,
    trait_type                  VARCHAR(20) NOT NULL,
    name                        VARCHAR(120),
    icon                        VARCHAR(120),
    special_trait_background    BOOLEAN,
    position_x                  INT,
    position_y                  INT,
    relative_position_id        VARCHAR(120)
);

COMMENT ON COLUMN mio_traits.owner_type IS '''template'', ''organization''';
COMMENT ON COLUMN mio_traits.trait_type IS '''trait'', ''add_trait'', ''override_trait''';

-- FK build order #88 → mio_traits
CREATE TABLE mio_trait_bonuses (
    id                          SERIAL PRIMARY KEY,
    trait_token                 VARCHAR(120) NOT NULL REFERENCES mio_traits(trait_token),
    bonus_category              VARCHAR(30) NOT NULL,
    bonus_key                   VARCHAR(80) NOT NULL,
    bonus_value                 NUMERIC(10,4) NOT NULL
);

COMMENT ON COLUMN mio_trait_bonuses.bonus_category IS '''equipment_bonus'', ''production_bonus'', ''organization_modifier''';

-- FK build order #89 → mio_traits (self-ref ×2)
CREATE TABLE mio_trait_prerequisites (
    id                          SERIAL PRIMARY KEY,
    trait_token                 VARCHAR(120) NOT NULL REFERENCES mio_traits(trait_token),
    parent_token                VARCHAR(120) NOT NULL REFERENCES mio_traits(trait_token),
    requirement_type            VARCHAR(15) NOT NULL
);

COMMENT ON COLUMN mio_trait_prerequisites.requirement_type IS '''any_parent'' or ''all_parents''';

-- FK build order #90 → mio_traits (self-ref ×2)
CREATE TABLE mio_trait_exclusions (
    trait_token_a               VARCHAR(120) NOT NULL REFERENCES mio_traits(trait_token),
    trait_token_b               VARCHAR(120) NOT NULL REFERENCES mio_traits(trait_token),
    PRIMARY KEY (trait_token_a, trait_token_b),
    CHECK (trait_token_a < trait_token_b)
);

-- FK build order #91
CREATE TABLE mio_policies (
    policy_key                  VARCHAR(120) PRIMARY KEY,
    icon                        VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #92 → mio_policies
CREATE TABLE mio_policy_bonuses (
    id                          SERIAL PRIMARY KEY,
    policy_key                  VARCHAR(120) NOT NULL REFERENCES mio_policies(policy_key),
    bonus_category              VARCHAR(30) NOT NULL,
    bonus_key                   VARCHAR(80) NOT NULL,
    bonus_value                 NUMERIC(10,4) NOT NULL
);

-- ============================================================
-- PHASE 19 — Raids (Götterdämmerung)
-- ============================================================

-- FK build order #93
CREATE TABLE raid_categories (
    category_key                VARCHAR(60) PRIMARY KEY,
    intel_source                VARCHAR(30),
    faction_influence_score_on_success INT,
    free_targeting              BOOLEAN,
    dlc_source                  VARCHAR(50)
);

-- FK build order #94 → raid_categories
CREATE TABLE raids (
    raid_key                    VARCHAR(80) PRIMARY KEY,
    category_key                VARCHAR(60) NOT NULL REFERENCES raid_categories(category_key),
    days_to_prepare             INT,
    command_power               INT,
    target_icon                 VARCHAR(120),
    launch_sound                VARCHAR(80),
    custom_map_icon             VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #95 → raids
CREATE TABLE raid_equipment_requirements (
    id                          SERIAL PRIMARY KEY,
    raid_key                    VARCHAR(80) NOT NULL REFERENCES raids(raid_key),
    requirement_group           SMALLINT NOT NULL,
    equipment_type              VARCHAR(120) NOT NULL,
    amount_min                  INT,
    amount_max                  INT
);

COMMENT ON COLUMN raid_equipment_requirements.requirement_group IS 'Alternative groups: satisfy ANY one group to launch';

-- ============================================================
-- PHASE 20 — Career Profile (By Blood Alone / Götterdämmerung)
-- ============================================================

-- FK build order #96
CREATE TABLE medals (
    medal_key                   VARCHAR(80) PRIMARY KEY,
    name                        VARCHAR(120) NOT NULL,
    description                 VARCHAR(120),
    frame_1                     SMALLINT,
    frame_2                     SMALLINT,
    frame_3                     SMALLINT,
    tracked_variable            VARCHAR(80),
    dlc_source                  VARCHAR(50)
);

-- FK build order #97 → medals
CREATE TABLE medal_tiers (
    medal_key                   VARCHAR(80) NOT NULL REFERENCES medals(medal_key),
    tier                        VARCHAR(10) NOT NULL,
    variable                    VARCHAR(80),
    threshold_value             INT,
    compare                     VARCHAR(40),
    PRIMARY KEY (medal_key, tier)
);

COMMENT ON COLUMN medal_tiers.tier IS '''bronze'', ''silver'', or ''gold''';

-- FK build order #98
CREATE TABLE ribbons (
    ribbon_key                  VARCHAR(80) PRIMARY KEY,
    name                        VARCHAR(120) NOT NULL,
    description                 VARCHAR(120),
    quote_text                  VARCHAR(120),
    happened_trigger            TEXT,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN ribbons.happened_trigger IS 'Scripted trigger stored as raw text';

-- FK build order #99
CREATE TABLE ace_modifiers (
    modifier_key                VARCHAR(60) PRIMARY KEY,
    chance                      NUMERIC(4,3) NOT NULL
);

-- FK build order #100 → ace_modifiers
CREATE TABLE ace_modifier_effects (
    id                          SERIAL PRIMARY KEY,
    modifier_key                VARCHAR(60) NOT NULL REFERENCES ace_modifiers(modifier_key),
    effect_key                  VARCHAR(80) NOT NULL,
    effect_value                NUMERIC(8,4) NOT NULL
);

-- FK build order #101 → ace_modifiers
CREATE TABLE ace_modifier_equipment_types (
    modifier_key                VARCHAR(60) NOT NULL REFERENCES ace_modifiers(modifier_key),
    equipment_type              VARCHAR(60) NOT NULL,
    PRIMARY KEY (modifier_key, equipment_type)
);

-- FK build order #102
CREATE TABLE unit_medals (
    medal_key                   VARCHAR(80) PRIMARY KEY,
    frame                       INT,
    icon                        VARCHAR(120),
    cost                        INT,
    dlc_source                  VARCHAR(50)
);

-- FK build order #103 → unit_medals
CREATE TABLE unit_medal_modifiers (
    id                          SERIAL PRIMARY KEY,
    medal_key                   VARCHAR(80) NOT NULL REFERENCES unit_medals(medal_key),
    modifier_key                VARCHAR(80) NOT NULL,
    modifier_value              NUMERIC(8,4) NOT NULL
);

-- ============================================================
-- PHASE 21 — Balance of Power & Continuous Focuses
-- ============================================================

-- FK build order #104
CREATE TABLE balance_of_power_definitions (
    bop_key                     VARCHAR(80) PRIMARY KEY,
    initial_value               NUMERIC(5,3),
    left_side                   VARCHAR(80),
    right_side                  VARCHAR(80),
    decision_category           VARCHAR(80),
    source_file                 TEXT NOT NULL
);

-- FK build order #105 → balance_of_power_definitions
CREATE TABLE bop_sides (
    bop_key                     VARCHAR(80) NOT NULL REFERENCES balance_of_power_definitions(bop_key),
    side_id                     VARCHAR(80) NOT NULL,
    side_position               VARCHAR(10) NOT NULL,
    icon                        VARCHAR(120),
    PRIMARY KEY (bop_key, side_id)
);

-- FK build order #106 → bop_sides
CREATE TABLE bop_ranges (
    range_id                    VARCHAR(80) PRIMARY KEY,
    bop_key                     VARCHAR(80) NOT NULL,
    side_id                     VARCHAR(80) NOT NULL,
    min_value                   NUMERIC(5,3) NOT NULL,
    max_value                   NUMERIC(5,3) NOT NULL,
    FOREIGN KEY (bop_key, side_id) REFERENCES bop_sides(bop_key, side_id)
);

-- FK build order #107 → bop_ranges
CREATE TABLE bop_range_modifiers (
    id                          SERIAL PRIMARY KEY,
    range_id                    VARCHAR(80) NOT NULL REFERENCES bop_ranges(range_id),
    modifier_key                VARCHAR(80) NOT NULL,
    modifier_value              NUMERIC(10,4) NOT NULL
);

-- FK build order #108
CREATE TABLE continuous_focus_palettes (
    palette_id                  VARCHAR(80) PRIMARY KEY,
    is_default                  BOOLEAN,
    reset_on_civilwar           BOOLEAN,
    position_x                  INT,
    position_y                  INT,
    source_file                 TEXT NOT NULL
);

-- FK build order #109 → continuous_focus_palettes
CREATE TABLE continuous_focuses (
    focus_id                    VARCHAR(120) PRIMARY KEY,
    palette_id                  VARCHAR(80) NOT NULL REFERENCES continuous_focus_palettes(palette_id),
    icon                        VARCHAR(120),
    daily_cost                  INT,
    available_if_capitulated    BOOLEAN,
    dlc_source                  VARCHAR(50)
);

-- FK build order #110 → continuous_focuses
CREATE TABLE continuous_focus_modifiers (
    id                          SERIAL PRIMARY KEY,
    focus_id                    VARCHAR(120) NOT NULL REFERENCES continuous_focuses(focus_id),
    modifier_key                VARCHAR(80) NOT NULL,
    modifier_value              NUMERIC(10,4) NOT NULL
);

-- ============================================================
-- PHASE 22 — Miscellaneous DLC Systems
-- ============================================================

-- FK build order #111
CREATE TABLE technology_sharing_groups (
    group_id                    VARCHAR(80) PRIMARY KEY,
    name                        VARCHAR(120),
    "desc"                        VARCHAR(200),
    picture                     VARCHAR(120),
    research_sharing_per_country_bonus NUMERIC(5,3),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #112
CREATE TABLE dynamic_modifiers (
    modifier_key                VARCHAR(120) PRIMARY KEY,
    icon                        VARCHAR(120),
    attacker_modifier           BOOLEAN,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

-- FK build order #113 → dynamic_modifiers
CREATE TABLE dynamic_modifier_effects (
    id                          SERIAL PRIMARY KEY,
    modifier_key                VARCHAR(120) NOT NULL REFERENCES dynamic_modifiers(modifier_key),
    effect_key                  VARCHAR(120) NOT NULL,
    effect_value_static         NUMERIC(10,4),
    effect_value_variable       VARCHAR(120)
);

COMMENT ON COLUMN dynamic_modifier_effects.effect_value_static IS 'Static numeric value; NULL if value is a variable reference';
COMMENT ON COLUMN dynamic_modifier_effects.effect_value_variable IS 'Variable name (e.g. sabotaged_oil); NULL if static';

-- FK build order #114
CREATE TABLE scientist_traits (
    trait_key                   VARCHAR(80) PRIMARY KEY,
    icon                        VARCHAR(120),
    dlc_source                  VARCHAR(50)
);

-- FK build order #115 → scientist_traits
CREATE TABLE scientist_trait_modifiers (
    id                          SERIAL PRIMARY KEY,
    trait_key                   VARCHAR(80) NOT NULL REFERENCES scientist_traits(trait_key),
    modifier_key                VARCHAR(80) NOT NULL,
    modifier_value              NUMERIC(8,4) NOT NULL
);

-- FK build order #116
CREATE TABLE peace_action_categories (
    category_key                VARCHAR(60) PRIMARY KEY,
    name                        VARCHAR(120),
    is_default                  BOOLEAN
);

-- FK build order #117 → peace_action_categories
CREATE TABLE peace_cost_modifiers (
    modifier_key                VARCHAR(120) PRIMARY KEY,
    category_key                VARCHAR(60) REFERENCES peace_action_categories(category_key),
    peace_action_type           VARCHAR(200),
    cost_multiplier             NUMERIC(6,3),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON COLUMN peace_cost_modifiers.peace_action_type IS 'Comma-separated: take_states, puppet, liberate, force_government';

-- ============================================================
-- PHASE 23 — Doctrines (Officer Corps / Military Experience)
-- ============================================================

-- FK build order #118
CREATE TABLE doctrine_folders (
    folder_key                  VARCHAR(20) PRIMARY KEY,
    name_loc                    VARCHAR(80),
    ledger                      VARCHAR(10) NOT NULL,
    xp_type                     VARCHAR(10) NOT NULL
);

COMMENT ON TABLE doctrine_folders IS 'Top-level doctrine categories: land, naval, air';
COMMENT ON COLUMN doctrine_folders.ledger IS 'army, navy, or air';
COMMENT ON COLUMN doctrine_folders.xp_type IS 'army, navy, or air — XP currency used';

-- FK build order #119 → doctrine_folders
CREATE TABLE doctrine_tracks (
    track_key                   VARCHAR(40) PRIMARY KEY,
    folder_key                  VARCHAR(20) NOT NULL REFERENCES doctrine_folders(folder_key),
    name_loc                    VARCHAR(80),
    mastery_multiplier          NUMERIC(6,2)
);

COMMENT ON TABLE doctrine_tracks IS 'Tracks within a doctrine folder (e.g. infantry, armor, operations)';

-- FK build order #120 → doctrine_folders
CREATE TABLE grand_doctrines (
    doctrine_key                VARCHAR(60) PRIMARY KEY,
    folder_key                  VARCHAR(20) NOT NULL REFERENCES doctrine_folders(folder_key),
    name_loc                    VARCHAR(80),
    xp_cost                     INTEGER NOT NULL DEFAULT 100,
    xp_type                     VARCHAR(10) NOT NULL,
    source_file                 TEXT NOT NULL
);

COMMENT ON TABLE grand_doctrines IS 'Mutually-exclusive grand doctrines (e.g. Mobile Warfare, Fleet in Being)';

-- FK build order #121 → grand_doctrines, doctrine_tracks
CREATE TABLE grand_doctrine_tracks (
    doctrine_key                VARCHAR(60) NOT NULL REFERENCES grand_doctrines(doctrine_key),
    track_key                   VARCHAR(40) NOT NULL REFERENCES doctrine_tracks(track_key),
    ordinal                     SMALLINT NOT NULL,
    PRIMARY KEY (doctrine_key, track_key)
);

COMMENT ON TABLE grand_doctrine_tracks IS 'Junction: which tracks belong to each grand doctrine';

-- FK build order #122 → doctrine_tracks
CREATE TABLE subdoctrines (
    subdoctrine_key             VARCHAR(80) PRIMARY KEY,
    track_key                   VARCHAR(40) NOT NULL REFERENCES doctrine_tracks(track_key),
    name_loc                    VARCHAR(80),
    xp_cost                     INTEGER NOT NULL DEFAULT 100,
    xp_type                     VARCHAR(10) NOT NULL,
    reward_count                SMALLINT NOT NULL DEFAULT 0,
    source_file                 TEXT NOT NULL
);

COMMENT ON TABLE subdoctrines IS 'Subdoctrines slotted into tracks; unlocked with military XP';
COMMENT ON COLUMN subdoctrines.reward_count IS 'Number of mastery reward tiers defined';

-- FK build order #123 → countries, grand_doctrines, subdoctrines
CREATE TABLE country_starting_doctrines (
    id                          SERIAL PRIMARY KEY,
    country_tag                 CHAR(3) NOT NULL REFERENCES countries(tag),
    date                        DATE NOT NULL DEFAULT '1936-01-01',
    doctrine_type               VARCHAR(15) NOT NULL,
    doctrine_key                VARCHAR(80) NOT NULL
);

COMMENT ON TABLE country_starting_doctrines IS 'Grand doctrines and subdoctrines pre-selected in country history';
COMMENT ON COLUMN country_starting_doctrines.doctrine_type IS 'grand or sub';
COMMENT ON COLUMN country_starting_doctrines.doctrine_key IS 'References grand_doctrines.doctrine_key or subdoctrines.subdoctrine_key';

-- ============================================================
-- Phase 24 — Factions (Ride of the Valkyries)
-- ============================================================

CREATE TABLE faction_rule_groups (
    rule_group_key              VARCHAR(80) PRIMARY KEY,
    source_file                 TEXT NOT NULL
);

COMMENT ON TABLE faction_rule_groups IS 'Groups that classify faction rules (ideology, geographical, war, peace, etc.)';

CREATE TABLE faction_rules (
    rule_key                    VARCHAR(120) PRIMARY KEY,
    rule_type                   VARCHAR(60) NOT NULL,
    rule_group_key              VARCHAR(80) REFERENCES faction_rule_groups(rule_group_key),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE faction_rules IS 'Individual faction rules (joining, dismissal, war declaration, peace, etc.)';
COMMENT ON COLUMN faction_rules.rule_type IS 'From type = field: joining_rules, peace_conference_rules, etc.';

CREATE TABLE faction_rule_group_members (
    rule_group_key              VARCHAR(80) NOT NULL REFERENCES faction_rule_groups(rule_group_key),
    rule_key                    VARCHAR(120) NOT NULL REFERENCES faction_rules(rule_key),
    PRIMARY KEY (rule_group_key, rule_key)
);

COMMENT ON TABLE faction_rule_group_members IS 'Junction: which rules belong to which rule groups';

CREATE TABLE faction_manifests (
    manifest_key                VARCHAR(120) PRIMARY KEY,
    name_loc                    VARCHAR(120),
    description_loc             VARCHAR(120),
    is_manifest                 BOOLEAN NOT NULL DEFAULT true,
    total_amount                INTEGER,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE faction_manifests IS 'Faction manifestos — ratio progress targets for faction objectives';
COMMENT ON COLUMN faction_manifests.total_amount IS 'From ratio_progress.total_amount';

CREATE TABLE faction_goals (
    goal_key                    VARCHAR(120) PRIMARY KEY,
    name_loc                    VARCHAR(120),
    description_loc             VARCHAR(120),
    category                    VARCHAR(20) NOT NULL,
    goal_group                  VARCHAR(80),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE faction_goals IS 'Faction goals (short/medium/long-term objectives for faction members)';
COMMENT ON COLUMN faction_goals.category IS 'short_term, medium_term, or long_term';
COMMENT ON COLUMN faction_goals.goal_group IS 'From group = FOCUS_FILTER_xxx';

CREATE TABLE faction_templates (
    template_key                VARCHAR(120) PRIMARY KEY,
    name_loc                    VARCHAR(120),
    manifest_key                VARCHAR(120) REFERENCES faction_manifests(manifest_key),
    icon                        VARCHAR(120),
    can_leader_join_other       BOOLEAN,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE faction_templates IS 'Faction template definitions (Allies, Axis, Comintern, generic, etc.)';
COMMENT ON COLUMN faction_templates.can_leader_join_other IS 'From can_leader_join_other_factions';

CREATE TABLE faction_template_goals (
    template_key                VARCHAR(120) NOT NULL REFERENCES faction_templates(template_key),
    goal_key                    VARCHAR(120) NOT NULL REFERENCES faction_goals(goal_key),
    PRIMARY KEY (template_key, goal_key)
);

COMMENT ON TABLE faction_template_goals IS 'Junction: goals assigned to each faction template';

CREATE TABLE faction_template_rules (
    template_key                VARCHAR(120) NOT NULL REFERENCES faction_templates(template_key),
    rule_key                    VARCHAR(120) NOT NULL REFERENCES faction_rules(rule_key),
    PRIMARY KEY (template_key, rule_key)
);

COMMENT ON TABLE faction_template_rules IS 'Junction: default rules assigned to each faction template';

CREATE TABLE faction_member_upgrade_groups (
    group_key                   VARCHAR(80) PRIMARY KEY,
    name_loc                    VARCHAR(120),
    description_loc             VARCHAR(120),
    default_upgrade_key         VARCHAR(80),
    upgrade_type                VARCHAR(80),
    icon                        VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE faction_member_upgrade_groups IS 'Groups for faction member upgrades (e.g. manpower contribution tiers)';

CREATE TABLE faction_member_upgrades (
    upgrade_key                 VARCHAR(80) PRIMARY KEY,
    group_key                   VARCHAR(80) REFERENCES faction_member_upgrade_groups(group_key),
    bonus                       NUMERIC(8,4),
    description_loc             VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE faction_member_upgrades IS 'Individual member upgrade tiers within a group';
COMMENT ON COLUMN faction_member_upgrades.bonus IS 'Numeric bonus value applied by this upgrade tier';

-- ============================================================
-- Phase 25 — Special Projects (Götterdämmerung)
-- ============================================================

CREATE TABLE special_project_specializations (
    specialization_key          VARCHAR(40) PRIMARY KEY,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE special_project_specializations IS 'R&D specialization categories (land, naval, air, nuclear)';

CREATE TABLE special_project_tags (
    tag_key                     VARCHAR(40) PRIMARY KEY,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE special_project_tags IS 'Classification tags for grouping special projects (tank, aircraft, etc.)';

CREATE TABLE special_projects (
    project_key                 VARCHAR(120) PRIMARY KEY,
    specialization_key          VARCHAR(40) NOT NULL REFERENCES special_project_specializations(specialization_key),
    project_tag                 VARCHAR(40) REFERENCES special_project_tags(tag_key),
    complexity                  VARCHAR(40),
    prototype_time              VARCHAR(40),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE special_projects IS 'Special R&D projects (flamethrower tanks, jet engines, nuclear bombs, etc.)';
COMMENT ON COLUMN special_projects.complexity IS 'Scripted value reference like sp_complexity.small';
COMMENT ON COLUMN special_projects.prototype_time IS 'Scripted value reference like sp_time.prototype.short';

CREATE TABLE special_project_rewards (
    reward_key                  VARCHAR(120) PRIMARY KEY,
    specialization_key          VARCHAR(40) REFERENCES special_project_specializations(specialization_key),
    fire_only_once              BOOLEAN NOT NULL DEFAULT false,
    threshold_min               INTEGER,
    threshold_max               INTEGER,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE special_project_rewards IS 'Prototype rewards triggered during project iteration';
COMMENT ON COLUMN special_project_rewards.threshold_min IS 'Minimum progress % to trigger';
COMMENT ON COLUMN special_project_rewards.threshold_max IS 'Maximum progress % to trigger';

CREATE TABLE special_project_reward_links (
    project_key                 VARCHAR(120) NOT NULL REFERENCES special_projects(project_key),
    reward_key                  VARCHAR(120) NOT NULL REFERENCES special_project_rewards(reward_key),
    PRIMARY KEY (project_key, reward_key)
);

COMMENT ON TABLE special_project_reward_links IS 'Junction: generic prototype rewards assigned to each project';

-- ============================================================
-- Phase 26 — Collections
-- ============================================================

CREATE TABLE collections (
    collection_key              VARCHAR(120) PRIMARY KEY,
    name_loc                    VARCHAR(120),
    input_source                VARCHAR(120),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE collections IS 'Scripted collection definitions used by faction manifests and triggers';
COMMENT ON COLUMN collections.input_source IS 'From input = game:all_countries, game:scope, collection:X';

-- ============================================================
-- Phase 27 — AI Faction Theaters
-- ============================================================

CREATE TABLE ai_faction_theaters (
    theater_key                 VARCHAR(80) PRIMARY KEY,
    name_loc                    VARCHAR(80),
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE ai_faction_theaters IS 'AI theater definitions for faction military planning';

CREATE TABLE ai_faction_theater_regions (
    theater_key                 VARCHAR(80) NOT NULL REFERENCES ai_faction_theaters(theater_key),
    region_id                   INT NOT NULL REFERENCES strategic_regions(strategic_region_id),
    PRIMARY KEY (theater_key, region_id)
);

COMMENT ON TABLE ai_faction_theater_regions IS 'Junction: strategic regions assigned to each AI theater';

-- ============================================================
-- Phase 28 — Timed Activities
-- ============================================================

CREATE TABLE timed_activities (
    activity_key                VARCHAR(80) PRIMARY KEY,
    source_file                 TEXT NOT NULL,
    dlc_source                  VARCHAR(50)
);

COMMENT ON TABLE timed_activities IS 'Timed activity definitions (e.g. stage_coup)';

CREATE TABLE timed_activity_equipment (
    activity_key                VARCHAR(80) NOT NULL REFERENCES timed_activities(activity_key),
    equipment_key               VARCHAR(120) NOT NULL,
    amount                      INTEGER NOT NULL,
    PRIMARY KEY (activity_key, equipment_key)
);

COMMENT ON TABLE timed_activity_equipment IS 'Equipment requirements for timed activities';

-- ============================================================
-- Deferred FK constraints on existing tables → new parent tables
-- ============================================================

ALTER TABLE provinces
    ADD CONSTRAINT fk_provinces_continent
    FOREIGN KEY (continent_id) REFERENCES continents(continent_id);

ALTER TABLE provinces
    ADD CONSTRAINT fk_provinces_terrain
    FOREIGN KEY (terrain) REFERENCES terrain_types(terrain_type);

ALTER TABLE states
    ADD CONSTRAINT fk_states_category
    FOREIGN KEY (state_category) REFERENCES state_categories(state_category);

-- ============================================================
-- Indexes for new tables (from design doc recommendations)
-- ============================================================

-- Phase 1
CREATE INDEX ix_equipment_definitions_archetype ON equipment_definitions (archetype_key);
CREATE INDEX ix_equipment_resources_equipment ON equipment_resources (equipment_key);

-- Phase 2
CREATE INDEX ix_province_building_positions_province ON province_building_positions (province_id);
CREATE INDEX ix_strategic_region_provinces_province ON strategic_region_provinces (province_id);
CREATE INDEX ix_province_adjacencies_from ON province_adjacencies (from_province_id);
CREATE INDEX ix_province_adjacencies_to ON province_adjacencies (to_province_id);
CREATE INDEX ix_province_railways_from ON province_railways (from_province_id);
CREATE INDEX ix_province_railways_to ON province_railways (to_province_id);

-- Phase 4
CREATE INDEX ix_technology_prerequisites_prereq ON technology_prerequisites (prerequisite_key);
CREATE INDEX ix_technology_enables_equipment_equip ON technology_enables_equipment (equipment_key);

-- Phase 5
CREATE INDEX ix_characters_country ON characters (country_tag);
CREATE INDEX ix_character_roles_character ON character_roles (character_id);

-- Phase 6
CREATE INDEX ix_division_templates_country ON division_templates (country_tag);
CREATE INDEX ix_divisions_country ON divisions (country_tag);
CREATE INDEX ix_divisions_template ON divisions (division_template_id);

-- Phase 7
CREATE INDEX ix_equipment_variants_owner ON equipment_variants (owner_tag);
CREATE INDEX ix_equipment_variant_modules_variant ON equipment_variant_modules (equipment_variant_id);
CREATE INDEX ix_equipment_variant_upgrades_variant ON equipment_variant_upgrades (equipment_variant_id);
CREATE INDEX ix_ships_task_force ON ships (task_force_id);

-- Phase 8
CREATE INDEX ix_air_wings_country ON air_wings (country_tag);

-- Phase 9
CREATE INDEX ix_ideas_slot ON ideas (slot);
CREATE INDEX ix_idea_modifiers_idea ON idea_modifiers (idea_key);
CREATE INDEX ix_country_starting_ideas_country ON country_starting_ideas (country_tag);

-- Phase 10
CREATE INDEX ix_focuses_tree ON focuses (focus_tree_id);
CREATE INDEX ix_focus_prerequisites_focus ON focus_prerequisites (focus_id);

-- Phase 16
CREATE INDEX ix_operations_dlc ON operations (dlc_source);
CREATE INDEX ix_operation_phase_options_group ON operation_phase_options (operation_key, sequence_index);
CREATE INDEX ix_intel_agency_upgrade_levels_upgrade ON intel_agency_upgrade_levels (upgrade_key, level_index);

-- Phase 18
CREATE INDEX ix_mio_organizations_template ON mio_organizations (template_key);
CREATE INDEX ix_mio_traits_owner ON mio_traits (owner_key, owner_type);
CREATE INDEX ix_mio_trait_bonuses_token ON mio_trait_bonuses (trait_token);

-- Phase 19
CREATE INDEX ix_raids_category ON raids (category_key);

-- Phase 20
CREATE INDEX ix_unit_medal_modifiers_medal ON unit_medal_modifiers (medal_key);

-- Phase 21
CREATE INDEX ix_bop_ranges_side ON bop_ranges (bop_key, side_id);
CREATE INDEX ix_bop_range_modifiers_range ON bop_range_modifiers (range_id);
CREATE INDEX ix_continuous_focuses_palette ON continuous_focuses (palette_id);

-- Phase 22
CREATE INDEX ix_dynamic_modifier_effects_modifier ON dynamic_modifier_effects (modifier_key);
CREATE INDEX ix_peace_cost_modifiers_category ON peace_cost_modifiers (category_key);

-- Phase 23
CREATE INDEX ix_doctrine_tracks_folder ON doctrine_tracks (folder_key);
CREATE INDEX ix_grand_doctrines_folder ON grand_doctrines (folder_key);
CREATE INDEX ix_subdoctrines_track ON subdoctrines (track_key);
CREATE INDEX ix_country_starting_doctrines_country ON country_starting_doctrines (country_tag);

-- Phase 24
CREATE INDEX ix_faction_rules_group ON faction_rules (rule_group_key);
CREATE INDEX ix_faction_rules_type ON faction_rules (rule_type);
CREATE INDEX ix_faction_goals_category ON faction_goals (category);
CREATE INDEX ix_faction_templates_manifest ON faction_templates (manifest_key);
CREATE INDEX ix_faction_member_upgrades_group ON faction_member_upgrades (group_key);

-- Phase 25
CREATE INDEX ix_special_projects_specialization ON special_projects (specialization_key);
CREATE INDEX ix_special_projects_tag ON special_projects (project_tag);
CREATE INDEX ix_special_project_rewards_spec ON special_project_rewards (specialization_key);

-- Phase 27
CREATE INDEX ix_ai_faction_theater_regions_region ON ai_faction_theater_regions (region_id);

-- ============================================================
-- Localisation table — English display names for game entities
-- Source: localisation/english/*_l_english.yml (from HOI4 install)
-- Keys map to state_name_key, technology_key, equipment_key, etc.
-- ============================================================
CREATE TABLE localisation (
    loc_key     VARCHAR(250) PRIMARY KEY,
    loc_value   TEXT         NOT NULL,
    source_file TEXT
);
CREATE INDEX ix_localisation_key ON localisation (loc_key);

-- ============================================================
-- User annotation table and index (as per design recommendations)
-- ============================================================
CREATE TABLE user_annotations (
    annotation_id  SERIAL PRIMARY KEY,
    entity_type    VARCHAR(50)  NOT NULL,
    entity_key     VARCHAR(200) NOT NULL,
    note           TEXT         NOT NULL,
    created_at     TIMESTAMPTZ  NOT NULL DEFAULT now()
);
CREATE INDEX ix_user_annotations_entity ON user_annotations (entity_type, entity_key);

-- End of schema definition
COMMIT;