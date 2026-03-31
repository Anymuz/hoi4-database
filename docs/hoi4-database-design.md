# HOI4 Database Design — Complete Schema

Status: **COMPLETE** (All Phases 1–23, including DLC)
Total tables: **127** (66 core + 61 DLC)

---

## Executive Summary

This document specifies a fully normalised (3NF) PostgreSQL relational database representing **all starting-state game data** for Hearts of Iron IV, including all DLC content. The schema covers 22 data domains across two tiers:

**Core (Phases 1–15, 66 tables):** global references, geography, map connectivity, countries, technologies, characters, division/naval/air OOB, ideas, focus trees, governance, country extensions, bookmarks, decisions.

**DLC (Phases 16–23, 61 tables):** espionage system (La Résistance), occupation & resistance, military-industrial organizations (Arms Against Tyranny), raids (Götterdämmerung), career profile medals & ribbons (By Blood Alone), balance of power, continuous focuses, technology sharing, dynamic modifiers, scientist traits, peace conference, doctrines (Officer Corps / Military Experience).

The database backs a REST API with primary access patterns:
- `GET /countries/{tag}` — ≤3 joins for country detail
- `GET /states/{id}` — ≤2 joins for state detail
- `GET /countries/{tag}/technologies` — 1 join
- `GET /countries/{tag}/characters` — 2 joins
- `GET /countries/{tag}/divisions` — 2 joins

All DLC-conditional data is retained via nullable `dlc_source VARCHAR(50)` columns. Entirely DLC-specific systems (operations, MIOs, raids, medals) have dedicated table groups rather than being shoehorned into base tables. The schema uses surrogate keys (SERIAL/BIGSERIAL) for junction tables and natural keys (game identifiers) for entity tables where the game defines a stable unique key.

---

## Data Source Coverage Matrix

