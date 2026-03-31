# Unit Types (All Files)

Source: `common/units/*.txt`

| unit_type | abbreviation | group | combat_width | max_strength | max_organisation | default_morale | manpower | training_time | suppression | weight | supply_consumption | source_file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fighter |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| cv_fighter |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| cas |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| cv_cas |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| nav_bomber |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| cv_nav_bomber |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| suicide_craft |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| cv_suicide_craft |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| tac_bomber |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| heavy_fighter |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| scout_plane |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| strat_bomber |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| maritime_patrol_plane |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| jet_fighter |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| jet_tac_bomber |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| jet_strat_bomber |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| rocket_interceptor |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| transport_plane |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| guided_missile |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| explosive_ammo |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| ballistic_missile |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| nuclear_missile |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| sam_missile |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| mothership |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| strat_bomber_intercontinental |  |  |  |  |  |  |  |  |  |  |  | air.txt |
| amphibious_armor | ATK | armor | 2 | 2 | 10 | 0.3 | 500 | 180 |  | 1 | 0.2 | amphibious_armor.txt |
| amphibious_light_armor | LAM | armor | 2 | 2 | 10 | 0.3 | 500 | 180 |  | 1 | 0.2 | amphibious_armor.txt |
| amphibious_medium_armor | MAM | armor | 2 | 2 | 10 | 0.3 | 500 | 180 |  | 1 | 0.2 | amphibious_armor.txt |
| amphibious_heavy_armor | HAM | armor | 2 | 2 | 10 | 0.3 | 500 | 180 |  | 1 | 0.2 | amphibious_armor.txt |
| amphibious_mechanized | AMT | mobile | 2 | 30 | 60 | 0.3 | 1200 | 120 | 1 | 1 | 0.18 | amphibious_mech.txt |
| anti_air | AA | support | 0 | 0.2 | 0 | 0.1 | 300 | 120 |  | 0.1 | 0.1 | anti-air.txt |
| anti_air_brigade | ANA | combat_support | 1 | 0.6 | 0 | 0.1 | 500 | 120 |  | 0.5 | 0.1 | anti-air_brigade.txt |
| mot_anti_air_brigade | MAA | mobile_combat_support | 1 | 0.6 | 0 | 0.1 | 500 | 120 |  | 0.5 | 0.15 | anti-air_brigade.txt |
| anti_tank | AT | support | 0 | 0.2 | 0 | 0.1 | 300 | 120 |  | 0.1 | 0.08 | anti_tank.txt |
| anti_tank_brigade | ANT | combat_support | 1 | 0.6 | 0 | 0 | 500 | 120 |  | 0.5 | 0.1 | anti_tank_brigade.txt |
| mot_anti_tank_brigade | MAT | mobile_combat_support | 1 | 0.6 | 0 | 0 | 500 | 120 |  | 0.5 | 0.15 | anti_tank_brigade.txt |
| armored_car | CAR | mobile | 2 | 5 | 20 | 0.3 | 500 | 180 | 2.5 | 0.8 | 0.14 | armored_car_battalion.txt |
| artillery | ART | support | 0 | 0.2 | 0 | 0.1 | 300 | 120 |  | 0.1 | 0.16 | artillery.txt |
| rocket_artillery | RART | support | 0 | 0.2 | 0 | 0.1 | 300 | 120 |  | 0.1 | 0.16 | artillery.txt |
| super_heavy_artillery | SHART | support | 0 | 0.2 | 0 | 0.1 | 1000 | 180 |  | 0.1 | 0.25 | artillery.txt |
| self_propelled_super_heavy_artillery | SPSHART | support | 0 | 0.2 | 0 | 0.1 | 1000 | 180 |  | 0.1 | 0.35 | artillery.txt |
| artillery_brigade | ART | combat_support | 3 | 0.6 | 0 | 0.1 | 500 | 120 |  | 0.5 | 0.21 | artillery_brigade.txt |
| mot_artillery_brigade | MRT | mobile_combat_support | 3 | 0.6 | 0 | 0.1 | 500 | 120 |  | 0.5 | 0.25 | artillery_brigade.txt |
| rocket_artillery_brigade | RRT | combat_support | 3 | 0.6 | 0 | 0.1 | 500 | 120 |  | 0.5 | 0.22 | artillery_brigade.txt |
| mot_rocket_artillery_brigade | TRA | mobile_combat_support | 3 | 0.6 | 0 | 0.1 | 500 | 120 |  | 0.5 | 0.25 | artillery_brigade.txt |
| motorized_rocket_brigade | MRA | mobile_combat_support | 3 | 0.6 | 0 | 0.1 | 500 | 120 |  | 0.5 | 0.25 | artillery_brigade.txt |
| battle_cruiser |  |  |  |  | 50 |  |  |  |  |  | 0.48 | battlecruiser.txt |
| battleship |  |  |  |  | 50 |  |  |  |  |  | 0.8 | battleship.txt |
| blackshirt_assault_battalion | BAB | support | 0 | 40 | 10 | 0.2 | 1000 | 120 | 1.5 | 0.4 | 0.06 | blackshirt_assault_battalion.txt |
| bus | BUS | mobile | 2 | 400 | 100 | 0.2 | 10 | 120 | 0 | 0.4 | 0.04 | bus.txt |
| carrier |  |  |  |  | 40 |  |  |  |  |  | 1.2 | carrier.txt |
| cavalry | CAV | mobile | 2 | 25 | 70 | 0.3 | 1000 | 120 | 2 | 0.5 | 0.06 | cavalry.txt |
| camelry | CAM | mobile | 2 | 30 | 70 | 0.3 | 1000 | 160 | 2 | 0.6 | 0.1 | cavalry.txt |
| elephantry | ELE | mobile | 2 | 30 | 55 | 0.25 | 1100 | 210 | 2.3 | 1.2 | 0.12 | cavalry.txt |
| destroyer |  |  |  |  | 35 |  |  |  |  |  | 0.04 | destroyer.txt |
| engineer | ENG | support | 0 | 2 | 20 | 0.3 | 300 | 120 |  | 0.1 | 0.02 | engineer.txt |
| pioneer_support | PIO | support | 0 | 2 | 20 | 0.3 | 300 | 120 |  | 0.1 | 0.02 | engineer.txt |
| jungle_pioneers_support | JLS | support | 0 | 1 | 30 | 0.3 | 500 | 120 |  | 0.1 | 0.1 | engineer.txt |
| assault_engineer | ASEC | support | 0 | 2 | 20 | 0.3 | 300 | 120 |  | 0.1 | 0.025 | engineer.txt |
| armored_engineer | AREC | support | 0 | 2 | 20 | 0.3 | 300 | 120 |  | 0.1 | 0.035 | engineer.txt |
| field_hospital | HOS | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.05 | field_hospital.txt |
| helicopter_field_hospital | HELF | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.070 | field_hospital.txt |
| light_flame_tank | LFT | support | 0 | 2 | 20 | 0.3 | 300 | 120 |  | 0.1 | 0.02 | flame_tank.txt |
| medium_flame_tank | MFT | support | 0 | 2 | 20 | 0.3 | 300 | 120 |  | 0.1 | 0.025 | flame_tank.txt |
| heavy_flame_tank | HFT | support | 0 | 2 | 20 | 0.3 | 300 | 120 |  | 0.1 | 0.03 | flame_tank.txt |
| heavy_armor | HTK | armor | 2 | 2 | 10 | 0.3 | 500 | 180 | 2.5 | 1.5 | 0.32 | heavy_armor.txt |
| heavy_cruiser |  |  |  |  | 40 |  |  |  |  |  | 0.4 | heavy_cruiser.txt |
| helicopter_brigade | HELB | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.070 | helicopter_brigade.txt |
| infantry | INF | infantry | 2 | 25 | 60 | 0.3 | 1000 | 90 | 1.5 | 0.5 | 0.06 | infantry.txt |
| bicycle_battalion | BIC | infantry | 2 | 25 | 60 | 0.3 | 1000 | 90 | 2 | 0.5 | 0.06 | infantry.txt |
| marine | MRN | infantry | 2 | 20 | 70 | 0.4 | 1000 | 120 | 1 | 0.5 | 0.05 | infantry.txt |
| marine_commando | MRC | infantry | 2 | 20 | 70 | 0.4 | 1000 | 120 | 1 | 0.5 | 0.05 | infantry.txt |
| mountaineers | MTN | infantry | 2 | 20 | 70 | 0.4 | 1000 | 120 | 1 | 0.5 | 0.05 | infantry.txt |
| ranger_battalion | RANBAT | infantry | 2 | 20 | 70 | 0.4 | 1000 | 120 | 1 | 0.5 | 0.05 | infantry.txt |
| paratrooper | PAR | infantry | 2 | 22 | 70 | 0.4 | 1000 | 150 | 1 | 0.5 | 0.05 | infantry.txt |
| motorized | MOT | mobile | 2 | 25 | 60 | 0.30 | 1200 | 90 | 2.2 | 0.75 | 0.065 | infantry.txt |
| mechanized | MEC | mobile | 2 | 30 | 60 | 0.3 | 1200 | 120 | 2 | 1 | 0.14 | infantry.txt |
| fake_intel_unit |  | infantry | 1 | 1 | 100 | 0.3 | 0 | 90 | 1 | 0.5 | 0.0 | infantry.txt |
| penal_battalion | PEN | infantry | 2 | 15 | 70 | 0.4 | 850 | 50 | 0.5 | 0.5 | 0.05 | infantry.txt |
| irregular_infantry | IRR | infantry | 2 | 30 | 45 | 0.2 | 1000 | 30 | 1.5 | 0.5 | 0.04 | infantry.txt |
| militia | MIL | infantry | 2 | 25 | 50 | 0.3 | 1000 | 80 | 1.5 | 0.5 | 0.06 | infantry.txt |
| land_cruiser | LCB | support | 0 | 15 | 60 | 0.3 | 1000 | 250 | 4 | 2 | 0.6 | land_cruiser.txt |
| light_armor | LTK | armor | 2 | 2 | 10 | 0.3 | 500 | 180 | 2.5 | 1 | 0.22 | light_armor.txt |
| light_cruiser |  |  |  |  | 40 |  |  |  |  |  | 0.16 | light_cruiser.txt |
| logistics_company | LOG | support | 0 | 1 | 10 | 0.3 | 500 | 120 |  | 0.1 |  | logistics.txt |
| helicopter_transport | HELT | support | 0 | 1 | 12 | 0.3 | 500 | 120 |  | 0.1 |  | logistics.txt |
| maintenance_company | MAIN | support | 0 | 1 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.03 | maintenance.txt |
| armored_maintenance | AMC | support | 0 | 0.1 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.035 | maintenance.txt |
| medium_armor | MTK | armor | 2 | 2 | 10 | 0.3 | 500 | 180 | 2.5 | 1.25 | 0.25 | medium_armor.txt |
| military_police | MP | support | 0 | 1 | 0 | 0.20 | 500 | 180 |  | 0.1 | 0.02 | military_police.txt |
| motorized_military_police | MMP | support | 0 | 2 | 10 | 0.20 | 500 | 200 |  | 0.1 | 0.03 | military_police.txt |
| modern_armor | OTK | armor | 2 | 2 | 10 | 0.3 | 500 | 180 | 2.5 | 1.5 | 0.25 | modern_armor.txt |
| railway_gun |  |  |  | 2000 |  |  |  |  |  | 1 | 0.2 | railway_gun.txt |
| super_heavy_railway_gun |  |  |  | 3500 |  |  |  |  |  | 1 | 0.5 | railway_gun.txt |
| recon | CREC | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.02 | recon.txt |
| mot_recon | MREC | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.02 | recon.txt |
| armored_car_recon | AREC | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.02 | recon.txt |
| light_tank_recon | TREC | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.02 | recon.txt |
| airborne_light_armor | LTA | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.02 | recon.txt |
| rangers_support | RAN | support | 0 | 2 | 30 | 0.3 | 500 | 120 |  | 0.1 | 0.06 | recon.txt |
| winter_logistics_support | WIN | support | 0 | 2 | 45 | 0.3 | 500 | 120 |  | 0.1 | 0.05 | recon.txt |
| long_range_patrol_support | LRP | support | 0 | 10 | 60 | 0.3 | 500 | 120 |  | 0.3 | 0.04 | recon.txt |
| helicopter_recon | HELR | support | 0 | 2 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.070 | recon.txt |
| repair_ship |  |  |  |  | 40 |  |  |  |  |  | 0.04 | repair_ships.txt |
| signal_company | SIG | support | 0 | 1 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.02 | signal.txt |
| armored_signal | ASC | support | 0 | 1 | 20 | 0.3 | 500 | 120 |  | 0.1 | 0.035 | signal.txt |
| light_sp_anti_air_brigade | LAA | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 0.75 | 1 | 0.1 | sp_anti-air_brigade.txt |
| medium_sp_anti_air_brigade | MAA | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 0.8 | 1.25 | 0.1 | sp_anti-air_brigade.txt |
| heavy_sp_anti_air_brigade | HAA | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 0.75 | 1.5 | 0.1 | sp_anti-air_brigade.txt |
| super_heavy_sp_anti_air_brigade | SAA | support | 0 | 0.6 | 0 | 0.1 | 500 | 180 | 0.75 | 1.75 | 0.1 | sp_anti-air_brigade.txt |
| modern_sp_anti_air_brigade | OAA | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 2 | 1.5 | 0.1 | sp_anti-air_brigade.txt |
| light_sp_artillery_brigade | LAR | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 1.25 | 1 | 0.42 | sp_artillery_brigade.txt |
| medium_sp_artillery_brigade | MAR | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 1.5 | 1.25 | 0.46 | sp_artillery_brigade.txt |
| heavy_sp_artillery_brigade | HAR | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 1.5 | 1.5 | 0.6 | sp_artillery_brigade.txt |
| super_heavy_sp_artillery_brigade | SAR | support | 0 | 0.6 | 0 | 0.1 | 500 | 180 | 1.25 | 1.75 | 0.8 | sp_artillery_brigade.txt |
| modern_sp_artillery_brigade | OAR | armor_combat_support | 2 | 0.6 | 0 | 0.1 | 500 | 180 | 1.5 | 1.5 | 0.5 | sp_artillery_brigade.txt |
| sturmtruppe_battalion | STB | support | 0 | 20 | 70 | 0.4 | 1000 | 120 | 1 | 0.5 | 0.05 | sturmtruppe_battalion.txt |
| submarine |  |  |  |  | 30 |  |  |  |  |  | 0.04 | submarine.txt |
| super_heavy_armor | STK | support | 0 | 2 | 10 | 0.3 | 500 | 180 | 2.5 | 1.0 | 0.4 | super_heavy_armor.txt |
| support_ship |  |  |  |  | 40 |  |  |  |  |  | 0.04 | support_ships.txt |
| light_tank_destroyer_brigade | LTD | armor_combat_support | 2 | 0.6 | 0 | 0.3 | 500 | 180 | 1.0 | 1 | 0.2 | tank_destroyer_brigade.txt |
| medium_tank_destroyer_brigade | MTD | armor_combat_support | 2 | 0.6 | 0 | 0.3 | 500 | 180 | 1.25 | 1.25 | 0.22 | tank_destroyer_brigade.txt |
| heavy_tank_destroyer_brigade | HTD | armor_combat_support | 2 | 0.6 | 0 | 0.3 | 500 | 180 | 1.25 | 1.5 | 0.3 | tank_destroyer_brigade.txt |
| super_heavy_tank_destroyer_brigade | STD | support | 0 | 0.6 | 0 | 0.3 | 500 | 180 | 1.25 | 1.75 | 0.4 | tank_destroyer_brigade.txt |
| modern_tank_destroyer_brigade | OTD | armor_combat_support | 2 | 0.6 | 0 | 0.3 | 500 | 180 | 1.25 | 1.5 | 0.25 | tank_destroyer_brigade.txt |
