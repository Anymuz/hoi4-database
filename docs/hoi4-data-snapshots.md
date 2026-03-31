# HOI4 Data Snapshots

Status: **COMPLETE** (all phases)

## Purpose
Extracted sample rows per table to validate mapping accuracy before SQL generation.

---

## Phase 1 — Global Reference Tables

### continents
Source: `map/continent.txt`

| continent_id | continent_key |
|---|---|
| 1 | europe |
| 2 | north_america |
| 3 | south_america |
| 4 | australia |
| 5 | africa |
| 6 | asia |
| 7 | middle_east |

### terrain_types
Source: `map/definition.csv` (distinct terrain values)

| terrain_type |
|---|
| forest |
| hills |
| mountain |
| plains |
| marsh |
| desert |
| urban |
| jungle |
| ocean |
| lakes |
| unknown |

### state_categories
Source: `history/states/*.txt`

| state_category |
|---|
| city |
| enclave |
| large_city |
| large_island |
| large_town |
| megalopolis |
| metropolis |
| pastoral |
| rural |
| small_island |
| tiny_island |
| town |
| wasteland |

### ideologies
Source: `common/ideologies/00_ideologies.txt`

| ideology_key | color_r | color_g | color_b |
|---|---|---|---|
| democratic | 0 | 0 | 255 |
| communism | 255 | 0 | 0 |
| fascism | 150 | 75 | 0 |
| neutrality | 124 | 124 | 124 |

### sub_ideologies
Source: `common/ideologies/00_ideologies.txt`

| sub_ideology_key | ideology_key |
|---|---|
| conservatism | democratic |
| marxism | communism |
| nazism | fascism |
| despotism | neutrality |
| socialism | democratic |
| stalinism | communism |
| fascism_ideology | fascism |
| oligarchism | neutrality |

### resource_types
Source: `common/resources/00_resources.txt`

| resource_key | icon_frame | cic | convoys |
|---|---|---|---|
| oil | 1 | 0.125 | 0.1 |
| aluminium | 2 | 0.125 | 0.1 |
| rubber | 3 | 0.125 | 0.1 |
| tungsten | 4 | 0.125 | 0.1 |
| steel | 5 | 0.125 | 0.1 |
| chromium | 6 | 0.125 | 0.1 |
| coal | 7 | 0.125 | 0.1 |

### unit_types (sample)
Source: `common/units/*.txt`

| unit_type_key | abbreviation | unit_group | combat_width | manpower | training_time | source_file |
|---|---|---|---|---|---|---|
| amphibious_armor | ATK | armor | 2 | 500 | 180 | amphibious_armor.txt |
| anti_air | AA | support | 0 | 300 | 120 | anti-air.txt |
| anti_air_brigade | ANA | combat_support | 1 | 500 | 120 | anti-air_brigade.txt |
| anti_tank | AT | support | 0 | 300 | 120 | anti_tank.txt |
| infantry | INF | infantry | 2 | 1000 | 120 | infantry.txt |

### equipment_definitions (sample)
Source: `common/units/equipment/*.txt`

| equipment_key | is_archetype | archetype_key | year | build_cost_ic | soft_attack | hard_attack | source_file |
|---|---|---|---|---|---|---|---|
| infantry_equipment | yes | — | 1933 | 0.5 | 6 | 1 | infantry.txt |
| infantry_equipment_0 | no | infantry_equipment | 1933 | — | — | — | infantry.txt |
| infantry_equipment_1 | no | infantry_equipment | 1936 | 0.5 | 6 | 1.5 | infantry.txt |
| artillery_equipment | yes | — | 1934 | 3.5 | 25 | 2 | artillery.txt |
| fighter_equipment_0 | no | fighter_equipment | 1933 | — | — | — | air_techs.txt |

### equipment_resources (sample)
Source: `common/units/equipment/*.txt`

| equipment_key | resource_key | amount | source_file |
|---|---|---|---|
| anti_air_equipment | steel | 2 | anti_air.txt |
| anti_tank_equipment | tungsten | 2 | anti_tank.txt |
| anti_tank_equipment | steel | 2 | anti_tank.txt |
| artillery_equipment | tungsten | 1 | artillery.txt |
| artillery_equipment | steel | 2 | artillery.txt |

### technologies (sample)
Source: `common/technologies/*.txt`

| technology_key | research_cost | start_year | folder_name | category | source_file |
|---|---|---|---|---|---|
| early_fighter | 2 | 1933 | air_techs_folder | light_air | air_techs.txt |
| fighter1 | 2 | 1936 | air_techs_folder | light_air | air_techs.txt |
| infantry_weapons | 2 | 1918 | infantry_folder | infantry_tech | infantry.txt |
| gwtank | 2 | 1918 | armor_folder | armor | armor.txt |
| basic_light_tank | 2 | 1934 | armor_folder | armor | armor.txt |