| Source Path Pattern | Target Table(s) | Row Estimate |
|---|---|---|
| `common/country_tags/00_countries.txt` | countries | 352 |
| `common/countries/*.txt` | countries (color, culture) | 430 |
| `history/countries/*.txt` | countries, country_starting_technologies, country_starting_ideas | 352 + 11,258 |
| `history/states/*.txt` | states, state_provinces, state_ownership_history, state_cores, state_victory_points, state_resources, state_buildings, province_buildings | 1,046 states |
| `map/definition.csv` | provinces | 13,382 |
| `map/buildings.txt` | province_building_positions | 65,659 |
| `map/continent.txt` | continents | 7 |
| `map/strategicregions/*.txt` | strategic_regions, strategic_region_provinces | 298 + 13,437 |
| `map/supply_nodes.txt` | supply_nodes | 727 |
| `common/resources/00_resources.txt` | resource_types | 7 |
| `common/buildings/00_buildings.txt` | building_types | ~25 |
| `common/technologies/*.txt` | technologies, technology_categories, technology_categories_junction, technology_prerequisites, technology_enables_equipment, technology_enables_units | 569 + 421 + 718 |
| `common/ideologies/00_ideologies.txt` | ideologies, sub_ideologies | 4 + ~25 |
| `common/units/*.txt` | unit_types | 125 |
| `common/units/equipment/*.txt` | equipment_definitions, equipment_resources | 308 + 454 |
| `common/characters/*.txt` | characters, character_roles, character_role_traits | 5,160 + 5,469 |
| `common/ideas/*.txt` | ideas, idea_modifiers | 5,947 + 11,105 |
| `common/national_focus/*.txt` | focus_trees, focuses, focus_prerequisites, focus_mutually_exclusive | 63 + 8,498 + 9,673 |
| `history/units/*.txt` (land) | division_templates, division_template_regiments, division_template_support, divisions | 797 + 4,580 + ~1,200 + 4,991 |
| `history/units/*_naval_*.txt` | fleets, task_forces, ships, equipment_variants | ~100 + ~300 + ~1,500 + ~500 |
| `history/units/*_air_*.txt` | air_wings | ~1,000 |
| `common/terrain/00_terrain.txt` | terrain_types, terrain_building_limits, terrain_combat_modifiers | 14 + ~20 + ~50 |
| `common/state_category/*.txt` | state_categories | 13 |
| `map/adjacencies.csv` | province_adjacencies | ~300 |
| `map/railways.txt` | province_railways | ~5,000 |
| `common/autonomous_states/*.txt` | autonomy_states, autonomy_state_modifiers | 19 + ~150 |
| `common/occupation_laws/*.txt` | occupation_laws, occupation_law_modifiers | ~10 + ~80 |
| `common/countries/*.txt` | country_visual_definitions | ~430 |
| `common/intelligence_agencies/*.txt` | intelligence_agencies | ~50 |
| `common/bookmarks/*.txt` | bookmarks, bookmark_countries | 2 + ~30 |
| `common/decisions/**/*.txt` | decision_categories, decisions | ~30 + ~500 |
| `common/operations/*.txt` | operations, operation_awarded_tokens, operation_equipment_requirements, operation_phase_groups, operation_phase_options | ~36 + ~20 + ~15 + ~100 + ~300 |
| `common/operation_phases/*.txt` | operation_phase_definitions, operation_phase_equipment | ~60 + ~20 |
| `common/operation_tokens/*.txt` | operation_tokens | 5 |
| `common/intelligence_agencies/*.txt` | intelligence_agencies (revised), intelligence_agency_names | ~50 + ~60 |
| `common/intelligence_agency_upgrades/*.txt` | intel_agency_upgrade_branches, intel_agency_upgrades, intel_agency_upgrade_levels, intel_agency_upgrade_progress_modifiers | 6 + ~30 + ~100 + ~60 |
| `common/resistance_compliance_modifiers/*.txt` | compliance_modifiers, compliance_modifier_effects, resistance_modifiers, resistance_modifier_effects | 5+~20 + 4+~15 |
| `common/resistance_activity/*.txt` | resistance_activities | ~15 |
| `common/military_industrial_organization/organizations/*.txt` | mio_templates, mio_organizations, mio_organization_equipment_types, mio_initial_traits, mio_traits, mio_trait_bonuses, mio_trait_prerequisites, mio_trait_exclusions | ~40 + ~300 + ~500 + ~340 + ~900 + ~1,500 + ~600 + ~200 |
| `common/military_industrial_organization/policies/*.txt` | mio_policies, mio_policy_bonuses | ~75 + ~200 |
| `common/equipment_groups/*.txt` | mio_equipment_groups, mio_equipment_group_members | ~25 + ~150 |
| `common/raids/**/*.txt` | raid_categories, raids, raid_equipment_requirements | 4 + ~20 + ~40 |
| `common/medals/*.txt` | medals, medal_tiers | ~30 + ~90 |
| `common/ribbons/*.txt` | ribbons | ~20 |
| `common/aces/*.txt` | ace_modifiers, ace_modifier_effects, ace_modifier_equipment_types | 9 + ~18 + ~20 |
| `common/unit_medals/*.txt` | unit_medals, unit_medal_modifiers | ~50 + ~150 |
| `common/bop/*.txt` | balance_of_power_definitions, bop_sides, bop_ranges, bop_range_modifiers | 8 + ~16 + ~50 + ~200 |
| `common/continuous_focus/*.txt` | continuous_focus_palettes, continuous_focuses, continuous_focus_modifiers | ~5 + ~40 + ~80 |
| `common/technology_sharing/*.txt` | technology_sharing_groups | ~15 |
| `common/dynamic_modifiers/*.txt` | dynamic_modifiers, dynamic_modifier_effects | ~80 + ~300 |
| `common/scientist_traits/*.txt` | scientist_traits, scientist_trait_modifiers | 7 + ~25 |
| `common/peace_conference/**/*.txt` | peace_action_categories, peace_cost_modifiers | 11 + ~80 |

---

## Normalization Notes

