# HOI4 Table Catalog

Status: **COMPLETE** (149 tables across 28 phases + infrastructure)

## How to Read This File
- Each table section includes purpose, source files, columns, keys, and relationship notes.
- Columns marked with `*` are part of the primary key.
- `(existing)` marks tables already in `sql/schema.sql` from Slice A.

---

## Phase 1 — Global Reference Tables

### continents
- **Purpose**: Continent lookup for province assignment
- **Source files**: `map/continent.txt`
- **Grain**: One row per continent
- **Primary key**: `continent_id`
- **Foreign keys**: None
- **Unique constraints**: `continent_key` UNIQUE

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| continent_id* | INT | Yes | Row order (1-based) | PK |
| continent_key | VARCHAR(40) | Yes | Continent name string | UNIQUE |

- **Row count**: 7
- **Relationship notes**: Referenced by `provinces.continent_id`

### terrain_types
- **Purpose**: Full terrain category definitions — combat modifiers, movement costs, attrition, supply penalties
- **Source files**: `common/terrain/00_terrain.txt` → `categories = { }` block
- **Grain**: One row per terrain category
- **Primary key**: `terrain_type`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| terrain_type* | VARCHAR(40) | Yes | Block name | PK, natural key |
| color_r | SMALLINT | No | color[0] | Map display |
| color_g | SMALLINT | No | color[1] | |
| color_b | SMALLINT | No | color[2] | |
| movement_cost | NUMERIC(4,2) | No | movement_cost | 1.0–2.0 |
| combat_width | INT | No | combat_width | 50–80 |
| combat_support_width | INT | No | combat_support_width | 25–40 |
| attrition | NUMERIC(4,2) | No | attrition | 0.0–0.35 |
| is_water | BOOLEAN | No | is_water | yes/no, default no |
| naval_terrain | BOOLEAN | No | naval_terrain | yes/no, default no |
| sound_type | VARCHAR(40) | No | sound_type | sea, forest, plains, desert |
| ai_terrain_importance_factor | NUMERIC(6,2) | No | ai_terrain_importance_factor | 0.1–10.0 |
| match_value | NUMERIC(6,2) | No | match_value | 0.5–10.0 |
| sickness_chance | NUMERIC(4,2) | No | sickness_chance | jungle, marsh |
| naval_mine_hit_chance | NUMERIC(6,2) | No | naval_mine_hit_chance | Water only |
| minimum_seazone_dominance | INT | No | minimum_seazone_dominance | Water only |
| enemy_army_bonus_air_superiority_factor | NUMERIC(4,2) | No | enemy_army_bonus_air_superiority_factor | -0.5 to 0 |
| supply_flow_penalty_factor | NUMERIC(5,3) | No | supply_flow_penalty_factor | -0.2 to 0.16 |
| truck_attrition_factor | NUMERIC(5,2) | No | truck_attrition_factor | 0.2–4.0 |

- **Row count**: 14 (unknown, ocean, lakes, forest, hills, mountain, plains, urban, jungle, marsh, desert, water_fjords, water_shallow_sea, water_deep_ocean)
- **Relationship notes**: Referenced by `provinces.terrain`. Parent of `terrain_building_limits` and `terrain_combat_modifiers`.

### terrain_building_limits
- **Purpose**: Per-terrain maximum building levels (e.g. bunker max 4 in forest, 5 in plains)
- **Source files**: `common/terrain/00_terrain.txt` → `buildings_max_level = { }` within each category
- **Grain**: One row per (terrain_type, building_key)
- **Primary key**: Composite `(terrain_type, building_key)`
- **Foreign keys**: `terrain_type → terrain_types`, `building_key → building_types`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| terrain_type* | VARCHAR(40) | Yes | Parent block name | FK, part of PK |
| building_key* | VARCHAR(80) | Yes | Key inside buildings_max_level | FK, part of PK |
| max_level | INT | Yes | Value | e.g. 4, 5, 6 |

- **Row count**: ~20 (land terrains × {bunker, coastal_bunker})
- **Relationship notes**: Junction between `terrain_types` and `building_types`

### terrain_combat_modifiers
- **Purpose**: Per-terrain combat modifiers for land units and per-ship-type naval penalties
- **Source files**: `common/terrain/00_terrain.txt` → `units = { }` blocks and ship-type blocks within naval terrain
- **Grain**: One row per (terrain, unit_class, modifier_key)
- **Primary key**: `id` (SERIAL)

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | BIGSERIAL | Yes | Auto | PK |
| terrain_type | VARCHAR(40) | Yes | Parent category | FK |
| unit_class | VARCHAR(40) | No | NULL for generic `units`, or ship type (destroyer, submarine, etc.) | |
| modifier_key | VARCHAR(80) | Yes | attack, movement, defence, navy_visibility, etc. | |
| modifier_value | NUMERIC(6,3) | Yes | Value | e.g. -0.15, -0.5 |

- **Row count**: ~50
- **Relationship notes**: Child of `terrain_types`. Land terrain has generic modifiers (unit_class = NULL); naval terrain has per-ship-type modifiers.

### state_categories
- **Purpose**: State economic tier reference — determines factory building slots
- **Source files**: `common/state_category/*.txt` (13 files: wasteland, enclave, tiny_island, small_island, pastoral, rural, town, large_town, city, large_city, large_island, metropolis, megalopolis)
- **Grain**: One row per category
- **Primary key**: `state_category`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| state_category* | VARCHAR(40) | Yes | Block name | PK, natural key |
| local_building_slots | INT | Yes | local_building_slots | 0 (wasteland) to 12 (megalopolis) |
| color_r | SMALLINT | No | color[0] | UI display |
| color_g | SMALLINT | No | color[1] | |
| color_b | SMALLINT | No | color[2] | |

- **Row count**: 13
- **Relationship notes**: Referenced by `states.state_category`

### resource_types (existing)
- **Purpose**: Resource definitions (oil, steel, etc.)
- **Source files**: `common/resources/00_resources.txt`
- **Grain**: One row per resource
- **Primary key**: `resource_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| resource_key* | VARCHAR(40) | Yes | Block name | PK |
| icon_frame | INT | No | icon_frame | UI reference |
| civilian_factory_cost_unit | NUMERIC(8,3) | No | cic | CIC cost per unit |
| convoy_cost_unit | NUMERIC(8,3) | No | convoys | Convoy cost per unit |
| source_file | TEXT | Yes | — | Provenance |

- **Row count**: 7

### building_types (existing)
- **Purpose**: Building type definitions and constraints
- **Source files**: `common/buildings/00_buildings.txt`
- **Grain**: One row per building type
- **Primary key**: `building_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| building_key* | VARCHAR(80) | Yes | Block name | PK |
| base_cost | INT | No | base_cost | IC cost |
| per_level_extra_cost | INT | No | per_level_extra_cost | |
| base_cost_conversion | INT | No | base_cost_conversion | |
| icon_frame | INT | No | icon_frame | |
| show_on_map | INT | No | show_on_map | |
| shares_slots | BOOLEAN | No | shares_slots | |
| state_max | INT | No | max_level (state) | |
| province_max | INT | No | max_level (province) | |
| is_state_level | BOOLEAN | Yes | Derived | |
| is_province_level | BOOLEAN | Yes | Derived | |
| only_coastal | BOOLEAN | No | only_costal | Source typo |
| source_file | TEXT | Yes | — | |
| dlc_source | VARCHAR(50) | No | DLC gate | |

- **Row count**: ~25 distinct building types