---

## Phase 2 — Geography

### provinces (sample)
Source: `map/definition.csv`

| province_id | map_r | map_g | map_b | province_kind | is_coastal | terrain | continent_id |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | land | false | unknown | 0 |
| 2 | 0 | 0 | 55 | land | false | forest | 1 |
| 4 | 0 | 0 | 232 | sea | true | ocean | 0 |
| 8 | 0 | 3 | 225 | land | false | hills | 1 |
| 1 | 230 | 81 | 119 | lake | false | lakes | 7 |

### province_building_positions (sample)
Source: `map/buildings.txt`

| province_id | building_type | pos_x | pos_y | pos_z | rotation | linked_province_id |
|---|---|---|---|---|---|---|
| 1 | arms_factory | 2946.00 | 11.63 | 1364.00 | 0.45 | — |
| 1 | industrial_complex | 2950.00 | 12.05 | 1361.00 | 3.12 | — |
| 1 | air_base | 2948.38 | 11.60 | 1359.45 | 0.15 | — |
| 1 | naval_base_spawn | 2954.00 | 9.70 | 1370.00 | 0.98 | 5579 |
| 1 | bunker | 2946.00 | 11.63 | 1364.00 | 5.69 | — |

### strategic_regions (sample)
Source: `map/strategicregions/*.txt`

| strategic_region_id | name_key | province_count | source_file |
|---|---|---|---|
| 1 | STRATEGICREGION_1 | 43 | 1-Southern England.txt |
| 10 | STRATEGICREGION_10 | 78 | 10-Southern Sweden.txt |
| 100 | STRATEGICREGION_100 | 9 | 100-Red Sea.txt |
| 126 | STRATEGICREGION_126 | 67 | 126-North Africa.txt |
| 129 | STRATEGICREGION_129 | 169 | 129-Asia minor.txt |

### supply_nodes (sample)
Source: `map/supply_nodes.txt`

| province_id | level |
|---|---|
| 67 | 1 |
| 101 | 1 |
| 121 | 1 |
| 241 | 1 |
| 306 | 1 |

### states (sample)
Source: `history/states/*.txt`

| state_id | state_name_key | manpower | state_category |
|---|---|---|---|
| 1 | STATE_1 | 43310 | town |
| 64 | STATE_64 | 5804412 | metropolis |
| 907 | STATE_907 | 6454865 | town |
| 219 | STATE_219 | 6814000 | megalopolis |
| 446 | STATE_446 | 2000000 | large_city |

---

## Phase 3 — Countries

### countries (sample)
Source: `common/country_tags/00_countries.txt`, `common/countries/*.txt`, `history/countries/*.txt`

| tag | country_file_path | color_r | color_g | color_b | capital_state_id | stability | war_support |
|---|---|---|---|---|---|---|---|
| GER | countries/Germany.txt | 106 | 119 | 89 | 64 | — | — |
| ENG | countries/United Kingdom.txt | 201 | 56 | 91 | 126 | 0.8 | 0.65 |
| SOV | countries/Soviet Union.txt | 220 | 0 | 0 | 219 | — | — |
| USA | countries/United States.txt | 83 | 101 | 164 | 361 | 0.96 | 0.1 |
| JAP | countries/Japan.txt | 192 | 116 | 67 | 282 | — | — |

### country_starting_technologies (sample)
Source: `history/countries/*.txt`

| country_tag | technology_key | source_file |
|---|---|---|
| GER | infantry_weapons | GER - Germany.txt |
| GER | infantry_weapons1 | GER - Germany.txt |
| GER | early_fighter | GER - Germany.txt |
| GER | gwtank | GER - Germany.txt |
| ENG | infantry_weapons | ENG - United Kingdom.txt |

### country_starting_ideas (sample, estimated from country history)
Source: `history/countries/*.txt`

| country_tag | idea_key | effective_date |
|---|---|---|
| GER | export_focus | 1936-01-01 |
| GER | partial_economic_mobilisation | 1936-01-01 |
| ENG | limited_exports | 1936-01-01 |
| USA | undisturbed_isolation | 1936-01-01 |
| SOV | civilian_economy | 1936-01-01 |

---

## Phase 4 — Technologies

### technology_prerequisites (sample)
Source: `common/technologies/*.txt`

| technology_key | prerequisite_key | source_file |
|---|---|---|
| fighter1 | early_fighter | air_techs.txt |
| fighter2 | fighter1 | air_techs.txt |
| fighter3 | fighter2 | air_techs.txt |
| basic_light_tank | gwtank | armor.txt |
| improved_light_tank | basic_light_tank | armor.txt |

### technology_enables_equipment (sample)
Source: `common/technologies/*.txt`