### 3NF Compliance
All tables satisfy 3NF: every non-key column depends on the whole key and nothing but the key.

### Key Design Decisions

1. **Natural keys for game entities**: `countries.tag`, `technologies.technology_key`, `equipment_definitions.equipment_key`, `ideas.idea_key`, `focuses.focus_id` use the game's own unique identifier as PK. This avoids unnecessary surrogate-to-natural joins for the most common API lookups.

2. **Surrogate keys for junction/instance tables**: Tables like `character_roles`, `division_templates`, `divisions`, `ships`, `air_wings` use SERIAL/BIGSERIAL PKs because the game data lacks a stable unique identifier.

3. **Effective date on history tables**: Slice A tables (state_ownership_history, state_cores, etc.) include `effective_date DATE` to support both the default 1936.1.1 bookmark and the 1939.9.1 alternate start. New phase tables use an `oob_file VARCHAR` column to track which OOB variant a record belongs to.

4. **Self-referential FKs**: `equipment_definitions.archetype_key` and `equipment_definitions.parent_key` reference the same table for the equipment inheritance chain. `technology_prerequisites` is a self-join on `technologies`.

5. **Focus prerequisite AND/OR modeling**: `focus_prerequisites` uses a `prerequisite_group INT` column. Focuses within the same group are OR alternatives; all groups must be satisfied (AND). This normalizes the game's `prerequisite = { focus = X focus = Y }` pattern.

---

## FK Dependency Build Order

Tables must be created in this order (no forward FK references):