### ideologies
- **Purpose**: Top-level ideology reference
- **Source files**: `common/ideologies/00_ideologies.txt`
- **Grain**: One row per ideology
- **Primary key**: `ideology_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| ideology_key* | VARCHAR(40) | Yes | Block name | PK |
| color_r | SMALLINT | Yes | color[0] | |
| color_g | SMALLINT | Yes | color[1] | |
| color_b | SMALLINT | Yes | color[2] | |

- **Row count**: 4 (democratic, communism, fascism, neutrality)

### sub_ideologies
- **Purpose**: Sub-ideology variants
- **Source files**: `common/ideologies/00_ideologies.txt`
- **Grain**: One row per sub-ideology
- **Primary key**: `sub_ideology_key`
- **Foreign keys**: `ideology_key → ideologies`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| sub_ideology_key* | VARCHAR(60) | Yes | types block name | PK |
| ideology_key | VARCHAR(40) | Yes | Parent block | FK |

- **Row count**: ~25 (conservatism, liberalism, socialism, marxism, stalinism, leninism, nazism, fascism_ideology, despotism, oligarchism, etc.)

### technology_categories
- **Purpose**: Tech tree category reference
- **Source files**: `common/technologies/*.txt`
- **Grain**: One row per category
- **Primary key**: `category_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| category_key* | VARCHAR(60) | Yes | Distinct category values | PK |

- **Row count**: ~40

### technologies (existing)
- **Purpose**: Technology definitions
- **Source files**: `common/technologies/*.txt`
- **Grain**: One row per technology
- **Primary key**: `technology_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| technology_key* | VARCHAR(120) | Yes | Block name | PK |
| technology_file | TEXT | Yes | Source filename | |
| start_year | SMALLINT | No | start_year | |
| research_cost | NUMERIC(6,3) | No | research_cost | |
| folder_name | VARCHAR(80) | No | folder | UI tree placement |
| source_file | TEXT | Yes | — | |

- **Row count**: 569

### unit_types
- **Purpose**: Sub-unit (battalion/company) type definitions
- **Source files**: `common/units/*.txt`
- **Grain**: One row per unit type
- **Primary key**: `unit_type_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| unit_type_key* | VARCHAR(80) | Yes | Block name | PK |
| abbreviation | VARCHAR(10) | No | abbreviation | |
| unit_group | VARCHAR(40) | No | group | armor, infantry, etc. |
| combat_width | NUMERIC(5,2) | No | combat_width | |
| max_strength | NUMERIC(8,2) | No | max_strength | |
| max_organisation | NUMERIC(8,2) | No | max_organisation | |
| default_morale | NUMERIC(5,2) | No | default_morale | |
| manpower | INT | No | manpower | |
| training_time | INT | No | training_time | Days |
| suppression | NUMERIC(5,2) | No | suppression | |
| weight | NUMERIC(5,2) | No | weight | |
| supply_consumption | NUMERIC(5,3) | No | supply_consumption | |
| source_file | TEXT | Yes | — | |
| dlc_source | VARCHAR(50) | No | DLC gate | |

- **Row count**: 125

### equipment_definitions
- **Purpose**: Equipment archetypes and concrete variants
- **Source files**: `common/units/equipment/*.txt`
- **Grain**: One row per equipment key (archetype or variant)
- **Primary key**: `equipment_key`
- **Foreign keys**: `archetype_key → equipment_definitions` (self), `parent_key → equipment_definitions` (self)

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| equipment_key* | VARCHAR(120) | Yes | Block name | PK |
| is_archetype | BOOLEAN | Yes | is_archetype = yes | |
| archetype_key | VARCHAR(120) | No | archetype | NULL for archetypes |
| parent_key | VARCHAR(120) | No | parent | Previous in upgrade chain |
| year | SMALLINT | No | year | |
| build_cost_ic | NUMERIC(8,2) | No | build_cost_ic | |
| reliability | NUMERIC(5,2) | No | reliability | |
| maximum_speed | NUMERIC(8,2) | No | maximum_speed | |
| defense | NUMERIC(8,2) | No | defense | |
| breakthrough | NUMERIC(8,2) | No | breakthrough | |
| soft_attack | NUMERIC(8,2) | No | soft_attack | |
| hard_attack | NUMERIC(8,2) | No | hard_attack | |
| ap_attack | NUMERIC(8,2) | No | ap_attack | |
| air_attack | NUMERIC(8,2) | No | air_attack | |
| armor_value | NUMERIC(8,2) | No | armor_value | |
| hardness | NUMERIC(5,2) | No | hardness | |
| is_buildable | BOOLEAN | No | is_buildable | |
| source_file | TEXT | Yes | — | |
| dlc_source | VARCHAR(50) | No | DLC gate | |

- **Row count**: 308
- **Relationship notes**: Self-referential through archetype_key and parent_key. NULL columns in variants inherit from archetype.

### equipment_resources
- **Purpose**: Resource costs per equipment item
- **Source files**: `common/units/equipment/*.txt`, resources block
- **Grain**: One row per (equipment, resource) pair
- **Primary key**: `(equipment_key, resource_key)`
- **Foreign keys**: `equipment_key → equipment_definitions`, `resource_key → resource_types`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| equipment_key* | VARCHAR(120) | Yes | Parent block | FK |
| resource_key* | VARCHAR(40) | Yes | Resource name | FK |
| amount | INT | Yes | Amount value | |
| source_file | TEXT | Yes | — | |

- **Row count**: 454

---

## Phase 2 — Geography

### provinces (existing)
- **Purpose**: Province map data
- **Source files**: `map/definition.csv`
- **Grain**: One row per province
- **Primary key**: `province_id`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| province_id* | INT | Yes | Column 1 | PK |
| map_r | SMALLINT | Yes | Column 2 | RGB color |
| map_g | SMALLINT | Yes | Column 3 | |
| map_b | SMALLINT | Yes | Column 4 | |
| province_kind | VARCHAR(20) | Yes | Column 5 | land/sea/lake |
| is_coastal | BOOLEAN | Yes | Column 6 | |
| terrain | VARCHAR(40) | Yes | Column 7 | forest, hills, etc. |
| continent_id | INT | Yes | Column 8 | |
| source_file | TEXT | Yes | — | |

- **Row count**: 13,382

### province_building_positions
- **Purpose**: 3D placement data for building slots
- **Source files**: `map/buildings.txt`
- **Grain**: One row per building marker position
- **Primary key**: `position_id` (BIGSERIAL)
- **Foreign keys**: `province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| position_id* | BIGSERIAL | Yes | Auto | PK |
| province_id | INT | Yes | Column 1 | FK |
| building_type | VARCHAR(80) | Yes | Column 2 | Building type name |
| pos_x | NUMERIC(10,2) | Yes | Column 3 | |
| pos_y | NUMERIC(10,2) | Yes | Column 4 | |
| pos_z | NUMERIC(10,2) | Yes | Column 5 | |
| rotation | NUMERIC(6,2) | Yes | Column 6 | |
| linked_province_id | INT | No | Column 7 | NULL when 0; naval_base_spawn link |

- **Row count**: 65,659

### strategic_regions
- **Purpose**: Strategic region (air/weather zone) definitions
- **Source files**: `map/strategicregions/*.txt`
- **Grain**: One row per strategic region
- **Primary key**: `strategic_region_id`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| strategic_region_id* | INT | Yes | id | PK |
| name_key | VARCHAR(80) | Yes | name | Localization key |
| source_file | TEXT | Yes | — | |

- **Row count**: 298

### strategic_region_provinces
- **Purpose**: Province membership in strategic regions
- **Source files**: `map/strategicregions/*.txt`, provinces list
- **Grain**: One row per (region, province) pair
- **Primary key**: `(strategic_region_id, province_id)`
- **Foreign keys**: `strategic_region_id → strategic_regions`, `province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| strategic_region_id* | INT | Yes | Parent block | FK |
| province_id* | INT | Yes | Province list entry | FK |

- **Row count**: 13,437

### supply_nodes
- **Purpose**: Supply hub locations
- **Source files**: `map/supply_nodes.txt`
- **Grain**: One row per supply node province
- **Primary key**: `province_id`
- **Foreign keys**: `province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| province_id* | INT | Yes | Column 2 | PK, FK |
| level | INT | Yes | Column 1 | Always 1 in current data |

- **Row count**: 727

### states (existing)
- **Purpose**: State definitions
- **Source files**: `history/states/*.txt`
- **Primary key**: `state_id`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| state_id* | INT | Yes | id | PK |
| state_name_key | VARCHAR(80) | Yes | name | Localization key |
| manpower | BIGINT | No | manpower | |
| state_category | VARCHAR(60) | No | state_category | |
| local_supplies | NUMERIC(8,3) | No | local_supplies | |
| source_file | TEXT | Yes | — | |

- **Row count**: 1,046

### state_provinces (existing)
- **Purpose**: State to province membership
- **Primary key**: `(state_id, province_id)`
- **Row count**: 10,240

### state_resources (existing)
- **Purpose**: Resource deposits by state
- **Primary key**: `state_resource_id` (BIGSERIAL)
- **Row count**: 689

### state_buildings (existing)
- **Purpose**: State-level building instances
- **Primary key**: `state_building_id` (BIGSERIAL)
- **Row count**: 2,641

### province_buildings (existing)
- **Purpose**: Province-level buildings (bunkers, naval bases, etc.)
- **Primary key**: `province_building_id` (BIGSERIAL)
- **Row count**: Varies

### state_victory_points (existing)
- **Purpose**: Victory point assignments per province
- **Primary key**: `state_victory_point_id` (BIGSERIAL)
- **Row count**: 915

---

## Phase 3 — Countries

### countries (existing)
- **Purpose**: Country master record
- **Source files**: `common/country_tags/*.txt`, `common/countries/*.txt`, `history/countries/*.txt`
- **Primary key**: `tag CHAR(3)`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| tag* | CHAR(3) | Yes | Tag from country_tags | PK |
| country_file_path | TEXT | Yes | Path from country_tags | |
| history_file_path | TEXT | No | Derived | |
| graphical_culture | VARCHAR(80) | No | graphical_culture | |
| graphical_culture_2d | VARCHAR(80) | No | graphical_culture_2d | |
| color_r | SMALLINT | No | color[0] | |
| color_g | SMALLINT | No | color[1] | |
| color_b | SMALLINT | No | color[2] | |
| capital_state_id | INT | No | capital | FK → states (deferred) |
| stability | NUMERIC(5,4) | No | set_stability | |
| war_support | NUMERIC(5,4) | No | set_war_support | |
| source_tag_file | TEXT | Yes | — | |
| source_country_file | TEXT | No | — | |
| source_history_file | TEXT | No | — | |

- **Row count**: 352

### state_ownership_history (existing)
- **Row count**: ~1,100

### province_controller_history (existing)
- **Row count**: Varies

### state_cores (existing)
- **Row count**: ~2,000

### country_starting_technologies (existing)
- **Row count**: 11,258

### country_starting_ideas
- **Purpose**: Ideas/spirits active at game start per country
- **Source files**: `history/countries/*.txt`, `add_ideas = { }` blocks
- **Grain**: One row per (country, idea) pair
- **Primary key**: `(country_tag, idea_key, effective_date)`
- **Foreign keys**: `country_tag → countries`, `idea_key → ideas`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| country_tag* | CHAR(3) | Yes | File context | FK |
| idea_key* | VARCHAR(120) | Yes | add_ideas value | FK |
| effective_date* | DATE | Yes | Date context | Default 1936.1.1 |
| source_file | TEXT | Yes | — | |
| dlc_source | VARCHAR(50) | No | DLC gate | |

- **Row count**: ~1,000 estimated

---

## Phase 4 — Technologies (detailed)

### technology_categories_junction
- **Purpose**: M:N link between technologies and categories
- **Source files**: `common/technologies/*.txt`, `categories = { }`
- **Grain**: One row per (tech, category) pair
- **Primary key**: `(technology_key, category_key)`
- **Foreign keys**: `technology_key → technologies`, `category_key → technology_categories`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| technology_key* | VARCHAR(120) | Yes | Tech block | FK |
| category_key* | VARCHAR(60) | Yes | Category value | FK |

- **Row count**: ~800

### technology_prerequisites
- **Purpose**: Directed tech prerequisite graph
- **Source files**: `common/technologies/*.txt`, `leads_to_tech`
- **Grain**: One row per prerequisite link
- **Primary key**: `(technology_key, prerequisite_key)`
- **Foreign keys**: Both → `technologies`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| technology_key* | VARCHAR(120) | Yes | Target tech | FK |
| prerequisite_key* | VARCHAR(120) | Yes | leads_to_tech source | FK |
| source_file | TEXT | Yes | — | |

- **Row count**: 421

### technology_enables_equipment
- **Purpose**: Equipment unlocked by technology
- **Source files**: `common/technologies/*.txt`, `enable_equipments = { }`
- **Grain**: One row per (tech, equipment) pair
- **Primary key**: `(technology_key, equipment_key)`
- **Foreign keys**: `technology_key → technologies`, `equipment_key → equipment_definitions`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| technology_key* | VARCHAR(120) | Yes | Tech block | FK |
| equipment_key* | VARCHAR(120) | Yes | Equipment key | FK |
| source_file | TEXT | Yes | — | |

- **Row count**: ~600

### technology_enables_units
- **Purpose**: Unit types unlocked by technology
- **Source files**: `common/technologies/*.txt`, `enable_subunits = { }`
- **Grain**: One row per (tech, unit_type) pair
- **Primary key**: `(technology_key, unit_type_key)`
- **Foreign keys**: `technology_key → technologies`, `unit_type_key → unit_types`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| technology_key* | VARCHAR(120) | Yes | Tech block | FK |
| unit_type_key* | VARCHAR(80) | Yes | Unit type key | FK |
| source_file | TEXT | Yes | — | |

- **Row count**: ~120

---

## Phase 5 — Characters

### characters
- **Purpose**: Master character record
- **Source files**: `common/characters/*.txt`
- **Grain**: One row per character
- **Primary key**: `character_id`
- **Foreign keys**: `country_tag → countries`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| character_id* | VARCHAR(120) | Yes | Block name | PK |
| name_key | VARCHAR(120) | No | name = X | Localization key |
| country_tag | CHAR(3) | Yes | Derived from filename | FK |
| gender | VARCHAR(10) | No | gender = male/female | |
| portrait_civilian | VARCHAR(200) | No | portraits.civilian.large | |
| portrait_army | VARCHAR(200) | No | portraits.army.large | |
| portrait_navy | VARCHAR(200) | No | portraits.navy.large | |
| source_file | TEXT | Yes | — | |

- **Row count**: 5,160

### character_roles
- **Purpose**: Roles held by characters (one character → many roles)
- **Source files**: `common/characters/*.txt`, role blocks
- **Grain**: One row per character role assignment
- **Primary key**: `character_role_id` (SERIAL)
- **Foreign keys**: `character_id → characters`, `sub_ideology_key → sub_ideologies` (nullable)

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| character_role_id* | SERIAL | Yes | Auto | PK |
| character_id | VARCHAR(120) | Yes | Parent block | FK |
| role_type | VARCHAR(30) | Yes | country_leader/field_marshal/corps_commander/navy_leader/advisor/operative | |
| sub_ideology_key | VARCHAR(60) | No | ideology = X | FK, leader roles only |
| skill | SMALLINT | No | skill | Military roles |
| attack_skill | SMALLINT | No | attack_skill | Army roles |
| defense_skill | SMALLINT | No | defense_skill | Army roles |
| planning_skill | SMALLINT | No | planning_skill | Army roles |
| logistics_skill | SMALLINT | No | logistics_skill | Army roles |
| maneuvering_skill | SMALLINT | No | maneuvering | Admiral roles |
| coordination_skill | SMALLINT | No | coordination | Admiral roles |
| legacy_id | INT | No | legacy_id | Internal ref |
| source_file | TEXT | Yes | — | |
| dlc_source | VARCHAR(50) | No | DLC gate | |

- **Row count**: 5,469

### character_traits
- **Purpose**: Trait definition reference
- **Source files**: `common/country_leader/*.txt`, trait definitions
- **Grain**: One row per trait
- **Primary key**: `trait_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| trait_key* | VARCHAR(80) | Yes | Trait identifier | PK |
| trait_type | VARCHAR(30) | No | Category | personality/command/navy/political |

- **Row count**: ~200

### character_role_traits
- **Purpose**: Traits assigned to character roles
- **Source files**: `common/characters/*.txt`, `traits = { }` within roles
- **Grain**: One row per (role, trait) pair
- **Primary key**: `(character_role_id, trait_key)`
- **Foreign keys**: `character_role_id → character_roles`, `trait_key → character_traits`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| character_role_id* | INT | Yes | Parent role | FK |
| trait_key* | VARCHAR(80) | Yes | Trait ref | FK |

- **Row count**: ~8,000

---

## Phase 6 — Division Templates & OOB

### division_templates
- **Purpose**: Division template definitions (composition blueprints)
- **Source files**: `history/units/*.txt` (land OOB)
- **Grain**: One row per template per OOB file
- **Primary key**: `division_template_id` (SERIAL)
- **Foreign keys**: `country_tag → countries`
- **Unique constraints**: `(country_tag, template_name, oob_file)`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| division_template_id* | SERIAL | Yes | Auto | PK |
| country_tag | CHAR(3) | Yes | OOB context | FK |
| template_name | VARCHAR(120) | Yes | name = "..." | |
| division_names_group | VARCHAR(80) | No | division_names_group | |
| oob_file | VARCHAR(120) | Yes | Source OOB filename | |
| source_file | TEXT | Yes | — | |

- **Row count**: 797

### division_template_regiments
- **Purpose**: Combat battalion grid slots per template
- **Source files**: `history/units/*.txt`, `regiments = { }` block
- **Grain**: One row per (template, grid_x, grid_y)
- **Primary key**: `(division_template_id, grid_x, grid_y)`
- **Foreign keys**: `division_template_id → division_templates`, `unit_type_key → unit_types`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| division_template_id* | INT | Yes | Parent template | FK |
| unit_type_key | VARCHAR(80) | Yes | type = X | FK |
| grid_x* | SMALLINT | Yes | x = N | Column position |
| grid_y* | SMALLINT | Yes | y = N | Row position |

- **Row count**: 4,580

### division_template_support
- **Purpose**: Support company grid slots per template
- **Source files**: `history/units/*.txt`, `support = { }` block
- **Grain**: One row per (template, grid_x, grid_y)
- **Primary key**: `(division_template_id, grid_x, grid_y)`
- **Foreign keys**: `division_template_id → division_templates`, `unit_type_key → unit_types`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| division_template_id* | INT | Yes | Parent template | FK |
| unit_type_key | VARCHAR(80) | Yes | type = X | FK |
| grid_x* | SMALLINT | Yes | x = N | Always 0 |
| grid_y* | SMALLINT | Yes | y = N | Support slot index |

- **Row count**: ~1,200

### divisions
- **Purpose**: Deployed division instances at game start
- **Source files**: `history/units/*.txt`, `units = { division = { } }`
- **Grain**: One row per deployed division
- **Primary key**: `division_id` (SERIAL)
- **Foreign keys**: `country_tag → countries`, `location_province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| division_id* | SERIAL | Yes | Auto | PK |
| country_tag | CHAR(3) | Yes | OOB context | FK |
| division_template_id | INT | No | Resolved by name | FK |
| template_name | VARCHAR(120) | Yes | division_template = "..." | |
| location_province_id | INT | No | location = N | FK |
| start_experience_factor | NUMERIC(4,2) | No | start_experience_factor | |
| oob_file | VARCHAR(120) | Yes | Source OOB filename | |
| source_file | TEXT | Yes | — | |

- **Row count**: 4,991

---

## Phase 7 — Naval OOB

### equipment_variants
- **Purpose**: Named design variants per country
- **Source files**: `history/units/*_naval_*.txt`, `create_equipment_variant`
- **Grain**: One row per (country, hull, version_name)
- **Primary key**: `equipment_variant_id` (SERIAL)
- **Foreign keys**: `owner_tag → countries`, `base_equipment_key → equipment_definitions`
- **Unique constraints**: `(owner_tag, base_equipment_key, version_name)`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| equipment_variant_id* | SERIAL | Yes | Auto | PK |
| owner_tag | CHAR(3) | Yes | Country context | FK |
| base_equipment_key | VARCHAR(120) | Yes | type = ship_hull_* | FK |
| version_name | VARCHAR(120) | Yes | name = "..." | |
| source_file | TEXT | Yes | — | |

- **Row count**: ~500

### fleets
- **Purpose**: Fleet-level naval organization
- **Source files**: `history/units/*_naval_*.txt`
- **Grain**: One row per fleet
- **Primary key**: `fleet_id` (SERIAL)
- **Foreign keys**: `country_tag → countries`, `naval_base_province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| fleet_id* | SERIAL | Yes | Auto | PK |
| country_tag | CHAR(3) | Yes | OOB context | FK |
| fleet_name | VARCHAR(200) | Yes | name = "..." | |
| naval_base_province_id | INT | No | naval_base = N | FK |
| oob_file | VARCHAR(120) | Yes | Source OOB filename | |
| source_file | TEXT | Yes | — | |

- **Row count**: ~100

### task_forces
- **Purpose**: Task force groupings within fleets
- **Source files**: `history/units/*_naval_*.txt`, `task_force = { }`
- **Grain**: One row per task force
- **Primary key**: `task_force_id` (SERIAL)
- **Foreign keys**: `fleet_id → fleets`, `location_province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| task_force_id* | SERIAL | Yes | Auto | PK |
| fleet_id | INT | Yes | Parent fleet | FK |
| task_force_name | VARCHAR(200) | Yes | name = "..." | |
| location_province_id | INT | No | location = N | FK |

- **Row count**: ~300

### ships
- **Purpose**: Individual ship instances
- **Source files**: `history/units/*_naval_*.txt`, `ship = { }`
- **Grain**: One row per ship
- **Primary key**: `ship_id` (SERIAL)
- **Foreign keys**: `task_force_id → task_forces`, `hull_equipment_key → equipment_definitions`, `owner_tag → countries`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| ship_id* | SERIAL | Yes | Auto | PK |
| task_force_id | INT | Yes | Parent TF | FK |
| ship_name | VARCHAR(200) | Yes | name = "..." | |
| definition | VARCHAR(60) | Yes | definition = destroyer/etc | Role type |
| hull_equipment_key | VARCHAR(120) | Yes | equipment.ship_hull_* type | FK |
| version_name | VARCHAR(120) | No | version_name = "..." | Design variant |
| owner_tag | CHAR(3) | Yes | owner = TAG | FK |
| pride_of_the_fleet | BOOLEAN | No | pride_of_the_fleet = yes | Default false |
| start_experience_factor | NUMERIC(4,2) | No | start_experience_factor | |
| source_file | TEXT | Yes | — | |

- **Row count**: ~1,500

---

## Phase 8 — Air OOB

### air_wings
- **Purpose**: Air wing deployments at game start
- **Source files**: `history/units/*_air_*.txt`
- **Grain**: One row per air wing
- **Primary key**: `air_wing_id` (SERIAL)
- **Foreign keys**: `country_tag → countries`, `location_state_id → states`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| air_wing_id* | SERIAL | Yes | Auto | PK |
| country_tag | CHAR(3) | Yes | owner or OOB context | FK |
| location_state_id | INT | Yes | Parent state_id key | FK |
| wing_name | VARCHAR(200) | No | name = "..." | Often absent |
| equipment_type | VARCHAR(120) | Yes | Equipment key | |
| amount | INT | Yes | amount = N | |
| version_name | VARCHAR(120) | No | version_name = "..." | Named variant |
| oob_file | VARCHAR(120) | Yes | Source OOB filename | |
| source_file | TEXT | Yes | — | |

- **Row count**: ~1,000

---

## Phase 9 — Ideas & National Spirits

### ideas
- **Purpose**: Idea/law/national spirit definitions
- **Source files**: `common/ideas/*.txt`
- **Grain**: One row per idea
- **Primary key**: `idea_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| idea_key* | VARCHAR(120) | Yes | Block name | PK |
| slot | VARCHAR(60) | Yes | Parent category block | economy, trade_laws, country, hidden_ideas, etc. |
| is_law | BOOLEAN | Yes | Derived | In a law category (economy, trade_laws, etc.) |
| cost | INT | No | cost | |
| removal_cost | INT | No | removal_cost | -1 = cannot remove |
| is_default | BOOLEAN | No | default = yes | |
| picture | VARCHAR(120) | No | picture | |
| source_file | TEXT | Yes | — | |
| dlc_source | VARCHAR(50) | No | DLC gate | |

- **Row count**: 5,947

### idea_modifiers
- **Purpose**: Modifier key-value pairs per idea
- **Source files**: `common/ideas/*.txt`, `modifier = { }`
- **Grain**: One row per (idea, modifier_key) pair
- **Primary key**: `idea_modifier_id` (BIGSERIAL)
- **Foreign keys**: `idea_key → ideas`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| idea_modifier_id* | BIGSERIAL | Yes | Auto | PK |
| idea_key | VARCHAR(120) | Yes | Parent idea | FK |
| modifier_key | VARCHAR(120) | Yes | Modifier name | e.g., consumer_goods_expected_value |
| modifier_value | NUMERIC(12,4) | Yes | Modifier value | |
| source_file | TEXT | Yes | — | |

- **Row count**: 11,105

---

## Phase 10 — National Focus Trees

### focus_trees
- **Purpose**: Focus tree containers
- **Source files**: `common/national_focus/*.txt`
- **Grain**: One row per focus tree
- **Primary key**: `focus_tree_id`
- **Foreign keys**: `country_tag → countries` (nullable for generic)

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| focus_tree_id* | VARCHAR(120) | Yes | id = X | PK |
| country_tag | CHAR(3) | No | Derived from country context | FK, NULL for generic |
| initial_x | INT | No | x = N | Tree layout offset |
| initial_y | INT | No | y = N | |
| source_file | TEXT | Yes | — | |

- **Row count**: 63

### focuses
- **Purpose**: Individual national focus definitions
- **Source files**: `common/national_focus/*.txt`, `focus = { }`
- **Grain**: One row per focus
- **Primary key**: `focus_id`
- **Foreign keys**: `focus_tree_id → focus_trees`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| focus_id* | VARCHAR(120) | Yes | id = X | PK |
| focus_tree_id | VARCHAR(120) | Yes | Parent tree | FK |
| cost | NUMERIC(5,1) | No | cost | |
| x_pos | INT | No | x | Grid position |
| y_pos | INT | No | y | |
| icon | VARCHAR(200) | No | icon | GFX reference |
| cancel_if_invalid | BOOLEAN | No | cancel_if_invalid | |
| continue_if_invalid | BOOLEAN | No | continue_if_invalid | |
| available_if_capitulated | BOOLEAN | No | available_if_capitulated | |
| source_file | TEXT | Yes | — | |
| dlc_source | VARCHAR(50) | No | DLC gate | |

- **Row count**: 8,498

### focus_prerequisites
- **Purpose**: Prerequisite links with AND/OR grouping
- **Source files**: `common/national_focus/*.txt`, `prerequisite = { focus = X }`
- **Grain**: One row per (focus, group, required_focus) triple
- **Primary key**: `(focus_id, prerequisite_group, required_focus_id)`
- **Foreign keys**: `focus_id → focuses`, `required_focus_id → focuses`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| focus_id* | VARCHAR(120) | Yes | Child focus | FK |
| prerequisite_group* | SMALLINT | Yes | Group index (0-based) | Same group = OR, different = AND |
| required_focus_id* | VARCHAR(120) | Yes | Required parent focus | FK |

- **Row count**: ~7,000 (prerequisite subset of 9,673 total links)

### focus_mutually_exclusive
- **Purpose**: Mutual exclusion pairs between focuses
- **Source files**: `common/national_focus/*.txt`, `mutually_exclusive = { focus = X }`
- **Grain**: One row per exclusion pair (normalized: a_id < b_id)
- **Primary key**: `(focus_a_id, focus_b_id)`
- **Foreign keys**: Both → `focuses`
- **Check constraint**: `focus_a_id < focus_b_id`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| focus_a_id* | VARCHAR(120) | Yes | First focus | FK |
| focus_b_id* | VARCHAR(120) | Yes | Second focus | FK, must be > a_id |

- **Row count**: ~1,300

---

## Phase 11 — Map Connectivity (NEW)

### province_adjacencies
- **Purpose**: Sea crossings, straits, and canals that connect provinces across water
- **Source files**: `map/adjacencies.csv`
- **Grain**: One row per adjacency
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `from_province_id → provinces`, `to_province_id → provinces`, `through_province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | BIGSERIAL | Yes | Auto | PK |
| from_province_id | INT | Yes | From (col 0) | FK |
| to_province_id | INT | Yes | To (col 1) | FK |
| adjacency_type | VARCHAR(20) | Yes | Type (col 2) | sea, land, etc. |
| through_province_id | INT | No | Through (col 3) | Sea zone province, FK |
| start_x | NUMERIC(8,1) | No | start_x (col 4) | -1 = not specified |
| start_y | NUMERIC(8,1) | No | start_y (col 5) | |
| stop_x | NUMERIC(8,1) | No | stop_x (col 6) | |
| stop_y | NUMERIC(8,1) | No | stop_y (col 7) | |
| adjacency_rule_name | VARCHAR(80) | No | adjacency_rule_name (col 8) | PANAMA_CANAL, KIEL_CANAL, SUEZ_CANAL, etc. |
| comment | VARCHAR(200) | No | Comment (col 9) | Human description |

- **Row count**: ~300
- **Relationship notes**: Self-referential on `provinces`. Named rules identify canals and major sea crossings.

### province_railways
- **Purpose**: Railway network connections between provinces (supply infrastructure)
- **Source files**: `map/railways.txt`
- **Grain**: One row per province-to-province rail segment
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `from_province_id → provinces`, `to_province_id → provinces`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | BIGSERIAL | Yes | Auto | PK |
| from_province_id | INT | Yes | Province pair[i] | FK |
| to_province_id | INT | Yes | Province pair[i+1] | FK |
| railway_level | SMALLINT | Yes | First number in line | 1–5 |

- **Row count**: ~5,000+ (each line lists a chain of provinces; expand to edges)
- **Relationship notes**: Railway file format is `level count prov1 prov2 ... provN`, meaning a chain. Each consecutive pair becomes a row.

---

## Phase 12 — Governance (NEW)

### autonomy_states
- **Purpose**: Subject/puppet autonomy levels (puppet, dominion, colony, reichskommissariat, etc.)
- **Source files**: `common/autonomous_states/*.txt` (19 files)
- **Grain**: One row per autonomy level
- **Primary key**: `autonomy_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| autonomy_key* | VARCHAR(80) | Yes | id = autonomy_X | PK |
| is_puppet | BOOLEAN | No | is_puppet | |
| is_default | BOOLEAN | No | default | |
| min_freedom_level | NUMERIC(4,2) | No | min_freedom_level | 0.0–1.0 |
| manpower_influence | NUMERIC(4,2) | No | manpower_influence | 0.0–1.0 |
| dlc_source | VARCHAR(80) | No | Filename prefix or DLC gate | |

- **Row count**: 19
- **Relationship notes**: Parent of `autonomy_state_modifiers`. Could be FK from country relationship data.

### autonomy_state_modifiers
- **Purpose**: Modifier key-value pairs per autonomy level (e.g. `autonomy_manpower_share = 0.9`)
- **Source files**: `common/autonomous_states/*.txt` → `modifier = { }` block
- **Grain**: One row per (autonomy_key, modifier_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `autonomy_key → autonomy_states`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | BIGSERIAL | Yes | Auto | PK |
| autonomy_key | VARCHAR(80) | Yes | Parent block | FK |
| modifier_key | VARCHAR(120) | Yes | Key inside modifier block | |
| modifier_value | NUMERIC(8,4) | Yes | Value | |

- **Row count**: ~150
- **Relationship notes**: Child of `autonomy_states`

### occupation_laws
- **Purpose**: Occupation policies applied to occupied states
- **Source files**: `common/occupation_laws/occupation_laws.txt`
- **Grain**: One row per occupation law
- **Primary key**: `occupation_law_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| occupation_law_key* | VARCHAR(80) | Yes | Block name | PK |
| icon_index | INT | No | icon frame number | |
| sound_effect | VARCHAR(120) | No | sound_effect | |
| gui_order | INT | No | gui_order | Sort order in UI |
| main_fallback_law | BOOLEAN | No | main_fallback_law | Exactly one is true |
| fallback_law_key | VARCHAR(80) | No | fallback_law | FK self-ref |

- **Row count**: ~10
- **Relationship notes**: Self-referential via `fallback_law_key`. Parent of `occupation_law_modifiers`.

### occupation_law_modifiers
- **Purpose**: State modifiers applied when an occupation law is in effect
- **Source files**: `common/occupation_laws/occupation_laws.txt` → `state_modifier = { }` and `suppressed_state_modifier = { }`
- **Grain**: One row per (law, modifier_key, is_suppressed)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `occupation_law_key → occupation_laws`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | BIGSERIAL | Yes | Auto | PK |
| occupation_law_key | VARCHAR(80) | Yes | Parent block | FK |
| modifier_key | VARCHAR(120) | Yes | Key inside state_modifier | |
| modifier_value | NUMERIC(8,4) | Yes | Value | |
| is_suppressed | BOOLEAN | Yes | false = state_modifier, true = suppressed_state_modifier | |

- **Row count**: ~80
- **Relationship notes**: Child of `occupation_laws`

---

## Phase 13 — Country Extensions (NEW)

### country_visual_definitions
- **Purpose**: Graphical culture assignment per country (determines unit sprites, portraits)
- **Source files**: `common/countries/*.txt` (one file per country)
- **Grain**: One row per country
- **Primary key**: `country_tag`
- **Foreign keys**: `country_tag → countries`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| country_tag* | CHAR(3) | Yes | Country context | PK, FK |
| graphical_culture | VARCHAR(80) | Yes | graphical_culture = X | e.g. western_european_gfx |
| graphical_culture_2d | VARCHAR(80) | No | graphical_culture_2d = X | e.g. western_european_2d |

- **Row count**: ~430
- **Relationship notes**: 1:1 with `countries`

### intelligence_agencies
> **SUPERSEDED** — See revised definition in Phase 16 (`intelligence_agencies (REVISED)`) with expanded columns: `default_tag`, `available_tag`, `source_file`, `dlc_source`, and child table `intelligence_agency_names`.

---

## Phase 14 — Bookmarks (NEW)

### bookmarks
- **Purpose**: Game start date scenarios (1936 Gathering Storm, 1939 Blitzkrieg, etc.)
- **Source files**: `common/bookmarks/*.txt`
- **Grain**: One row per bookmark
- **Primary key**: `bookmark_id` (SERIAL)
- **Foreign keys**: `default_country_tag → countries`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| bookmark_id* | SERIAL | Yes | Auto | PK |
| bookmark_name | VARCHAR(120) | Yes | name = "..." | Localization key |
| bookmark_date | DATE | Yes | date = YYYY.M.D | |
| picture_gfx | VARCHAR(120) | No | picture | |
| default_country_tag | CHAR(3) | No | default_country | FK |

- **Row count**: 2
- **Relationship notes**: Parent of `bookmark_countries`

### bookmark_countries
- **Purpose**: Featured countries per bookmark with starting ideology
- **Source files**: `common/bookmarks/*.txt` → country blocks inside bookmark
- **Grain**: One row per (bookmark, country)
- **Primary key**: Composite `(bookmark_id, country_tag)`
- **Foreign keys**: `bookmark_id → bookmarks`, `country_tag → countries`, `ideology_key → ideologies`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| bookmark_id* | INT | Yes | Parent bookmark | FK |
| country_tag* | CHAR(3) | Yes | TAG block name | FK |
| ideology_key | VARCHAR(40) | No | ideology = X | FK |

- **Row count**: ~30
- **Relationship notes**: Junction between `bookmarks` and `countries`

---

## Phase 15 — Decisions (NEW)

### decision_categories
- **Purpose**: Decision category groupings
- **Source files**: `common/decisions/categories/*.txt`
- **Grain**: One row per category
- **Primary key**: `category_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| category_key* | VARCHAR(80) | Yes | Block name | PK |
| icon | VARCHAR(120) | No | icon | GFX key |
| picture_gfx | VARCHAR(120) | No | picture | |
| priority | INT | No | priority | Sort order |

- **Row count**: ~30
- **Relationship notes**: Parent of `decisions`

### decisions
- **Purpose**: Political, diplomatic, and strategic decision definitions
- **Source files**: `common/decisions/*.txt`
- **Grain**: One row per decision
- **Primary key**: `decision_key`
- **Foreign keys**: `category_key → decision_categories`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| decision_key* | VARCHAR(120) | Yes | Block name | PK |
| category_key | VARCHAR(80) | Yes | Parent category block | FK |
| icon | VARCHAR(120) | No | icon | GFX key |
| cost | INT | No | cost | Political power cost |
| fire_only_once | BOOLEAN | No | fire_only_once | |
| dlc_source | VARCHAR(80) | No | DLC gate | |

- **Row count**: ~500+
- **Relationship notes**: Child of `decision_categories`. Scripted triggers/effects stored as text if needed.

---

## Phase 16 — Espionage System (La Résistance)

### operations
- **Purpose**: Espionage operation type definitions — each is a template for a mission operatives can execute against a target country
- **Source files**: `common/operations/*.txt` (6 files: `00_operations.txt`, `LaR_FRA_operations.txt`, `LaR_historical_operations.txt`, `NSB_historical_operations.txt`, `POL_historical_operations.txt`)
- **Grain**: One row per named operation
- **Primary key**: `operation_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| operation_key* | VARCHAR(120) | Yes | Block name (e.g. `operation_rescue_operative`) | PK, natural key |
| name | VARCHAR(120) | No | name | Loc key for display name |
| desc | VARCHAR(120) | No | desc | Loc key for description |
| icon | VARCHAR(120) | No | icon | GFX key |
| map_icon | VARCHAR(120) | No | map_icon | GFX key |
| priority | INT | No | priority | Sort order (0+) |
| days | INT | No | days | Duration in days (35–90+) |
| network_strength | INT | No | network_strength | Required network % (0–100) |
| operatives | INT | No | operatives | Required operative count (0–4) |
| risk_chance | NUMERIC(4,3) | No | risk_chance | 0.0–1.0 |
| experience | INT | No | experience | XP gained on success |
| cost_multiplier | NUMERIC(5,3) | No | cost_multiplier | Scales cost with network (0 = flat) |
| outcome_extra_chance | NUMERIC(4,3) | No | outcome_extra_chance | Chance for bonus outcome (0.0–1.0) |
| prevent_captured_operative_to_die | BOOLEAN | No | prevent_captured_operative_to_die | Default false |
| scale_cost_independent_of_target | BOOLEAN | No | scale_cost_independent_of_target | Default false |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC gate in `visible`/`available` | e.g. "La Resistance" |

- **Row count**: ~36
- **Relationship notes**: Parent of `operation_equipment_requirements`, `operation_phase_groups`. References `operation_tokens` via `awarded_tokens` list.

### operation_awarded_tokens
- **Purpose**: Junction — which `operation_tokens` are awarded on successful completion of each operation
- **Source files**: `common/operations/*.txt` → `awarded_tokens = { }` block
- **Grain**: One row per (operation, token)
- **Primary key**: Composite `(operation_key, token_key)`
- **Foreign keys**: `operation_key → operations`, `token_key → operation_tokens`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| operation_key* | VARCHAR(120) | Yes | Parent operation | FK, part of PK |
| token_key* | VARCHAR(60) | Yes | Token name inside awarded_tokens | FK, part of PK |

- **Row count**: ~20
- **Relationship notes**: M:N junction between operations and operation_tokens

### operation_equipment_requirements
- **Purpose**: Equipment consumed/required to launch an operation
- **Source files**: `common/operations/*.txt` → `equipment = { }` block per operation
- **Grain**: One row per (operation, equipment_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `operation_key → operations`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| operation_key | VARCHAR(120) | Yes | Parent operation | FK |
| equipment_key | VARCHAR(120) | Yes | Equipment type key | Matches `equipment_definitions.equipment_key` where available |
| amount | INT | Yes | Value | Quantity required |

- **Row count**: ~15 (most operations have empty equipment blocks)
- **Relationship notes**: Child of `operations`

### operation_phase_groups
- **Purpose**: Each operation has 1–N sequential phase groups (phases block 1, block 2, block 3...). Each group represents one step in the operation timeline.
- **Source files**: `common/operations/*.txt` → multiple `phases = { }` blocks per operation
- **Grain**: One row per (operation, sequence_index)
- **Primary key**: Composite `(operation_key, sequence_index)`
- **Foreign keys**: `operation_key → operations`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| operation_key* | VARCHAR(120) | Yes | Parent operation | FK, part of PK |
| sequence_index* | SMALLINT | Yes | Ordinal (1-based) of phases block | Part of PK |

- **Row count**: ~100 (avg 3 groups × 36 operations)
- **Relationship notes**: Parent of `operation_phase_options`

### operation_phase_options
- **Purpose**: Within each phase group, the weighted phase choices the game can select from
- **Source files**: `common/operations/*.txt` → entries inside each `phases = { }` block
- **Grain**: One row per (operation, group_index, phase_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `(operation_key, sequence_index) → operation_phase_groups`, `phase_key → operation_phase_definitions`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| operation_key | VARCHAR(120) | Yes | Parent operation | FK |
| sequence_index | SMALLINT | Yes | Which phases block | FK (composite with operation_key) |
| phase_key | VARCHAR(120) | Yes | Phase name (e.g. `infiltration_border`) | FK → operation_phase_definitions |
| base_weight | INT | Yes | base value | Weight for random selection (25, 33, etc.) |

- **Row count**: ~300
- **Relationship notes**: Child of `operation_phase_groups`, references `operation_phase_definitions`

### operation_phase_definitions
- **Purpose**: Reusable operation phase templates — each defines one possible step (infiltrate by border, exfiltrate by submarine, etc.)
- **Source files**: `common/operation_phases/*.txt` (15 files)
- **Grain**: One row per named phase definition
- **Primary key**: `phase_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| phase_key* | VARCHAR(120) | Yes | Block name (e.g. `infiltration_paradrop`) | PK, natural key |
| name | VARCHAR(120) | No | name | Loc key |
| desc | VARCHAR(200) | No | desc | Loc key |
| outcome | VARCHAR(120) | No | outcome | Loc key for outcome text |
| icon | VARCHAR(120) | No | icon | GFX key |
| picture | VARCHAR(120) | No | picture | GFX key for phase image |
| return_on_complete | BOOLEAN | No | return_on_complete | Default false |
| source_file | TEXT | Yes | — | Provenance |

- **Row count**: ~60
- **Relationship notes**: Referenced by `operation_phase_options.phase_key`. May have equipment requirements (see below).

### operation_phase_equipment
- **Purpose**: Equipment consumed by a specific phase definition (e.g. paradrop costs 1 transport_plane_equipment)
- **Source files**: `common/operation_phases/*.txt` → `equipment = { }` block
- **Grain**: One row per (phase, equipment_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `phase_key → operation_phase_definitions`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| phase_key | VARCHAR(120) | Yes | Parent phase | FK |
| equipment_key | VARCHAR(120) | Yes | Equipment type key | e.g. `transport_plane_equipment`, `infantry_equipment` |
| amount | INT | No | amount value | Quantity consumed |
| days | INT | No | days value | Duration of equipment reservation |

- **Row count**: ~10
- **Relationship notes**: Child of `operation_phase_definitions`

### operation_tokens
- **Purpose**: Named tokens representing persistent intelligence infiltration results (e.g. "infiltrated civilian government")
- **Source files**: `common/operation_tokens/00_OperationTokens.txt`
- **Grain**: One row per token
- **Primary key**: `token_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| token_key* | VARCHAR(60) | Yes | Block name (e.g. `token_civilian`) | PK, natural key |
| name | VARCHAR(120) | No | name | Loc key |
| desc | VARCHAR(200) | No | desc | Loc key |
| icon | VARCHAR(120) | No | icon | GFX key |
| text_icon | VARCHAR(120) | No | text_icon | Inline text icon GFX |
| intel_source | VARCHAR(30) | No | intel_source | airforce, army, civilian, navy |
| intel_gain | INT | No | intel_gain | Intel points awarded (5–10) |

- **Row count**: 5
- **Relationship notes**: Referenced by `operation_awarded_tokens`

### intelligence_agencies (REVISED)
- **Purpose**: Default intelligence agency logos and names per country — expanded from existing 4-column table
- **Source files**: `common/intelligence_agencies/00_intelligence_agencies.txt`
- **Grain**: One row per agency definition (multiple can exist per country, e.g. GER has Abwehr + Stasi)
- **Primary key**: `agency_id` (SERIAL)
- **Foreign keys**: `default_tag → countries`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| agency_id* | SERIAL | Yes | Auto | PK |
| picture_gfx | VARCHAR(120) | Yes | picture | GFX sprite key |
| default_tag | CHAR(3) | No | default.tag | Country this is default for, FK |
| available_tag | CHAR(3) | No | available.original_tag | Restricts which country can use |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC gate inside `available`/`default` blocks | e.g. "La Resistance" |

- **Row count**: ~50
- **Relationship notes**: Parent of `intelligence_agency_names`. Child of `countries` via `default_tag`.

### intelligence_agency_names
- **Purpose**: Each agency can have multiple possible display names (randomly chosen at game start)
- **Source files**: `common/intelligence_agencies/00_intelligence_agencies.txt` → `names = { }` list
- **Grain**: One row per (agency, name)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `agency_id → intelligence_agencies`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| agency_id | INT | Yes | Parent agency | FK |
| name | VARCHAR(200) | Yes | Quoted string inside `names = { }` | Display name ("MI6", "SIS") |

- **Row count**: ~60
- **Relationship notes**: Child of `intelligence_agencies`

### intel_agency_upgrade_branches
- **Purpose**: Top-level upgrade branch categories for intelligence agencies (6 branches)
- **Source files**: `common/intelligence_agency_upgrades/intelligence_agency_upgrades.txt`
- **Grain**: One row per branch
- **Primary key**: `branch_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| branch_key* | VARCHAR(60) | Yes | Block name (e.g. `branch_intelligence`, `branch_defense`) | PK, natural key |

- **Row count**: 6 (branch_intelligence, branch_defense, branch_terror, branch_propaganda, branch_operative_training, branch_operative_improvement)
- **Relationship notes**: Parent of `intel_agency_upgrades`

### intel_agency_upgrades
- **Purpose**: Individual upgrade definitions within each branch
- **Source files**: `common/intelligence_agency_upgrades/intelligence_agency_upgrades.txt` → nested blocks
- **Grain**: One row per upgrade
- **Primary key**: `upgrade_key`
- **Foreign keys**: `branch_key → intel_agency_upgrade_branches`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| upgrade_key* | VARCHAR(80) | Yes | Block name (e.g. `upgrade_economy_civilian`) | PK, natural key |
| branch_key | VARCHAR(60) | Yes | Parent branch block | FK |
| picture | VARCHAR(120) | No | picture | GFX key |
| frame | VARCHAR(120) | No | frame | GFX frame reference |
| sound | VARCHAR(120) | No | sound | Sound event key |

- **Row count**: ~20
- **Relationship notes**: Parent of `intel_agency_upgrade_levels` and `intel_agency_upgrade_progress_modifiers`

### intel_agency_upgrade_levels
- **Purpose**: Per-level modifier values for each upgrade (upgrades can have 1–4 levels, each with different modifiers)
- **Source files**: `common/intelligence_agency_upgrades/intelligence_agency_upgrades.txt` → `level = { modifier = { } }` blocks
- **Grain**: One row per (upgrade, level_index, modifier_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `upgrade_key → intel_agency_upgrades`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| upgrade_key | VARCHAR(80) | Yes | Parent upgrade | FK |
| level_index | SMALLINT | Yes | Ordinal of `level` block (1-based) | |
| modifier_key | VARCHAR(80) | Yes | Key inside modifier block | e.g. `civilian_intel_factor`, `intelligence_agency_defense` |
| modifier_value | NUMERIC(8,4) | Yes | Value | e.g. 0.25, 1.5 |

- **Row count**: ~40
- **Relationship notes**: Child of `intel_agency_upgrades`

### intel_agency_upgrade_progress_modifiers
- **Purpose**: Modifiers applied while an upgrade is being constructed (e.g. civilian_factory_use = 5)
- **Source files**: `common/intelligence_agency_upgrades/intelligence_agency_upgrades.txt` → `modifiers_during_progress = { }` block
- **Grain**: One row per (upgrade, modifier_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `upgrade_key → intel_agency_upgrades`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| upgrade_key | VARCHAR(80) | Yes | Parent upgrade | FK |
| modifier_key | VARCHAR(80) | Yes | Key inside modifiers_during_progress | e.g. `civilian_factory_use` |
| modifier_value | NUMERIC(8,4) | Yes | Value | e.g. 5, 8, 10 |

- **Row count**: ~20
- **Relationship notes**: Child of `intel_agency_upgrades`

---

## Phase 17 — Occupation & Resistance (La Résistance)

### compliance_modifiers
- **Purpose**: Compliance threshold milestones — at each threshold, state modifiers activate for the occupier
- **Source files**: `common/resistance_compliance_modifiers/compliance_modifiers.txt`
- **Grain**: One row per threshold level
- **Primary key**: `modifier_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| modifier_key* | VARCHAR(60) | Yes | Block name (e.g. `compliance_15`) | PK, natural key |
| type | VARCHAR(40) | Yes | type | `core_compliance_modifier` |
| icon | VARCHAR(120) | No | icon | GFX sprite:frame ref |
| small_icon | VARCHAR(120) | No | small_icon | Progress bar icon |
| threshold | INT | Yes | threshold | % level (15, 25, 40, 60, 80) |
| margin | INT | No | margin | Hysteresis band (typically 2) |
| dlc_source | VARCHAR(50) | No | DLC gate in `visible` | e.g. "La Resistance" |
| source_file | TEXT | Yes | — | Provenance |

- **Row count**: 5
- **Relationship notes**: Parent of `compliance_modifier_effects`

### compliance_modifier_effects
- **Purpose**: Key-value state modifier pairs for each compliance threshold
- **Source files**: `common/resistance_compliance_modifiers/compliance_modifiers.txt` → `state_modifier = { }` block
- **Grain**: One row per (modifier, key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `modifier_key → compliance_modifiers`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| modifier_key | VARCHAR(60) | Yes | Parent threshold | FK |
| effect_key | VARCHAR(80) | Yes | Key inside state_modifier | e.g. `enemy_operative_detection_chance`, `local_factories` |
| effect_value | NUMERIC(10,4) | Yes | Value | e.g. 0.25, -0.25, 0.005 |

- **Row count**: ~12
- **Relationship notes**: Child of `compliance_modifiers`

### resistance_modifiers
- **Purpose**: Resistance threshold milestones — at each threshold, state modifiers penalise the occupier
- **Source files**: `common/resistance_compliance_modifiers/resistance_modifiers.txt`
- **Grain**: One row per threshold level
- **Primary key**: `modifier_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| modifier_key* | VARCHAR(60) | Yes | Block name (e.g. `resistance_25`) | PK, natural key |
| type | VARCHAR(40) | Yes | type | `state_resistance_modifier` or `core_resistance_modifier` |
| icon | VARCHAR(120) | No | icon | GFX sprite:frame ref |
| small_icon | VARCHAR(120) | No | small_icon | Progress bar icon |
| threshold | INT | Yes | threshold | % level (25, 50, 75, 90) |
| margin | INT | No | margin | Hysteresis band |
| source_file | TEXT | Yes | — | Provenance |

- **Row count**: 4
- **Relationship notes**: Parent of `resistance_modifier_effects`

### resistance_modifier_effects
- **Purpose**: Key-value state modifier pairs for each resistance threshold
- **Source files**: `common/resistance_compliance_modifiers/resistance_modifiers.txt` → `state_modifier = { }` block
- **Grain**: One row per (modifier, key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `modifier_key → resistance_modifiers`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| modifier_key | VARCHAR(60) | Yes | Parent threshold | FK |
| effect_key | VARCHAR(80) | Yes | Key inside state_modifier | e.g. `resistance_garrison_penetration_chance`, `resistance_damage_to_garrison` |
| effect_value | NUMERIC(10,4) | Yes | Value | e.g. 0.5, 1.0, -0.5 |

- **Row count**: ~10
- **Relationship notes**: Child of `resistance_modifiers`

### resistance_activities
- **Purpose**: Resistance action types that occupied states can perform (sabotage factories, etc.)
- **Source files**: `common/resistance_activity/resistance_activity.txt`
- **Grain**: One row per activity type
- **Primary key**: `activity_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| activity_key* | VARCHAR(80) | Yes | Block name (e.g. `sabotage_arms_factory`) | PK, natural key |
| alert_text | VARCHAR(120) | No | alert_text | Loc key for map alert |
| max_amount | INT | No | max_amount | Max simultaneous instances |
| duration | INT | No | duration | Days active |
| source_file | TEXT | Yes | — | Provenance |

- **Row count**: ~15
- **Relationship notes**: Standalone reference table. Weight/effect blocks are scripted logic (not stored).

---

## Phase 18 — Military-Industrial Organizations (Arms Against Tyranny)

### mio_equipment_groups
- **Purpose**: Named equipment group categories used for MIO assignment (e.g. "all light tanks", "all destroyers")
- **Source files**: `common/equipment_groups/mio_equipment_groups.txt`
- **Grain**: One row per group
- **Primary key**: `group_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| group_key* | VARCHAR(80) | Yes | Block name (e.g. `mio_cat_eq_all_light_tank`) | PK, natural key |

- **Row count**: ~30
- **Relationship notes**: Parent of `mio_equipment_group_members`

### mio_equipment_group_members
- **Purpose**: Junction — equipment types belonging to each MIO equipment group
- **Source files**: `common/equipment_groups/mio_equipment_groups.txt` → `equipment_type = { }` list
- **Grain**: One row per (group, equipment_type)
- **Primary key**: Composite `(group_key, equipment_type)`
- **Foreign keys**: `group_key → mio_equipment_groups`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| group_key* | VARCHAR(80) | Yes | Parent group | FK, part of PK |
| equipment_type* | VARCHAR(120) | Yes | Entry in equipment_type list | Equipment chassis/type key |

- **Row count**: ~150
- **Relationship notes**: Child of `mio_equipment_groups`

### mio_templates
- **Purpose**: Generic reusable MIO organization templates (e.g. `generic_tank_organization`, `generic_heavy_tank_organization`)
- **Source files**: `common/military_industrial_organization/organizations/00_generic_organization.txt`
- **Grain**: One row per generic template
- **Primary key**: `template_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| template_key* | VARCHAR(120) | Yes | Block name (e.g. `generic_tank_organization`) | PK, natural key |
| icon | VARCHAR(120) | No | icon | GFX key |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC gate in `allowed` | "Arms Against Tyranny" |

- **Row count**: ~25 generic templates
- **Relationship notes**: Parent of `mio_organizations` (via `include`), `mio_traits`, `mio_organization_equipment_types`

### mio_organizations
- **Purpose**: Country-specific MIO instances — each inherits from a generic template and may add/override traits
- **Source files**: `common/military_industrial_organization/organizations/*.txt` (50+ country files)
- **Grain**: One row per country-specific MIO
- **Primary key**: `organization_key`
- **Foreign keys**: `template_key → mio_templates`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| organization_key* | VARCHAR(120) | Yes | Block name (e.g. `GER_porsche_organization`) | PK, natural key |
| template_key | VARCHAR(120) | No | include | FK to generic template; NULL if standalone |
| icon | VARCHAR(120) | No | icon | GFX key (overrides template icon) |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC gate in `allowed` | |

- **Row count**: ~250
- **Relationship notes**: Child of `mio_templates`. Parent of `mio_traits` (via `add_trait`/`override_trait`), `mio_organization_equipment_types`.

### mio_organization_equipment_types
- **Purpose**: Equipment type categories assigned to each MIO (template or org-level)
- **Source files**: `common/military_industrial_organization/organizations/*.txt` → `equipment_type = { }` list
- **Grain**: One row per (owner, equipment_type)
- **Primary key**: `id` (SERIAL)

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| owner_key | VARCHAR(120) | Yes | Parent template_key or organization_key | References mio_templates or mio_organizations |
| owner_type | VARCHAR(10) | Yes | Derived | 'template' or 'organization' |
| equipment_type | VARCHAR(120) | Yes | Entry in equipment_type list | May be a group key or direct equipment key |

- **Row count**: ~300
- **Relationship notes**: Polymorphic child of `mio_templates` or `mio_organizations`

### mio_initial_traits
- **Purpose**: The starting trait every MIO template begins with (defines the baseline bonuses)
- **Source files**: `common/military_industrial_organization/organizations/*.txt` → `initial_trait = { }` block
- **Grain**: One row per template/org that defines an initial_trait
- **Primary key**: `id` (SERIAL)

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| owner_key | VARCHAR(120) | Yes | Parent template_key or organization_key | |
| owner_type | VARCHAR(10) | Yes | Derived | 'template' or 'organization' |
| name | VARCHAR(120) | No | name | Loc key |

- **Row count**: ~25
- **Relationship notes**: Parent of `mio_trait_bonuses` entries where owner is the initial_trait id

### mio_traits
- **Purpose**: Trait tree nodes within an MIO — each is a selectable upgrade with position, bonuses, and prerequisites
- **Source files**: `common/military_industrial_organization/organizations/*.txt` → `trait = { }`, `add_trait = { }`, `override_trait = { }` blocks
- **Grain**: One row per trait node
- **Primary key**: `trait_token`
- **Foreign keys**: `owner_key → mio_templates` or `mio_organizations`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| trait_token* | VARCHAR(120) | Yes | token | PK, natural key (globally unique) |
| owner_key | VARCHAR(120) | Yes | Parent template or org block | Polymorphic FK |
| owner_type | VARCHAR(10) | Yes | Derived | 'template', 'organization' |
| trait_type | VARCHAR(20) | Yes | Derived | 'trait', 'add_trait', 'override_trait' |
| name | VARCHAR(120) | No | name | Loc key |
| icon | VARCHAR(120) | No | icon | GFX key |
| special_trait_background | BOOLEAN | No | special_trait_background | Default false |
| position_x | INT | No | position.x | Grid column |
| position_y | INT | No | position.y | Grid row |
| relative_position_id | VARCHAR(120) | No | relative_position_id | Token of reference trait for relative placement |

- **Row count**: ~600
- **Relationship notes**: Parent of `mio_trait_bonuses`, `mio_trait_prerequisites`, `mio_trait_exclusions`

### mio_trait_bonuses
- **Purpose**: Bonus key-value pairs per trait — equipment_bonus, production_bonus, or organization_modifier
- **Source files**: `common/military_industrial_organization/organizations/*.txt` → `equipment_bonus`, `production_bonus`, `organization_modifier` blocks inside traits
- **Grain**: One row per (trait, bonus_category, bonus_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `trait_token → mio_traits`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| trait_token | VARCHAR(120) | Yes | Parent trait | FK |
| bonus_category | VARCHAR(30) | Yes | Block name | 'equipment_bonus', 'production_bonus', 'organization_modifier' |
| bonus_key | VARCHAR(80) | Yes | Key inside block | e.g. `armor_value`, `production_capacity_factor`, `reliability` |
| bonus_value | NUMERIC(10,4) | Yes | Value | e.g. -0.05, 0.15 |

- **Row count**: ~1500
- **Relationship notes**: Child of `mio_traits`. Also used for `mio_initial_traits` bonuses (via trait_token = initial trait name).

### mio_trait_prerequisites
- **Purpose**: Parent trait requirements — any_parent and all_parents relationships
- **Source files**: `common/military_industrial_organization/organizations/*.txt` → `any_parent = { }`, `all_parents = { }` blocks
- **Grain**: One row per (trait, required_parent, requirement_type)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `trait_token → mio_traits`, `parent_token → mio_traits`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| trait_token | VARCHAR(120) | Yes | Child trait | FK |
| parent_token | VARCHAR(120) | Yes | Required parent trait | FK |
| requirement_type | VARCHAR(15) | Yes | Derived | 'any_parent' or 'all_parents' |

- **Row count**: ~400
- **Relationship notes**: Self-referencing junction on `mio_traits`

### mio_trait_exclusions
- **Purpose**: Mutually exclusive trait pairs — selecting one bars the other
- **Source files**: `common/military_industrial_organization/organizations/*.txt` → `mutually_exclusive = { }` block
- **Grain**: One row per (trait, excluded_trait), stored in canonical order (trait_a < trait_b)
- **Primary key**: Composite `(trait_token_a, trait_token_b)`
- **Foreign keys**: Both → `mio_traits`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| trait_token_a* | VARCHAR(120) | Yes | First trait (alphabetically) | FK, part of PK |
| trait_token_b* | VARCHAR(120) | Yes | Second trait | FK, part of PK |

- **Row count**: ~100
- **Relationship notes**: Symmetric M:N exclusion on `mio_traits`

### mio_policies
- **Purpose**: MIO policy definitions — global bonuses a player can assign to an MIO at sufficient size
- **Source files**: `common/military_industrial_organization/policies/_general_policies.txt`, `_land_policies.txt`, `_navy_policies.txt`, `_air_policies.txt`
- **Grain**: One row per policy
- **Primary key**: `policy_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| policy_key* | VARCHAR(120) | Yes | Block name (e.g. `mio_policy_general_ruthless_contracts`) | PK, natural key |
| icon | VARCHAR(120) | No | icon | GFX key |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC gate in `allowed` | |

- **Row count**: ~25
- **Relationship notes**: Parent of `mio_policy_bonuses`

### mio_policy_bonuses
- **Purpose**: Modifier key-value pairs per policy — organization_modifier, production_bonus, equipment_bonus
- **Source files**: `common/military_industrial_organization/policies/*.txt` → `organization_modifier`, `production_bonus`, `equipment_bonus` blocks
- **Grain**: One row per (policy, category, key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `policy_key → mio_policies`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| policy_key | VARCHAR(120) | Yes | Parent policy | FK |
| bonus_category | VARCHAR(30) | Yes | Block name | 'organization_modifier', 'production_bonus', 'equipment_bonus' |
| bonus_key | VARCHAR(80) | Yes | Key inside block | e.g. `military_industrial_organization_funds_gain`, `production_efficiency_cap_factor` |
| bonus_value | NUMERIC(10,4) | Yes | Value | |

- **Row count**: ~60
- **Relationship notes**: Child of `mio_policies`

---

## Phase 19 — Raids System (Götterdämmerung / No Compromise, No Surrender)

### raid_categories
- **Purpose**: Top-level raid category groupings (air, paratrooper, nuclear, land infiltration)
- **Source files**: `common/raids/categories/raid_categories.txt`
- **Grain**: One row per category
- **Primary key**: `category_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| category_key* | VARCHAR(60) | Yes | Block name (e.g. `air_raids`) | PK, natural key |
| intel_source | VARCHAR(30) | No | intel_source | air, army |
| faction_influence_score_on_success | INT | No | faction_influence_score_on_success | Can be negative (nuclear) |
| free_targeting | BOOLEAN | No | free_targeting | Default false |
| dlc_source | VARCHAR(50) | No | DLC gate in `visible` | e.g. "Gotterdammerung", "No Compromise, No Surrender" |

- **Row count**: 4
- **Relationship notes**: Parent of `raids`

### raids
- **Purpose**: Individual raid type definitions — each is a mission template players can plan and execute
- **Source files**: `common/raids/*.txt` (6 files: `air_raids.txt`, `air_raids_custom.txt`, `nuclear_raids.txt`, `paratrooper_raids.txt`, `paratrooper_raids_custom.txt`, `land_infiltration_custom.txt`)
- **Grain**: One row per named raid type
- **Primary key**: `raid_key`
- **Foreign keys**: `category_key → raid_categories`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| raid_key* | VARCHAR(80) | Yes | Block name (e.g. `facility_strike`) | PK, natural key |
| category_key | VARCHAR(60) | Yes | category | FK |
| days_to_prepare | INT | No | days_to_prepare | Days before launch (30–90) |
| command_power | INT | No | command_power | CP cost to initiate |
| target_icon | VARCHAR(120) | No | target_icon | GFX key |
| launch_sound | VARCHAR(80) | No | launch_sound | Audio event key |
| custom_map_icon | VARCHAR(120) | No | custom_map_icon | GFX key |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC gate in `allowed` | e.g. "Gotterdammerung" |

- **Row count**: ~15
- **Relationship notes**: Parent of `raid_equipment_requirements`

### raid_equipment_requirements
- **Purpose**: Equipment needed to execute a raid — each raid can have multiple `unit_requirements` blocks (alternative fulfilment paths)
- **Source files**: `common/raids/*.txt` → `unit_requirements = { equipment = { } }` blocks
- **Grain**: One row per (raid, requirement_group, equipment_type)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `raid_key → raids`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| raid_key | VARCHAR(80) | Yes | Parent raid | FK |
| requirement_group | SMALLINT | Yes | Ordinal of unit_requirements block (1-based) | Alternative groups: satisfy ANY one group |
| equipment_type | VARCHAR(120) | Yes | type entry | e.g. `tactical_bomber`, `strategic_bomber`, `paratroopers` |
| amount_min | INT | No | amount.min | Minimum required |
| amount_max | INT | No | amount.max | Maximum usable |

- **Row count**: ~40
- **Relationship notes**: Child of `raids`

---

## Phase 20 — Career Profile (By Blood Alone / Götterdämmerung)

### medals
- **Purpose**: Career profile medal definitions — awarded based on cumulative stats across game sessions
- **Source files**: `common/medals/00_medals.txt`
- **Grain**: One row per medal
- **Primary key**: `medal_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| medal_key* | VARCHAR(80) | Yes | Block name (e.g. `stalwart_defender_medal`) | PK, natural key |
| name | VARCHAR(120) | Yes | name | Loc key |
| description | VARCHAR(120) | No | description | Loc key |
| frame_1 | SMALLINT | No | frames[0] | Sprite layer 1 frame |
| frame_2 | SMALLINT | No | frames[1] | Sprite layer 2 frame |
| frame_3 | SMALLINT | No | frames[2] | Sprite layer 3 frame |
| tracked_variable | VARCHAR(80) | No | debug entry | Stat variable name |
| dlc_source | VARCHAR(50) | No | — | "By Blood Alone" |

- **Row count**: ~15
- **Relationship notes**: Parent of `medal_tiers`, `medal_layer_colors`

### medal_tiers
- **Purpose**: Bronze/silver/gold threshold values per medal — the stat value needed to achieve each tier
- **Source files**: `common/medals/00_medals.txt` → `bronze`, `silver`, `gold` blocks → `career_profile_check_value`
- **Grain**: One row per (medal, tier)
- **Primary key**: Composite `(medal_key, tier)`
- **Foreign keys**: `medal_key → medals`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| medal_key* | VARCHAR(80) | Yes | Parent medal | FK, part of PK |
| tier* | VARCHAR(10) | Yes | 'bronze', 'silver', or 'gold' | Part of PK |
| variable | VARCHAR(80) | Yes | var | Stat variable to check (matches `debug`) |
| threshold_value | INT | Yes | value | Stat value required |
| compare | VARCHAR(40) | No | compare | e.g. `greater_than_or_equals` |

- **Row count**: ~45 (15 medals × 3 tiers)
- **Relationship notes**: Child of `medals`

### ribbons
- **Purpose**: Career profile ribbon definitions — awarded for specific in-game achievements per session
- **Source files**: `common/ribbons/00_ribbons.txt`
- **Grain**: One row per ribbon
- **Primary key**: `ribbon_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| ribbon_key* | VARCHAR(80) | Yes | Block name (e.g. `offense_is_the_best_defense`) | PK, natural key |
| name | VARCHAR(120) | Yes | name | Loc key |
| description | VARCHAR(120) | No | description | Loc key |
| quote_text | VARCHAR(120) | No | quote_text | Loc key |
| happened_trigger | TEXT | No | happened block | Scripted trigger (stored as raw text) |
| dlc_source | VARCHAR(50) | No | — | "By Blood Alone" |

- **Row count**: ~20
- **Relationship notes**: Standalone. Frames/colors are UI presentation (could be stored but are purely cosmetic arrays).

### ace_modifiers
- **Purpose**: Ace pilot modifier profiles — base bonuses for aces assigned to equipment types
- **Source files**: `common/aces/00_aces.txt` → `modifiers = { }` block
- **Grain**: One row per named ace modifier profile
- **Primary key**: `modifier_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| modifier_key* | VARCHAR(60) | Yes | Block name (e.g. `fighter_good`) | PK, natural key |
| chance | NUMERIC(4,3) | Yes | chance | Probability weight (0.05–0.9) |

- **Row count**: 9 (fighter_good/unique/genius, bomber_good/unique/genius, support_good/unique/genius)
- **Relationship notes**: Parent of `ace_modifier_effects`, `ace_modifier_equipment_types`

### ace_modifier_effects
- **Purpose**: Key-value stat bonuses per ace modifier profile
- **Source files**: `common/aces/00_aces.txt` → `effect = { }` block per modifier
- **Grain**: One row per (modifier, effect_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `modifier_key → ace_modifiers`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| modifier_key | VARCHAR(60) | Yes | Parent ace modifier | FK |
| effect_key | VARCHAR(80) | Yes | Key inside effect block | e.g. `air_attack_factor`, `air_agility_factor` |
| effect_value | NUMERIC(8,4) | Yes | Value | e.g. 0.03, 0.15 |

- **Row count**: ~25
- **Relationship notes**: Child of `ace_modifiers`

### ace_modifier_equipment_types
- **Purpose**: Junction — which equipment types each ace modifier applies to
- **Source files**: `common/aces/00_aces.txt` → `type = { }` list per modifier
- **Grain**: One row per (modifier, equipment_type)
- **Primary key**: Composite `(modifier_key, equipment_type)`
- **Foreign keys**: `modifier_key → ace_modifiers`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| modifier_key* | VARCHAR(60) | Yes | Parent ace modifier | FK, part of PK |
| equipment_type* | VARCHAR(60) | Yes | Entry in type list | e.g. `fighter`, `heavy_fighter`, `strategic_bomber` |

- **Row count**: ~15
- **Relationship notes**: Child of `ace_modifiers`

### unit_medals
- **Purpose**: Divisional medal definitions — purchasable decorations that grant unit modifier bonuses (Götterdämmerung DLC)
- **Source files**: `common/unit_medals/00_default.txt` → `unit_medals = { }` block
- **Grain**: One row per unit medal
- **Primary key**: `medal_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| medal_key* | VARCHAR(80) | Yes | Block name (e.g. `krigskorset`) | PK, natural key |
| frame | INT | No | frame | Sprite frame number |
| icon | VARCHAR(120) | No | icon | GFX key |
| cost | INT | No | cost | Command power cost (typically 30) |
| dlc_source | VARCHAR(50) | No | — | "Gotterdammerung" |

- **Row count**: ~100 (6+ medals per country × many countries)
- **Relationship notes**: Parent of `unit_medal_modifiers`

### unit_medal_modifiers
- **Purpose**: Key-value unit modifier pairs per divisional medal
- **Source files**: `common/unit_medals/00_default.txt` → `unit_modifiers = { }` block
- **Grain**: One row per (medal, modifier_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `medal_key → unit_medals`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| medal_key | VARCHAR(80) | Yes | Parent medal | FK |
| modifier_key | VARCHAR(80) | Yes | Key inside unit_modifiers | e.g. `army_morale_factor`, `experience_loss_factor` |
| modifier_value | NUMERIC(8,4) | Yes | Value | e.g. 0.1, -0.07 |

- **Row count**: ~200
- **Relationship notes**: Child of `unit_medals`

---

## Phase 21 — Balance of Power & Continuous Focuses

### balance_of_power_definitions
- **Purpose**: Balance of Power (BOP) instance definitions — each represents a political/social tug-of-war for a specific country
- **Source files**: `common/bop/*.txt` (8 files: BRA, DEN, ETH, FIN, ITA, PRC, SWE, SWI)
- **Grain**: One row per BOP instance
- **Primary key**: `bop_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| bop_key* | VARCHAR(80) | Yes | Block name (e.g. `BRA_political_military_balance`) | PK, natural key |
| initial_value | NUMERIC(5,3) | No | initial_value | Starting position (-1.0 to 1.0) |
| left_side | VARCHAR(80) | No | left_side | Side ID string |
| right_side | VARCHAR(80) | No | right_side | Side ID string |
| decision_category | VARCHAR(80) | No | decision_category | FK-like ref to decision_categories |
| source_file | TEXT | Yes | — | Provenance |

- **Row count**: ~8
- **Relationship notes**: Parent of `bop_sides`

### bop_sides
- **Purpose**: The two sides of each BOP — left and right, each with an icon and nested ranges
- **Source files**: `common/bop/*.txt` → `side = { }` blocks plus the neutral `range` at root
- **Grain**: One row per (bop, side_id)
- **Primary key**: Composite `(bop_key, side_id)`
- **Foreign keys**: `bop_key → balance_of_power_definitions`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| bop_key* | VARCHAR(80) | Yes | Parent BOP | FK, part of PK |
| side_id* | VARCHAR(80) | Yes | id inside side block (e.g. `BRA_bop_left_side`) | Part of PK |
| side_position | VARCHAR(10) | Yes | Derived | 'left', 'right', or 'neutral' |
| icon | VARCHAR(120) | No | icon | GFX key |

- **Row count**: ~24 (8 BOPs × ~3 sides incl. neutral)
- **Relationship notes**: Parent of `bop_ranges`

### bop_ranges
- **Purpose**: Value ranges within each BOP side — each range activates at a min/max threshold and applies modifiers
- **Source files**: `common/bop/*.txt` → `range = { }` blocks inside each `side` or at root
- **Grain**: One row per (bop, side, range_id)
- **Primary key**: `range_id`
- **Foreign keys**: `(bop_key, side_id) → bop_sides`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| range_id* | VARCHAR(80) | Yes | id (e.g. `BRA_independent_civilian_government`) | PK, natural key |
| bop_key | VARCHAR(80) | Yes | Parent BOP | FK |
| side_id | VARCHAR(80) | Yes | Parent side | FK (composite with bop_key) |
| min_value | NUMERIC(5,3) | Yes | min | -1.0 to 1.0 |
| max_value | NUMERIC(5,3) | Yes | max | -1.0 to 1.0 |

- **Row count**: ~50
- **Relationship notes**: Parent of `bop_range_modifiers`

### bop_range_modifiers
- **Purpose**: Key-value modifier pairs activated when a BOP is within a specific range
- **Source files**: `common/bop/*.txt` → `modifier = { }` block inside each range
- **Grain**: One row per (range, modifier_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `range_id → bop_ranges`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| range_id | VARCHAR(80) | Yes | Parent range | FK |
| modifier_key | VARCHAR(80) | Yes | Key inside modifier block | e.g. `stability_factor`, `political_power_factor` |
| modifier_value | NUMERIC(10,4) | Yes | Value | e.g. 0.15, -0.2 |

- **Row count**: ~200
- **Relationship notes**: Child of `bop_ranges`

### continuous_focus_palettes
- **Purpose**: Container for continuous focus groupings — each palette is scoped to specific countries via trigger
- **Source files**: `common/continuous_focus/*.txt`
- **Grain**: One row per palette
- **Primary key**: `palette_id`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| palette_id* | VARCHAR(80) | Yes | id (e.g. `generic_focus`) | PK, natural key |
| is_default | BOOLEAN | No | default | yes/no |
| reset_on_civilwar | BOOLEAN | No | reset_on_civilwar | |
| position_x | INT | No | position.x | UI x coordinate |
| position_y | INT | No | position.y | UI y coordinate |
| source_file | TEXT | Yes | — | Provenance |

- **Row count**: ~5
- **Relationship notes**: Parent of `continuous_focuses`

### continuous_focuses
- **Purpose**: Individual continuous focus definitions — ongoing bonuses that cost daily political power
- **Source files**: `common/continuous_focus/*.txt` → `focus = { }` blocks inside palette
- **Grain**: One row per focus
- **Primary key**: `focus_id`
- **Foreign keys**: `palette_id → continuous_focus_palettes`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| focus_id* | VARCHAR(120) | Yes | id (e.g. `DEN_undermine_overlord_continuous_focus`) | PK, natural key |
| palette_id | VARCHAR(80) | Yes | Parent palette | FK |
| icon | VARCHAR(120) | No | icon | GFX key |
| daily_cost | INT | No | daily_cost | PP per day (typically 1) |
| available_if_capitulated | BOOLEAN | No | available_if_capitulated | Default false |
| dlc_source | VARCHAR(50) | No | DLC gate in `available` | e.g. "Arms Against Tyranny", "By Blood Alone" |

- **Row count**: ~30
- **Relationship notes**: Parent of `continuous_focus_modifiers`

### continuous_focus_modifiers
- **Purpose**: Key-value modifier pairs per continuous focus
- **Source files**: `common/continuous_focus/*.txt` → `modifier = { }` block inside each focus
- **Grain**: One row per (focus, modifier_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `focus_id → continuous_focuses`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| focus_id | VARCHAR(120) | Yes | Parent focus | FK |
| modifier_key | VARCHAR(80) | Yes | Key inside modifier block | e.g. `power_balance_weekly`, `compliance_growth_on_our_occupied_states` |
| modifier_value | NUMERIC(10,4) | Yes | Value | |

- **Row count**: ~40
- **Relationship notes**: Child of `continuous_focuses`

---

## Phase 22 — Miscellaneous DLC Systems

### technology_sharing_groups
- **Purpose**: Research sharing group definitions — countries in the same faction share a tech bonus
- **Source files**: `common/technology_sharing/*.txt` (10 files)
- **Grain**: One row per sharing group
- **Primary key**: `group_id`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| group_id* | VARCHAR(80) | Yes | id (e.g. `commonwealth_research`) | PK, natural key |
| name | VARCHAR(120) | No | name | Loc key |
| desc | VARCHAR(200) | No | desc | Loc key |
| picture | VARCHAR(120) | No | picture | GFX key |
| research_sharing_per_country_bonus | NUMERIC(5,3) | No | research_sharing_per_country_bonus | 0.05–0.15 |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | Derived from source file name | e.g. "Together for Victory", "Death or Dishonor" |

- **Row count**: ~15
- **Relationship notes**: Standalone reference. Availability triggers are scripted (not stored).

### dynamic_modifiers
- **Purpose**: Named modifier templates that can be added/removed at runtime via script effects — contain arbitrary modifier key-value pairs
- **Source files**: `common/dynamic_modifiers/*.txt` (8 files)
- **Grain**: One row per modifier definition
- **Primary key**: `modifier_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| modifier_key* | VARCHAR(120) | Yes | Block name (e.g. `sabotaged_resources`) | PK, natural key |
| icon | VARCHAR(120) | No | icon | GFX key |
| attacker_modifier | BOOLEAN | No | attacker_modifier | Default false; if yes, applies in combat |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | Derived from source file name | |

- **Row count**: ~80
- **Relationship notes**: Parent of `dynamic_modifier_effects`

### dynamic_modifier_effects
- **Purpose**: Key-value modifier pairs within each dynamic modifier definition
- **Source files**: `common/dynamic_modifiers/*.txt` → plain key = value lines (non-structural)
- **Grain**: One row per (modifier, effect_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `modifier_key → dynamic_modifiers`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| modifier_key | VARCHAR(120) | Yes | Parent modifier | FK |
| effect_key | VARCHAR(120) | Yes | Modifier key name | e.g. `temporary_state_resource_oil`, `recruitable_population_factor` |
| effect_value_static | NUMERIC(10,4) | No | Static numeric value | NULL if value is a variable reference |
| effect_value_variable | VARCHAR(80) | No | Variable name | e.g. `sabotaged_oil`; NULL if static |

- **Row count**: ~250
- **Relationship notes**: Child of `dynamic_modifiers`. Values can be either static numbers or variable references.

### scientist_traits
- **Purpose**: Scientist trait definitions — modifiers for special project research speed (Götterdämmerung DLC)
- **Source files**: `common/scientist_traits/00_traits.txt`
- **Grain**: One row per trait
- **Primary key**: `trait_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| trait_key* | VARCHAR(80) | Yes | Block name (e.g. `scientist_trait_genius`) | PK, natural key |
| icon | VARCHAR(120) | No | icon | GFX key |
| dlc_source | VARCHAR(50) | No | — | "Gotterdammerung" |

- **Row count**: 7
- **Relationship notes**: Parent of `scientist_trait_modifiers`

### scientist_trait_modifiers
- **Purpose**: Key-value modifier pairs per scientist trait
- **Source files**: `common/scientist_traits/00_traits.txt` → `modifier = { }` block
- **Grain**: One row per (trait, modifier_key)
- **Primary key**: `id` (SERIAL)
- **Foreign keys**: `trait_key → scientist_traits`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| id* | SERIAL | Yes | Auto | PK |
| trait_key | VARCHAR(80) | Yes | Parent trait | FK |
| modifier_key | VARCHAR(80) | Yes | Key inside modifier block | e.g. `special_project_speed_factor`, `scientist_xp_gain_factor` |
| modifier_value | NUMERIC(8,4) | Yes | Value | e.g. 0.1, -0.1 |

- **Row count**: ~15
- **Relationship notes**: Child of `scientist_traits`

### peace_action_categories
- **Purpose**: Peace conference cost modifier groupings — categorise why a peace action is cheaper/more expensive
- **Source files**: `common/peace_conference/categories/00_peace_action_categories.txt`
- **Grain**: One row per category
- **Primary key**: `category_key`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| category_key* | VARCHAR(60) | Yes | Block name (e.g. `occupation`, `is_core`) | PK, natural key |
| name | VARCHAR(120) | No | name | Loc key |
| is_default | BOOLEAN | No | default | Only one category is default |

- **Row count**: 11
- **Relationship notes**: Parent of `peace_cost_modifiers`. DLC: By Blood Alone overhaul.

### peace_cost_modifiers
- **Purpose**: Scripted cost multipliers for peace actions — each rule adjusts the cost of taking/puppeting/liberating states
- **Source files**: `common/peace_conference/cost_modifiers/*.txt` (17 files)
- **Grain**: One row per named cost modifier rule
- **Primary key**: `modifier_key`
- **Foreign keys**: `category_key → peace_action_categories`

| Column | Type | Required | Source field | Notes |
|---|---|---|---|---|
| modifier_key* | VARCHAR(120) | Yes | Block name (e.g. `generic_is_core`) | PK, natural key |
| category_key | VARCHAR(60) | Yes | category | FK |
| peace_action_type | VARCHAR(200) | No | peace_action_type | Comma-separated list: `take_states`, `puppet`, `liberate`, `force_government` |
| cost_multiplier | NUMERIC(6,3) | No | cost_multiplier | Multiplicative factor (0.25 = 75% reduction) |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC gate | "By Blood Alone" |

- **Row count**: ~80
- **Relationship notes**: Child of `peace_action_categories`. Enable triggers are scripted (not stored).

---

## Phase 23 — Doctrines (Officer Corps / Military Experience)

Doctrines are unlocked via military experience (Army/Navy/Air XP) through the Officer Corps, NOT through research slots. Each branch (land, naval, air) has a doctrine folder containing mutually-exclusive grand doctrines, which each define tracks of subdoctrines.

### doctrine_folders

Top-level doctrine categories: land, naval, air.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| folder_key | VARCHAR(20) | Yes (PK) | block key | `land`, `naval`, `air` |
| name_loc | VARCHAR(80) | No | name | Localisation key |
| ledger | VARCHAR(10) | Yes | ledger | `army`, `navy`, `air` |
| xp_type | VARCHAR(10) | Yes | — | XP currency (mirrors ledger) |

- **Source**: `common/doctrines/folders/doctrine_folders.txt`
- **Row count**: 3
- **Relationship notes**: Parent of `doctrine_tracks` and `grand_doctrines`.

### doctrine_tracks

Tracks within a doctrine folder (e.g. infantry, armor, operations for land).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| track_key | VARCHAR(40) | Yes (PK) | block key | e.g. `infantry`, `armor`, `capital_ships` |
| folder_key | VARCHAR(20) | Yes (FK) | filename | Derived from filename prefix |
| name_loc | VARCHAR(80) | No | name | Localisation key |
| mastery_multiplier | NUMERIC(6,2) | No | mastery.multiplier | Mastery XP scaling factor |

- **Source**: `common/doctrines/tracks/*.txt`
- **Row count**: 12 (4 land + 4 naval + 4 air)
- **Relationship notes**: FK → `doctrine_folders`. Parent of `grand_doctrine_tracks` and `subdoctrines`.

### grand_doctrines

Mutually-exclusive grand doctrines within a folder (e.g. Mobile Warfare, Superior Firepower).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| doctrine_key | VARCHAR(60) | Yes (PK) | block key | e.g. `new_mobile_warfare` |
| folder_key | VARCHAR(20) | Yes (FK) | folder | `land`, `naval`, `air` |
| name_loc | VARCHAR(80) | No | name | Localisation key |
| xp_cost | INTEGER | Yes | xp_cost | Always 100 in base game |
| xp_type | VARCHAR(10) | Yes | xp_type | `army`, `navy`, `air` |
| source_file | TEXT | Yes | — | Provenance |

- **Source**: `common/doctrines/grand_doctrines/*.txt`
- **Row count**: 10 (4 land + 3 naval + 3 air)
- **Relationship notes**: FK → `doctrine_folders`. Parent of `grand_doctrine_tracks`.

### grand_doctrine_tracks

Junction table: which tracks belong to each grand doctrine.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| doctrine_key | VARCHAR(60) | Yes (PK, FK) | parent block | Grand doctrine key |
| track_key | VARCHAR(40) | Yes (PK, FK) | tracks list | Track key |
| ordinal | SMALLINT | Yes | list order | Position in the tracks list |

- **Source**: `common/doctrines/grand_doctrines/*.txt` (tracks block)
- **Row count**: 40
- **Relationship notes**: FK → `grand_doctrines`, `doctrine_tracks`.

### subdoctrines

Subdoctrines slotted into tracks; unlocked with military XP.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| subdoctrine_key | VARCHAR(80) | Yes (PK) | block key | e.g. `mobile_infantry` |
| track_key | VARCHAR(40) | Yes (FK) | track | Assigned track |
| name_loc | VARCHAR(80) | No | name | Localisation key |
| xp_cost | INTEGER | Yes | xp_cost | Always 100 in base game |
| xp_type | VARCHAR(10) | Yes | xp_type | `army`, `navy`, `air` |
| reward_count | SMALLINT | Yes | rewards block | Number of mastery reward tiers |
| source_file | TEXT | Yes | — | Provenance |

- **Source**: `common/doctrines/subdoctrines/**/*.txt`
- **Row count**: ~86
- **Relationship notes**: FK → `doctrine_tracks`.

### country_starting_doctrines

Grand doctrines and subdoctrines pre-selected in country history files.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| id | SERIAL | Yes (PK) | — | Auto-increment |
| country_tag | CHAR(3) | Yes (FK) | filename tag | Country code |
| date | DATE | Yes | date block context | `1936-01-01` for top-level, date from block otherwise |
| doctrine_type | VARCHAR(15) | Yes | command | `grand` or `sub` |
| doctrine_key | VARCHAR(80) | Yes | value | References grand_doctrines or subdoctrines |
| source_file | TEXT | Yes | — | Provenance |

- **Source**: `history/countries/*.txt` (`set_grand_doctrine`, `set_sub_doctrine`)
- **Row count**: ~927
- **Relationship notes**: FK → `countries`.

---

## Phase 24 — Factions (Ride of the Valkyries)

### faction_rule_groups

Groups that classify faction rules (ideology, geographical, war declaration, peace, etc.).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| rule_group_key | VARCHAR(80) | Yes (PK) | block key | e.g. `rule_group_ideology` |
| source_file | TEXT | Yes | — | Provenance |

- **Source**: `common/factions/rules/groups/rule_groups.txt`
- **Row count**: ~15
- **Relationship notes**: Parent of `faction_rule_group_members`.

### faction_rules

Individual faction rules (joining, dismissal, war declaration, peace, etc.).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| rule_key | VARCHAR(120) | Yes (PK) | block key | e.g. `joining_rule_non_fascist` |
| rule_type | VARCHAR(60) | Yes | type | `joining_rules`, `peace_conference_rules`, etc. |
| rule_group_key | VARCHAR(80) | No (FK) | derived | From rule_groups membership |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/factions/rules/*.txt`
- **Row count**: ~53
- **Relationship notes**: FK → `faction_rule_groups`. Parent of `faction_template_rules`.

### faction_rule_group_members

Junction: which rules belong to which rule groups.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| rule_group_key | VARCHAR(80) | Yes (PK, FK) | parent block | Rule group key |
| rule_key | VARCHAR(120) | Yes (PK, FK) | child entry | Rule key |

- **Source**: `common/factions/rules/groups/rule_groups.txt`
- **Row count**: ~60
- **Relationship notes**: FK → `faction_rule_groups`, `faction_rules`.

### faction_manifests

Faction manifestos — ratio progress targets for faction objectives.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| manifest_key | VARCHAR(120) | Yes (PK) | block key | e.g. `faction_manifest_defense_of_democracy` |
| name_loc | VARCHAR(120) | No | name | Localisation key |
| description_loc | VARCHAR(120) | No | description | Localisation key |
| is_manifest | BOOLEAN | Yes | is_manifest | Always true in data |
| total_amount | INTEGER | No | ratio_progress.total_amount | Target count for completion ratio |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/factions/goals/faction_manifests.txt`
- **Row count**: ~36
- **Relationship notes**: Parent of `faction_templates`.

### faction_goals

Faction goals (short/medium/long-term objectives for faction members).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| goal_key | VARCHAR(120) | Yes (PK) | block key | e.g. `faction_goal_one_germany` |
| name_loc | VARCHAR(120) | No | name | Localisation key |
| description_loc | VARCHAR(120) | No | description | Localisation key |
| category | VARCHAR(20) | Yes | filename/category | `short_term`, `medium_term`, or `long_term` |
| goal_group | VARCHAR(80) | No | group | e.g. `FOCUS_FILTER_ANNEXATION` |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/factions/goals/faction_goals_*.txt`
- **Row count**: ~156
- **Relationship notes**: Parent of `faction_template_goals`.

### faction_templates

Faction template definitions (Allies, Axis, Comintern, generic, etc.).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| template_key | VARCHAR(120) | Yes (PK) | block key | e.g. `faction_template_allies` |
| name_loc | VARCHAR(120) | No | name | Display name or loc key |
| manifest_key | VARCHAR(120) | No (FK) | manifest | Manifest reference |
| icon | VARCHAR(120) | No | icon | GFX sprite name |
| can_leader_join_other | BOOLEAN | No | can_leader_join_other_factions | Default NULL |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/factions/templates/*.txt`
- **Row count**: ~65
- **Relationship notes**: FK → `faction_manifests`. Parent of `faction_template_goals`, `faction_template_rules`.

### faction_template_goals

Junction: goals assigned to each faction template.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| template_key | VARCHAR(120) | Yes (PK, FK) | parent template | Template key |
| goal_key | VARCHAR(120) | Yes (PK, FK) | goals list entry | Goal key |

- **Source**: `common/factions/templates/*.txt` (goals block)
- **Row count**: ~200
- **Relationship notes**: FK → `faction_templates`, `faction_goals`.

### faction_template_rules

Junction: default rules assigned to each faction template.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| template_key | VARCHAR(120) | Yes (PK, FK) | parent template | Template key |
| rule_key | VARCHAR(120) | Yes (PK, FK) | default_rules entry | Rule key |

- **Source**: `common/factions/templates/*.txt` (default_rules block)
- **Row count**: ~250
- **Relationship notes**: FK → `faction_templates`, `faction_rules`.

### faction_member_upgrade_groups

Groups for faction member upgrades (e.g. manpower contribution tiers).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| group_key | VARCHAR(80) | Yes (PK) | block key | e.g. `faction_member_upgrade_manpower_group` |
| name_loc | VARCHAR(120) | No | name | Localisation key |
| description_loc | VARCHAR(120) | No | desc | Localisation key |
| default_upgrade_key | VARCHAR(80) | No | default_upgrade | Default member upgrade |
| upgrade_type | VARCHAR(80) | No | upgrade_type | Type identifier |
| icon | VARCHAR(120) | No | icon | GFX sprite name |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/factions/member_upgrades/member_groups/member_upgrade_groups.txt`
- **Row count**: ~1
- **Relationship notes**: Parent of `faction_member_upgrades`.

### faction_member_upgrades

Individual member upgrade tiers within a group.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| upgrade_key | VARCHAR(80) | Yes (PK) | block key | e.g. `faction_manpower_sharing1` |
| group_key | VARCHAR(80) | No (FK) | parent group | FK to upgrade groups |
| bonus | NUMERIC(8,4) | No | bonus | Numeric bonus value |
| description_loc | VARCHAR(120) | No | desc | Localisation key |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/factions/member_upgrades/member_upgrades.txt`
- **Row count**: ~4
- **Relationship notes**: FK → `faction_member_upgrade_groups`.

---

## Phase 25 — Special Projects (Götterdämmerung)

### special_project_specializations

R&D specialization categories (land, naval, air, nuclear).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| specialization_key | VARCHAR(40) | Yes (PK) | block key | e.g. `specialization_land` |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/special_projects/specialization/specializations.txt`
- **Row count**: 4
- **Relationship notes**: Parent of `special_projects`, `special_project_rewards`.

### special_project_tags

Classification tags for grouping special projects.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| tag_key | VARCHAR(40) | Yes (PK) | list entry | e.g. `sp_tag_tank` |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/special_projects/project_tags/tags.txt`
- **Row count**: 14
- **Relationship notes**: Parent of `special_projects`.

### special_projects

Special R&D projects (flamethrower tanks, jet engines, nuclear bombs, etc.).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| project_key | VARCHAR(120) | Yes (PK) | block key | e.g. `sp_land_flamethrower_tank` |
| specialization_key | VARCHAR(40) | Yes (FK) | specialization | R&D category |
| project_tag | VARCHAR(40) | No (FK) | project_tags | Classification tag |
| complexity | VARCHAR(40) | No | complexity | Scripted value ref |
| prototype_time | VARCHAR(40) | No | prototype_time | Scripted value ref |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | allowed DLC guard | NULL = base game |

- **Source**: `common/special_projects/projects/*.txt`
- **Row count**: ~48
- **Relationship notes**: FK → `special_project_specializations`, `special_project_tags`. Parent of `special_project_reward_links`.

### special_project_rewards

Prototype rewards triggered during project iteration.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| reward_key | VARCHAR(120) | Yes (PK) | block key | e.g. `sp_land_generic_reward_scientist_xp_1` |
| specialization_key | VARCHAR(40) | No (FK) | derived from filename | R&D category |
| fire_only_once | BOOLEAN | Yes | fire_only_once | Default false |
| threshold_min | INTEGER | No | threshold.min | Min progress % |
| threshold_max | INTEGER | No | threshold.max | Max progress % |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/special_projects/prototype_rewards/*.txt`
- **Row count**: ~82
- **Relationship notes**: FK → `special_project_specializations`. Parent of `special_project_reward_links`.

### special_project_reward_links

Junction: generic prototype rewards assigned to each project.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| project_key | VARCHAR(120) | Yes (PK, FK) | parent project | Project |
| reward_key | VARCHAR(120) | Yes (PK, FK) | generic_prototype_rewards entry | Reward |

- **Source**: `common/special_projects/projects/*.txt` (generic_prototype_rewards block)
- **Row count**: ~300
- **Relationship notes**: FK → `special_projects`, `special_project_rewards`.

---

## Phase 26 — Collections

### collections

Scripted collection definitions used by faction manifests and triggers.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| collection_key | VARCHAR(120) | Yes (PK) | block key | e.g. `world_at_peace_countries` |
| name_loc | VARCHAR(120) | No | name | Localisation key |
| input_source | VARCHAR(120) | No | input | `game:all_countries`, `game:scope`, `collection:X` |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/collections/*.txt`
- **Row count**: ~72
- **Relationship notes**: Referenced by faction manifests (completed_amount_collection).

---

## Phase 27 — AI Faction Theaters

### ai_faction_theaters

AI theater definitions for faction military planning.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| theater_key | VARCHAR(80) | Yes (PK) | block key | e.g. `western_europe` |
| name_loc | VARCHAR(80) | No | name | Localisation key |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/ai_faction_theaters/ai_faction_theaters.txt`
- **Row count**: ~30
- **Relationship notes**: Parent of `ai_faction_theater_regions`.

### ai_faction_theater_regions

Junction: strategic regions assigned to each AI theater.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| theater_key | VARCHAR(80) | Yes (PK, FK) | parent theater | Theater key |
| region_id | INT | Yes (PK, FK) | regions list entry | Strategic region ID |

- **Source**: `common/ai_faction_theaters/ai_faction_theaters.txt` (regions block)
- **Row count**: ~180
- **Relationship notes**: FK → `ai_faction_theaters`, `strategic_regions`.

---

## Phase 28 — Timed Activities

### timed_activities

Timed activity definitions (e.g. stage_coup).

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| activity_key | VARCHAR(80) | Yes (PK) | block key | e.g. `stage_coup` |
| source_file | TEXT | Yes | — | Provenance |
| dlc_source | VARCHAR(50) | No | DLC guard | NULL = base game |

- **Source**: `common/timed_activities/*.txt`
- **Row count**: 1
- **Relationship notes**: Parent of `timed_activity_equipment`.

### timed_activity_equipment

Equipment requirements for timed activities.

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| activity_key | VARCHAR(80) | Yes (PK, FK) | parent activity | Activity key |
| equipment_key | VARCHAR(120) | Yes (PK) | equipment_need key | Equipment identifier |
| amount | INTEGER | Yes | equipment_need value | Required quantity |

- **Source**: `common/timed_activities/*.txt` (equipment_need block)
- **Row count**: 1
- **Relationship notes**: FK → `timed_activities`.

---

## Infrastructure Tables

### user_annotations
- **Purpose**: API-facing user notes — free-form metadata on any entity
- **Source files**: Created via API POST
- **Grain**: One row per annotation
- **Primary key**: `annotation_id` (SERIAL)

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| annotation_id | SERIAL | Yes (PK) | — | Auto-increment |
| entity_type | VARCHAR(50) | Yes | API input | e.g. `country`, `state`, `technology` |
| entity_key | VARCHAR(200) | Yes | API input | e.g. `GER`, `64`, `infantry_weapons` |
| note | TEXT | Yes | API input | Free-text annotation |
| created_at | TIMESTAMPTZ | Yes | DEFAULT now() | Creation timestamp |

- **Row count**: 0 (user-generated)
- **Relationship notes**: No FKs. Index on (entity_type, entity_key).

### localisation
- **Purpose**: English display names for game keys (states, technologies, ideas, etc.)
- **Source files**: `localisation/english/*_l_english.yml` (189 files in HOI4 install)
- **Grain**: One row per localisation key
- **Primary key**: `loc_key`

| Column | Type | NOT NULL | Source field | Notes |
|---|---|---|---|---|
| loc_key | VARCHAR(250) | Yes (PK) | YAML key before `:` | e.g. `STATE_64`, `infantry_weapons` |
| loc_value | TEXT | Yes | Quoted string value | e.g. `Brandenburg`, `Infantry Weapons I` |
| source_file | TEXT | No | Filename | Provenance tracking |

- **Row count**: 117,490
- **Relationship notes**: No FKs. Referenced via LEFT JOIN from `api_country_detail` and `api_state_detail` functions.

---

## Summary — New Tables Added in Phases 16–22

| Phase | Domain | Tables Added | Total New Rows (est.) |
|---|---|---|---|
| 16 | Espionage System | `operations`, `operation_awarded_tokens`, `operation_equipment_requirements`, `operation_phase_groups`, `operation_phase_options`, `operation_phase_definitions`, `operation_phase_equipment`, `operation_tokens`, `intelligence_agencies` (REVISED), `intelligence_agency_names`, `intel_agency_upgrade_branches`, `intel_agency_upgrades`, `intel_agency_upgrade_levels`, `intel_agency_upgrade_progress_modifiers` | ~750 |
| 17 | Occupation & Resistance | `compliance_modifiers`, `compliance_modifier_effects`, `resistance_modifiers`, `resistance_modifier_effects`, `resistance_activities` | ~50 |
| 18 | MIO System | `mio_equipment_groups`, `mio_equipment_group_members`, `mio_templates`, `mio_organizations`, `mio_organization_equipment_types`, `mio_initial_traits`, `mio_traits`, `mio_trait_bonuses`, `mio_trait_prerequisites`, `mio_trait_exclusions`, `mio_policies`, `mio_policy_bonuses` | ~3,200 |
| 19 | Raids | `raid_categories`, `raids`, `raid_equipment_requirements` | ~60 |
| 20 | Career Profile | `medals`, `medal_tiers`, `ribbons`, `ace_modifiers`, `ace_modifier_effects`, `ace_modifier_equipment_types`, `unit_medals`, `unit_medal_modifiers` | ~550 |
| 21 | BOP & Continuous Focuses | `balance_of_power_definitions`, `bop_sides`, `bop_ranges`, `bop_range_modifiers`, `continuous_focus_palettes`, `continuous_focuses`, `continuous_focus_modifiers` | ~340 |
| 22 | Misc DLC | `technology_sharing_groups`, `dynamic_modifiers`, `dynamic_modifier_effects`, `scientist_traits`, `scientist_trait_modifiers`, `peace_action_categories`, `peace_cost_modifiers` | ~460 |
| 23 | Doctrines (Officer Corps) | `doctrine_folders`, `doctrine_tracks`, `grand_doctrines`, `grand_doctrine_tracks`, `subdoctrines`, `country_starting_doctrines` | ~1,078 |
| 24 | Factions | `faction_rule_groups`, `faction_rules`, `faction_rule_group_members`, `faction_manifests`, `faction_goals`, `faction_templates`, `faction_template_goals`, `faction_template_rules`, `faction_member_upgrade_groups`, `faction_member_upgrades` | ~584 |
| 25 | Special Projects | `special_project_specializations`, `special_project_tags`, `special_projects`, `special_project_rewards`, `special_project_reward_links` | ~448 |
| 26 | Collections | `collections` | ~72 |
| 27 | AI Faction Theaters | `ai_faction_theaters`, `ai_faction_theater_regions` | ~210 |
| 28 | Timed Activities | `timed_activities`, `timed_activity_equipment` | ~2 |
| Infra | Infrastructure | `user_annotations`, `localisation` | ~117,490 |
| **Totals** | | **77 new tables + 2 infra** | **~125,284 rows** |

**Running total: 66 existing + 77 new + 4 schema-only + 2 infrastructure = 149 tables**

(Note: `intelligence_agencies` is a revision of an existing table, so net new tables = 50; but the new child table `intelligence_agency_names` makes 51 new table definitions.)

---

## FK Dependency / Build Order (Phases 16–22)

Tables must be created in this order to satisfy FK constraints:

```
-- Phase 16: Espionage
1.  operation_tokens
2.  operation_phase_definitions
3.  operation_phase_equipment               (FK → operation_phase_definitions)
4.  operations
5.  operation_awarded_tokens                (FK → operations, operation_tokens)
6.  operation_equipment_requirements        (FK → operations)
7.  operation_phase_groups                  (FK → operations)
8.  operation_phase_options                 (FK → operation_phase_groups, operation_phase_definitions)
9.  intelligence_agencies                   (FK → countries)
10. intelligence_agency_names               (FK → intelligence_agencies)
11. intel_agency_upgrade_branches
12. intel_agency_upgrades                   (FK → intel_agency_upgrade_branches)
13. intel_agency_upgrade_levels             (FK → intel_agency_upgrades)
14. intel_agency_upgrade_progress_modifiers (FK → intel_agency_upgrades)

-- Phase 17: Occupation & Resistance
15. compliance_modifiers
16. compliance_modifier_effects             (FK → compliance_modifiers)
17. resistance_modifiers
18. resistance_modifier_effects             (FK → resistance_modifiers)
19. resistance_activities

-- Phase 18: MIO
20. mio_equipment_groups
21. mio_equipment_group_members             (FK → mio_equipment_groups)
22. mio_templates
23. mio_organizations                       (FK → mio_templates)
24. mio_organization_equipment_types        (polymorphic → mio_templates | mio_organizations)
25. mio_initial_traits                      (polymorphic → mio_templates | mio_organizations)
26. mio_traits                              (polymorphic → mio_templates | mio_organizations)
27. mio_trait_bonuses                       (FK → mio_traits)
28. mio_trait_prerequisites                 (FK → mio_traits self-ref ×2)
29. mio_trait_exclusions                    (FK → mio_traits self-ref ×2)
30. mio_policies
31. mio_policy_bonuses                      (FK → mio_policies)

-- Phase 19: Raids
32. raid_categories
33. raids                                   (FK → raid_categories)
34. raid_equipment_requirements             (FK → raids)

-- Phase 20: Career Profile
35. medals
36. medal_tiers                             (FK → medals)
37. ribbons
38. ace_modifiers
39. ace_modifier_effects                    (FK → ace_modifiers)
40. ace_modifier_equipment_types            (FK → ace_modifiers)
41. unit_medals
42. unit_medal_modifiers                    (FK → unit_medals)

-- Phase 21: BOP & Continuous Focuses
43. balance_of_power_definitions
44. bop_sides                               (FK → balance_of_power_definitions)
45. bop_ranges                              (FK → bop_sides)
46. bop_range_modifiers                     (FK → bop_ranges)
47. continuous_focus_palettes
48. continuous_focuses                       (FK → continuous_focus_palettes)
49. continuous_focus_modifiers               (FK → continuous_focuses)

-- Phase 22: Misc DLC
50. technology_sharing_groups
51. dynamic_modifiers
52. dynamic_modifier_effects                (FK → dynamic_modifiers)
53. scientist_traits
54. scientist_trait_modifiers               (FK → scientist_traits)
55. peace_action_categories
56. peace_cost_modifiers                    (FK → peace_action_categories)

-- Phase 24: Factions
57. faction_rule_groups
58. faction_rules                           (FK → faction_rule_groups)
59. faction_rule_group_members              (FK → faction_rule_groups, faction_rules)
60. faction_manifests
61. faction_goals
62. faction_templates                       (FK → faction_manifests)
63. faction_template_goals                  (FK → faction_templates, faction_goals)
64. faction_template_rules                  (FK → faction_templates, faction_rules)
65. faction_member_upgrade_groups
66. faction_member_upgrades                 (FK → faction_member_upgrade_groups)

-- Phase 25: Special Projects
67. special_project_specializations
68. special_project_tags
69. special_projects                        (FK → special_project_specializations, special_project_tags)
70. special_project_rewards                 (FK → special_project_specializations)
71. special_project_reward_links            (FK → special_projects, special_project_rewards)

-- Phase 26: Collections
72. collections

-- Phase 27: AI Faction Theaters
73. ai_faction_theaters
74. ai_faction_theater_regions              (FK → ai_faction_theaters, strategic_regions)

-- Phase 28: Timed Activities
75. timed_activities
76. timed_activity_equipment                (FK → timed_activities)
```

---

## Index Recommendations (Phases 16–28)

| Table | Index | Rationale |
|---|---|---|
| `operations` | `idx_operations_dlc` ON (dlc_source) | Filter operations by DLC |
| `operation_phase_options` | `idx_opo_group` ON (operation_key, sequence_index) | Lookup phases per group |
| `intel_agency_upgrade_levels` | `idx_iaul_upgrade` ON (upgrade_key, level_index) | Ordered level retrieval |
| `mio_organizations` | `idx_mio_org_template` ON (template_key) | JOIN to template |
| `mio_traits` | `idx_mio_traits_owner` ON (owner_key, owner_type) | Traits per org |
| `mio_trait_bonuses` | `idx_mio_tb_token` ON (trait_token) | Bonuses per trait |
| `bop_ranges` | `idx_bop_ranges_side` ON (bop_key, side_id) | Ranges per side |
| `bop_range_modifiers` | `idx_bop_rm_range` ON (range_id) | Modifiers per range |
| `peace_cost_modifiers` | `idx_pcm_category` ON (category_key) | Filter by category |
| `dynamic_modifier_effects` | `idx_dme_modifier` ON (modifier_key) | Effects per modifier |
| `unit_medal_modifiers` | `idx_umm_medal` ON (medal_key) | Modifiers per medal |
| `raids` | `idx_raids_category` ON (category_key) | Raids by category |
| `continuous_focuses` | `idx_cf_palette` ON (palette_id) | Focuses per palette |
| `faction_rules` | `idx_faction_rules_group` ON (rule_group_key) | Rules per group |
| `faction_rules` | `idx_faction_rules_type` ON (rule_type) | Rules by type |
| `faction_goals` | `idx_faction_goals_category` ON (category) | Goals by category |
| `faction_templates` | `idx_faction_templates_manifest` ON (manifest_key) | Templates per manifest |
| `faction_member_upgrades` | `idx_fmu_group` ON (group_key) | Upgrades per group |
| `special_projects` | `idx_sp_specialization` ON (specialization_key) | Projects per specialization |
| `special_projects` | `idx_sp_tag` ON (project_tag) | Projects per tag |
| `special_project_rewards` | `idx_spr_spec` ON (specialization_key) | Rewards per specialization |
| `ai_faction_theater_regions` | `idx_aftr_region` ON (region_id) | Theater lookup by region |

---

## DLC Field Register (Phases 16–28)

| Table | Column / Scope | DLC Guard | Notes |
|---|---|---|---|
| `operations` | `dlc_source` | "La Resistance" | All operations require LaR |
| `operation_tokens` | Entire table | "La Resistance" | 5 tokens |
| `operation_phase_definitions` | Entire table | "La Resistance" | |
| `intelligence_agencies` | `dlc_source` | "La Resistance" | Agency system requires LaR |
| `intel_agency_upgrade_branches` | Entire table | "La Resistance" | |
| `compliance_modifiers` | `dlc_source` on compliance_80 | "La Resistance" | Threshold 80 has LaR guard |
| `resistance_modifiers` | Entire table | "La Resistance" | |
| `resistance_activities` | Entire table | "La Resistance" | |
| `raid_categories` | `dlc_source` per row | "Gotterdammerung", "No Compromise, No Surrender" | Mixed DLC |
| `raids` | `dlc_source` | "Gotterdammerung" | Most raids are Götterdämmerung |
| `mio_templates` | `dlc_source` | "Arms Against Tyranny" | Entire MIO system |
| `mio_organizations` | `dlc_source` | Various | Per-country DLC checks |
| `mio_policies` | `dlc_source` | "Arms Against Tyranny" | |
| `medals` | `dlc_source` | "By Blood Alone" | Career profile feature |
| `ribbons` | `dlc_source` | "By Blood Alone" | |
| `ace_modifiers` | Entire table | "By Blood Alone" | |
| `unit_medals` | `dlc_source` | "Gotterdammerung" | |
| `balance_of_power_definitions` | Entire table | Various per country | BBA, AAT, ToA |
| `continuous_focuses` | `dlc_source` per row | Various | "Arms Against Tyranny", "By Blood Alone" |
| `technology_sharing_groups` | `dlc_source` | "Together for Victory" + others | Base + DLC groups |
| `dynamic_modifiers` | `dlc_source` per file | Various | Per-DLC files |
| `scientist_traits` | Entire table | "Gotterdammerung" | |
| `peace_action_categories` | Entire table | "By Blood Alone" | Peace overhaul |
| `peace_cost_modifiers` | `dlc_source` | "By Blood Alone" | |
| `faction_rule_groups` | Entire table | "Ride of the Valkyries" | Faction system |
| `faction_rules` | `dlc_source` | "Ride of the Valkyries" | |
| `faction_manifests` | `dlc_source` | "Ride of the Valkyries" | |
| `faction_goals` | `dlc_source` | "Ride of the Valkyries" | |
| `faction_templates` | `dlc_source` | "Ride of the Valkyries" | |
| `faction_member_upgrade_groups` | Entire table | "Ride of the Valkyries" | |
| `faction_member_upgrades` | `dlc_source` | "Ride of the Valkyries" | |
| `special_project_specializations` | `dlc_source` | "Gotterdammerung" | R&D projects |
| `special_project_tags` | `dlc_source` | "Gotterdammerung" | |
| `special_projects` | `dlc_source` | Various | Per-project DLC guards |
| `special_project_rewards` | `dlc_source` | "Gotterdammerung" | |
| `collections` | Entire table | "Ride of the Valkyries" | Used by factions |
| `ai_faction_theaters` | Entire table | "Ride of the Valkyries" | AI faction planning |