| technology_key | equipment_key | source_file |
|---|---|---|
| early_fighter | fighter_equipment_0 | air_techs.txt |
| fighter1 | fighter_equipment_1 | air_techs.txt |
| early_transport_plane | transport_plane_equipment_1 | air_techs.txt |
| infantry_weapons | infantry_equipment_0 | infantry.txt |
| gwtank | gw_tank_equipment | armor.txt |

---

## Phase 5 — Characters

### characters (sample)
Source: `common/characters/*.txt`

| character_id | name_key | country_tag | gender | source_file |
|---|---|---|---|---|
| GER_adolf_hitler | GER_adolf_hitler | GER | male | GER.txt |
| GER_erwin_rommel | GER_erwin_rommel | GER | male | GER.txt |
| GER_karl_donitz | GER_karl_donitz | GER | male | GER.txt |
| SOV_joseph_stalin | SOV_joseph_stalin | SOV | male | SOV.txt |
| ENG_winston_churchill | ENG_winston_churchill | ENG | male | ENG.txt |

### character_roles (sample)
Source: `common/characters/*.txt`

| character_id | role_type | sub_ideology_key | skill | attack_skill | defense_skill |
|---|---|---|---|---|---|
| GER_adolf_hitler | country_leader | nazism | — | — | — |
| GER_konrad_adenauer | country_leader | conservatism | — | — | — |
| GER_werner_von_blomberg | field_marshal | — | 3 | 2 | 3 |
| GER_erwin_rommel | advisor | — | — | — | — |
| GER_karl_donitz | advisor | — | — | — | — |

---

## Phase 6 — Division Templates & OOB

### division_templates (sample)
Source: `history/units/*.txt`

| country_tag | template_name | division_names_group | oob_file |
|---|---|---|---|
| GER | Infanterie-Division | GER_INF_01 | GER_1936.txt |
| GER | Panzer-Division | GER_ARM_01 | GER_1936.txt |
| ENG | Infantry Division | ENG_INF_01 | ENG_1936.txt |
| SOV | Strelkovaya Divisiia | SOV_INF_01 | SOV_1936.txt |
| USA | Infantry Division | USA_INF_01 | USA_1936.txt |

### division_template_regiments (sample — GER Infanterie-Division)
Source: `history/units/GER_1936.txt`

| template_name | unit_type_key | grid_x | grid_y |
|---|---|---|---|
| Infanterie-Division | infantry | 0 | 0 |
| Infanterie-Division | infantry | 0 | 1 |
| Infanterie-Division | infantry | 0 | 2 |
| Infanterie-Division | infantry | 1 | 0 |
| Infanterie-Division | infantry | 1 | 1 |
| Infanterie-Division | infantry | 1 | 2 |

### division_template_support (sample — GER)
Source: `history/units/GER_1936.txt`

| template_name | unit_type_key | grid_x | grid_y |
|---|---|---|---|
| Infanterie-Division | engineer | 0 | 0 |
| Infanterie-Division | artillery | 0 | 1 |
| Panzer-Division | mot_recon | 0 | 0 |
| Panzer-Division | engineer | 0 | 1 |
| Panzer-Division | artillery | 0 | 2 |

### divisions (sample)
Source: `history/units/*.txt`

| country_tag | template_name | location_province_id | start_experience_factor | oob_file |
|---|---|---|---|---|
| AFG | Royal Guard | 10737 | 0.3 | AFG_1936.txt |
| GER | Infanterie-Division | 6389 | 0.3 | GER_1936.txt |
| GER | Panzer-Division | 3562 | 0.3 | GER_1936.txt |
| ENG | Infantry Division | 3839 | — | ENG_1936.txt |
| SOV | Strelkovaya Divisiia | 217 | — | SOV_1936.txt |

---

## Phase 7 — Naval OOB

### fleets (sample — GER)
Source: `history/units/GER_1936_naval_mtg.txt`

| country_tag | fleet_name | naval_base_province_id | oob_file |
|---|---|---|---|
| GER | Kriegsmarine | 241 | GER_1936_naval_mtg.txt |
| GER | Unterseeboots-Flotte | 6389 | GER_1936_naval_mtg.txt |

### task_forces (sample — GER)
Source: `history/units/GER_1936_naval_mtg.txt`

| fleet_name | task_force_name | location_province_id |
|---|---|---|
| Kriegsmarine | Hochseeflotte | 241 |
| Kriegsmarine | Ostseeflotte | 6332 |
| Kriegsmarine | Marineschule Kiel | 6389 |
| Unterseeboots-Flotte | I. U-Boots Flottille Weddigen | 6389 |
| Unterseeboots-Flotte | II. U-Boots-Ausbildungs-Gruppe | 241 |

### ships (sample — GER)
Source: `history/units/GER_1936_naval_mtg.txt`