```
 1. continents
 2. terrain_types
 3. state_categories
 4. resource_types                    (existing)
 5. building_types                    (existing)
 6. ideologies
 7. sub_ideologies                    → ideologies
 8. technology_categories
 9. technologies                      (existing)
10. unit_types
11. equipment_definitions             → self-ref (archetype, parent)
12. equipment_resources               → equipment_definitions, resource_types
13. provinces                          (existing)
14. province_building_positions       → provinces
15. strategic_regions
16. strategic_region_provinces        → strategic_regions, provinces
17. supply_nodes                      → provinces
18. states                            (existing)
19. state_provinces                   (existing) → states, provinces
20. state_resources                   (existing) → states, resource_types
21. state_buildings                   (existing) → states, building_types
22. state_victory_points              (existing) → states, provinces
23. province_buildings                (existing) → provinces, states, building_types
24. countries                          (existing) → states (deferred)
25. state_ownership_history           (existing) → states, countries
26. province_controller_history       (existing) → provinces, states, countries
27. state_cores                       (existing) → states, countries
28. country_starting_technologies     (existing) → countries, technologies
29. technology_categories_junction    → technologies, technology_categories
30. technology_prerequisites          → technologies (self-ref)
31. technology_enables_equipment      → technologies, equipment_definitions
32. technology_enables_units          → technologies, unit_types
33. character_traits
34. characters                        → countries
35. character_roles                   → characters, sub_ideologies
36. character_role_traits             → character_roles, character_traits
37. ideas
38. idea_modifiers                    → ideas
39. country_starting_ideas            → countries, ideas
40. focus_trees                       → countries (nullable)
41. focuses                           → focus_trees
42. focus_prerequisites               → focuses (self-ref)
43. focus_mutually_exclusive          → focuses (self-ref)
44. division_templates                → countries
45. division_template_regiments       → division_templates, unit_types
46. division_template_support         → division_templates, unit_types
47. divisions                         → division_templates, provinces
48. equipment_variants                → countries, equipment_definitions
49. fleets                            → countries, provinces
50. task_forces                       → fleets, provinces
51. ships                             → task_forces, equipment_definitions, countries
52. air_wings                         → countries, states
-- Phase 11: Governance
53. autonomy_states
54. autonomy_state_modifiers          → autonomy_states
55. occupation_laws                   → self-ref (fallback)
56. occupation_law_modifiers          → occupation_laws
-- Phase 12-15: Extensions
57. country_visual_definitions        → countries
58. intelligence_agencies             → countries
59. intelligence_agency_names         → intelligence_agencies
60. bookmarks                         → countries
61. bookmark_countries                → bookmarks, countries, ideologies
62. decision_categories
63. decisions                         → decision_categories
-- Phase 16: Espionage
64. operation_tokens
65. operation_phase_definitions
66. operation_phase_equipment         → operation_phase_definitions
67. operations
68. operation_awarded_tokens          → operations, operation_tokens
69. operation_equipment_requirements  → operations
70. operation_phase_groups            → operations
71. operation_phase_options           → operation_phase_groups, operation_phase_definitions
72. intel_agency_upgrade_branches
73. intel_agency_upgrades             → intel_agency_upgrade_branches
74. intel_agency_upgrade_levels       → intel_agency_upgrades
75. intel_agency_upgrade_progress_modifiers → intel_agency_upgrades
-- Phase 17: Occupation & Resistance
76. compliance_modifiers
77. compliance_modifier_effects       → compliance_modifiers
78. resistance_modifiers
79. resistance_modifier_effects       → resistance_modifiers
80. resistance_activities
-- Phase 18: MIO
81. mio_equipment_groups
82. mio_equipment_group_members       → mio_equipment_groups
83. mio_templates
84. mio_organizations                 → mio_templates, countries
85. mio_organization_equipment_types  → mio_templates | mio_organizations
86. mio_initial_traits                → mio_templates | mio_organizations
87. mio_traits                        → mio_templates | mio_organizations
88. mio_trait_bonuses                 → mio_traits
89. mio_trait_prerequisites           → mio_traits (self-ref)
90. mio_trait_exclusions              → mio_traits (self-ref)
91. mio_policies
92. mio_policy_bonuses                → mio_policies
-- Phase 19: Raids
93. raid_categories
94. raids                             → raid_categories
95. raid_equipment_requirements       → raids
-- Phase 20: Career Profile
96. medals
97. medal_tiers                       → medals
98. ribbons
99. ace_modifiers
100. ace_modifier_effects             → ace_modifiers
101. ace_modifier_equipment_types     → ace_modifiers
102. unit_medals
103. unit_medal_modifiers             → unit_medals
-- Phase 21: BOP & Continuous Focuses
104. balance_of_power_definitions     → countries
105. bop_sides                        → balance_of_power_definitions
106. bop_ranges                       → bop_sides
107. bop_range_modifiers              → bop_ranges
108. continuous_focus_palettes
109. continuous_focuses               → continuous_focus_palettes
110. continuous_focus_modifiers       → continuous_focuses
-- Phase 22: Misc DLC
111. technology_sharing_groups
112. dynamic_modifiers
113. dynamic_modifier_effects         → dynamic_modifiers
114. scientist_traits
115. scientist_trait_modifiers        → scientist_traits
116. peace_action_categories
117. peace_cost_modifiers             → peace_action_categories
-- Phase 23: Doctrines (Officer Corps / Military Experience)
118. doctrine_folders
119. doctrine_tracks                  → doctrine_folders
120. grand_doctrines                  → doctrine_folders
121. grand_doctrine_tracks            → grand_doctrines, doctrine_tracks
122. subdoctrines                     → doctrine_tracks
123. country_starting_doctrines       → countries
```

---

## Table Build Notes

### Phase 1 — Global Reference Tables (9 tables)
No FK dependencies. Create first. `continents`, `terrain_types`, `state_categories` are small enum-like lookup tables. `ideologies` (4 rows) and `sub_ideologies` (~25 rows) define the political system. `technology_categories` (~40 rows) for the tech tree categorization. `unit_types` (125 rows) and `equipment_definitions` (308 rows) define the military unit/equipment catalog. `equipment_resources` (454 rows) links equipment to raw material costs.

### Phase 2 — Geography (4 new tables)
`province_building_positions` (65,659 rows) is the largest table by volume — it stores 3D coordinates for every building slot marker on the map. `strategic_regions` (298) and `strategic_region_provinces` (13,437) map the air/weather zone system. `supply_nodes` (727) replaces the expected `supply_areas` table — only `supply_nodes.txt` exists in this installation.