| task_force_name | ship_name | definition | hull_equipment_key | version_name | owner_tag | pride_of_the_fleet |
|---|---|---|---|---|---|---|
| Hochseeflotte | Deutschland | heavy_cruiser | ship_hull_cruiser_panzerschiff | Deutschland | GER | no |
| Hochseeflotte | Admiral Scheer | heavy_cruiser | ship_hull_cruiser_panzerschiff | Deutschland | GER | yes |
| Hochseeflotte | Nürnberg | light_cruiser | ship_hull_cruiser_2 | Leipzig | GER | no |
| Hochseeflotte | Jaguar | destroyer | ship_hull_light_1 | Type 24 | GER | no |
| I. U-Boots Flottille Weddigen | U-7 | submarine | ship_hull_submarine_1 | Type II | GER | no |

---

## Phase 8 — Air OOB

### air_wings (sample — GER)
Source: `history/units/GER_1936_air_bba.txt`

| country_tag | location_state_id | wing_name | equipment_type | amount | version_name |
|---|---|---|---|---|---|
| GER | 763 | — | small_plane_airframe_0 | 40 | He 51 |
| GER | 64 | — | small_plane_airframe_0 | 80 | He 51 |
| GER | 64 | Jagdgeschwader 132 | medium_plane_airframe_0 | 80 | Do 23 |
| GER | 64 | Kampfgeschwader 153 | transport_plane_equipment_1 | 80 | — |
| GER | 58 | — | small_plane_naval_bomber_airframe_1 | 72 | Do 22 |

---

## Phase 9 — Ideas & National Spirits

### ideas (sample)
Source: `common/ideas/*.txt`

| idea_key | slot | is_law | cost | removal_cost | is_default | source_file |
|---|---|---|---|---|---|---|
| civilian_economy | economy | yes | 150 | -1 | yes | _economic.txt |
| war_economy | economy | yes | 150 | -1 | no | _economic.txt |
| export_focus | trade_laws | yes | 150 | -1 | yes | _economic.txt |
| free_trade | trade_laws | yes | 150 | -1 | no | _economic.txt |
| fascist_assault_divisions | country | no | — | — | no | _event.txt |

### idea_modifiers (sample)
Source: `common/ideas/*.txt`

| idea_key | modifier_key | modifier_value |
|---|---|---|
| civilian_economy | consumer_goods_expected_value | 0.35 |
| civilian_economy | production_speed_industrial_complex_factor | -0.3 |
| civilian_economy | production_speed_arms_factory_factor | -0.1 |
| war_economy | consumer_goods_expected_value | 0.20 |
| free_trade | min_export | 0.80 |

---

## Phase 10 — Focus Trees

### focus_trees (sample)
Source: `common/national_focus/*.txt`

| focus_tree_id | country_tag | initial_x | initial_y | source_file |
|---|---|---|---|---|
| german_focus | GER | 76 | 0 | germany.txt |
| generic_focus | — | — | — | generic.txt |
| argentine_focus_tree | ARG | 25 | 0 | argentina.txt |
| finnish_focus | FIN | 23 | 0 | finland.txt |
| french_focus | FRA | — | — | france.txt |

### focuses (sample)
Source: `common/national_focus/*.txt`

| focus_id | focus_tree_id | cost | x_pos | y_pos | icon | source_file |
|---|---|---|---|---|---|---|
| AFG_expand_telegraph_network | afghanistan_tree | 5 | -21 | 0 | GFX_focus_AFG_telegraph | afghanistan.txt |
| AFG_sugar_processing | afghanistan_tree | 10 | 1 | 1 | GFX_focus_AFG_sugar_factory | afghanistan.txt |
| AFG_clear_malarial_swamps | afghanistan_tree | 5 | -8 | 1 | GFX_focus_AFG_anti_malaria | afghanistan.txt |
| AFG_iron_mines | afghanistan_tree | 10 | -1 | 1 | GFX_focus_generic_steel | afghanistan.txt |
| AFG_modern_economy | afghanistan_tree | 10 | 1 | 1 | GFX_focus_AFG_a_modern_economy | afghanistan.txt |

### focus_prerequisites (sample)
Source: `common/national_focus/*.txt`

| focus_id | prerequisite_group | required_focus_id |
|---|---|---|
| AFG_sugar_processing | 0 | AFG_expand_telegraph_network |
| AFG_fruit_packing | 0 | AFG_expand_telegraph_network |
| AFG_iron_mines | 0 | AFG_kajaki_dam |
| AFG_modern_economy | 0 | AFG_iron_mines |
| AFG_expand_karakul_lambskin_industry | 0 | AFG_fruit_packing |

### focus_mutually_exclusive (sample)
Source: `common/national_focus/*.txt`

| focus_a_id | focus_b_id |
|---|---|
| AFG_look_to_other_partners | AFG_renew_soviet_trade_agreement |