### Phase 3 — Countries (1 new table)
Most country tables exist from Slice A. The only addition is `country_starting_ideas` for the `add_ideas = { }` blocks.

### Phase 4 — Technologies (4 new tables)
`technology_categories_junction` handles the M:N relationship between techs and categories. `technology_prerequisites` (421 rows) is the directed graph of `leads_to_tech` links. `technology_enables_equipment` and `technology_enables_units` capture what each tech unlocks.

### Phase 5 — Characters (4 new tables)
`characters` (5,160 rows) holds the master character record. `character_roles` (5,469 rows) allows one character to hold multiple roles (leader + general + advisor). Skill fields (attack, defense, planning, logistics) are nullable since they only apply to military roles. `character_traits` and `character_role_traits` form the trait junction.

### Phase 6 — Division Templates & OOB (4 new tables)
`division_templates` (797 rows) define the blueprint; `division_template_regiments` (4,580 rows) and `division_template_support` (~1,200 rows) specify the grid layout. `divisions` (4,991 rows) are deployed instances referencing templates by name.

### Phase 7 — Naval OOB (4 new tables)
Three-level hierarchy: `fleets` → `task_forces` → `ships`. `equipment_variants` (~500 rows) holds named design variants (e.g., "Leipzig" class cruiser). Ships reference both the hull equipment type and the variant name.

### Phase 8 — Air OOB (1 new table)
`air_wings` combines wing metadata with equipment assignment in a single table. Each row is one wing with its equipment type, amount, and location state.

### Phase 9 — Ideas (2 new tables + 1 from Phase 3)
`ideas` (5,947 rows) covers laws, national spirits, hidden ideas, and advisor slots. `idea_modifiers` (11,105 rows) stores the key-value modifier pairs. `country_starting_ideas` (from Phase 3) completes the junction.

### Phase 10 — Focus Trees (4 new tables)
`focus_trees` (63 rows) are containers. `focuses` (8,498 rows) are the nodes. `focus_prerequisites` and `focus_mutually_exclusive` encode the graph edges from the 9,673 total links extracted.

### Phase 11 — Governance (4 tables)
`autonomy_states` (19 rows) define puppet/dominion/colony autonomy levels with modifier key-value pairs in `autonomy_state_modifiers` (~150 rows). `occupation_laws` (~10 rows) define garrison policies with self-referential fallback chains and separate modifier tables for normal vs. suppressed state modifiers.

### Phase 12–15 — Extensions (6 tables)
`country_visual_definitions` (430 rows) stores graphical culture assignments. `intelligence_agencies` (~50 rows) holds agency definitions with `intelligence_agency_names` child table for multiple possible display names. `bookmarks` (2 rows) and `bookmark_countries` (~30 rows) define game start scenarios. `decision_categories` (~30 rows) and `decisions` (~500 rows) cover the political decision system.

### Phase 16 — Espionage System (14 tables, La Résistance)
The operations system is the most complex DLC addition. `operations` (36 rows) define mission templates with duration, risk, network requirements. `operation_phase_groups` and `operation_phase_options` model the sequential phase selection mechanic (each operation has 1-N phase groups, each containing weighted phase alternatives). `operation_phase_definitions` (~60 rows) are reusable phase templates referenced across operations. `operation_tokens` (5 rows) are intel resources awarded on success. Intelligence agency upgrades use a 3-level hierarchy: `intel_agency_upgrade_branches` (6) → `intel_agency_upgrades` (~30) → `intel_agency_upgrade_levels` (~100), with separate `progress_modifiers` for construction-phase effects.

### Phase 17 — Occupation & Resistance (5 tables, La Résistance)
`compliance_modifiers` (5 thresholds: 15/25/40/60/80) and `resistance_modifiers` (thresholds: 25/50/75/90) define state-level modifier tiers that activate based on compliance/resistance percentages. Each has a child `*_effects` table for key-value state modifiers. `resistance_activities` (~15 rows) define sabotage types like `sabotage_arms_factory` and `sabotage_infrastructure`.

### Phase 18 — Military-Industrial Organizations (12 tables, Arms Against Tyranny)
The largest DLC system by row count (~3,200 total). `mio_templates` (~40 generic templates) serve as base definitions inherited by `mio_organizations` (~300 country-specific orgs). Each org has a trait tree modeled via `mio_traits` (~900 nodes) with `mio_trait_bonuses` (~1,500 key-value modifier rows), `mio_trait_prerequisites` (parent dependencies), and `mio_trait_exclusions` (mutual exclusion pairs). `mio_policies` (~75) provide separate modifier sets. `mio_equipment_groups` (~25) categorize equipment types the MIO applies to.

### Phase 19 — Raids (3 tables, Götterdämmerung)
`raid_categories` (4 rows: air, paratrooper, nuclear, land infiltration) define category-level properties. `raids` (~20 definitions) specify individual raid missions with preparation time, command power cost, and target types. `raid_equipment_requirements` (~40 rows) specifies essential and additional equipment per raid.

### Phase 20 — Career Profile (8 tables, By Blood Alone)
`medals` (~30) and `medal_tiers` (~90) model the 3-tier career achievement system (bronze/silver/gold thresholds tracking gameplay statistics). `ribbons` (~20) are achievement markers with scripted trigger conditions. `ace_modifiers` (9 entries for fighter/bomber/support × good/unique/genius) define ace pilot combat bonuses. `unit_medals` (~50) are per-country military decorations with `unit_medal_modifiers` (~150 modifier key-values).

### Phase 21 — Balance of Power & Continuous Focuses (7 tables)
`balance_of_power_definitions` (8 country-specific BOP instances) each have two `bop_sides` with hierarchical `bop_ranges` containing threshold-based `bop_range_modifiers`. `continuous_focus_palettes` (~5) contain `continuous_focuses` (~40) with daily PP cost and modifier key-values.

### Phase 22 — Misc DLC Systems (7 tables)
`technology_sharing_groups` (~15 groups across multiple DLCs) enable research sharing bonuses within factions/blocs. `dynamic_modifiers` (~80) and their child `dynamic_modifier_effects` (~300) store runtime-applied modifier templates. `scientist_traits` (7) define special project bonuses. `peace_action_categories` (11) and `peace_cost_modifiers` (~80) model the By Blood Alone peace conference overhaul.

### Phase 23 — Doctrines / Officer Corps (6 tables, Götterdämmerung)
Doctrines are purchased with military experience (Army/Navy/Air XP) through the Officer Corps — distinct from the research-slot technology tree. `doctrine_folders` (3: land, naval, air) define the top-level categories. `doctrine_tracks` (12: 4 per branch) group subdoctrines by mastery category. `grand_doctrines` (10: 4 land, 3 naval, 3 air) are mutually-exclusive choices per folder; `grand_doctrine_tracks` (40 junction rows) maps tracks to grand doctrines. `subdoctrines` (~86) are slotted into tracks with mastery reward tiers. `country_starting_doctrines` (~927 rows) captures both `set_grand_doctrine` and `set_sub_doctrine` assignments from country history files, with date scoping for 1936/1939 bookmarks.

---

## API Access Optimization Strategy

### Primary API Views

**`api_country_detail`** for `GET /countries/{tag}`:
```
countries LEFT JOIN state_ownership_history (owned state count)
          LEFT JOIN sub_ideologies (ruling ideology)
```

**`api_state_detail`** for `GET /states/{id}`:
```
states JOIN state_ownership_history (current owner)
       LEFT JOIN state_resources
       LEFT JOIN state_buildings
```

**`api_country_technologies`** for `GET /countries/{tag}/technologies`:
```
country_starting_technologies JOIN technologies
```

**`api_country_characters`** for `GET /countries/{tag}/characters`:
```
characters JOIN character_roles LEFT JOIN character_role_traits
```

### Index Recommendations

| Index | Purpose |
|---|---|
| `countries(tag)` PK | Country lookup |
| `state_ownership_history(owner_tag, effective_date)` | Country→states |
| `state_resources(state_id)` | State detail |
| `state_buildings(state_id)` | State detail |
| `country_starting_technologies(country_tag)` | Tech list per country |
| `characters(country_tag)` | Character list per country |
| `character_roles(character_id)` | Role lookup |
| `division_templates(country_tag)` | Template list |
| `divisions(country_tag)` | Division list |
| `focuses(focus_tree_id)` | Focus tree expansion |
| `ideas(slot)` | Idea slot lookup |
| `air_wings(country_tag)` | Air OOB per country |
| `ships(task_force_id)` | Ship-in-TF lookup |
| `idea_modifiers(idea_key)` | Modifier expansion |
| `focus_prerequisites(focus_id)` | Prereq lookup |
| `operations(dlc_source)` | Filter operations by DLC |
| `operation_phase_options(operation_key, sequence_index)` | Phases per group |
| `intel_agency_upgrade_levels(upgrade_key, level_index)` | Ordered level retrieval |
| `mio_organizations(template_key)` | JOIN to template |
| `mio_traits(owner_key, owner_type)` | Traits per org |
| `mio_trait_bonuses(trait_token)` | Bonuses per trait |
| `bop_ranges(bop_key, side_id)` | Ranges per side |
| `bop_range_modifiers(range_id)` | Modifiers per range |
| `peace_cost_modifiers(category_key)` | Filter by category |
| `dynamic_modifier_effects(modifier_key)` | Effects per modifier |
| `unit_medal_modifiers(medal_key)` | Modifiers per medal |
| `raids(category_key)` | Raids by category |
| `continuous_focuses(palette_id)` | Focuses per palette |

---

## DLC-Conditional Field Strategy

All DLC-gated data uses nullable `dlc_source VARCHAR(50)` columns:
- `NULL` → base-game data (always valid)
- Populated → DLC name gating this record (e.g., `"No Step Back"`, `"Man the Guns"`, `"By Blood Alone"`)

### DLC Field Register

| Table | Column | DLC Examples | Handling |
|---|---|---|---|
| building_types | dlc_source | Various | NULL = base game |
| state_ownership_history | dlc_source | Various | DLC-conditional owner changes |
| province_controller_history | dlc_source | Various | DLC-conditional controller |
| state_cores | dlc_source | Various | DLC-conditional core status |
| state_victory_points | dlc_source | Various | DLC-conditional VP |
| state_resources | dlc_source | Various | DLC-conditional resources |
| state_buildings | dlc_source | Various | DLC-conditional buildings |
| province_buildings | dlc_source | Various | DLC-conditional province buildings |
| country_starting_technologies | dlc_source | NSB, MTG, BBA, AAT | DLC-specific tech sets |
| country_starting_ideas | dlc_source | Various | DLC-gated starting spirits |
| technologies | dlc_source | NSB, BBA | DLC-only technologies |
| character_roles | dlc_source | Various | DLC-conditional character assignments |
| ideas | dlc_source | Various | DLC-only ideas |
| focuses | dlc_source | Various | DLC-only focuses |
| equipment_definitions | dlc_source | NSB, MTG, BBA | DLC-only equipment |
| unit_types | dlc_source | Various | DLC-only unit types |
| operations | dlc_source | La Résistance | All operations require LaR |
| operation_tokens | whole table | La Résistance | 5 intel tokens |
| intelligence_agencies | dlc_source | La Résistance | Agency system |
| compliance_modifiers | dlc_source on compliance_80 | La Résistance | Threshold 80 has LaR guard |
| resistance_modifiers | whole table | La Résistance | Resistance threshold system |
| resistance_activities | whole table | La Résistance | Sabotage activity types |
| raid_categories | dlc_source | Götterdämmerung, NCNS | Mixed DLC |
| raids | dlc_source | Götterdämmerung | Most raids |
| mio_templates | whole table | Arms Against Tyranny | Entire MIO system |
| mio_organizations | dlc_source | Various | Per-country DLC checks |
| mio_policies | dlc_source | Arms Against Tyranny | MIO policy system |
| medals | dlc_source | By Blood Alone | Career profile |
| ribbons | dlc_source | By Blood Alone | Career ribbons |
| ace_modifiers | whole table | By Blood Alone | Ace pilot bonuses |
| unit_medals | dlc_source | Götterdämmerung | Unit decorations |
| balance_of_power_definitions | whole table | BBA, AAT, ToA | Per-country BOP |
| continuous_focuses | dlc_source | AAT, BBA | DLC-gated continuous focuses |
| technology_sharing_groups | dlc_source | Together for Victory + others | Research sharing |
| dynamic_modifiers | dlc_source | Various | Per-DLC modifier files |
| scientist_traits | whole table | Götterdämmerung | Special project traits |
| peace_action_categories | whole table | By Blood Alone | Peace overhaul |
| peace_cost_modifiers | dlc_source | By Blood Alone | Peace cost rules |

---

## Validation Strategy and Accuracy Risks

### High-Confidence Domains
- **Provinces** (definition.csv): deterministic CSV parse, 13,382 rows
- **Resources/Buildings**: single source file each, straightforward
- **Technologies**: well-structured, explicit keys
- **Focus trees**: consistent pattern across all files

### Medium-Confidence Domains
- **Country history**: complex nested blocks with dated sections and DLC conditionals
- **Characters**: role-specific fields vary by type; conditional blocks
- **Equipment**: archetype inheritance means many fields are inherited (NULL = use parent)

### Low-Confidence / Known Risks
- **Division templates**: names are not unique IDs; same name in multiple OOB files
- **Focus prerequisites**: AND/OR grouping requires tracking block boundaries
- **Idea modifiers**: 100+ distinct modifier keys; some conditional modifier blocks
- **province_building_positions**: 65,659 rows of floating-point positional data

### Mitigation
- Row count validation after ETL against data dump totals
- FK constraint enforcement catches orphan references
- Unique constraint enforcement prevents duplicates
- Sample spot-checks against game wiki for major nations (GER, SOV, USA, ENG, JAP)

---

## Row Count Estimates (Largest Tables)

| Table | Estimated Rows |
|---|---|
| province_building_positions | 65,659 |
| provinces | 13,382 |
| strategic_region_provinces | 13,437 |
| country_starting_technologies | 11,258 |
| idea_modifiers | 11,105 |
| state_provinces | 10,240 |
| focus links (prereqs + mutual excl.) | 9,673 |
| focuses | 8,498 |
| character_role_traits | ~8,000 |
| ideas | 5,947 |
| character_roles | 5,469 |
| characters | 5,160 |
| divisions | 4,991 |
| division_template_regiments | 4,580 |
| state_buildings | 2,641 |
| ships | ~1,500 |
| division_template_support | ~1,200 |
| states | 1,046 |
| air_wings | ~1,000 |
| state_victory_points | 915 |
| division_templates | 797 |
| supply_nodes | 727 |
| state_resources | 689 |
| technologies | 569 |
| equipment_resources | 454 |
| countries | 352 |
| equipment_definitions | 308 |
| strategic_regions | 298 |

---

## Persisted Deliverables Checklist

- [x] `docs/hoi4-database-design.md` — This file
- [x] `docs/hoi4-table-catalog.md` — Table-by-table specifications
- [x] `docs/hoi4-data-snapshots.md` — Sample rows per table
- [x] `docs/hoi4-source-to-table-map.md` — Complete source→table mapping
- [x] `docs/hoi4-er-diagram.mmd` — Complete Mermaid ER diagram
- [x] `tools/db_etl/manifest.md` — ETL module inventory
- [x] `tools/db_etl/runbook.md` — Extraction pipeline runbook
