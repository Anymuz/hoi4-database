# Decisions (All Files)

Source: `common/decisions/*.txt`

| decision_key | category_key | icon | cost | fire_only_once | dlc_source | source_file |
|---|---|---|---|---|---|---|
| debug_show_decisions | debug_decisions |  |  |  |  | _debug_decisions.txt |
| debug_hide_decisions | debug_decisions |  |  |  |  | _debug_decisions.txt |
| debug_max_infleunce | debug_decisions |  |  |  |  | _debug_decisions.txt |
| debug_calc_resources | debug_decisions |  |  |  |  | _debug_decisions.txt |
| research_all_tank_techs_nsb | debug_decisions | generic_tank |  |  |  | _debug_decisions.txt |
| add_efficiency_growth_debug | debug_decisions | generic_research | 0 |  |  | _debug_decisions.txt |
| remove_efficiency_growth_debug | debug_decisions | generic_research | 0 |  |  | _debug_decisions.txt |
| decrease_efficiency_growth_debug | debug_decisions | generic_research | 0 |  |  | _debug_decisions.txt |
| history_entry_debug | debug_decisions | generic_research | 0 |  |  | _debug_decisions.txt |
| create_operative_debug | debug_decisions | generic_research | 0 |  |  | _debug_decisions.txt |
| create_recruitable_operative_not_to_spy_master_debug | debug_decisions | generic_research | 0 |  |  | _debug_decisions.txt |
| create_recruitable_operative_debug | debug_decisions | generic_research | 0 |  |  | _debug_decisions.txt |
| FRA_capture_operative_debug | debug_decisions |  | 0 |  |  | _debug_decisions.txt |
| FRA_turn_operative_debug | debug_decisions |  | 0 |  |  | _debug_decisions.txt |
| harm_operative_debug | debug_decisions |  | 0 |  |  | _debug_decisions.txt |
| add_random_nationality | debug_decisions |  | 0 |  |  | _debug_decisions.txt |
| add_1_convoy | debug_decisions |  | 0 |  |  | _debug_decisions.txt |
| slot_machine | debug_decisions |  |  |  |  | _debug_decisions.txt |
| decryption_tech_1 | debug_decisions |  |  |  |  | _debug_decisions.txt |
| decryption_tech_2 | debug_decisions |  |  |  |  | _debug_decisions.txt |
| decryption_tech_3 | debug_decisions |  |  |  |  | _debug_decisions.txt |
| encryption_tech_1 | debug_decisions |  |  |  |  | _debug_decisions.txt |
| encryption_tech_2 | debug_decisions |  |  |  |  | _debug_decisions.txt |
| encryption_tech_3 | debug_decisions |  |  |  |  | _debug_decisions.txt |
| plane_generator_test | debug_decisions |  |  |  |  | _debug_decisions.txt |
| debug_clr_dreadnought_flags | debug_decisions | GFX_decision_generic_naval | 0 |  |  | _debug_decisions.txt |
| unlock_supersonic_jet | debug_decisions |  |  |  |  | _debug_decisions.txt |
| unlock_all_radars | debug_decisions |  |  |  |  | _debug_decisions.txt |
| debug_gain_claimed_states | debug_decisions |  |  |  |  | _debug_decisions.txt |
| request_reinstatement | governments_in_exile | generic_independence | 10 |  |  | _exiled_governments_decisions.txt |
| grant_parliamentary_audience | governments_in_exile | eng_install_government |  |  |  | _exiled_governments_decisions.txt |
| lobby_for_parliamentary_support | governments_in_exile | eng_install_government |  |  |  | _exiled_governments_decisions.txt |
| public_support_for_from | governments_in_exile | eng_install_government |  |  |  | _exiled_governments_decisions.txt |
| exile_recruitment_campaign | governments_in_exile | eng_propaganda_campaigns |  |  |  | _exiled_governments_decisions.txt |
| exile_extraction_campaign | governments_in_exile | oppression | 0 |  |  | _exiled_governments_decisions.txt |
| purge_infiltrators | governments_in_exile | generic_political_discourse |  |  |  | _exiled_governments_decisions.txt |
| expatriate_donations | governments_in_exile | ger_military_buildup | 25 |  |  | _exiled_governments_decisions.txt |
| request_control_of_navy | governments_in_exile | generic_naval | 25 | yes |  | _exiled_governments_decisions.txt |
| weapons_for_the_resistance | category_exile_forces | generic_ignite_civil_war | 50 |  |  | _exiled_governments_decisions.txt |
| unity_parade | category_exile_forces | generic_nationalism | 50 | yes |  | _exiled_governments_decisions.txt |
| joint_training_exercise | category_exile_forces | eng_blackshirt_march | 0 |  |  | _exiled_governments_decisions.txt |
| targeted_race_for_the_bomb | political_actions | generic_research |  |  |  | _generic_decisions.txt |
| improved_worker_conditions | political_actions | generic_industry | 100 |  |  | _generic_decisions.txt |
| dismantle_maginot | economy_decisions | generic_construction | 50 | yes |  | _generic_decisions.txt |
| restructure_supply_system | economy_decisions | GFX_decision_generic_construction |  | yes |  | _generic_decisions.txt |
| seize_some_trains_woo | economy_decisions | GFX_decision_hol_draw_up_staff_plans |  |  |  | _generic_decisions.txt |
| war_propaganda | propaganda_efforts | generic_prepare_civil_war | 150 |  | La Resistance | _generic_decisions.txt |
| war_propaganda_casualties | propaganda_efforts | generic_prepare_civil_war | 100 |  |  | _generic_decisions.txt |
| war_propaganda_convoys | propaganda_efforts | GFX_decision_generic_naval | 100 |  |  | _generic_decisions.txt |
| war_propaganda_bombing | propaganda_efforts | GFX_decision_generic_air | 100 |  |  | _generic_decisions.txt |
| war_propaganda_radio_industry | propaganda_efforts | generic_prepare_civil_war | 75 | yes | Trial of Allegiance | _generic_decisions.txt |
| war_propaganda_film_industry | propaganda_efforts | generic_prepare_civil_war | 100 | yes | La Resistance | _generic_decisions.txt |
| blow_suez_canal | operations | GFX_decision_generic_ignite_civil_war | 75 |  | Waking the Tiger | _generic_decisions.txt |
| blow_panama_canal | operations | GFX_decision_generic_ignite_civil_war | 75 |  | Waking the Tiger | _generic_decisions.txt |
| rebuild_suez_canal | special_projects | GFX_decision_generic_special_project | 120 |  |  | _generic_decisions.txt |
| rebuild_panama_canal | special_projects | GFX_decision_generic_special_project | 400 |  |  | _generic_decisions.txt |
| emergency_factory_conversion_defensive | war_measures | generic_industry | 100 |  |  | _generic_decisions.txt |
| emergency_factory_conversion_offensive | war_measures | generic_industry | 100 |  |  | _generic_decisions.txt |
| desperate_defense | war_measures | generic_prepare_civil_war | 50 |  |  | _generic_decisions.txt |
| women_in_the_workforce | war_measures | generic_industry | 100 |  |  | _generic_decisions.txt |
| war_bonds | war_measures | generic_industry |  |  |  | _generic_decisions.txt |
| diversify_special_forces | war_measures | GFX_decision_generic_military | 50 | yes | Arms Against Tyranny | _generic_decisions.txt |
| object_to_attaches | foreign_politics |  | 50 |  | Waking the Tiger | _generic_decisions.txt |
| infrastructure_building_slot | economy_decisions | generic_construction | 100 |  |  | _generic_decisions.txt |
| war_building_slot | economy_decisions | generic_construction | 50 |  | Man the Guns | _generic_decisions.txt |
| CHI_close_burma_road | foreign_support |  | 0 |  |  | _generic_decisions.txt |
| CHI_reopen_burma_road | foreign_support |  | 0 |  |  | _generic_decisions.txt |
| CHI_close_ledo_road | foreign_support |  | 0 |  |  | _generic_decisions.txt |
| CHI_reopen_ledo_road | foreign_support |  | 0 |  |  | _generic_decisions.txt |
| CHI_close_the_hump | foreign_support |  | 0 |  |  | _generic_decisions.txt |
| CHI_reopen_the_hump | foreign_support |  | 0 |  |  | _generic_decisions.txt |
| CHI_close_hanoi_route | foreign_support |  | 0 |  |  | _generic_decisions.txt |
| purchase_ships_eng | generic_purchase_old_ships_category | GFX_decision_generic_naval | 50 |  |  | _generic_decisions.txt |
| purchase_ships_sov | generic_purchase_old_ships_category | GFX_decision_generic_naval | 50 |  |  | _generic_decisions.txt |
| purchase_ships_ger | generic_purchase_old_ships_category | GFX_decision_generic_naval | 50 |  |  | _generic_decisions.txt |
| purchase_ships_usa | generic_purchase_old_ships_category | GFX_decision_generic_naval | 50 |  |  | _generic_decisions.txt |
| refit_to_destroyer | generic_refit_civilian_ships_category | GFX_decision_generic_merge_plant_ship | 15 |  | Man the Guns | _generic_decisions.txt |
| refit_to_cruiser | generic_refit_civilian_ships_category | GFX_decision_generic_merge_plant_ship | 30 |  | Man the Guns | _generic_decisions.txt |
| invite_GER_henschel_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_GER_heinkel_organization | foreign_mio_decisions_category | generic_air | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_GER_junkers_organization | foreign_mio_decisions_category | generic_air | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_GER_opel_organization | foreign_mio_decisions_category | generic_motorized | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_GER_mauser_organization | foreign_mio_decisions_category | generic_prepare_civil_war | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_SOV_okmo_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_SOV_nevskoye_design_bureau_organization | foreign_mio_decisions_category | generic_naval | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_SOV_ilyushin_design_bureau_organization | foreign_mio_decisions_category | generic_air | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_SOV_gaz_organization | foreign_mio_decisions_category | generic_motorized | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ENG_vickers_armstrong_eng_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ENG_yarrow_shipbuilders_organization | foreign_mio_decisions_category | generic_naval | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ENG_john_brown_organization | foreign_mio_decisions_category | generic_naval | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ENG_fairey_aviation_organization | foreign_mio_decisions_category | generic_air | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ENG_vauxhall_organization | foreign_mio_decisions_category | generic_motorized | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ITA_fiat_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ITA_crda_organization | foreign_mio_decisions_category | generic_naval | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_ITA_lancia_organization | foreign_mio_decisions_category | generic_motorized | 50 | yes | Battle for the Bosporus | aat_mio_decisions.txt |
| invite_CZE_ckd_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_CZE_skoda_armor_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_CZE_avia_organization | foreign_mio_decisions_category | generic_air | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_CZE_skoda_artillery_organization | foreign_mio_decisions_category | generic_industry | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_FRA_renault_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_FRA_bloch_organization | foreign_mio_decisions_category | generic_air | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_FRA_mas_organization | foreign_mio_decisions_category | generic_prepare_civil_war | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_JAP_maizuru_naval_arsenal_organization | foreign_mio_decisions_category | generic_naval | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_JAP_mitsubishi_organization | foreign_mio_decisions_category | generic_air | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_JAP_nissan_organization | foreign_mio_decisions_category | generic_motorized | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_SWE_landsverk_organization | foreign_mio_decisions_category | generic_tank | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_SWE_volvo_organization | foreign_mio_decisions_category | generic_motorized | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| invite_SWE_bofors_organization | foreign_mio_decisions_category | generic_industry | 50 | yes | By Blood Alone | aat_mio_decisions.txt |
| AFG_propose_oil_concession_deal | AFG_oil_concessions_category | GFX_decision_oil | 0 |  |  | AFG.txt |
| AFG_nationalize_oil | AFG_oil_concessions_category | GFX_decision_oil | 0 |  |  | AFG.txt |
| AFG_radical_students_countdown | AFG_radical_students_category | GFX_decision_revolt |  |  |  | AFG.txt |
| AFG_placate_the_graduates | AFG_radical_students_category | GFX_decision_generic_political_address | 50 |  |  | AFG.txt |
| AFG_expand_education_facilities | AFG_radical_students_category | GFX_decision_generic_political_address | 50 |  |  | AFG.txt |
| AFG_setup_tank_mio | AFG_radical_students_category | GFX_decision_generic_merge_plant_tank | 50 | yes | Arms Against Tyranny | AFG.txt |
| AFG_setup_aircraft_mio | AFG_radical_students_category | GFX_decision_SWE_set_air_budget | 50 | yes | Arms Against Tyranny | AFG.txt |
| AFG_setup_artillery_mio | AFG_radical_students_category | GFX_decision_generic_fortification | 50 | yes | Arms Against Tyranny | AFG.txt |
| AFG_cross_border_target_state | AFG_cross_border_ties_category | GFX_decision_revolt |  | yes |  | AFG.txt |
| AFG_suggest_integrate_state | AFG_cross_border_ties_category | GFX_decision_eng_trade_unions_demand | 30 | yes |  | AFG.txt |
| AFG_propose_peace_for_state | AFG_cross_border_ties_category | GFX_decision_hol_exchange_intelligence_data | 30 |  |  | AFG.txt |
| AFG_propose_peace_for_tajikistan | AFG_cross_border_ties_category | GFX_decision_hol_exchange_intelligence_data | 30 |  |  | AFG.txt |
| AFG_expand_quami | AFG_quami_category | GFX_decision_generic_reorganize_irregulars |  |  |  | AFG.txt |
| AFG_raise_quami | AFG_quami_category | GFX_decision_generic_prepare_civil_war | 25 |  |  | AFG.txt |
| AFG_relieve_quami | AFG_quami_category | GFX_decision_SWI_dismiss_council | 0 |  |  | AFG.txt |
| AFG_demand_end_to_communist_influence | AFG_foreign_intervention_category | GFX_decision_SOV_secure_the_administration | 30 |  |  | AFG.txt |
| AFG_demand_end_to_fascist_influence | AFG_foreign_intervention_category | GFX_decision_ger_reichskommissariats | 30 |  |  | AFG.txt |
| AFG_demand_end_to_democratic_influence | AFG_foreign_intervention_category | GFX_decision_generic_form_nation | 30 |  |  | AFG.txt |
| AFG_core_central_asian_state | AFG_develop_central_asia_category | GFX_decision_hol_exchange_intelligence_data | 30 |  |  | AFG.txt |
| AFG_crackdown_on_dissent | AFG_shadows_of_the_emir_category | GFX_decision_generic_protection |  |  |  | AFG.txt |
| AFG_invite_to_turko_persian_faction | AFG_turko_persian_heritage_category | GFX_decision_generic_protection | 50 | yes |  | AFG.txt |
| AFG_support_resistance_in_state | AFG_turkik_alliance_category | GFX_decision_revolt | 30 |  |  | AFG.txt |
| AFG_support_resistance_in_state_middle_east | AFG_turkik_alliance_category | GFX_decision_revolt | 30 |  |  | AFG.txt |
| SOV_afg_crush_resistance_in_state | AFG_turkik_alliance_category | GFX_decision_revolt | 50 |  | Graveyard of Empires | AFG.txt |
| AFG_claim_state | AFG_kabul_conference_category | GFX_decision_revolt | 30 |  |  | AFG.txt |
| AFG_claim_state_middle_east | AFG_kabul_conference_category | GFX_decision_revolt | 30 |  |  | AFG.txt |
| AFG_recruit_turkestan_legion | AFG_turkestan_legion_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | AFG.txt |
| AFG_a_royal_successor_decision | political_actions | GFX_decision_generic_monarchy | 150 | yes |  | AFG.txt |
| AFG_caliphate_core_state | political_actions | GFX_decision_infiltrate_state | 50 | yes |  | AFG.txt |
| AFG_empire_core_state | political_actions | GFX_decision_infiltrate_state | 35 | yes |  | AFG.txt |
| AFG_mughal_core_state | political_actions | GFX_decision_infiltrate_state | 35 | yes |  | AFG.txt |
| AFG_move_the_capital_to_delhi_decision | political_actions |  | 50 |  | Graveyard of Empires | AFG.txt |
| AFG_sikh_recruitment | AFG_sikh_recruitment_cat | GFX_decision_generic_prepare_civil_war | 30 | yes |  | AFG.txt |
| invite_to_org | african_union_category | GFX_decision_generic_orginization_of_african_unity | 15 |  |  | African_Union_decisions.txt |
| invite_to_ACB | african_union_category | GFX_decision_gre_paying_ifc_debt | 25 |  |  | African_Union_decisions.txt |
| invite_to_exec_council | african_union_category | GFX_decision_eng_trade_unions_support | 50 |  |  | African_Union_decisions.txt |
| integrate_into_org | african_union_category | GFX_decision_generic_form_nation |  | yes |  | African_Union_decisions.txt |
| invite_to_org_alliance | african_union_category | GFX_decision_generic_military | 25 |  |  | African_Union_decisions.txt |
| leave_org_of_african_unity | african_union_category | GFX_decision_generic_break_treaty | 150 | yes |  | African_Union_decisions.txt |
| threaten_member_state | african_union_category | GFX_decision_generic_assassination | 25 |  |  | African_Union_decisions.txt |
| detect_infiltration | communist_infiltration | generic_army_support | 100 |  |  | anti_japan_infiltration.txt |
| communist_infiltration_in_east_hebei | communist_infiltration | generic_civil_support | 10 |  |  | anti_japan_infiltration.txt |
| communist_infiltration_in_jehol | communist_infiltration | generic_civil_support | 10 |  |  | anti_japan_infiltration.txt |
| communist_infiltration_in_south_chahar | communist_infiltration | generic_civil_support | 10 |  |  | anti_japan_infiltration.txt |
| communist_infiltration_in_chahar | communist_infiltration | generic_civil_support | 10 |  |  | anti_japan_infiltration.txt |
| communist_infiltration_in_heilungkiang | communist_infiltration | generic_civil_support | 10 |  |  | anti_japan_infiltration.txt |
| communist_infiltration_in_liaoning | communist_infiltration | generic_civil_support | 10 |  |  | anti_japan_infiltration.txt |
| ARG_federal_intervention_in_state | ARG_intervenciones_federales_decisions | GFX_decision_eng_trade_unions_demand | 50 | yes |  | ARG.txt |
| ARG_loan_from_britain | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_pay_back_britain | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_loan_from_germany | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_pay_back_germany | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_loan_from_usa | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_pay_back_usa | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_loan_from_italy | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_pay_back_italy | ARG_international_loan_decisions | GFX_decision_gre_paying_ifc_debt | 75 |  |  | ARG.txt |
| ARG_exploit_la_vaca_muerta | prospect_for_resources | oil | 50 | yes |  | ARG.txt |
| ARG_appease_the_allies | ARG_balancing_act_decisions | GFX_decision_SWI_swiss_democratic_tradition_campaign | 100 |  | Arms Against Tyranny | ARG.txt |
| ARG_appease_the_axis | ARG_balancing_act_decisions | GFX_decision_ger_reichskommissariats | 100 |  | Arms Against Tyranny | ARG.txt |
| ARG_military_coup_attempt | ARG_military_coup_decisions | generic_ignite_civil_war |  | yes |  | ARG.txt |
| ARG_military_state_absorption_mission | ARG_military_coup_decisions | GFX_decision_eng_blackshirt_speech |  |  |  | ARG.txt |
| ARG_sanction_the_generals | ARG_military_coup_decisions | GFX_decision_eng_trade_unions_support | 100 |  |  | ARG.txt |
| ARG_increase_military_salaries | ARG_military_coup_decisions | GFX_decision_eng_trade_unions_support | 50 |  |  | ARG.txt |
| ARG_core_conquered_state | ARG_south_american_unity_decisions | GFX_decision_generic_form_nation | 75 | yes |  | ARG.txt |
| ARG_peace_out | ARG_island_negotiations_decisions | GFX_decision_eng_trade_unions_support | 75 | yes |  | ARG.txt |
| ARG_england_demands_peace | ARG_island_negotiations_decisions | GFX_decision_eng_propaganda_campaigns | 100 | yes |  | ARG.txt |
| AUS_german_animosity_towards_high_command | AUS_antischluss_category | GFX_decision_generic_assassination |  | yes |  | AUS.txt |
| AUS_up_security_around_high_command | AUS_antischluss_category | GFX_decision_generic_army_support | 30 | yes |  | AUS.txt |
| AUS_state_garrison | AUS_antischluss_category | GFX_decision_generic_protection | 25 | yes |  | AUS.txt |
| AUS_fortification_effort | AUS_antischluss_category | GFX_decision_generic_fortification | 50 |  |  | AUS.txt |
| AUS_civ_industry_effort_effort | AUS_antischluss_category | GFX_decision_generic_factory | 50 |  |  | AUS.txt |
| AUS_arms_industry_effort_effort | AUS_antischluss_category | GFX_decision_generic_industry | 50 |  |  | AUS.txt |
| AUS_extended_workshifts | AUS_antischluss_category | GFX_decision_generic_factory | 50 |  |  | AUS.txt |
| AUS_recruitment_push | AUS_antischluss_category | GFX_decision_generic_military |  | yes |  | AUS.txt |
| AUS_send_volunteers_to_italy | AUS_supporting_italy_in_ethiopia_category | GFX_decision_generic_military | 50 | yes |  | AUS.txt |
| AUS_send_infantry_equipment_to_italy | AUS_supporting_italy_in_ethiopia_category | GFX_decision_generic_prepare_civil_war | 100 | yes |  | AUS.txt |
| AUS_speak_out_against_embargo | AUS_supporting_italy_in_ethiopia_category | GFX_decision_eng_trade_unions_demand | 50 | yes |  | AUS.txt |
| AUS_integrating_german_cores_decision | AUS_becoming_grossosterreich_category | GFX_decision_generic_political_address | 100 |  |  | AUS.txt |
| AUS_becoming_grossosterreich_decision | AUS_becoming_grossosterreich_category | GFX_decision_eng_trade_unions_support | 50 | yes |  | AUS.txt |
| AUS_subjugating_the_lands_of_old_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_hol_draw_up_staff_plans |  | yes |  | AUS.txt |
| AUS_annexing_the_lands_of_old_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_generic_prepare_civil_war |  | yes |  | AUS.txt |
| AUS_anti_FROM_speech_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_eng_blackshirt_speech | 50 | yes |  | AUS.txt |
| AUS_military_exercises_on_border_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_generic_prepare_civil_war | 50 | yes |  | AUS.txt |
| AUS_arm_border_guards_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_generic_reorganize_irregulars | 25 | yes |  | AUS.txt |
| AUS_offer_nap_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_eng_trade_unions_support | 50 | yes |  | AUS.txt |
| AUS_industrial_bribery_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_generic_construction | 50 | yes |  | AUS.txt |
| AUS_joint_military_exercises_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_generic_military | 50 | yes |  | AUS.txt |
| AUS_further_balkan_demands | AUS_subjugating_the_lands_of_old_category | GFX_decision_eng_trade_unions_demand |  | yes |  | AUS.txt |
| AUS_installing_a_habsburg_ruler_decision | AUS_subjugating_the_lands_of_old_category | GFX_decision_generic_monarchy | 25 | yes |  | AUS.txt |
| AUS_hand_bosnia_to_our_cro_puppet | AUS_subjugating_the_lands_of_old_category | GFX_decision_generic_form_nation | 25 | yes |  | AUS.txt |
| AUS_the_danubian_federation_decision | AUS_the_danubian_federation_category | GFX_decision_generic_protection | 100 | yes |  | AUS.txt |
| AUS_the_danubian_federation_observers_decision | AUS_the_danubian_federation_category | GFX_decision_generic_protection | 100 | yes |  | AUS.txt |
| AUS_industrial_coaxing_decision | AUS_the_danubian_federation_category | GFX_decision_generic_factory | 100 | yes |  | AUS.txt |
| AUS_trade_coaxing_descision | AUS_the_danubian_federation_category | GFX_decision_hol_attract_foreign_investors | 50 | yes | Arms Against Tyranny | AUS.txt |
| AUS_propose_a_federative_union_decision | AUS_the_danubian_federation_category | GFX_decision_eng_trade_unions_demand | 150 | yes | Gotterdammerung | AUS.txt |
| AUS_spur_danubian_communism_decision | AUS_danubian_communism_category | GFX_decision_generic_civil_support | 100 | yes |  | AUS.txt |
| AUS_demand_liberation_of_workers_decision | AUS_danubian_communism_category | GFX_decision_generic_political_rally | 150 | yes |  | AUS.txt |
| AUS_reintegrate_FROM_italy_decision | AUS_reintegrating_the_empire_category | GFX_decision_category_generic_propaganda | 100 | yes |  | AUS.txt |
| AUS_reintegrate_FROM_switzerland_decision | AUS_reintegrating_the_empire_category | GFX_decision_category_generic_propaganda | 100 | yes |  | AUS.txt |
| formalize_the_entente | BALTIC_entente | GFX_decision_hol_exchange_intelligence_data |  | yes | No Compromise, No Surrender | BALTIC.txt |
| abandon_the_entente | BALTIC_entente | GFX_decision_generic_break_treaty |  | yes |  | BALTIC.txt |
| BALTIC_promote_communism | convert_neighbours_baltic_cat | hol_draw_up_staff_plans | 50 |  |  | BALTIC.txt |
| BALTIC_promote_communism_militancy | convert_neighbours_baltic_cat | hol_draw_up_staff_plans |  |  |  | BALTIC.txt |
| BALTIC_promote_unity_BLR | infiltrate_belarus_decisions | { | 25 |  |  | BALTIC.txt |
| BALTIC_belarus_uprising | infiltrate_belarus_decisions | GFX_decision_revolt |  | yes |  | BALTIC.txt |
| BALTIC_forest_brothers_resistance | BALTIC_forest_brother_resistance_cat | GFX_decision_revolt |  |  |  | BALTIC.txt |
| BEL_requisition_congolese_funds_decision | political_actions | GFX_decision_generic_fundraising | 0 |  |  | BEL.txt |
| BEL_invest_congo_gold_into_infrastructure_decision | political_actions | GFX_decision_generic_construction | 10 |  |  | BEL.txt |
| BEL_invest_congo_gold_into_welfare_decision | political_actions | GFX_decision_generic_welfare | 10 |  |  | BEL.txt |
| BEL_invest_congo_diamonds_into_construction_decision | political_actions | GFX_decision_hol_attract_foreign_investors | 10 |  |  | BEL.txt |
| BEL_dismantle_BEL_SPR_alliance_decision | political_actions | GFX_decision_generic_break_treaty | 10 |  |  | BEL.txt |
| BEL_emergency_measures_on_production_front | political_actions | GFX_decision_generic_industry | 100 | yes |  | BEL.txt |
| BEL_remove_flooded_tank_barriers | BEL_belgian_defences_cat | generic_construction |  |  |  | BEL.txt |
| BEL_gold_reserves_welfare | BEL_gold_reserves_cat | GFX_decision_generic_welfare | 50 |  |  | BEL.txt |
| BEL_gold_reserves_construction | BEL_gold_reserves_cat | GFX_decision_generic_construction | 50 |  |  | BEL.txt |
| BEL_gold_reserves_industry | BEL_gold_reserves_cat | GFX_decision_generic_factory | 50 |  |  | BEL.txt |
| BEL_request_equipment_decision | BEL_government_in_exile_cat | GFX_decision_generic_industry | 50 |  |  | BEL.txt |
| BEL_request_factory_access_decision | BEL_government_in_exile_cat | GFX_decision_generic_industry | 50 |  |  | BEL.txt |
| BEL_share_military_experience | BEL_government_in_exile_cat | GFX_decision_generic_industry | 50 |  |  | BEL.txt |
| BEL_force_congolese_capitulation_decision | war_measures | GFX_decision_eng_trade_unions_support | 25 |  |  | BEL.txt |
| BEL_invite_to_the_european_union_decision | BEL_closer_european_union_cat | GFX_decision_eng_trade_unions_support | 50 | yes |  | BEL.txt |
| BEL_establish_research_sharing_group_decision | BEL_closer_european_union_cat | GFX_decision_hol_exchange_intelligence_data | 100 | yes |  | BEL.txt |
| BEL_propose_limited_federalization_descision | BEL_closer_european_union_cat | GFX_decision_hol_exchange_intelligence_data | 100 | yes |  | BEL.txt |
| BEL_complete_integration_of_from_decision | BEL_cores_in_gallic_france_cat | GFX_decision_generic_operation | 100 | yes |  | BEL.txt |
| BEL_guns_for_the_spaniards_decision | BEL_intervention_in_spain_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | BEL.txt |
| BEL_more_equipment_for_the_spanish_decision | BEL_intervention_in_spain_cat | GFX_decision_generic_industry | 50 | yes |  | BEL.txt |
| BEL_speech_in_support_of_spain_decision | BEL_intervention_in_spain_cat | GFX_decision_generic_political_address | 100 | yes |  | BEL.txt |
| BEL_encourage_emigration_to_spain_decision | BEL_intervention_in_spain_cat | GFX_decision_eng_propaganda_campaigns | 75 | yes |  | BEL.txt |
| BEL_intervene_on_side_of_SPR | BEL_intervention_in_spain_cat | GFX_faction_logo_generic_11 | 100 |  |  | BEL.txt |
| BEL_form_alliance_with_spain | BEL_intervention_in_spain_cat | GFX_decision_eng_trade_unions_support | 50 | yes |  | BEL.txt |
| BEL_communist_constitution_decision | BEL_rekindle_the_red_flame_cat | GFX_decision_eng_trade_unions_support | 100 | yes |  | BEL.txt |
| BEL_worker_rallies_decision | BEL_rekindle_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | BEL.txt |
| BEL_increased_union_powers_decision | BEL_rekindle_the_red_flame_cat | GFX_decision_eng_trade_unions_demand | 50 | yes |  | BEL.txt |
| BEL_boost_miner_unions_decision | BEL_rekindle_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | BEL.txt |
| BEL_boost_construction_unions_decision | BEL_rekindle_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | BEL.txt |
| BEL_boost_factory_workers_unions_decision | BEL_rekindle_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | BEL.txt |
| BOL_reintegrate_litoral_department | BOL_bolivian_irredentism | GFX_decision_BOL_reintegrate_litoral_department | 100 |  | Trial of Allegiance | BOL.txt |
| BOL_reintegrate_acre_state | BOL_bolivian_irredentism | GFX_decision_BOL_reintegrate_acre_state | 100 |  | Trial of Allegiance | BOL.txt |
| BOL_establish_arica_department | BOL_bolivian_irredentism | GFX_decision_BOL_establish_arica_department | 120 |  | Trial of Allegiance | BOL.txt |
| BOL_embrace_plurinationalism | political_actions | GFX_decision_SOV_place_hq | 120 |  | Trial of Allegiance | BOL.txt |
| BOL_david_toros_resignation | political_actions | GFX_decision_generic_break_treaty | 100 |  | Trial of Allegiance | BOL.txt |
| BRA_federal_investment_in_rural_state | BRA_industrial_decisions | GFX_decision_gre_paying_ifc_debt | 30 | yes |  | BRA.txt |
| BRA_integralist_support | BRA_ensure_support_cat | GFX_decision_BRA_integralism | 20 | yes |  | BRA.txt |
| BRA_recruit_green_shirts | BRA_ensure_support_cat | GFX_decision_eng_blackshirt_march | 20 | yes |  | BRA.txt |
| BRA_execute_the_cohen_plan | BRA_ensure_support_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | BRA.txt |
| BRA_deal_with_the_cangaceiro_dec | BRA_cangaceiro_decision_cat | GFX_decision_generic_prepare_civil_war |  |  |  | BRA.txt |
| BRA_cangaceiro_mission | BRA_cangaceiro_decision_cat | GFX_decision_revolt |  |  |  | BRA.txt |
| BRA_washington_accords_mission | BRA_good_neighbor_decisions | GFX_decision_generic_prepare_civil_war |  | yes |  | BRA.txt |
| BRA_invite_to_mercosul | BRA_mercosul_decisions | GFX_decision_eng_trade_unions_support | 20 |  |  | BRA.txt |
| BRA_amazonian_settlement_in_state | BRA_amazonian_settlement_cat | GFX_decision_generic_construction | 50 | yes |  | BRA.txt |
| BRA_jaguar_diplomacy_decision | BRA_jaguar_diplomacy_cat | GFX_decision_eng_trade_unions_support | 25 |  |  | BRA.txt |
| BRA_oust_the_empires_decision | BRA_oust_the_empires_decision_cat | GFX_decision_generic_political_rally | 50 |  |  | BRA.txt |
| BRA_sway_the_neighbors_decision | BRA_sway_the_neighbors_cat | GFX_decision_generic_prepare_civil_war | 50 |  |  | BRA.txt |
| BRA_counter_influence_decision | BRA_counter_influence_cat | GFX_decision_eng_trade_unions_support | 100 |  |  | BRA.txt |
| BRA_invite_foreign_mio | BRA_invite_foreign_companies_cat | GFX_decision_generic_industry | 30 |  |  | BRA.txt |
| BRA_integrate_state | BRA_america_do_sul_cat | GFX_decision_generic_operation | 20 |  |  | BRA.txt |
| BRA_invite_to_ussa | BRA_us_of_south_america_cat | GFX_decision_infiltrate_state | 100 |  |  | BRA.txt |
| BRA_invite_to_faction | BRA_us_of_south_america_cat | GFX_decision_eng_trade_unions_support | 20 |  |  | BRA.txt |
| BRA_recruit_foreign_legion | BRA_foreign_legion_cat | GFX_decision_generic_prepare_civil_war |  |  |  | BRA.txt |
| rename_guapore_to_rondonia_decision | political_actions | GFX_decision_eng_trade_unions_support | 50 | yes |  | BRA.txt |
| BUL_a_royal_visit | BUL_internal_factions | eng_ally_imperialist_coup |  |  |  | BUL.txt |
| BUL_cooperation_zveno_speech | BUL_internal_factions | GFX_decision_bul_speech_zveno |  |  |  | BUL.txt |
| BUL_cooperation_bs_speech | BUL_internal_factions | GFX_decision_bul_speech_bs |  |  |  | BUL.txt |
| BUL_cooperation_bzns_speech | BUL_internal_factions | GFX_decision_bul_speech_bzns |  |  |  | BUL.txt |
| BUL_cooperation_nsm_speech | BUL_internal_factions | GFX_decision_bul_speech_nsm |  |  |  | BUL.txt |
| BUL_cooperation_zveno_joint_act | BUL_internal_factions | GFX_decision_bul_joint_act_zveno |  |  |  | BUL.txt |
| BUL_cooperation_bs_joint_act | BUL_internal_factions | GFX_decision_bul_joint_act_bs |  |  |  | BUL.txt |
| BUL_cooperation_bzns_joint_act | BUL_internal_factions | GFX_decision_bul_joint_act_bzns |  |  |  | BUL.txt |
| BUL_cooperation_nsm_joint_act | BUL_internal_factions | GFX_decision_bul_joint_act_nsm |  |  |  | BUL.txt |
| BUL_cooperation_bolster_zveno | BUL_internal_factions | GFX_decision_bul_bolster_zveno |  | yes |  | BUL.txt |
| BUL_cooperation_zveno_social_renovation_directory | BUL_internal_factions | GFX_decision_bul_legalize_zveno |  | yes |  | BUL.txt |
| BUL_cooperation_bs_legalize_faction | BUL_internal_factions | GFX_decision_bul_legalize_bs |  |  |  | BUL.txt |
| BUL_cooperation_bzns_legalize_faction | BUL_internal_factions | GFX_decision_bul_legalize_bzns |  | yes |  | BUL.txt |
| BUL_cooperation_nsm_legalize_faction | BUL_internal_factions | GFX_decision_bul_legalize_nsm |  | yes |  | BUL.txt |
| BUL_cooperation_fund_zveno | BUL_internal_factions | GFX_decision_bul_fund_zveno |  |  |  | BUL.txt |
| BUL_cooperation_fund_bs | BUL_internal_factions | GFX_decision_bul_fund_bs |  |  |  | BUL.txt |
| BUL_cooperation_fund_bzns | BUL_internal_factions | GFX_decision_bul_fund_bzns |  |  |  | BUL.txt |
| BUL_cooperation_fund_nsm | BUL_internal_factions | GFX_decision_bul_fund_nsm |  |  |  | BUL.txt |
| BUL_cooperation_appoint_zveno_members | BUL_internal_factions | GFX_decision_bul_appoint_members_zveno |  | yes |  | BUL.txt |
| BUL_cooperation_appoint_bs_members | BUL_internal_factions | GFX_decision_bul_appoint_members_bs |  | yes |  | BUL.txt |
| BUL_cooperation_appoint_bzns_members | BUL_internal_factions | GFX_decision_bul_appoint_members_bzns |  | yes |  | BUL.txt |
| BUL_cooperation_appoint_nsm_members | BUL_internal_factions | GFX_decision_bul_appoint_members_nsm |  | yes |  | BUL.txt |
| BUL_cooperation_integrate_zveno | BUL_internal_factions | GFX_decision_bul_integrate_zveno |  | yes |  | BUL.txt |
| BUL_cooperation_integrate_bs | BUL_internal_factions | GFX_decision_bul_integrate_bs |  | yes |  | BUL.txt |
| BUL_cooperation_integrate_bzns | BUL_internal_factions | GFX_decision_bul_integrate_bzns |  | yes |  | BUL.txt |
| BUL_cooperation_integrate_nsm | BUL_internal_factions | GFX_decision_bul_integrate_nsm |  | yes |  | BUL.txt |
| BUL_opression_discredit_zveno_leaders | BUL_internal_factions | GFX_decision_bul_discredit_zveno |  |  |  | BUL.txt |
| BUL_opression_discredit_bs_leaders | BUL_internal_factions | GFX_decision_bul_discredit_bs |  |  |  | BUL.txt |
| BUL_opression_discredit_bzns_leaders | BUL_internal_factions | GFX_decision_bul_discredit_bzns |  |  |  | BUL.txt |
| BUL_opression_discredit_nsm_leaders | BUL_internal_factions | GFX_decision_bul_discredit_nsm |  |  |  | BUL.txt |
| BUL_opression_dispose_of_zveno_generals | BUL_internal_factions | GFX_decision_bul_ban_media_zveno |  | yes |  | BUL.txt |
| BUL_opression_ban_bs_media | BUL_internal_factions | GFX_decision_bul_ban_media_bs |  |  |  | BUL.txt |
| BUL_opression_ban_bzns_media | BUL_internal_factions | GFX_decision_bul_ban_media_bzns |  |  |  | BUL.txt |
| BUL_opression_ban_nsm_media | BUL_internal_factions | GFX_decision_bul_ban_media_nsm |  |  |  | BUL.txt |
| BUL_opression_anti_zveno_speech | BUL_internal_factions | GFX_decision_bul_against_zveno |  |  |  | BUL.txt |
| BUL_opression_anti_bs_speech | BUL_internal_factions | GFX_decision_bul_against_bs |  |  |  | BUL.txt |
| BUL_opression_anti_bzns_speech | BUL_internal_factions | GFX_decision_bul_against_bzns |  |  |  | BUL.txt |
| BUL_opression_anti_nsm_speech | BUL_internal_factions | GFX_decision_bul_against_nsm |  |  |  | BUL.txt |
| BUL_opression_imprison_zveno_leaders | BUL_internal_factions | GFX_decision_bul_imprison_leaders_zveno |  | yes |  | BUL.txt |
| BUL_opression_imprison_bs_leaders | BUL_internal_factions | GFX_decision_bul_imprison_leaders_bs |  | yes |  | BUL.txt |
| BUL_opression_imprison_bzns_leaders | BUL_internal_factions | GFX_decision_bul_imprison_leaders_bzns |  | yes |  | BUL.txt |
| BUL_opression_imprison_nsm_leaders | BUL_internal_factions | GFX_decision_bul_imprison_leaders_nsm |  | yes |  | BUL.txt |
| BUL_opression_raid_zveno_supporters | BUL_internal_factions | GFX_decision_bul_raid_zveno |  |  |  | BUL.txt |
| BUL_opression_raid_bs_supporters | BUL_internal_factions | GFX_decision_bul_raid_bs |  |  |  | BUL.txt |
| BUL_opression_raid_bzns_supporters | BUL_internal_factions | GFX_decision_bul_raid_bzns |  |  |  | BUL.txt |
| BUL_opression_raid_nsm_supporters | BUL_internal_factions | GFX_decision_bul_raid_nsm |  |  |  | BUL.txt |
| BUL_opression_destroy_zveno | BUL_internal_factions | GFX_decision_bul_destroy_zveno |  | yes |  | BUL.txt |
| BUL_opression_destroy_bs | BUL_internal_factions | GFX_decision_bul_destroy_bs |  | yes |  | BUL.txt |
| BUL_opression_destroy_bzns | BUL_internal_factions | GFX_decision_bul_destroy_bzns |  | yes |  | BUL.txt |
| BUL_opression_destroy_nsm | BUL_internal_factions | GFX_decision_bul_destroy_nsm |  | yes |  | BUL.txt |
| BUL_opression_repress_zveno | BUL_internal_factions | GFX_decision_bul_repress_zveno |  |  |  | BUL.txt |
| BUL_opression_repress_bs | BUL_internal_factions | GFX_decision_bul_repress_bs |  |  |  | BUL.txt |
| BUL_opression_repress_bzns | BUL_internal_factions | GFX_decision_bul_repress_bzns |  |  |  | BUL.txt |
| BUL_opression_repress_nsm | BUL_internal_factions | GFX_decision_bul_repress_nsm |  |  |  | BUL.txt |
| BUL_impending_zveno_coup | BUL_internal_factions | GFX_decision_generic_civil_support |  | yes | La Resistance | BUL.txt |
| BUL_repress_imro_propaganda | BUL_macedonian_revolutionary_organizations | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | BUL.txt |
| BUL_repress_imro_persecute_activists | BUL_macedonian_revolutionary_organizations | GFX_decision_generic_police_action | 25 | yes |  | BUL.txt |
| BUL_repress_imro_destroy_organization | BUL_macedonian_revolutionary_organizations | GFX_decision_oppression | 25 |  |  | BUL.txt |
| BUL_support_imro_make_contacts | BUL_macedonian_revolutionary_organizations | GFX_decision_generic_political_discourse | 50 | yes |  | BUL.txt |
| BUL_support_imro_supply_activists | BUL_macedonian_revolutionary_organizations | GFX_decision_generic_industry | 50 | yes |  | BUL.txt |
| BUL_support_imro_prepare_bulgarian_occupation | BUL_macedonian_revolutionary_organizations | GFX_decision_generic_nationalism | 50 | yes |  | BUL.txt |
| BUL_support_imro_militias | BUL_macedonian_revolutionary_organizations | GFX_decision_generic_military | 50 | yes |  | BUL.txt |
| BUL_support_imro_garrisons | BUL_macedonian_revolutionary_organizations | GFX_decision_generic_prepare_civil_war | 50 | yes |  | BUL.txt |
| BUL_repress_imro_foreign | BUL_macedonian_revolutionary_organizations_foreign | GFX_decision_generic_police_action | 25 | yes |  | BUL.txt |
| BUL_destroy_imro_foreign | BUL_macedonian_revolutionary_organizations_foreign | GFX_decision_oppression | 25 |  |  | BUL.txt |
| BUL_ff_impending_coup_mission | BUL_the_fatherland_front_dec_cat | generic_prepare_civil_war |  | yes |  | BUL.txt |
| BUL_ff_approaching_zveno_mission | BUL_the_fatherland_front_dec_cat | generic_political_discourse |  | yes |  | BUL.txt |
| BUL_ff_approaching_bs_mission | BUL_the_fatherland_front_dec_cat | generic_political_discourse |  | yes |  | BUL.txt |
| BUL_ff_approaching_bzns_mission | BUL_the_fatherland_front_dec_cat | generic_political_discourse |  | yes |  | BUL.txt |
| BUL_ff_root_out_sympathizers | BUL_the_fatherland_front_dec_cat | generic_military | 35 |  |  | BUL.txt |
| BUL_ff_massive_arrests | BUL_the_fatherland_front_dec_cat | generic_arrest | 75 |  |  | BUL.txt |
| BUL_ff_deal_the_final_blow | BUL_the_fatherland_front_dec_cat | oppression | 75 | yes |  | BUL.txt |
| BUL_demonstrate_our_policies_of_peace | BUL_rearmament | GFX_decision_generic_form_nation | 50 | yes |  | BUL.txt |
| BUL_negotiate_bulgarian_rearmament | BUL_rearmament | GFX_decision_generic_industry | 50 | yes |  | BUL.txt |
| BUL_pressure_to_lift_army_restrictions | BUL_rearmament | GFX_decision_eng_trade_unions_support | 50 | yes |  | BUL.txt |
| BUL_refuse_army_restrictions | BUL_rearmament | GFX_decision_generic_break_treaty | 50 | yes | Arms Against Tyranny | BUL.txt |
| BUL_purchase_infantry_equipment | BUL_purchase_equipment | generic_industry |  |  |  | BUL.txt |
| BUL_purchase_artillery | BUL_purchase_equipment | ger_military_buildup |  |  |  | BUL.txt |
| BUL_purchase_military_vehicles | BUL_purchase_equipment | generic_trucks |  |  |  | BUL.txt |
| BUL_purchase_armor | BUL_purchase_equipment | generic_tank |  |  |  | BUL.txt |
| BUL_purchase_aircraft | BUL_purchase_equipment | generic_air |  |  |  | BUL.txt |
| BUL_purchase_ships | BUL_purchase_equipment | GFX_decision_generic_naval |  |  | Man the Guns | BUL.txt |
| BUL_german_industrial_agreements | BUL_foreign_agreements | generic_factory |  |  |  | BUL.txt |
| BUL_british_industrial_agreements | BUL_foreign_agreements | generic_factory |  |  |  | BUL.txt |
| BUL_soviet_industrial_agreements | BUL_foreign_agreements | generic_factory |  |  |  | BUL.txt |
| BUL_military_agreements | BUL_foreign_agreements | generic_tank |  | yes |  | BUL.txt |
| BUL_naval_agreements | BUL_foreign_agreements | generic_naval |  | yes |  | BUL.txt |
| BUL_aircraft_agreements | BUL_foreign_agreements | generic_air |  | yes |  | BUL.txt |
| BUL_mineral_extraction_in_the_rhodopes | prospect_for_resources | chromium | 25 |  | Battle for the Bosporus | BUL.txt |
| BUL_uranium_concession_agreement | prospect_for_resources | eng_trade_unions_support | 0 | yes | Battle for the Bosporus | BUL.txt |
| BUL_demand_our_historical_claims | BUL_negotiate_claims_in_the_balkans | hol_draw_up_staff_plans | 75 | yes |  | BUL.txt |
| BUL_secure_occupation_in_balkan_state | BUL_negotiate_claims_in_the_balkans | hol_draw_up_staff_plans | 25 | yes |  | BUL.txt |
| BUL_bulgarian_reintegration_campaign | BUL_bulgarian_administration_of_the_balkans | GFX_decision_generic_nationalism | 35 |  |  | BUL.txt |
| BUL_germany_donate_fighters | BUL_align_bulgaria | generic_air | 0 | yes |  | BUL.txt |
| BUL_germany_demand_military_access | BUL_align_bulgaria | hol_draw_up_staff_plans | 25 | yes |  | BUL.txt |
| BUL_germany_demand_replacement_of_bulgarian_prime_minister | BUL_align_bulgaria | eng_trade_unions_demand | 5 | yes |  | BUL.txt |
| BUL_develop_balkan_federation_project | BUL_the_balkan_federation_dream | GFX_decision_eng_trade_unions_support | 15 | yes |  | BUL.txt |
| BUL_balkan_federation_propaganda | BUL_the_balkan_federation_dream | GFX_decision_eng_propaganda_campaigns | 50 |  |  | BUL.txt |
| BUL_destabilize_country | BUL_the_balkan_federation_dream | GFX_decision_revolt | 50 |  |  | BUL.txt |
| BUL_fight_alongside_country_comrades | BUL_the_balkan_federation_dream | GFX_decision_generic_prepare_civil_war |  | yes |  | BUL.txt |
| BUL_balkan_federation_industrial_aid | BUL_the_balkan_federation_dream | GFX_decision_generic_factory | 15 |  |  | BUL.txt |
| BUL_balkan_federation_economic_aid | BUL_the_balkan_federation_dream | GFX_decision_hol_attract_foreign_investors | 15 |  |  | BUL.txt |
| BUL_balkan_federation_military_aid | BUL_the_balkan_federation_dream | GFX_decision_generic_military | 15 |  |  | BUL.txt |
| BUL_balkan_federation_demand_turkish_territory | BUL_the_balkan_federation_dream | GFX_decision_generic_military | 75 |  |  | BUL.txt |
| BUL_brainwash_political_prisoners | BUL_plot_against_boris_dec_cat | GFX_decision_generic_brainwash | 50 | yes |  | BUL.txt |
| BUL_persuade_faction_members | BUL_plot_against_boris_dec_cat | GFX_decision_hol_attract_foreign_investors | 75 | yes |  | BUL.txt |
| BUL_draw_up_a_plan_for_regicide | BUL_plot_against_boris_dec_cat | GFX_decision_generic_operation | 50 | yes |  | BUL.txt |
| BUL_seek_foreign_support | BUL_plot_against_boris_dec_cat | GFX_decision_eng_trade_unions_support | 50 | yes |  | BUL.txt |
| BUL_execute_plan | BUL_plot_against_boris_dec_cat | GFX_decision_generic_political_discourse | 50 | yes |  | BUL.txt |
| BUL_fate_of_the_balkans_influence_government | BUL_the_fate_of_the_balkans_dec_cat | GFX_decision_generic_political_discourse | 15 |  |  | BUL.txt |
| BUL_fate_of_the_balkans_ultimatum | BUL_the_fate_of_the_balkans_dec_cat | GFX_decision_eng_trade_unions_support | 35 |  |  | BUL.txt |
| BUL_fate_of_the_balkans_bring_back_state | BUL_the_fate_of_the_balkans_dec_cat | GFX_decision_infiltrate_state | 50 |  |  | BUL.txt |
| BUL_fate_of_the_balkans_demand_submission | BUL_the_fate_of_the_balkans_dec_cat | GFX_decision_eng_trade_unions_demand | 50 |  |  | BUL.txt |
| BUL_dominance_in_the_black_sea_mission | BUL_dominance_in_the_seas | GFX_decision_generic_operation |  | yes |  | BUL.txt |
| BUL_dominance_in_the_aegean_sea_mission | BUL_dominance_in_the_seas | GFX_decision_generic_operation |  | yes |  | BUL.txt |
| BUL_dominance_in_the_adriatic_sea_mission | BUL_dominance_in_the_seas | GFX_decision_generic_operation |  | yes |  | BUL.txt |
| BUL_appoint_tsankov | political_actions | GFX_decision_generic_speech | 50 | yes | Battle for the Bosporus | BUL.txt |
| BUL_appoint_georgiev | political_actions | GFX_decision_generic_speech | 50 | yes | Battle for the Bosporus | BUL.txt |
| BUL_balkan_confederation_industrial_investment | BUL_balkan_confederation | GFX_decision_generic_factory | 15 |  |  | BUL.txt |
| BUL_balkan_confederation_capital_injection | BUL_balkan_confederation | GFX_decision_gre_investment_decisions | 15 |  |  | BUL.txt |
| BUL_balkan_confederation_balkan_summit | BUL_balkan_confederation | GFX_decision_generic_form_nation | 75 |  |  | BUL.txt |
| CHI_Dannes_debugg_fiesta | debug_decisions | generic_nationalism |  |  |  | CHI_decisions.txt |
| CHI_release_korea | CHI_anti_imperialism | generic_nationalism |  | yes |  | CHI_decisions.txt |
| CHI_warlord_core_territories | CHI_warlord_core_territories_cat | GFX_decision_generic_form_nation | 50 | yes |  | CHI_decisions.txt |
| CHI_warlord_core_manchuria | CHI_warlord_core_territories_cat | GFX_decision_generic_form_nation | 50 | yes |  | CHI_decisions.txt |
| CHI_army_reform | CHI_army_reform | generic_prepare_civil_war | 0 |  |  | CHI_decisions.txt |
| CHI_lessons_of_war | CHI_army_reform | generic_army_support | 0 | yes |  | CHI_decisions.txt |
| CHI_bolster_our_ranks | CHI_army_reform | generic_prepare_civil_war |  | yes |  | CHI_decisions.txt |
| CHI_60_divisions_plan | CHI_army_reform | generic_operation | 90 | yes |  | CHI_decisions.txt |
| CHI_forced_loans | economy_decisions | ger_mefo_bills | 100 |  |  | CHI_decisions.txt |
| CHI_scorched_earth_tactics | war_measures | generic_scorched_earth | 25 |  |  | CHI_decisions.txt |
| CHI_industrial_evacuations_from_state | CHI_industrial_evacuations | generic_scorched_earth | 25 |  | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_gansu | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_hainan | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_guangzhou | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_guangdong | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_nanning | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_fujian | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_zhejiang | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_shandong | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_jiangsu | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_guangxi | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_jiangxi | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_hunan | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_anhui | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_henan | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_beijing | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_shanghai | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_hebei | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_ningxia | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_hubei | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_industrial_evacuations_from_qingdao | CHI_industrial_evacuations | generic_scorched_earth | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_integrate_the_army | CHI_integrate_the_warlords | generic_prepare_civil_war | 150 | yes |  | CHI_decisions.txt |
| CHI_integrate_the_administration | CHI_integrate_the_warlords | generic_political_discourse | 150 | yes |  | CHI_decisions.txt |
| CHI_full_integration | CHI_integrate_the_warlords | oppression | 150 | yes |  | CHI_decisions.txt |
| CHI_detect_infiltration | CHI_communist_infiltration | oppression | 100 |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_gansu | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_shandong | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_jiangsu | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_henan | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_beijing | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_hebei | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_shanxi | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_suiyuan | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_xian | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_communist_infiltration_in_ordos | CHI_communist_infiltration | infiltrate_state |  |  |  | CHI_decisions.txt |
| CHI_flying_tigers | foreign_support | generic_air | 25 | yes | By Blood Alone | CHI_decisions.txt |
| CHI_soviet_volunteer_group | foreign_support | generic_air | 25 | yes | By Blood Alone | CHI_decisions.txt |
| CHI_expand_the_burma_road | foreign_support | generic_construction | 25 |  |  | CHI_decisions.txt |
| CHI_expand_the_ledo_road | foreign_support | generic_construction | 25 |  |  | CHI_decisions.txt |
| CHI_expand_the_airlift | foreign_support | generic_construction | 25 |  |  | CHI_decisions.txt |
| CHI_suspend_the_inter_party_coordination_council | political_actions | oppression | 25 |  |  | CHI_decisions.txt |
| CHI_reinstate_the_inter_party_coordination_council | political_actions | generic_political_discourse | 25 |  |  | CHI_decisions.txt |
| CHI_join_united_front | political_actions |  | 5 |  |  | CHI_decisions.txt |
| CHI_move_the_capital | political_actions |  | 50 |  | Waking the Tiger | CHI_decisions.txt |
| CHI_instigate_xian_incident | CHI_xian_incident | generic_political_discourse | 25 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_overlordship_over_indochina | operations | generic_operation |  | yes |  | CHI_decisions.txt |
| CHI_overlordship_over_indochina_tsr | operations | generic_operation | 50 | yes |  | CHI_decisions.txt |
| CHI_free_indochina_tsr | operations | generic_operation | 50 | yes |  | CHI_decisions.txt |
| CHI_build_a_carrier | prestigious_projects | generic_naval |  | yes |  | CHI_decisions.txt |
| CHI_breach_the_yellow_river | CHI_occupation_actions | GFX_decision_hol_inundate_water_lines | 20 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_demonstrate_our_resolve_decision | CHI_war_of_resistance_cat | GFX_decision_generic_speech | 25 |  |  | CHI_decisions.txt |
| CHI_holding_state_mission | CHI_war_of_resistance_cat | GFX_decision_generic_protection |  |  |  | CHI_decisions.txt |
| CHI_declare_war_zone | CHI_war_of_resistance_cat | GFX_decision_jap_conquer_china |  |  |  | CHI_decisions.txt |
| CHI_bog_them_down | CHI_war_of_resistance_cat | GFX_decision_hol_draw_up_staff_plans |  |  |  | CHI_decisions.txt |
| CHI_highlight_northwestern_road_fake_decision | CHI_lend_lease_missions_cat | GFX_decision_generic_operation | 0 |  |  | CHI_decisions.txt |
| CHI_highlight_the_hump_decision | CHI_lend_lease_missions_cat | GFX_decision_generic_operation | 0 |  |  | CHI_decisions.txt |
| CHI_highlight_hanoi_route_decision | CHI_lend_lease_missions_cat | GFX_decision_generic_operation | 0 |  |  | CHI_decisions.txt |
| CHI_highlight_burma_road_decision | CHI_lend_lease_missions_cat | GFX_decision_generic_operation | 0 |  |  | CHI_decisions.txt |
| CHI_request_tank_aid_from_russia_decision | CHI_lend_lease_missions_cat | GFX_decision_generic_tank | 50 | yes |  | CHI_decisions.txt |
| CHI_open_the_north_west_highway_decision | CHI_lend_lease_missions_cat | GFX_decision_generic_trucks | 50 | yes |  | CHI_decisions.txt |
| CHI_use_expat_community_for_more_cic_decision | CHI_lend_lease_missions_cat | GFX_decision_hol_exchange_intelligence_data | 75 | yes |  | CHI_decisions.txt |
| CHI_burma_campaign_mission | CHI_lend_lease_missions_cat | generic_tank |  | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_indo_chinese_campaign_mission | CHI_lend_lease_missions_cat | generic_tank |  | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_improving_neglected_countryside_mission | CHI_internal_politics_cat | GFX_decision_generic_research |  |  |  | CHI_decisions.txt |
| CHI_improving_inefficient_economy_mission | CHI_internal_politics_cat | GFX_decision_generic_merge_plant_materiel |  |  |  | CHI_decisions.txt |
| CHI_reeducate_bai_chonxi_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_yu_hanmou_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_sun_tongxuan_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_song_zheyuan_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_wang_jingguo_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_hu_ruoyu_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_gu_zhutong_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_zhang_xueliang_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_ma_bufang_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_ma_hongkui_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_ma_buqing_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_ma_zhancang_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_yulbars_khan_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_sheng_shiqi_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_altanochir_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_reeducate_yu_zhishan_decision | CHI_internal_politics_cat | GFX_decision_generic_army_support | 25 | yes |  | CHI_decisions.txt |
| CHI_core_asian_state | CHI_internal_politics_cat | GFX_decision_generic_form_nation | 30 | yes |  | CHI_decisions.txt |
| CHI_invest_in_officer_training | CHI_internal_politics_cat | GFX_decision_generic_military | 100 |  |  | CHI_decisions.txt |
| CHI_press_warlord_to_become_puppet | CHI_integrate_the_warlords_sea_cat | GFX_decision_eng_trade_unions_demand |  | yes |  | CHI_decisions.txt |
| CHI_press_warlord_to_become_puppet_upgrade | CHI_integrate_the_warlords_sea_cat | GFX_decision_eng_trade_unions_demand |  | yes |  | CHI_decisions.txt |
| CHI_press_warlord_to_become_puppet_with_affirm_civilian_primacy | CHI_integrate_the_warlords_sea_cat | GFX_decision_eng_trade_unions_demand |  | yes |  | CHI_decisions.txt |
| CHI_press_warlord_to_become_puppet_upgrade_with_affirm_civilian_primacy | CHI_integrate_the_warlords_sea_cat | GFX_decision_eng_trade_unions_demand |  | yes |  | CHI_decisions.txt |
| CHI_warlord_autonomy_drift_decision | CHI_integrate_the_warlords_sea_cat | GFX_decision_eng_trade_unions_support |  |  |  | CHI_decisions.txt |
| CHI_warlord_autonomy_drift_decision_upgrade | CHI_integrate_the_warlords_sea_cat | GFX_decision_eng_trade_unions_support |  |  |  | CHI_decisions.txt |
| CHI_warlord_autonomy_allocate_lend_lease_decision | CHI_integrate_the_warlords_sea_cat | generic_prepare_civil_war |  |  |  | CHI_decisions.txt |
| CHI_warlord_autonomy_offer_economic_support_decision | CHI_integrate_the_warlords_sea_cat | GFX_decision_generic_consumer_goods |  |  |  | CHI_decisions.txt |
| CHI_warlord_autonomy_offer_industrial_support_decision | CHI_integrate_the_warlords_sea_cat | GFX_decision_generic_industry |  |  |  | CHI_decisions.txt |
| CHI_integrating_states | CHI_integrate_the_warlords_sea_cat | GFX_decision_generic_political_address | 100 |  |  | CHI_decisions.txt |
| CHI_kwantung_army_impatience_dummy | CHI_avoid_another_crisis_cat |  |  |  |  | CHI_decisions.txt |
| CHI_concessions_docking_rights | CHI_avoid_another_crisis_cat |  | 25 | yes |  | CHI_decisions.txt |
| CHI_concessions_airbase_rights | CHI_avoid_another_crisis_cat |  | 25 | yes |  | CHI_decisions.txt |
| CHI_concessions_give_resource_rights | CHI_avoid_another_crisis_cat | GFX_decision_eng_trade_unions_demand | 25 |  |  | CHI_decisions.txt |
| CHI_concessions_give_coastal_states | CHI_avoid_another_crisis_cat | GFX_decision_eng_trade_unions_support | 50 |  |  | CHI_decisions.txt |
| CHI_concessions_give_puppet | CHI_avoid_another_crisis_cat | GFX_decision_eng_trade_unions_support | 50 |  |  | CHI_decisions.txt |
| CHI_invite_free_countries | CHI_build_up_our_faction_cat | GFX_decision_eng_trade_unions_support | 50 |  |  | CHI_decisions.txt |
| CHI_set_up_puppet | CHI_build_up_our_faction_cat | generic_prepare_civil_war | 0 |  |  | CHI_decisions.txt |
| CHI_renegotiate_with_warlord | CHI_tsr_renegotiating_with_warlords_cat | GFX_decision_generic_decision | 25 |  |  | CHI_decisions.txt |
| CHI_intervene_in_guangdong | CHI_the_lingguang_incident_cat | generic_nationalism | 100 | yes |  | CHI_decisions.txt |
| GDC_restore_order | CHI_the_lingguang_incident_cat | generic_nationalism | 10 |  |  | CHI_decisions.txt |
| CHI_growing_impatience_dummy | CHI_the_lingguang_incident_cat |  |  |  |  | CHI_decisions.txt |
| CHI_growing_impatience | CHI_the_lingguang_incident_cat |  |  |  |  | CHI_decisions.txt |
| GXC_fortify_our_borders | CHI_the_lingguang_incident_cat | GFX_decision_generic_mountain_fortification | 20 | yes |  | CHI_decisions.txt |
| GXC_anti_japanese_demonstration | CHI_the_lingguang_incident_cat | GFX_decision_eng_blackshirt_march | 20 | yes |  | CHI_decisions.txt |
| GXC_persuade_the_warlords | CHI_the_lingguang_incident_cat | GFX_decision_generic_political_discourse | 20 | yes |  | CHI_decisions.txt |
| GXC_further_negotiation | CHI_the_lingguang_incident_cat | GFX_decision_hol_exchange_intelligence_data | 20 | yes |  | CHI_decisions.txt |
| CHI_accelerate_urban_tutelage_decision | CHI_the_political_tutelage_cat | GFX_decision_generic_political_rally |  | yes |  | CHI_decisions.txt |
| CHI_accelerate_rural_tutelage_decision | CHI_the_political_tutelage_cat | GFX_decision_generic_political_address |  | yes |  | CHI_decisions.txt |
| CHI_invite_demo_asian_nation_to_faction_decison | CHI_republican_interests_cat | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | CHI_decisions.txt |
| CHI_stir_democratic_sentiments_in_asia_decison | CHI_republican_interests_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | CHI_decisions.txt |
| CHI_oust_the_empires_decision | CHI_republican_interests_cat | GFX_decision_generic_political_rally | 50 |  |  | CHI_decisions.txt |
| CHI_press_warlord_to_become_puppet_democratic | CHI_integrate_the_warlords_democratic_sea_cat | GFX_decision_eng_trade_unions_demand |  | yes |  | CHI_decisions.txt |
| CHI_warlord_autonomy_drift_demcoratic_decision | CHI_integrate_the_warlords_democratic_sea_cat | generic_prepare_civil_war |  |  |  | CHI_decisions.txt |
| CHI_warlord_democratic_drift_minquan_decision | CHI_integrate_the_warlords_democratic_sea_cat | GFX_decision_SWI_swiss_democratic_tradition_campaign |  |  |  | CHI_decisions.txt |
| CHI_develop_warlord_industry_decision | CHI_integrate_the_warlords_democratic_sea_cat | GFX_decision_hol_attract_foreign_investors | 50 | yes |  | CHI_decisions.txt |
| CHI_integrating_states_democratic | CHI_integrate_the_warlords_democratic_sea_cat | GFX_decision_generic_political_address | 75 |  |  | CHI_decisions.txt |
| CHI_form_x_force | CHI_x_y_force_cat |  |  | yes |  | CHI_decisions.txt |
| CHI_form_y_force | CHI_x_y_force_cat |  |  | yes |  | CHI_decisions.txt |
| RNG_import_imperial_way_buddhism_decision | RNG_state_shintoism_decisions | GFX_decision_hol_exchange_intelligence_data | 50 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| RNG_one_people_united_under_shinto_decision | RNG_state_shintoism_decisions | GFX_decision_generic_civil_support | 50 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| RNG_state_shinto_in_education_decision | RNG_state_shintoism_decisions | GFX_decision_SOV_academy_of_sciences | 75 | yes | No Compromise, No Surrender | CHI_decisions.txt |
| CHI_fascist_infiltrate_state | PRC_infiltration_sea_cat | { |  |  |  | CHI_decisions.txt |
| CHI_counter_fascist_infiltration_measures | PRC_infiltration_sea_cat | { |  |  |  | CHI_decisions.txt |
| CHI_counter_fascist_infiltration_measures_level_3 | PRC_infiltration_sea_cat | GFX_decisions_generic_infiltration_3 | 100 |  |  | CHI_decisions.txt |
| YUN_core_state | political_actions | GFX_decision_infiltrate_state | 50 | yes |  | CHI_warlord_decisions.txt |
| CHI_internal_party_support_fascism | CHI_seek_japanese_support | generic_political_discourse | 35 |  |  | CHI_warlord_decisions.txt |
| CHI_aggresive_prosecution_of_opposition_fascism | CHI_seek_japanese_support | generic_civil_support | 0 |  |  | CHI_warlord_decisions.txt |
| CHI_internal_party_support_communism | CHI_seek_japanese_support | generic_political_discourse | 35 |  |  | CHI_warlord_decisions.txt |
| CHI_aggresive_prosecution_of_opposition_communism | CHI_seek_japanese_support | generic_civil_support | 0 |  |  | CHI_warlord_decisions.txt |
| CHI_internal_party_support_neutrality | CHI_seek_japanese_support | generic_political_discourse | 35 |  |  | CHI_warlord_decisions.txt |
| CHI_aggresive_prosecution_of_opposition_neutrality | CHI_seek_japanese_support | generic_civil_support | 0 |  |  | CHI_warlord_decisions.txt |
| CHI_internal_party_support_democratic | CHI_seek_japanese_support | generic_political_discourse | 35 |  |  | CHI_warlord_decisions.txt |
| CHI_approach_japan | CHI_seek_japanese_support | jap_pacific_guardian |  | yes |  | CHI_warlord_decisions.txt |
| SIK_war_halting | CHI_war_in_sinkiang | GFX_decision_generic_ignite_civil_war |  | yes |  | CHI_warlord_decisions.txt |
| KHM_holding_out | CHI_war_in_sinkiang | GFX_decision_generic_ignite_civil_war |  | yes |  | CHI_warlord_decisions.txt |
| SIC_push_into_xikang | SIC_xikang_offensive | border_war | 25 | yes |  | CHI_warlord_decisions.txt |
| SIC_push_into_xikang_mission | SIC_xikang_offensive | border_war |  |  |  | CHI_warlord_decisions.txt |
| SND_show_support_for_government | SND_unclear_loyalties_cat | GFX_decision_hol_exchange_intelligence_data | 25 |  |  | CHI_warlord_decisions.txt |
| SND_expel_japanese | SND_unclear_loyalties_cat | GFX_decision_generic_break_treaty | 25 |  |  | CHI_warlord_decisions.txt |
| SND_army_integration | SND_unclear_loyalties_cat | GFX_decision_generic_military | 25 |  |  | CHI_warlord_decisions.txt |
| SND_han_fuju_stays | SND_unclear_loyalties_cat | GFX_decision_generic_protection | 25 |  |  | CHI_warlord_decisions.txt |
| SND_swear_fealty_to_the_emperor | SND_unclear_loyalties_cat | GFX_decision_JAP_army_faction | 150 |  |  | CHI_warlord_decisions.txt |
| CHI_seek_party_support | CHI_tsr_power_struggle_cat | GFX_decision_hol_exchange_intelligence_data |  |  |  | CHI_warlord_decisions.txt |
| CHI_tsr_seek_warlord_support | CHI_tsr_power_struggle_cat | generic_civil_support | 50 | yes |  | CHI_warlord_decisions.txt |
| TSR_pay_for_support_from_warlord_PP | CHI_tsr_power_struggle_cat | generic_civil_support | 75 | yes |  | CHI_warlord_decisions.txt |
| TSR_pay_for_support_from_warlord_manpower | CHI_tsr_power_struggle_cat | generic_civil_support | 0 | yes |  | CHI_warlord_decisions.txt |
| TSR_pay_for_support_from_warlord_equipment | CHI_tsr_power_struggle_cat | generic_civil_support | 0 | yes |  | CHI_warlord_decisions.txt |
| CHI_warlord_propaganda_army | CHI_tsr_power_struggle_cat | GFX_decision_SWE_set_army_budget | 50 | yes |  | CHI_warlord_decisions.txt |
| CHI_warlord_propaganda_air | CHI_tsr_power_struggle_cat | GFX_decision_SWE_set_air_budget | 50 | yes |  | CHI_warlord_decisions.txt |
| CHI_warlord_propaganda_navy | CHI_tsr_power_struggle_cat | GFX_decision_generic_naval | 50 | yes |  | CHI_warlord_decisions.txt |
| CHI_warlord_propaganda_stable | CHI_tsr_power_struggle_cat | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | CHI_warlord_decisions.txt |
| CHI_tsr_take_national_leadership | CHI_tsr_power_struggle_cat | generic_nationalism | 75 | yes |  | CHI_warlord_decisions.txt |
| CHI_war_in_south_halting | CHI_war_in_liangguang | GFX_decision_generic_ignite_civil_war |  | yes |  | CHI_warlord_decisions.txt |
| GDC_holding_out | CHI_war_in_liangguang | GFX_decision_generic_ignite_civil_war |  | yes |  | CHI_warlord_decisions.txt |
| XIC_war_halting | XIC_war_in_yanan | GFX_decision_generic_ignite_civil_war |  | yes |  | CHI_warlord_decisions.txt |
| PRC_holding_out | XIC_war_in_yanan | GFX_decision_generic_ignite_civil_war |  | yes |  | CHI_warlord_decisions.txt |
| CHL_expand_araucanian_forestry_decision | CHL_industrial_decisions | GFX_decision_generic_forestry | 75 |  |  | CHL.txt |
| CHL_expand_chilean_forestry_decision | CHL_industrial_decisions | GFX_decision_generic_forestry | 100 |  |  | CHL.txt |
| CHL_take_loans_for_factory | CHL_industrial_decisions | GFX_decision_gre_investment_decisions | 50 |  |  | CHL.txt |
| CHL_take_loans_for_economy | CHL_industrial_decisions | GFX_decision_gre_investment_decisions | 100 |  |  | CHL.txt |
| CHL_take_loans_for_economy_2 | CHL_industrial_decisions | GFX_decision_gre_investment_decisions | 120 |  |  | CHL.txt |
| CHL_expand_araucanian_steelworks_decision | CHL_industrial_decisions | GFX_decision_steel | 100 |  |  | CHL.txt |
| CHL_buy_american_rifles | CHL_industrial_decisions | GFX_decision_generic_industry | 50 |  | Arms Against Tyranny | CHL.txt |
| CHL_buy_american_artillery | CHL_industrial_decisions | GFX_decision_generic_industry | 50 |  | Arms Against Tyranny | CHL.txt |
| CHL_buy_american_support_equipment | CHL_industrial_decisions | GFX_decision_generic_industry | 50 |  | Arms Against Tyranny | CHL.txt |
| CHL_establish_conadi | CHL_mapuche_reconcilliation_decisions | GFX_decision_eng_trade_unions_support | 75 |  |  | CHL.txt |
| CHL_protect_indigeous_lands | CHL_mapuche_reconcilliation_decisions | GFX_decision_generic_operation | 30 |  |  | CHL.txt |
| CHL_grant_full_rights_to_the_mapuche | CHL_mapuche_reconcilliation_decisions | GFX_decision_CHL_grant_full_rights_to_the_mapuche | 120 |  |  | CHL.txt |
| CHL_incorporate_mapuche_organizations | CHL_mapuche_reconcilliation_decisions | GFX_decision_generic_political_discourse | 110 |  |  | CHL.txt |
| CHL_nacista_coup_attempt | CHL_nacista_insurgency_decisions | GFX_decision_CHL_nacista_coup_attempt |  | yes |  | CHL.txt |
| CHL_nacistas_gathering_support_mission | CHL_nacista_insurgency_decisions | GFX_decision_eng_blackshirt_speech |  | yes |  | CHL.txt |
| CHL_nacista_newpapers_propaganda_mission | CHL_nacista_insurgency_decisions | GFX_decision_hol_radio_oranje |  | yes |  | CHL.txt |
| CHL_nacistas_approaching_ibanez_mission | CHL_nacista_insurgency_decisions | GFX_decision_generic_political_discourse |  | yes |  | CHL.txt |
| CHL_nacista_influence_in_the_universities_mission | CHL_nacista_insurgency_decisions | GFX_decision_SOV_place_hq |  | yes |  | CHL.txt |
| CHL_nacistas_approaching_foreign_fascists_mission | CHL_nacista_insurgency_decisions | GFX_decision_ger_reichskommissariats |  | yes |  | CHL.txt |
| CHL_nacistas_making_final_preparations_mission | CHL_nacista_insurgency_decisions | GFX_decision_generic_operation |  | yes |  | CHL.txt |
| CHL_expand_the_carabineros | CHL_nacista_insurgency_decisions | GFX_decision_CHL_carabineros | 75 |  |  | CHL.txt |
| CHL_open_investigations_against_the_nacistas | CHL_nacista_insurgency_decisions | GFX_decision_eng_trade_unions_support | 75 |  |  | CHL.txt |
| CHL_counterract_nationalist_thought_in_universities | CHL_nacista_insurgency_decisions | GFX_decision_SWI_no_elected_president | 50 |  |  | CHL.txt |
| CHL_strengthen_the_anti_fascist_coalition | CHL_nacista_insurgency_decisions | GFX_decision_hol_exchange_intelligence_data | 75 |  |  | CHL.txt |
| CHL_criticize_liberal_complacency | CHL_nacista_insurgency_decisions | GFX_decision_generic_political_rally | 100 |  |  | CHL.txt |
| CHL_demand_snap_election | CHL_nacista_insurgency_decisions | GFX_decision_generic_civil_support | 100 |  |  | CHL.txt |
| CHL_promote_ideology_rallies_americas | political_actions | generic_political_rally | 50 | yes |  | CHL.txt |
| CHL_recall_pedro_dartnell_to_active_service | political_actions | GFX_decision_generic_pickelhaube | 30 |  | Trial of Allegiance | CHL.txt |
| CHL_invite_peter_adolf_ceasar_to_chile | political_actions | GFX_decision_generic_army_support | 75 |  | Trial of Allegiance | CHL.txt |
| CHL_recall_manuel_santiago_pedregal_to_active_service | political_actions | GFX_decision_generic_army_support | 25 |  | Trial of Allegiance | CHL.txt |
| CHL_anti_fascist_coalition_forming | CHL_nacista_decisions | GFX_decision_generic_political_discourse |  | yes |  | CHL.txt |
| CHL_crackdown_on_fascists_bad_mission | CHL_nacista_decisions | GFX_decision_hol_radio_oranje |  | yes |  | CHL.txt |
| CHL_carabineros_being_secured_mission | CHL_nacista_decisions | GFX_decision_CHL_carabineros |  | yes |  | CHL.txt |
| CHL_national_falange_cooperation_mission | CHL_nacista_decisions | GFX_decision_generic_political_discourse |  | yes |  | CHL.txt |
| CHL_government_funds_being_extracted_mission | CHL_nacista_decisions | GFX_decision_gre_investment_decisions |  | yes |  | CHL.txt |
| CHL_republican_guards_in_exile_mission | CHL_nacista_decisions | GFX_decision_generic_army_support |  | yes |  | CHL.txt |
| CHL_preparing_another_naval_mutiny_mission | CHL_nacista_decisions | GFX_decision_generic_merge_plant_ship |  | yes |  | CHL.txt |
| CHL_reintigrate_tacna_fascist | CHL_nacista_decisions | GFX_decision_generic_nationalism | 50 |  |  | CHL.txt |
| CHL_intigrate_tierra_del_fuego_fascist | CHL_nacista_decisions | GFX_decision_generic_nationalism | 50 |  |  | CHL.txt |
| CHL_occupy_the_panama_canal | CHL_nacista_decisions | GFX_decision_infiltrate_state | 100 | yes |  | CHL.txt |
| CHL_occupy_belize | CHL_nacista_decisions | GFX_decision_infiltrate_state | 100 | yes |  | CHL.txt |
| CHL_integrate_rio_de_la_plata | CHL_nacista_decisions | GFX_decision_generic_form_nation | 100 |  |  | CHL.txt |
| CHL_introduce_authoritarianism_fascist | CHL_nacista_decisions | GFX_decision_generic_police_action | 50 |  |  | CHL.txt |
| CHL_adopt_the_patria_vieja_flag_decision | CHL_nacista_decisions | GFX_decision_eng_trade_unions_support | 25 |  |  | CHL.txt |
| CHL_support_resistance_decision | CHL_anti_colonialism_category | GFX_decision_generic_nationalism |  | yes |  | CHL.txt |
| CHL_arm_resistance_decision | CHL_anti_colonialism_category | GFX_decision_generic_prepare_civil_war |  | yes |  | CHL.txt |
| CHL_integrate_the_caribbean | CHL_hispanic_unity_decisions | GFX_decision_generic_nationalism | 100 |  |  | CHL.txt |
| CHL_integrate_central_america | CHL_hispanic_unity_decisions | GFX_decision_generic_nationalism | 100 |  |  | CHL.txt |
| CHL_integrate_mexico | CHL_hispanic_unity_decisions | GFX_decision_generic_nationalism | 100 |  |  | CHL.txt |
| CHL_liberate_american_hispanics | CHL_hispanic_unity_decisions | GFX_decision_generic_nationalism | 100 |  |  | CHL.txt |
| CHL_ibanez_ruling_by_decree_mission | CHL_mapuche_nationalism_decisions | GFX_decision_eng_trade_unions_support |  | yes |  | CHL.txt |
| CHL_ibanez_seeking_foreign_investments_mission | CHL_mapuche_nationalism_decisions | GFX_decision_gre_investment_decisions |  | yes |  | CHL.txt |
| CHL_ibanez_alianza_popular_libertadora_mission | CHL_mapuche_nationalism_decisions | GFX_decision_generic_political_discourse |  | yes |  | CHL.txt |
| CHL_ibanez_outlaw_socialism_mission | CHL_mapuche_nationalism_decisions | GFX_decision_generic_civil_support |  | yes |  | CHL.txt |
| CHL_ibanez_strengthening_the_carabineros_mission | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_carabineros |  | yes |  | CHL.txt |
| CHL_ibanez_cracking_down_on_mapuche_organizations_mission | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_ibanez_cracking_down_on_mapuche_organizations_mission |  | yes |  | CHL.txt |
| CHL_ibanez_utlilizing_national_populism_mission | CHL_mapuche_nationalism_decisions | GFX_decision_eng_blackshirt_speech |  | yes |  | CHL.txt |
| CHL_ibanez_selling_arica_mission | CHL_mapuche_nationalism_decisions | GFX_decision_hol_attract_foreign_investors |  | yes |  | CHL.txt |
| CHL_ibanez_securing_weapon_arsenals_mission | CHL_mapuche_nationalism_decisions | GFX_decision_generic_industry |  | yes |  | CHL.txt |
| CHL_ibanez_approaching_argentinian_army_mission | CHL_mapuche_nationalism_decisions | GFX_decision_generic_military |  | yes |  | CHL.txt |
| CHL_mapuche_form_defense_groups | CHL_mapuche_nationalism_decisions | GFX_decision_generic_prepare_civil_war | 10 |  |  | CHL.txt |
| CHL_integrate_the_south_atlantic_islands_mapuche | CHL_mapuche_nationalism_decisions | GFX_decision_generic_nationalism | 75 |  |  | CHL.txt |
| CHL_mapuche_liberate_rapa_nuis | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_rapa_nuis | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_tahiti | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_tahiti | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_samoa | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_samoa | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_hawaii | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_hawaii | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_guarani | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_guarani | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_inca | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_inca | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_miskito | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_miskito | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_maya | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_maya | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_inuit | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_inuit | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_charrua | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_charrua | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_itza | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_itza | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_nahua | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_nahua | 50 |  |  | CHL.txt |
| CHL_mapuche_liberate_isthmo_amerindia | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_liberate_isthmo_amerindia | 50 |  |  | CHL.txt |
| CHL_mapuche_reorganize_the_bolivian_government | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_reorganize_the_bolivian_government | 50 |  |  | CHL.txt |
| CHL_mapuche_reorganize_the_brazilian_government | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_reorganize_the_brazilian_government | 50 |  |  | CHL.txt |
| CHL_mapuche_reorganize_the_mexican_government | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_reorganize_the_mexican_government | 50 |  |  | CHL.txt |
| CHL_mapuche_establish_a_guianan_government | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_establish_a_guianan_government | 50 |  |  | CHL.txt |
| CHL_mapuche_reorganize_the_canadian_government | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_reorganize_the_canadian_government | 50 |  |  | CHL.txt |
| CHL_mapuche_reorganize_the_american_government | CHL_mapuche_nationalism_decisions | GFX_decision_CHL_mapuche_reorganize_the_american_government | 50 |  |  | CHL.txt |
| CHL_integrate_the_kingdom_of_mexico | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 100 |  |  | CHL.txt |
| CHL_integrate_french_guyana | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 50 |  |  | CHL.txt |
| CHL_integrate_st_pierre | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 25 |  |  | CHL.txt |
| CHL_integrate_french_caribbean | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 50 |  |  | CHL.txt |
| CHL_integrate_corsica | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 50 |  |  | CHL.txt |
| CHL_integrate_northern_france | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 120 |  |  | CHL.txt |
| CHL_integrate_southern_france | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 120 |  |  | CHL.txt |
| CHL_integrate_rio_grande_do_sul | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 100 |  |  | CHL.txt |
| CHL_integrate_quebec | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 100 |  |  | CHL.txt |
| CHL_araucania_establish_inca_kingdom | CHL_monarchist_decisions | GFX_decision_CHL_mapuche_liberate_inca | 50 |  |  | CHL.txt |
| CHL_integrate_the_south_atlantic_islands_araucania | CHL_monarchist_decisions | GFX_decision_generic_nationalism | 75 |  |  | CHL.txt |
| CHL_araucania_establish_a_guianan_government | CHL_monarchist_decisions | GFX_decision_CHL_mapuche_establish_a_guianan_government | 50 |  |  | CHL.txt |
| CHL_araucania_establish_a_hispaniolan_kingdom | CHL_monarchist_decisions | GFX_decision_CHL_araucania_establish_a_hispaniolan_kingdom | 50 |  |  | CHL.txt |
| CHL_bolster_revolutionaries_americas | CHL_the_hispanic_revolutions_decisions | GFX_decision_POL_organize_strike_two | 75 | yes |  | CHL.txt |
| CHL_initiate_a_revolution | CHL_the_hispanic_revolutions_decisions | GFX_decision_generic_independence | 100 | yes |  | CHL.txt |
| COG_embrace_autentiite_decision | political_actions | GFX_decision_eng_trade_unions_support | 25 |  |  | COG.txt |
| COG_recall_armand_huyghe_to_active_service | political_actions | GFX_decision_generic_belgian_colonial_helmet |  |  | Gotterdammerung | COG.txt |
| COG_recall_fredrik_valdemar_olsen_to_active_service | political_actions | GFX_decision_generic_army_support |  |  | Gotterdammerung | COG.txt |
| COG_recall_charles_tombeur_to_active_service | political_actions | GFX_decision_generic_army_support |  |  | Gotterdammerung | COG.txt |
| COG_recall_leopold_de_koninck_to_active_service | political_actions | GFX_decision_generic_belgian_colonial_helmet |  |  | Gotterdammerung | COG.txt |
| COG_increased_food_production_scheme_decision | political_actions | GFX_decision_hol_exchange_intelligence_data | 15 |  | Gotterdammerung | COG.txt |
| COG_integrate_kongolese_separatists | political_actions | GFX_decision_infiltrate_state | 10 |  | Gotterdammerung | COG.txt |
| COG_move_the_capital_to_loango | political_actions | GFX_decision_generic_operation | 25 |  | Gotterdammerung | COG.txt |
| COG_move_the_capital_to_bujumbura | political_actions | GFX_decision_generic_operation | 25 |  | Gotterdammerung | COG.txt |
| COG_move_the_capital_to_kigali | political_actions | GFX_decision_generic_operation | 25 |  | Gotterdammerung | COG.txt |
| COG_core_conquered_state_burundi | political_actions | GFX_decision_generic_form_nation | 75 | yes |  | COG.txt |
| COG_core_conquered_state_mittelafrika | political_actions | GFX_decision_generic_form_nation | 75 | yes |  | COG.txt |
| COG_investments_into_civ_factory | COG_industrial_investment_decisions | GFX_decision_gre_investment_decisions | 50 |  |  | COG.txt |
| COG_investments_into_villages | COG_industrial_investment_decisions | GFX_decision_generic_welfare | 50 |  |  | COG.txt |
| COG_kimberite_pipes_to_expand_bakwanga_mine | COG_industrial_investment_decisions | GFX_decision_generic_construction | 50 |  |  | COG.txt |
| COG_sell_diamonds_on_the_black_market_decision | economy_decisions | GFX_decision_hol_attract_foreign_investors | 5 |  |  | COG.txt |
| COG_oust_the_gold_barons | economy_decisions | GFX_decision_SWI_dismiss_council | 75 |  |  | COG.txt |
| COG_offer_uranium_sales_decision | economy_decisions | GFX_decision_gre_investment_decisions | 150 | yes |  | COG.txt |
| COG_cancel_the_trade_deal_decision | economy_decisions | GFX_decision_SWI_dismiss_council | 50 |  |  | COG.txt |
| COG_uranium_trust_invitation_decision | economy_decisions | GFX_decision_eng_trade_unions_support | 75 | yes |  | COG.txt |
| COG_force_leopoldville_capitulation_decision | war_measures | GFX_decision_eng_trade_unions_support | 25 |  |  | COG.txt |
| COG_expand_ruanda_urundi_cash_crop_farming | COG_ruanda_urundi_decisions | GFX_decision_POL_organize_strike_two | 50 |  |  | COG.txt |
| COG_utilize_volcanic_soils_to_cultivate_coffee | COG_ruanda_urundi_decisions | GFX_decision_POL_looming_peasants_strike | 75 |  |  | COG.txt |
| COG_improve_ruandan_civil_adminsitration | COG_ruanda_urundi_decisions | GFX_decision_eng_trade_unions_support | 25 |  |  | COG.txt |
| COG_improve_urundian_civil_adminsitration | COG_ruanda_urundi_decisions | GFX_decision_eng_trade_unions_support | 25 |  |  | COG.txt |
| COG_ruanda_urundi_conscription_centers | COG_ruanda_urundi_decisions | GFX_decision_generic_military | 50 |  |  | COG.txt |
| COG_invest_in_cfl | COG_the_empain_group_decisions | GFX_decision_generic_train | 75 |  |  | COG.txt |
| COG_invest_in_mirundi | COG_the_empain_group_decisions | GFX_decision_tungsten | 75 |  |  | COG.txt |
| COG_found_cominor | COG_the_empain_group_decisions | GFX_decision_aluminium | 50 |  |  | COG.txt |
| COG_invest_in_miluba | COG_the_empain_group_decisions | GFX_decision_generic_construction | 75 |  |  | COG.txt |
| COG_invest_in_minerga | COG_the_empain_group_decisions | GFX_decision_generic_factory | 50 |  |  | COG.txt |
| COG_support_resistance_decision | COG_anti_colonialism_category | GFX_decision_generic_nationalism |  | yes |  | COG.txt |
| COG_arm_resistance_decision | COG_anti_colonialism_category | GFX_decision_generic_prepare_civil_war |  | yes |  | COG.txt |
| COG_support_independence_decision | COG_anti_colonialism_category | GFX_decision_eng_propaganda_campaigns | 15 |  |  | COG.txt |
| COG_anti_colonialism_decision | COG_anti_colonialism_category | GFX_decision_eng_propaganda_campaigns | 15 | yes |  | COG.txt |
| COG_freedom_at_gunpoint_dynamic | COG_freedom_at_gunpoint_category | GFX_decision_generic_prepare_civil_war | 50 |  |  | COG.txt |
| COG_freedom_at_gunpoint_offer_peace | COG_freedom_at_gunpoint_category | GFX_decision_generic_form_nation | 50 |  |  | COG.txt |
| COG_freedom_at_gunpoint_subject_decision | COG_freedom_at_gunpoint_category | GFX_decision_generic_prepare_civil_war | 50 |  |  | COG.txt |
| COG_freedom_at_gunpoint_subject_offer_peace | COG_freedom_at_gunpoint_category | GFX_decision_generic_form_nation | 50 |  |  | COG.txt |
| COG_core_conquered_state | COG_congo_integration_decisions | GFX_decision_generic_form_nation | 75 | yes |  | COG.txt |
| DEBUG_DANNE | debug_decisions |  |  |  |  | DEN.txt |
| DEBUG_remove_bop_debug | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_show_bop_debug | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_absurdly_high_increase_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_very_high_increase_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_high_increase_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_medium_increase_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_low_increase_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_very_low_increase_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_absurdly_high_decrease_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_very_high_decrease_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_high_decrease_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_medium_decrease_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_low_decrease_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_very_low_decrease_value | DEN_balance_of_power_category |  |  |  |  | DEN.txt |
| DEN_bop_defend_our_chosen_path | DEN_balance_of_power_category | GFX_decision_generic_speech | 0 |  |  | DEN.txt |
| DEN_bop_exile_royal_family | DEN_balance_of_power_category | GFX_decision_generic_speech | 50 |  |  | DEN.txt |
| DEN_bop_ban_elections | DEN_balance_of_power_category | GFX_decision_generic_speech | 150 |  |  | DEN.txt |
| DEN_bop_motion_of_no_confidence | DEN_balance_of_power_category | GFX_decision_generic_speech |  |  |  | DEN.txt |
| DEN_bop_criticize_the_country_leader | DEN_balance_of_power_category | GFX_decision_generic_speech |  |  |  | DEN.txt |
| DEN_bop_defend_our_chosen_path_neutrality | DEN_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | DEN.txt |
| DEN_bop_ban_all_political_uniforms | DEN_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | DEN.txt |
| DEN_bop_unban_oppositions_uniforms | DEN_balance_of_power_category | GFX_decision_generic_political_address |  |  |  | DEN.txt |
| DEN_bop_defend_the_policy_of_neutrality | DEN_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | DEN.txt |
| DEN_bop_speak_out_in_favor_of_disarmament | DEN_balance_of_power_category | GFX_decision_generic_political_address |  |  |  | DEN.txt |
| DEN_bop_speak_out_against_warfare | DEN_balance_of_power_category | GFX_decision_generic_political_address |  |  |  | DEN.txt |
| DEN_bop_expand_the_welfare | DEN_balance_of_power_category | GFX_decision_generic_welfare |  | yes |  | DEN.txt |
| DEN_bop_unban_all_political_uniforms | DEN_balance_of_power_category | GFX_decision_generic_political_address |  |  |  | DEN.txt |
| DEN_bop_ban_oppositions_uniforms | DEN_balance_of_power_category | GFX_decision_generic_speech |  |  |  | DEN.txt |
| DEN_bop_defend_our_chosen_path_rearmament | DEN_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | DEN.txt |
| DEN_bop_criticize_our_preparedness | DEN_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | DEN.txt |
| DEN_bop_question_our_defenses | DEN_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | DEN.txt |
| DEN_bop_speak_out_against_welfare | DEN_balance_of_power_category | GFX_decision_generic_political_address |  |  |  | DEN.txt |
| DEN_bop_speak_out_in_favor_of_rearmament | DEN_balance_of_power_category | GFX_decision_generic_protection |  |  |  | DEN.txt |
| DEN_bop_landstorm | DEN_balance_of_power_category | GFX_decision_generic_protection |  | yes |  | DEN.txt |
| DEN_bop_hold_a_military_parade | DEN_balance_of_power_category | GFX_decision_generic_military |  |  |  | DEN.txt |
| DEBUG_remove_bop_occupation_debug | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_show_bop_occupation_debug | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_absurdly_high_increase_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_very_high_increase_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_high_increase_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_medium_increase_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_low_increase_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_very_low_increase_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_absurdly_high_decrease_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_very_high_decrease_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_high_decrease_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_medium_decrease_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_low_decrease_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_bop_occupation_very_low_decrease_value | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_opinion_modifier_small | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEBUG_DEN_opinion_modifier_big | DEN_occupation_category |  |  |  |  | DEN.txt |
| DEN_bop_occupation_strikes | DEN_occupation_category | GFX_decision_generic_civil_support |  |  |  | DEN.txt |
| DEN_bop_occupation_criticize_collaboration | DEN_occupation_category | GFX_decision_eng_propaganda_campaigns |  |  |  | DEN.txt |
| DEN_bop_occupation_resistance_coordination | DEN_occupation_category | GFX_decision_generic_civil_support |  | yes |  | DEN.txt |
| DEN_bop_occupation_raid_depots | DEN_occupation_category | GFX_decision_generic_civil_support |  |  |  | DEN.txt |
| DEN_bop_occupation_sabotage_civ_industry | DEN_occupation_category | GFX_decision_generic_ignite_civil_war |  | yes |  | DEN.txt |
| DEN_bop_occupation_sabotage_mil_industry | DEN_occupation_category | GFX_decision_generic_ignite_civil_war |  | yes |  | DEN.txt |
| DEN_bop_occupation_underground_factories | DEN_occupation_category | GFX_decision_generic_prepare_civil_war |  |  |  | DEN.txt |
| DEN_bop_occupation_funnel_resources_danish_brigade | DEN_occupation_category | GFX_decision_generic_industry |  | yes |  | DEN.txt |
| DEN_bop_occupation_switch_ideology | DEN_occupation_category | GFX_decision_eng_propaganda_campaigns |  |  |  | DEN.txt |
| DEN_bop_occupation_ban_elections | DEN_occupation_category | GFX_decision_generic_speech |  |  |  | DEN.txt |
| DEN_bop_occupation_defend_collaboration | DEN_occupation_category | GFX_decision_eng_propaganda_campaigns |  | yes |  | DEN.txt |
| DEN_bop_occupation_censor_the_media | DEN_occupation_category | GFX_decision_eng_trade_unions_support |  | yes |  | DEN.txt |
| DEN_bop_occupation_remove_political_agitator | DEN_occupation_category | GFX_decision_generic_political_discourse |  | yes |  | DEN.txt |
| DEN_bop_occupation_ban_communism | DEN_occupation_category | GFX_decision_generic_speech |  | yes |  | DEN.txt |
| DEN_bop_occupation_allow_communism | DEN_occupation_category | GFX_decision_generic_political_address |  | yes |  | DEN.txt |
| DEN_bop_occupation_ban_fascism | DEN_occupation_category | GFX_decision_generic_speech |  | yes |  | DEN.txt |
| DEN_bop_occupation_allow_fascism | DEN_occupation_category | GFX_decision_generic_political_address |  | yes |  | DEN.txt |
| DEN_bop_occupation_allow_democratism | DEN_occupation_category | GFX_decision_generic_political_address |  | yes |  | DEN.txt |
| DEN_seek_foreign_support_decision | DEN_resistance_category | GFX_decision_hol_exchange_intelligence_data | 0 |  |  | DEN.txt |
| DEN_ask_for_weapons_decision | DEN_resistance_category | GFX_decision_generic_prepare_civil_war |  |  |  | DEN.txt |
| DEN_seek_danish_brigades_host | DEN_resistance_category | GFX_decision_generic_military | 0 |  |  | DEN.txt |
| DEN_buy_foreign_destroyers | DEN_resistance_category | GFX_decision_generic_naval |  | yes |  | DEN.txt |
| DEN_annex_denmark | DEN_overlord_category | GFX_decision_oppression | 100 | yes |  | DEN.txt |
| DEN_seize_jylland | DEN_overlord_category | GFX_decision_oppression | 100 | yes |  | DEN.txt |
| DEN_reclaim_sonderjylland | DEN_overlord_category | GFX_decision_eng_trade_unions_support | 50 | yes |  | DEN.txt |
| DEN_install_plenipotentiary | DEN_overlord_category | GFX_decision_oppression | 50 | yes |  | DEN.txt |
| DEN_demand_country_leader_resignation | DEN_overlord_category | GFX_decision_eng_trade_unions_demand | 25 | yes |  | DEN.txt |
| DEN_demand_government_change | DEN_overlord_category | GFX_decision_eng_trade_unions_demand | 50 | yes |  | DEN.txt |
| DEN_demand_communist_ban | DEN_overlord_category | GFX_decision_eng_trade_unions_demand | 25 | yes |  | DEN.txt |
| DEN_demand_fascist_ban | DEN_overlord_category | GFX_decision_eng_trade_unions_demand | 25 | yes |  | DEN.txt |
| DEN_demand_weapon_deliveries | DEN_overlord_category | GFX_decision_generic_prepare_civil_war | 25 |  |  | DEN.txt |
| DEN_demand_troops | DEN_overlord_category | GFX_decision_generic_military | 25 |  |  | DEN.txt |
| DEN_overlord_requests_the_return_of_the_faroes | DEN_overlord_category | GFX_decision_generic_operation | 50 | yes |  | DEN.txt |
| DEN_overlord_requests_greenland_back | DEN_overlord_category | generic_operation | 50 | yes |  | DEN.txt |
| DEN_increase_trade_with_denmark | DEN_trade_deal_category | GFX_decision_eng_trade_unions_support | 50 | yes |  | DEN.txt |
| DEN_cancel_trade_with_denmark | DEN_trade_deal_category | GFX_decision_generic_break_treaty | 0 | yes |  | DEN.txt |
| DEN_cancel_trade_with_country | DEN_trade_deal_category | GFX_decision_generic_break_treaty | 0 | yes |  | DEN.txt |
| DEN_forts_in_sjaelland | DEN_fortification_category | GFX_decision_generic_fortification |  | yes |  | DEN.txt |
| DEN_forts_in_fyn | DEN_fortification_category | GFX_decision_generic_fortification |  | yes |  | DEN.txt |
| DEN_forts_in_norrejylland | DEN_fortification_category | GFX_decision_generic_fortification |  | yes |  | DEN.txt |
| DEN_forts_in_sonderjylland | DEN_fortification_category | GFX_decision_generic_fortification |  | yes |  | DEN.txt |
| DEN_coastal_forts_in_sjaelland | DEN_fortification_category | GFX_decision_generic_coastal_fortification |  | yes |  | DEN.txt |
| DEN_coastal_forts_in_fyn | DEN_fortification_category | GFX_decision_generic_coastal_fortification |  | yes |  | DEN.txt |
| DEN_coastal_forts_in_norrejylland | DEN_fortification_category | GFX_decision_generic_coastal_fortification |  | yes |  | DEN.txt |
| DEN_coastal_forts_in_sonderjylland | DEN_fortification_category | GFX_decision_generic_coastal_fortification |  | yes |  | DEN.txt |
| DEN_develop_state_greenland | DEN_development_category | GFX_decision_generic_construction | 101 |  |  | DEN.txt |
| DEN_develop_state_bornholm | DEN_development_category | GFX_decision_generic_construction | 910 |  |  | DEN.txt |
| DEN_develop_state_faroes | DEN_development_category | GFX_decision_generic_construction | 337 |  |  | DEN.txt |
| DEN_develop_state_gotland | DEN_development_category | GFX_decision_generic_construction | 124 |  |  | DEN.txt |
| DEN_develop_state_iceland | DEN_development_category | GFX_decision_generic_construction | 100 |  |  | DEN.txt |
| DEN_develop_state_norrejylland | DEN_development_category | GFX_decision_generic_construction | 99 |  |  | DEN.txt |
| DEN_develop_state_sonderjylland | DEN_development_category | GFX_decision_generic_construction | 912 |  |  | DEN.txt |
| DEN_develop_state_sjaelland | DEN_development_category | GFX_decision_generic_construction | 37 |  |  | DEN.txt |
| DEN_develop_state_fyn | DEN_development_category | GFX_decision_generic_construction | 911 |  |  | DEN.txt |
| DEN_deploy_the_home_guard | DEN_military_category | GFX_decision_generic_protection |  |  |  | DEN.txt |
| DEN_remove_the_home_guard | DEN_military_category | GFX_decision_eng_blackshirt_march | 0 |  |  | DEN.txt |
| DEN_deploy_landstormen | DEN_military_category | GFX_decision_generic_military |  |  |  | DEN.txt |
| DEN_recall_landstormen | DEN_military_category | GFX_decision_eng_blackshirt_march | 0 |  |  | DEN.txt |
| DEN_army_drills | DEN_military_category | GFX_decision_generic_military |  |  |  | DEN.txt |
| DEN_navy_drills | DEN_military_category | GFX_decision_generic_military |  |  |  | DEN.txt |
| DEN_air_drills | DEN_military_category | GFX_decision_generic_military |  |  |  | DEN.txt |
| DEN_seek_guarantor | DEN_danish_security_category | GFX_decision_hol_exchange_intelligence_data | 0 |  |  | DEN.txt |
| DEN_seek_an_alliance | DEN_danish_security_category | GFX_decision_hol_exchange_intelligence_data | 0 |  | No Compromise, No Surrender | DEN.txt |
| DEN_invite_nordic_countries | DEN_nordic_security_category | GFX_decision_generic_protection | 0 |  |  | DEN.txt |
| DEN_invade_nordic_countries | DEN_nordic_security_category | GFX_decision_generic_prepare_civil_war | 0 |  |  | DEN.txt |
| DEN_integrate_iceland | DEN_integration_puppets_category | GFX_decision_generic_nationalism |  | yes |  | DEN.txt |
| DEN_integrate_sweden | DEN_integration_puppets_category | GFX_decision_generic_nationalism |  | yes |  | DEN.txt |
| DEN_integrate_finland | DEN_integration_puppets_category | GFX_decision_generic_nationalism |  | yes |  | DEN.txt |
| DEN_integrate_norway | DEN_integration_puppets_category | GFX_decision_generic_nationalism |  | yes |  | DEN.txt |
| DEN_demand_icelandic_territory | DEN_demand_territory_category | GFX_decision_eng_trade_unions_demand | 75 |  |  | DEN.txt |
| DEN_demand_swedish_territory | DEN_demand_territory_category | GFX_decision_eng_trade_unions_demand | 75 |  |  | DEN.txt |
| DEN_demand_finnish_territory | DEN_demand_territory_category | GFX_decision_eng_trade_unions_demand | 75 |  |  | DEN.txt |
| DEN_demand_norwegian_territory | DEN_demand_territory_category | GFX_decision_eng_trade_unions_demand | 75 |  |  | DEN.txt |
| DEN_rally_the_icelanders | DEN_pan_scandinavianism_decisions_category | GFX_decision_generic_nationalism |  |  |  | DEN.txt |
| DEN_rally_the_swedes | DEN_pan_scandinavianism_decisions_category | GFX_decision_generic_nationalism |  |  |  | DEN.txt |
| DEN_rally_the_finnish | DEN_pan_scandinavianism_decisions_category | GFX_decision_generic_nationalism |  |  |  | DEN.txt |
| DEN_rally_the_norwegians | DEN_pan_scandinavianism_decisions_category | GFX_decision_generic_nationalism |  |  |  | DEN.txt |
| DEN_swedish_steel_for_security | DEN_swedish_steel_production_category | GFX_decision_steel | 0 |  |  | DEN.txt |
| DEN_northern_national_front_invitation | DEN_danish_faction_category | GFX_decision_generic_protection | 25 |  |  | DEN.txt |
| DEN_northern_security_pact_invitation | DEN_danish_faction_category | GFX_decision_generic_protection | 50 |  |  | DEN.txt |
| DEN_northern_technological_advancements_group_invite | DEN_danish_faction_category | GFX_decision_generic_research | 25 |  |  | DEN.txt |
| DEN_influence_countries_decision | DEN_influence_countries_category | GFX_decision_SWI_expand_covert_operations | 50 |  |  | DEN.txt |
| DEN_offer_protection_decision | DEN_offer_protection_category | GFX_decision_generic_protection | 50 | yes |  | DEN.txt |
| DEN_request_the_return_of_the_faroes | DEN_return_occupied_territory_category | GFX_decision_generic_operation | 0 | yes | Arms Against Tyranny | DEN.txt |
| DEN_request_greenland_back | DEN_return_occupied_territory_category | generic_operation | 0 | yes | Arms Against Tyranny | DEN.txt |
| HUN_closer_ties_to_CZE | political_actions |  | 75 |  |  | DOD_hungary.txt |
| HUN_call_in_sweden | political_actions |  | 0 |  |  | DOD_hungary.txt |
| HUN_call_in_hungary | political_actions |  | 0 |  |  | DOD_hungary.txt |
| ENG_narvik_crisis | ENG_narvik_crisis_cat | generic_operation | 10 | yes |  | ENG.txt |
| ENG_narvik_crisis_blow_up_mines | ENG_narvik_crisis_cat | generic_operation |  |  |  | ENG.txt |
| ENG_explode_the_swedish_iron_ore_mine | ENG_narvik_crisis_cat | eng_support_imperialist_coup |  | yes |  | ENG.txt |
| ENG_urge_restraint | ENG_organize_the_blackshirts | eng_propaganda_campaigns | 25 |  |  | ENG.txt |
| ENG_blackshirt_march_in_northern_ireland | ENG_organize_the_blackshirts | eng_blackshirt_march | 26 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_the_highlands | ENG_organize_the_blackshirts | eng_blackshirt_march | 6 | yes |  | ENG.txt |
| ENG_blackshirt_march_on_the_isle_of_man | ENG_organize_the_blackshirts | eng_blackshirt_march | 6 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_aberdeenshire | ENG_organize_the_blackshirts | eng_blackshirt_march | 17 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_cumbria | ENG_organize_the_blackshirts | eng_blackshirt_march | 31 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_lanark | ENG_organize_the_blackshirts | eng_blackshirt_march | 48 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_lothian | ENG_organize_the_blackshirts | eng_blackshirt_march | 31 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_northern_england | ENG_organize_the_blackshirts | eng_blackshirt_march | 46 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_yorkshire | ENG_organize_the_blackshirts | eng_blackshirt_march | 91 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_lancashire | ENG_organize_the_blackshirts | eng_blackshirt_march | 113 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_wales | ENG_organize_the_blackshirts | eng_blackshirt_march | 49 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_west_midlands | ENG_organize_the_blackshirts | eng_blackshirt_march | 76 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_east_midlands | ENG_organize_the_blackshirts | eng_blackshirt_march | 47 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_east_anglia | ENG_organize_the_blackshirts | eng_blackshirt_march | 30 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_gloucestershire | ENG_organize_the_blackshirts | eng_blackshirt_march | 39 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_london | ENG_organize_the_blackshirts | eng_blackshirt_march | 173 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_cornwall | ENG_organize_the_blackshirts | eng_blackshirt_march | 27 | yes |  | ENG.txt |
| ENG_blackshirt_march_in_sussex | ENG_organize_the_blackshirts | eng_blackshirt_march | 67 | yes |  | ENG.txt |
| ENG_march_on_downing_street | ENG_organize_the_blackshirts | eng_blackshirt_march | 100 | yes |  | ENG.txt |
| ENG_reconciliatory_speech | ENG_organize_the_blackshirts | eng_blackshirt_march | 50 |  |  | ENG.txt |
| ENG_speech_against_germany | ENG_organize_the_blackshirts | eng_blackshirt_speech | 50 |  |  | ENG.txt |
| ENG_the_mosley_plan | ENG_organize_the_blackshirts | generic_construction | 25 | yes |  | ENG.txt |
| ENG_enforce_blackouts | ENG_homeland_defense_decision_cat | GFX_decision_eng_propaganda_campaigns | 50 |  |  | ENG.txt |
| ENG_end_the_blackouts | ENG_homeland_defense_decision_cat | GFX_decision_eng_propaganda_campaigns | 50 |  |  | ENG.txt |
| ENG_promote_the_blitz_spirit | ENG_homeland_defense_decision_cat | GFX_decision_eng_install_government | 50 |  |  | ENG.txt |
| ENG_the_homeland_defense_act | ENG_homeland_defense_decision_cat | GFX_decision_eng_trade_unions_support | 15 | yes |  | ENG.txt |
| ENG_establish_the_local_defense_volunteers | ENG_homeland_defense_decision_cat | GFX_decision_eng_blackshirt_march | 25 | yes |  | ENG.txt |
| ENG_utilize_home_guard_in_factories | ENG_homeland_defense_decision_cat | GFX_decision_generic_industry | 50 | yes |  | ENG.txt |
| ENG_raise_the_home_guard_in_state | ENG_homeland_defense_decision_cat | GFX_decision_generic_protection | 25 | yes |  | ENG.txt |
| ENG_send_the_home_guard_back_home | ENG_homeland_defense_decision_cat | GFX_decision_SWI_dismiss_council | 10 | yes |  | ENG.txt |
| ENG_support_imperialist_coup_in_canada | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 100 | yes |  | ENG.txt |
| ENG_support_imperialist_coup_in_canada_mission_1 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_suppress_imperialist_coup_in_canada | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_support_imperialist_coup_in_canada_mission_2 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_renew_support_for_imperialist_coup_in_canada | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_support_imperialist_coup_in_south_africa | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 100 | yes |  | ENG.txt |
| ENG_support_imperialist_coup_in_south_africa_mission_1 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_suppress_imperialist_coup_in_south_africa | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_support_imperialist_coup_in_south_africa_mission_2 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_renew_support_for_imperialist_coup_in_south_africa | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_support_imperialist_coup_in_australia | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 100 | yes |  | ENG.txt |
| ENG_support_imperialist_coup_in_australia_mission_1 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_suppress_imperialist_coup_in_australia | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_support_imperialist_coup_in_australia_mission_2 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_renew_support_for_imperialist_coup_in_australia | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_support_imperialist_coup_in_new_zealand | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 100 | yes |  | ENG.txt |
| ENG_support_imperialist_coup_in_new_zealand_mission_1 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_suppress_imperialist_coup_in_new_zealand | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_support_imperialist_coup_in_new_zealand_mission_2 | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup |  |  |  | ENG.txt |
| ENG_renew_support_for_imperialist_coup_in_new_zealand | ENG_appeal_to_imperial_loyalists | eng_support_imperialist_coup | 50 |  |  | ENG.txt |
| ENG_ally_the_canadian_imperialist_uprising | ENG_appeal_to_imperial_loyalists | eng_ally_imperialist_coup |  | yes | Death or Dishonor | ENG.txt |
| ENG_ally_the_south_african_imperialist_uprising | ENG_appeal_to_imperial_loyalists | eng_ally_imperialist_coup |  | yes | Death or Dishonor | ENG.txt |
| ENG_ally_the_australian_imperialist_uprising | ENG_appeal_to_imperial_loyalists | eng_ally_imperialist_coup |  | yes | Death or Dishonor | ENG.txt |
| ENG_ally_the_new_zealand_imperialist_uprising | ENG_appeal_to_imperial_loyalists | eng_ally_imperialist_coup |  | yes | Death or Dishonor | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_1 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_2 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_3 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_4 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_5 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_6 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_7 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_8 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_9 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_10 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_11 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_12 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_13 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_14 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_15 | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minister_appointment_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_legislation_amendment | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 150 | yes |  | ENG.txt |
| ENG_trade_unions_demand_legislation_amendment_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_conscription_limitations | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 75 | yes |  | ENG.txt |
| ENG_trade_unions_demand_conscription_limitations_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_workplace_safety_legislation | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 75 | yes |  | ENG.txt |
| ENG_trade_unions_demand_workplace_safety_legislation_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_increase_in_paid_leave | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 75 | yes |  | ENG.txt |
| ENG_trade_unions_demand_increase_in_paid_leave_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_minimum_pay_increase | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 75 | yes |  | ENG.txt |
| ENG_trade_unions_demand_minimum_pay_increase_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_construction_safety_legislation | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 75 | yes |  | ENG.txt |
| ENG_trade_unions_demand_construction_safety_legislation_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_mandatory_union_days | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_mandatory_union_days_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_trade_unions_demand_referendum | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand | 100 | yes |  | ENG.txt |
| ENG_trade_unions_demand_referendum_mission | ENG_concessions_to_the_trade_unions | eng_trade_unions_demand |  |  |  | ENG.txt |
| ENG_request_trade_union_support_for_new_factories | ENG_concessions_to_the_trade_unions | eng_trade_unions_support |  |  |  | ENG.txt |
| ENG_request_trade_union_factory_worker_support | ENG_concessions_to_the_trade_unions | eng_trade_unions_support |  |  |  | ENG.txt |
| ENG_request_trade_union_dockyard_worker_support | ENG_concessions_to_the_trade_unions | eng_trade_unions_support |  |  |  | ENG.txt |
| ENG_request_trade_union_construction_worker_support | ENG_concessions_to_the_trade_unions | eng_trade_unions_support |  |  |  | ENG.txt |
| ENG_request_trade_union_war_propaganda_support | ENG_concessions_to_the_trade_unions | eng_trade_unions_support |  |  |  | ENG.txt |
| ENG_expected_decolonization | ENG_concessions_to_the_trade_unions | eng_abdication_crisis |  | yes |  | ENG.txt |
| ENG_impose_martial_law_on_canada | ENG_move_to_secure_the_dominions | generic_civil_support | 50 | yes |  | ENG.txt |
| ENG_propaganda_campaigns_in_canada | ENG_move_to_secure_the_dominions | eng_propaganda_campaigns | 25 | yes |  | ENG.txt |
| ENG_replace_government_in_canada_fascism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_replace_government_in_canada_communism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_impose_martial_law_on_south_africa | ENG_move_to_secure_the_dominions | generic_civil_support | 50 | yes |  | ENG.txt |
| ENG_propaganda_campaigns_in_south_africa | ENG_move_to_secure_the_dominions | eng_propaganda_campaigns | 25 | yes |  | ENG.txt |
| ENG_replace_government_in_south_africa_fascism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_replace_government_in_south_africa_communism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_impose_martial_law_on_british_raj | ENG_move_to_secure_the_dominions | generic_civil_support | 50 | yes |  | ENG.txt |
| ENG_propaganda_campaigns_in_british_raj | ENG_move_to_secure_the_dominions | eng_propaganda_campaigns | 25 | yes |  | ENG.txt |
| ENG_replace_government_in_british_raj_fascism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_replace_government_in_british_raj_communism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_impose_martial_law_on_australia | ENG_move_to_secure_the_dominions | generic_civil_support | 50 | yes |  | ENG.txt |
| ENG_propaganda_campaigns_in_australia | ENG_move_to_secure_the_dominions | eng_propaganda_campaigns | 25 | yes |  | ENG.txt |
| ENG_replace_government_in_australia_fascism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_replace_government_in_australia_communism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_impose_martial_law_on_new_zealand | ENG_move_to_secure_the_dominions | generic_civil_support | 50 | yes |  | ENG.txt |
| ENG_propaganda_campaigns_in_new_zealand | ENG_move_to_secure_the_dominions | eng_propaganda_campaigns | 25 | yes |  | ENG.txt |
| ENG_replace_government_in_new_zealand_fascism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_replace_government_in_new_zealand_communism | ENG_move_to_secure_the_dominions | eng_install_government | 50 | yes |  | ENG.txt |
| ENG_imperial_conference_decision | ENG_imperial_conference_decision | generic_political_discourse |  | yes |  | ENG.txt |
| ENG_discuss_imperial_defense | ENG_imperial_conference_decision | eng_trade_unions_support | 50 | yes |  | ENG.txt |
| ENG_discuss_imperial_trade | ENG_imperial_conference_decision | eng_trade_unions_support | 50 | yes |  | ENG.txt |
| ENG_discuss_imperial_economy | ENG_imperial_conference_decision | eng_trade_unions_support | 50 | yes |  | ENG.txt |
| ENG_discuss_appeasement | ENG_imperial_conference_decision | eng_trade_unions_support | 50 | yes |  | ENG.txt |
| ENG_discuss_imperial_federation | ENG_imperial_conference_decision | eng_imperial_federation | 100 | yes |  | ENG.txt |
| hold_blood_toil_tears_sweat_speech | political_actions | generic_political_discourse | 50 | yes |  | ENG.txt |
| hold_fight_on_the_beaches_speech | political_actions | generic_political_discourse | 50 | yes |  | ENG.txt |
| hold_this_was_their_finest_hour_speech | political_actions | generic_political_discourse | 50 | yes |  | ENG.txt |
| macdonald_proposal | political_actions |  | 50 | yes |  | ENG.txt |
| ENG_invoke_the_alliance_of_1373 | political_actions | generic_prepare_civil_war | 100 |  |  | ENG.txt |
| ENG_request_azores_lease | political_actions |  | 50 | yes |  | ENG.txt |
| ENG_abdication_crisis | political_actions | eng_abdication_crisis |  | yes |  | ENG.txt |
| ENG_britain_demands_treaty_compliance | political_actions | generic_naval |  |  |  | ENG.txt |
| ENG_declare_american_monarchy | political_actions | eng_install_government |  | yes |  | ENG.txt |
| ENG_install_american_monarchy | political_actions | eng_install_government |  | yes |  | ENG.txt |
| ENG_create_pan_north_american_state | political_actions | eng_install_government |  | yes |  | ENG.txt |
| operation_fork | operations | generic_operation | 35 | yes |  | ENG.txt |
| ENG_operation_valentine | operations | generic_operation | 25 | yes | Arms Against Tyranny | ENG.txt |
| invade_ireland | operations | generic_operation | 75 | yes |  | ENG.txt |
| mers_el_kebir_raid | operations | generic_naval | 100 | yes |  | ENG.txt |
| ENG_demand_treaty_compliance | ENG_enforce_the_naval_treaties | eng_trade_unions_demand | 50 |  |  | ENG.txt |
| EST_vaps_uprising | EST_vaps_revolt_category | GFX_decision_revolt |  | yes |  | EST.txt |
| EST_vaps_crackdown | EST_vaps_revolt_category | GFX_decision_oppression |  | yes |  | EST.txt |
| EST_divide_veterans_societies | EST_fight_vaps_decisions |  |  | yes |  | EST.txt |
| EST_disrupt_vaps_recruitment | EST_fight_vaps_decisions |  |  | yes |  | EST.txt |
| EST_crackdown_on_vaps | EST_fight_vaps_decisions |  |  | yes |  | EST.txt |
| EST_put_vaps_leaders_on_trial | EST_fight_vaps_decisions |  |  | yes |  | EST.txt |
| EST_launch_vaps_investigation | EST_fight_vaps_decisions |  |  | yes |  | EST.txt |
| EST_anti_vaps_propaganda | EST_fight_vaps_decisions |  | 50 | yes |  | EST.txt |
| EST_delay_the_crackdown | EST_fight_vaps_decisions |  | 25 | yes |  | EST.txt |
| EST_stomp_the_vaps | march_through_estonia | GFX_decision_revolt |  | yes |  | EST.txt |
| EST_march_in_state | march_through_estonia | hol_draw_up_staff_plans | 25 |  |  | EST.txt |
| EST_march_in_FIN_state | EST_convert_FIN_cat | hol_draw_up_staff_plans | 25 |  |  | EST.txt |
| EST_march_in_FIN_capital | EST_convert_FIN_cat | hol_draw_up_staff_plans | 25 |  |  | EST.txt |
| ETH_defeat_italy | ETH_defeat_italy_category | GFX_decision_generic_prepare_civil_war |  | yes |  | ETH.txt |
| ETH_coup_haile_selassie_imru | democratic_on_the_rise | GFX_decision_generic_prepare_civil_war | 100 | yes |  | ETH.txt |
| ETH_formal_request_to_host | governments_in_exile | GFX_decision_eng_trade_unions_support | 150 | yes |  | ETH.txt |
| ETH_false_flag_operation_decision | governments_in_exile | GFX_decision_generic_ignite_civil_war |  | yes |  | ETH.txt |
| ETH_throw_grand_party_for_host | governments_in_exile | GFX_decision_gre_investment_decisions |  |  |  | ETH.txt |
| ETH_take_loans | governments_in_exile | GFX_decision_hol_attract_foreign_investors | 50 |  |  | ETH.txt |
| ETH_fundraising_campaign_decision | governments_in_exile | GFX_decision_generic_fundraising | 50 |  |  | ETH.txt |
| ETH_recruit_mercenaries_from_host | governments_in_exile | GFX_decision_generic_military |  |  |  | ETH.txt |
| ETH_recruit_aircrews_from_host | governments_in_exile | GFX_decision_generic_air |  |  |  | ETH.txt |
| ETH_recruit_merchant_marines_from_host | governments_in_exile | GFX_decision_generic_merge_plant_ship |  |  |  | ETH.txt |
| ETH_buy_rifles_from_host | governments_in_exile | GFX_decision_generic_prepare_civil_war |  |  |  | ETH.txt |
| ETH_buy_support_equipment_from_host | governments_in_exile | GFX_decision_generic_merge_plant_materiel |  |  |  | ETH.txt |
| ETH_buy_tanks_from_host | governments_in_exile | GFX_decision_generic_tank |  |  | No Step Back | ETH.txt |
| ETH_disband_the_chitet | ETH_chitet_category | GFX_decision_ETH_chitet | 0 |  |  | ETH.txt |
| ETH_host_country_decision | ETH_second_italo_ethiopian_war_category | generic_prepare_civil_war | 0 |  |  | ETH.txt |
| ETH_buy_rifles | ETH_second_italo_ethiopian_war_category | generic_prepare_civil_war | 50 |  |  | ETH.txt |
| ETH_buy_artillery | ETH_second_italo_ethiopian_war_category | generic_prepare_civil_war | 50 |  |  | ETH.txt |
| ETH_buy_support_equipment | ETH_second_italo_ethiopian_war_category | generic_prepare_civil_war | 50 |  |  | ETH.txt |
| ETH_buy_anti_tank_guns | ETH_second_italo_ethiopian_war_category | generic_prepare_civil_war | 50 |  |  | ETH.txt |
| ETH_time_based_war_escalation_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_generic_ignite_civil_war |  |  |  | ETH.txt |
| ITA_time_based_war_escalation_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_generic_operation |  |  | By Blood Alone | ETH.txt |
| ETH_christmas_offensive_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_generic_prepare_civil_war |  | yes |  | ETH.txt |
| ETH_hold_the_north_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_border_war |  | yes |  | ETH.txt |
| ETH_hold_the_south_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_border_war |  | yes |  | ETH.txt |
| ETH_hold_addis_ababa_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_border_war |  | yes |  | ETH.txt |
| ETH_conquer_addis_ababa_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_generic_operation |  | yes |  | ETH.txt |
| ETH_hold_harar_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_generic_operation |  | yes |  | ETH.txt |
| ETH_conquer_harar_mission | ETH_second_italo_ethiopian_war_category | GFX_decision_generic_operation |  | yes |  | ETH.txt |
| ETH_set_up_gideon_force_decision | ETH_italian_occupation_category | GFX_decision_generic_army_support | 25 | yes |  | ETH.txt |
| ETH_build_local_resistance_force | ETH_italian_occupation_category | GFX_decision_revolt |  |  |  | ETH.txt |
| ETH_launch_large_scale_uprising | ETH_italian_occupation_category | GFX_decision_revolt | 150 | yes |  | ETH.txt |
| ETH_italian_uprising_warning_mission | ETH_italian_occupation_category | GFX_decision_revolt |  |  |  | ETH.txt |
| ETH_italian_control_mission | ETH_italian_occupation_category | GFX_decision_generic_operation |  |  |  | ETH.txt |
| ETH_support_resistance_decision | ETH_anti_colonialism_category | GFX_decision_generic_nationalism |  | yes |  | ETH.txt |
| ETH_arm_resistance_decision | ETH_anti_colonialism_category | GFX_decision_generic_prepare_civil_war |  | yes |  | ETH.txt |
| ETH_support_independence_decision | ETH_anti_colonialism_category | GFX_decision_eng_propaganda_campaigns | 15 |  |  | ETH.txt |
| ETH_anti_colonialism_decision | ETH_anti_colonialism_category | GFX_decision_eng_propaganda_campaigns | 15 | yes |  | ETH.txt |
| ETH_demand_peace_decision | ETH_anti_colonialism_category | GFX_decision_generic_civil_support | 100 | yes |  | ETH.txt |
| ETH_electrify_state | ETH_improve_country_category | decision_generic_electricity | 25 | yes |  | ETH.txt |
| ETH_improve_communications_in_state | ETH_improve_country_category | GFX_decision_SOV_academy_of_sciences | 15 |  |  | ETH.txt |
| ETH_invest_in_state_industry | ETH_improve_country_category | GFX_decision_generic_factory | 15 | yes |  | ETH.txt |
| ETH_local_development_state_grows_mission | ETH_improve_country_category | GFX_decision_generic_operation |  |  |  | ETH.txt |
| ETH_local_development_industry_grows_mission | ETH_improve_country_category | GFX_decision_generic_operation |  |  |  | ETH.txt |
| ETH_local_development_arms_industry_grows_mission | ETH_improve_country_category | GFX_decision_generic_operation |  |  |  | ETH.txt |
| ETH_local_development_improved_production_mission | ETH_improve_country_category | GFX_decision_generic_operation |  |  |  | ETH.txt |
| ETH_prospect_for_resources | ETH_improve_country_category | GFX_decision_generic_construction | 25 | yes |  | ETH.txt |
| ETH_japanese_industrial_investments_decision | ETH_improve_country_category | GFX_decision_generic_factory | 50 | yes |  | ETH.txt |
| ETH_japanese_dockyard_investments_decision | ETH_improve_country_category | GFX_decision_generic_naval | 50 | yes |  | ETH.txt |
| ETH_japanese_infrastructure_investments_decision | ETH_improve_country_category | GFX_decision_generic_construction | 50 | yes |  | ETH.txt |
| ETH_recall_balco_safo_decision | ETH_centralization_balance_of_power_category | GFX_decision_generic_military | 10 | yes |  | ETH.txt |
| ETH_bop_increase_mesafint_privileges | ETH_centralization_balance_of_power_category | GFX_decision_gre_investment_decisions | 25 |  |  | ETH.txt |
| ETH_bop_increase_anarchist_influence | ETH_centralization_balance_of_power_category | GFX_decision_SOV_the_workers_dictatorship | 25 |  |  | ETH.txt |
| ETH_bop_increase_communist_influence | ETH_centralization_balance_of_power_category | GFX_decision_SOV_secure_the_administration | 25 |  |  | ETH.txt |
| ETH_bop_increase_the_power_of_the_mekwanint | ETH_centralization_balance_of_power_category | GFX_decision_gre_investment_decisions | 25 |  |  | ETH.txt |
| ETH_retake_territory_mission | ETH_centralization_balance_of_power_category | GFX_decision_generic_operation |  |  |  | ETH.txt |
| ETH_Education_reform_decentralized_BoP | ETH_centralization_balance_of_power_category | GFX_decision_eng_trade_unions_support | 25 | yes |  | ETH.txt |
| ETH_Education_reform_centralized_BoP | ETH_centralization_balance_of_power_category | GFX_decision_eng_trade_unions_support | 25 | yes |  | ETH.txt |
| ETH_road_reform_local_BoP | ETH_centralization_balance_of_power_category | GFX_decision_rubber | 25 | yes |  | ETH.txt |
| ETH_road_reform_highways_BoP | ETH_centralization_balance_of_power_category | GFX_decision_rubber | 25 | yes |  | ETH.txt |
| ETH_officer_reforms_centralized_BoP | ETH_centralization_balance_of_power_category | GFX_decision_generic_army_support | 25 | yes |  | ETH.txt |
| ETH_officer_reforms_decentralized_BoP | ETH_centralization_balance_of_power_category | GFX_decision_generic_army_support | 25 | yes |  | ETH.txt |
| ETH_BoP_purge_communists | ETH_centralization_balance_of_power_category | GFX_decision_SOV_secure_the_administration | 25 | yes |  | ETH.txt |
| ETH_BoP_expand_red_guards | ETH_centralization_balance_of_power_category | GFX_decision_SOV_secure_the_administration | 25 | yes |  | ETH.txt |
| ETH_BoP_expand_black_lions | ETH_centralization_balance_of_power_category | GFX_decision_generic_civil_support | 25 | yes |  | ETH.txt |
| ETH_BoP_purge_anarchists | ETH_centralization_balance_of_power_category | GFX_decision_generic_civil_support | 25 | yes |  | ETH.txt |
| ETH_freedom_at_gunpoint_dynamic | ETH_freedom_at_gunpoint_category | GFX_decision_generic_prepare_civil_war | 50 |  |  | ETH.txt |
| ETH_freedom_at_gunpoint_offer_peace | ETH_freedom_at_gunpoint_category | GFX_decision_generic_form_nation | 50 |  |  | ETH.txt |
| ETH_take_DJI | ETH_exploit_french_weakness_category | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_reintegrate_core | ETH_reintegrate_former_territory_category | GFX_decision_generic_form_nation | 20 |  |  | ETH.txt |
| ETH_core_551 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_886 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_883 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_269 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_884 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_906 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_268 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_293 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_659 | ethiopian_empire_decisions | GFX_decision_border_war | 25 | yes |  | ETH.txt |
| ETH_core_east_african_states | ETH_consolidate_east_africa_category | GFX_decision_generic_form_nation | 20 |  |  | ETH.txt |
| ETH_form_horn_of_africa | ETH_consolidate_east_africa_category | GFX_decision_generic_form_nation | 20 | yes |  | ETH.txt |
| ETH_build_infrastructure | ETH_improve_the_horn_of_africa_category | GFX_decision_generic_construction | 25 | yes |  | ETH.txt |
| ETH_build_railway | ETH_improve_the_horn_of_africa_category | GFX_decision_generic_construction | 25 | yes |  | ETH.txt |
| ETH_invest_horn_industry | ETH_improve_the_horn_of_africa_category | GFX_decision_generic_construction | 25 | yes |  | ETH.txt |
| ETH_integrate_economies | ETH_improve_the_horn_of_africa_category | GFX_decision_generic_construction | 75 | yes |  | ETH.txt |
| DEBUG_MIO_SHOW_DEBUG_MIO_ARCHETYPES | debug_decisions |  |  |  |  | FIN.txt |
| DEBUG_MIO_HIDE_DEBGU_MIO_ARCHETYPES | debug_decisions |  |  |  |  | FIN.txt |
| DEBUG_FIN_deactivate_BOP | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_make_decisions_faster_and_free | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_make_decisions_go_back_to_normal | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_absurdly_high_increase_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_high_increase_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_medium_increase_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_low_increase_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_very_low_increase_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_absurdly_high_decrease_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_high_decrease_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_medium_decrease_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_low_decrease_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_bop_very_low_decrease_value | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_set_max_bop | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| DEBUG_FIN_set_min_bop | FIN_balance_of_power_category |  |  |  |  | FIN.txt |
| FIN_prepare_motti_tactics_in_state | FIN_motti_tactics_category | generic_operation |  |  |  | FIN.txt |
| FIN_cancel_motti_tactics_in_state | FIN_motti_tactics_category | GFX_decision_FIN_stop_motti_tactics |  |  |  | FIN.txt |
| FIN_set_up_weapon_caches_in_state | FIN_national_defense_category | GFX_decision_ger_military_buildup |  |  |  | FIN.txt |
| FIN_surrender_to_the_soviet_union | FIN_national_defense_category | GFX_decision_generic_form_nation | 35 |  |  | FIN.txt |
| FIN_demand_peace_negotiations | FIN_national_defense_category | GFX_decision_eng_trade_unions_support |  | yes |  | FIN.txt |
| FIN_hold_leningrad_mission | FIN_national_defense_category | GFX_decision_hol_draw_up_staff_plans |  |  |  | FIN.txt |
| FIN_coastal_garrisons | FIN_national_defense_category | GFX_decision_generic_military |  | yes |  | FIN.txt |
| FIN_mining_the_sea | FIN_national_defense_category | GFX_decision_generic_naval_mine |  | yes | Man the Guns | FIN.txt |
| FIN_search_for_weapon_caches_in_state | FIN_finnish_resistance_category | GFX_decision_FIN_weapon_caches |  |  |  | FIN.txt |
| FIN_retake_leningrad_mission | war_measures | GFX_decision_hol_draw_up_staff_plans |  |  |  | FIN.txt |
| FIN_motion_of_no_confidence_against_leader | FIN_balance_of_power_category | GFX_decision_SWI_dismiss_council |  |  |  | FIN.txt |
| FIN_resignation_of_kallio | FIN_balance_of_power_category | GFX_decision_SWI_no_elected_president | 75 |  |  | FIN.txt |
| FIN_form_a_military_government | FIN_balance_of_power_category | GFX_decision_gre_faction_management | 150 | yes |  | FIN.txt |
| FIN_resignation_of_mannerheim | FIN_balance_of_power_category | GFX_decision_SWI_no_elected_president | 50 | yes |  | FIN.txt |
| FIN_appeal_to_the_finnish_spirit | FIN_balance_of_power_category | GFX_decision_generic_civil_support |  |  |  | FIN.txt |
| FIN_entice_the_masses | FIN_balance_of_power_category | GFX_decision_eng_propaganda_campaigns |  |  |  | FIN.txt |
| FIN_organize_the_opposition | FIN_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | FIN.txt |
| FIN_appoint_yrjo_leino_as_president | FIN_balance_of_power_category | GFX_decision_generic_speech | 15 | yes | Arms Against Tyranny | FIN.txt |
| FIN_gather_popular_support | FIN_the_path_to_socialism | GFX_decision_generic_civil_support | 70 | yes |  | FIN.txt |
| FIN_crack_down_on_fascists | FIN_the_path_to_socialism | GFX_decision_generic_police_action | 70 | yes |  | FIN.txt |
| FIN_crack_down_on_the_military | FIN_the_path_to_socialism | GFX_decision_generic_arrest | 70 | yes |  | FIN.txt |
| FIN_prepare_construction_workers_actions | FIN_the_path_to_socialism | GFX_decision_generic_construction | 70 | yes |  | FIN.txt |
| FIN_align_the_trade_unions | FIN_the_path_to_socialism | GFX_decision_generic_political_discourse | 70 | yes |  | FIN.txt |
| FIN_purchase_soviet_equipment | FIN_the_path_to_socialism | GFX_decision_generic_industry | 150 | yes |  | FIN.txt |
| FIN_infiltrate_soviet_commandos | FIN_the_path_to_socialism | GFX_decision_generic_military | 70 | yes |  | FIN.txt |
| FIN_call_to_union_activism | FIN_the_path_to_socialism | GFX_decision_generic_political_rally | 15 | yes |  | FIN.txt |
| FIN_push_for_cabinet_participation | FIN_the_path_to_socialism | GFX_decision_generic_political_address | 35 | yes |  | FIN.txt |
| FIN_gather_funds_for_womens_shelters | FIN_the_path_to_socialism | GFX_decision_generic_fundraising | 45 | yes |  | FIN.txt |
| FIN_request_extradition_of_kullervo_manner | political_actions | GFX_decision_eng_trade_unions_support | 25 | yes | Arms Against Tyranny | FIN.txt |
| FIN_prioritize_light_industry | economy_decisions | GFX_decision_generic_consumer_goods |  |  | Arms Against Tyranny | FIN.txt |
| FIN_prioritize_heavy_industry | economy_decisions | GFX_decision_generic_factory |  |  | Arms Against Tyranny | FIN.txt |
| FIN_rebalance_industrial_focus | economy_decisions | GFX_decision_generic_factory | 25 |  | Arms Against Tyranny | FIN.txt |
| FIN_request_an_armistice_with_moscow | FIN_foreign_politics_decision_category | GFX_decision_hol_war_on_pacifism | 35 |  |  | FIN.txt |
| FIN_request_to_switch_sides_in_the_war | FIN_foreign_politics_decision_category | GFX_decision_generic_political_discourse | 35 |  |  | FIN.txt |
| FIN_pressure_country_government_baltic | FIN_foreign_politics_decision_category | generic_political_discourse |  |  |  | FIN.txt |
| FIN_promote_ideology_rallies_baltic | FIN_foreign_politics_decision_category | generic_political_rally |  | yes |  | FIN.txt |
| FIN_fight_alongside_country_comrades_baltic | FIN_foreign_politics_decision_category | generic_prepare_civil_war |  |  |  | FIN.txt |
| FIN_pressure_country_government_nordic | FIN_foreign_politics_decision_category | generic_political_discourse |  |  |  | FIN.txt |
| FIN_promote_ideology_rallies_nordic | FIN_foreign_politics_decision_category | generic_political_rally |  | yes |  | FIN.txt |
| FIN_fight_alongside_country_comrades_nordic | FIN_foreign_politics_decision_category | generic_prepare_civil_war |  |  |  | FIN.txt |
| FIN_secure_the_military | FIN_coup_preparations | GFX_decision_generic_civil_support | 70 | yes |  | FIN.txt |
| FIN_purchase_german_equipment | FIN_coup_preparations | GFX_decision_generic_industry | 150 | yes |  | FIN.txt |
| FIN_appeal_to_the_middle_class | FIN_coup_preparations | GFX_decision_generic_civil_support | 50 | yes |  | FIN.txt |
| FIN_stir_anti_soviet_sentiment_in_karelia | FIN_the_last_kinship_war | GFX_decision_POL_organize_strike_two | 50 | yes |  | FIN.txt |
| FIN_instigate_a_new_karelian_uprising | FIN_the_last_kinship_war | GFX_decision_generic_civil_support |  | yes |  | FIN.txt |
| FIN_crush_the_karelian_insurrection | FIN_finno_soviet_kinship_war | GFX_decision_generic_civil_support |  | yes |  | FIN.txt |
| FIN_integrate_karelia_puppet | FIN_confederated_finno_russian_republics_category | GFX_decision_generic_nationalism | 35 |  |  | FIN.txt |
| FIN_integrate_karelia_states | FIN_confederated_finno_russian_republics_category | GFX_decision_infiltrate_state |  |  |  | FIN.txt |
| FIN_integrate_karelia_additional_states | FIN_confederated_finno_russian_republics_category | GFX_decision_infiltrate_state |  |  |  | FIN.txt |
| FIN_integrate_veps_states | FIN_confederated_finno_russian_republics_category | GFX_decision_infiltrate_state |  |  |  | FIN.txt |
| FIN_integrate_veps_additional_states | FIN_confederated_finno_russian_republics_category | GFX_decision_infiltrate_state |  |  |  | FIN.txt |
| FIN_integrate_ingria_states | FIN_confederated_finno_russian_republics_category | GFX_decision_infiltrate_state |  |  |  | FIN.txt |
| FIN_integrate_ingria_additional_states | FIN_confederated_finno_russian_republics_category | GFX_decision_infiltrate_state |  |  |  | FIN.txt |
| FIN_integrate_leningrad | FIN_confederated_finno_russian_republics_category | GFX_decision_infiltrate_state |  |  |  | FIN.txt |
| nation_building | foreign_influence | eng_propaganda_campaigns |  |  |  | foreign_influence.txt |
| socialist_education | foreign_influence | eng_propaganda_campaigns |  |  |  | foreign_influence.txt |
| paramilitary_training | foreign_influence | eng_propaganda_campaigns |  |  |  | foreign_influence.txt |
| military_parade | foreign_influence | eng_propaganda_campaigns |  |  |  | foreign_influence.txt |
| police_action | foreign_influence | generic_prepare_civil_war | 50 |  |  | foreign_influence.txt |
| fraternal_republic | foreign_influence | generic_prepare_civil_war | 50 |  |  | foreign_influence.txt |
| ultranationalist_coup | foreign_influence | generic_prepare_civil_war | 50 |  |  | foreign_influence.txt |
| military_dictatorship | foreign_influence | generic_prepare_civil_war | 50 |  |  | foreign_influence.txt |
| instantiate_collaboration | foreign_influence | generic_prepare_civil_war | 0 |  |  | foreign_influence.txt |
| form_scandinavia | form_scandinavia_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_nordic_league | form_nordic_league_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_north_sea_empire | form_north_sea_category | generic_form_nation |  |  | Arms Against Tyranny | formable_nation_decisions.txt |
| form_baltic_sea_empire | form_baltic_sea_empire_category | generic_form_nation |  |  | Arms Against Tyranny | formable_nation_decisions.txt |
| form_gran_colombia | form_gran_colombia_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_austria_hungary | form_austria_hungary_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| reintegrate_austro_hungarian_empire | form_austria_hungary_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_commonwealth | form_commonwealth_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| form_united_netherlands | form_united_netherlands_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_united_central_america | form_united_central_america_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| integrate_northern_gran_colombia | form_united_central_america_category | GFX_decision_eng_trade_unions_support |  |  | Waking the Tiger | formable_nation_decisions.txt |
| integrate_yucatan | form_united_central_america_category | GFX_decision_eng_trade_unions_support |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_baltic_federation | form_baltic_federation_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_ottoman_empire | form_ottoman_empire_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| ott_reform_the_eyalet_of_rumelia | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_merge_the_eyalets_of_morea_crete_and_kibris | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_enlarge_the_vilayet_of_bosnia | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_restore_the_vilayet_of_the_danube_and_moldova | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_restore_the_vilayet_of_halep | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_restore_the_vilayet_of_beirut | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_restore_the_vilayet_of_baghdad | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_extend_the_lasha_eyalet | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_merge_the_eyalets_of_jeddah_habesh_and_yemen | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_integrate_the_khedivate_of_egypt | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_restore_the_vilayet_of_tripolitania | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| ott_absorb_the_tunis_and_algerian_eyalets | form_ottoman_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| form_european_union | form_european_union_category | generic_form_nation |  |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_alpine_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_iberian_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_west_slavic_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_baltic_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_british_isles_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_scandinavian_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_karelo_finnish_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_balkan_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 150 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_aegean_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_belarusian_and_ukrainian_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_caucasian_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_kuban_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 100 |  | Gotterdammerung | formable_nation_decisions.txt |
| EU_russian_expansion_decision | form_european_union_category | GFX_decision_generic_nationalism | 150 |  | Gotterdammerung | formable_nation_decisions.txt |
| form_mutapa | form_mutapa_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_roman_empire | form_roman_empire_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| reintigrate_hispania | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| reintigrate_dacia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| reintigrate_moesia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| reintigrate_aegyptus | form_roman_empire_category | GFX_decision_generic_nationalism | 75 |  | Waking the Tiger | formable_nation_decisions.txt |
| restore_mesopotamia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| reconquer_galatia_et_cappadocia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| integrate_armenian_lands | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| restore_order_in_arabia_petra | form_roman_empire_category | GFX_decision_generic_nationalism | 75 |  | Waking the Tiger | formable_nation_decisions.txt |
| restore_order_in_mauretania | form_roman_empire_category | GFX_decision_generic_nationalism | 75 |  | Waking the Tiger | formable_nation_decisions.txt |
| return_to_pannonia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| restore_roman_rule_to_raetia_et_noricum | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| restore_roman_rule_to_gaul | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| restore_roman_rule_to_belgica | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| occupy_iberia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| return_to_britannia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| conquer_hibernia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| conquer_caledonia | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| avenge_teutoburg | form_roman_empire_category | GFX_decision_generic_nationalism | 100 |  | Waking the Tiger | formable_nation_decisions.txt |
| reestablish_the_bosporan_kingdom | form_roman_empire_category | GFX_decision_generic_nationalism | 120 |  | Waking the Tiger | formable_nation_decisions.txt |
| form_persian_empire | form_persian_empire_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_byzantine_empire | form_byzantine_empire_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| byz_restore_byzantium | form_byzantine_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| byz_triumph_for_the_balkans | form_byzantine_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| byz_triumph_for_italy | form_byzantine_empire_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| byz_triumph_for_middle_east | form_byzantine_empire_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| byz_triumph_for_egypt_and_tunis | form_byzantine_empire_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_arabia | form_arabia_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| integrate_the_fertile_crescent | form_arabia_category | GFX_decision_generic_nationalism |  | yes | Waking the Tiger | formable_nation_decisions.txt |
| integrate_the_levantine_states | form_arabia_category | GFX_decision_generic_nationalism |  | yes | Waking the Tiger | formable_nation_decisions.txt |
| integrate_the_western_mashriq | form_arabia_category | GFX_decision_generic_nationalism |  | yes | Waking the Tiger | formable_nation_decisions.txt |
| integrate_the_eastern_maghreb | form_arabia_category | GFX_decision_generic_nationalism |  | yes | Waking the Tiger | formable_nation_decisions.txt |
| integrate_the_al_maghribiyah_and_al_jazair | form_arabia_category | GFX_decision_generic_nationalism |  | yes | Waking the Tiger | formable_nation_decisions.txt |
| integrate_the_west_sahara | form_arabia_category | GFX_decision_generic_nationalism |  | yes | Waking the Tiger | formable_nation_decisions.txt |
| form_majapahit_empire | form_majapahit_empire_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| integrate_papua | form_majapahit_empire_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| integrate_the_northern_malays | form_majapahit_empire_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| integrate_the_philippines | form_majapahit_empire_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| form_maphilindo | form_maphilindo_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| integrate_siam | form_maphilindo_category |  |  | yes |  | formable_nation_decisions.txt |
| integrate_indochina | form_maphilindo_category |  |  | yes |  | formable_nation_decisions.txt |
| integrate_burma | form_maphilindo_category |  |  | yes |  | formable_nation_decisions.txt |
| form_rattanakosin_kingdom | form_rattanakosin_kingdom_category | generic_form_nation |  |  | Waking the Tiger | formable_nation_decisions.txt |
| form_hre | form_hre_category | generic_form_nation |  |  | Gotterdammerung | formable_nation_decisions.txt |
| form_greater_german_reich | form_greater_german_reich_category | generic_form_nation | 25 |  | Waking the Tiger | formable_nation_decisions.txt |
| form_greater_proletarian_state | form_greater_german_state_category | generic_form_nation |  |  | Gotterdammerung | formable_nation_decisions.txt |
| form_andalusia | form_andalusia_category | generic_form_nation |  |  | La Resistance | formable_nation_decisions.txt |
| adu_restore_sultanate_of_africa | form_andalusia_category | generic_form_nation |  |  | La Resistance | formable_nation_decisions.txt |
| adu_mediterrenean_emirates | form_andalusia_category | generic_form_nation |  |  | La Resistance | formable_nation_decisions.txt |
| adu_restore_umayyad_caliphate | form_andalusia_category | generic_form_nation |  |  | La Resistance | formable_nation_decisions.txt |
| adu_recreate_rashid_expansion | form_andalusia_category | generic_form_nation |  |  | La Resistance | formable_nation_decisions.txt |
| adu_northern_expansion | form_andalusia_category | generic_form_nation |  |  | La Resistance | formable_nation_decisions.txt |
| unite_maghreb | maghreb_formable_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| form_polynesia | form_polynesia_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| NZL_demand_islands | form_polynesia_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| form_greater_greece | form_greater_greece_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| GRE_appoint_aristotle_onassis_as_prime_minister | form_greater_greece_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| rename_antalya | form_greater_greece_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| rename_gjirokaster | form_greater_greece_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| GRE_move_capital_to_constantinople | form_greater_greece_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| move_capital_to_thessaloniki | form_greater_greece_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| form_macedonian_empire | form_macedonian_empire_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| form_turan | form_turan_category | generic_form_nation |  |  | Battle for the Bosporus | formable_nation_decisions.txt |
| TUR_appoint_nihal_atziz_as_president | form_turan_category | GFX_decision_generic_political_address |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| integrate_the_magyars | form_turan_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| assimilate_the_chinese_turks | form_turan_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| unite_with_the_finno_ugrians | form_turan_category | generic_form_nation |  | yes | Battle for the Bosporus | formable_nation_decisions.txt |
| form_turkestan | form_turkestan_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| form_mountainous_republic | form_mountainous_republic_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| form_transcaucasian_republic | form_transcaucasus_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| unite_azeris | form_transcaucasus_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| claim_northern_caucasus | form_transcaucasus_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| liberate_anatolian_peoples | form_transcaucasus_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| restore_kalmyks | form_transcaucasus_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| restore_crimean_khanate | form_transcaucasus_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| release_turkish_kurdistan | form_transcaucasus_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| form_siberian_republic | form_siberia_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| conquer_the_fareast | form_siberia_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| push_to_the_urals | form_siberia_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| liberate_the_ainu | form_siberia_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| liberate_manchuria | form_siberia_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| form_idel_uralic_republic | form_idel_ural_category | generic_form_nation |  |  | No Step Back | formable_nation_decisions.txt |
| form_empire_of_axum | form_ethiopian_empire_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| ETH_move_capital_to_axum | form_ethiopian_empire_category | generic_form_nation | 50 | yes |  | formable_nation_decisions.txt |
| form_empire_of_solomon | form_ethiopian_empire_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| ETH_move_capital_to_jerusalem | form_ethiopian_empire_category | generic_form_nation | 50 | yes |  | formable_nation_decisions.txt |
| form_empire_of_zion | form_ethiopian_empire_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| form_east_africa | form_east_africa_category | generic_form_nation |  |  | Gotterdammerung | formable_nation_decisions.txt |
| integrate_ruanda_urundi | form_east_africa_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| dominate_malawi | form_east_africa_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| liberate_sidamo | form_east_africa_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| unite_the_somalis | form_east_africa_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| conquer_the_comoros | form_east_africa_category | generic_form_nation |  | yes |  | formable_nation_decisions.txt |
| form_the_horn_of_africa | form_horn_of_africa_africa_category | generic_form_nation |  |  | By Blood Alone | formable_nation_decisions.txt |
| conquer_socotra | form_horn_of_africa_africa_category | generic_form_nation |  |  | By Blood Alone | formable_nation_decisions.txt |
| integrate_the_south | form_horn_of_africa_africa_category | generic_form_nation |  |  | By Blood Alone | formable_nation_decisions.txt |
| the_upper_nile | form_horn_of_africa_africa_category | generic_form_nation |  |  | By Blood Alone | formable_nation_decisions.txt |
| proclaim_greater_italy | greater_italy_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| proclaim_sweden_hungary | form_sweden_hungary_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| unite_the_antilles | antilles_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| integrate_the_netherlands_antilles | antilles_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| integrate_trinidad_and_tobago | antilles_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| unite_latin_africa | latin_africa_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| declare_germany_reunified_decision | germany_formable_category | generic_form_nation | 100 |  |  | formable_nation_decisions.txt |
| reintegrate_luxemburg | germany_formable_category | generic_form_nation | 25 |  |  | formable_nation_decisions.txt |
| reintegrate_elsass_lothringen | germany_formable_category | generic_form_nation | 25 |  |  | formable_nation_decisions.txt |
| reintegrate_south_jutland | germany_formable_category | generic_form_nation | 25 |  |  | formable_nation_decisions.txt |
| reintegrate_east_prussia | germany_formable_category | generic_form_nation | 50 |  |  | formable_nation_decisions.txt |
| reintegrate_silesia | germany_formable_category | generic_form_nation | 50 |  |  | formable_nation_decisions.txt |
| reintegrate_posen_west_prussia | germany_formable_category | generic_form_nation | 75 |  |  | formable_nation_decisions.txt |
| neo_assyrian_empire_decision | neo_assyrian_empire_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| neo_mesopotamia_decision | neo_mesopotamia_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| unite_greater_mongolia | greater_mongolia_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| unite_hui_states | greater_hui_state_category | generic_form_nation |  |  |  | formable_nation_decisions.txt |
| FRA_communist_civil_war_decision | FRA_civil_unrest_category | generic_civil_support |  |  |  | FRA.txt |
| FRA_fascist_civil_war_decision | FRA_civil_unrest_category | generic_civil_support |  |  |  | FRA.txt |
| FRA_scuttle_the_fleet | FRA_vichy_france | generic_ignite_civil_war | 0 |  |  | FRA.txt |
| FRA_case_anton_mission | FRA_vichy_france | generic_tank |  | yes |  | FRA.txt |
| FRA_demand_unification_with_vichy | FRA_vichy_france |  | 0 | yes |  | FRA.txt |
| FRA_failsafe_join_axis | FRA_vichy_france |  | 0 | yes |  | FRA.txt |
| test_free_france | category_test_decisions |  | 0 |  |  | FRA.txt |
| test_vichy_france | category_test_decisions |  | 0 |  |  | FRA.txt |
| FRA_order_weapons_in_USA | FRA_weapons_purchases_category | generic_prepare_civil_war | 50 |  | Arms Against Tyranny | FRA.txt |
| FRA_order_artillery_in_USA | FRA_weapons_purchases_category | ger_military_buildup | 75 |  | Arms Against Tyranny | FRA.txt |
| FRA_order_tanks_in_USA | FRA_weapons_purchases_category | GFX_decision_generic_tank | 100 |  | Arms Against Tyranny | FRA.txt |
| FRA_order_fighters_in_USA | FRA_weapons_purchases_category | generic_air | 100 |  | By Blood Alone | FRA.txt |
| FRA_order_bombers_in_USA | FRA_weapons_purchases_category | generic_air | 100 |  | By Blood Alone | FRA.txt |
| FRA_invite_FROM_to_non_intervention | FRA_spanish_intervention_category |  | 25 | yes |  | FRA.txt |
| FRA_allow_non_military_aid | FRA_spanish_intervention_category |  | 25 |  |  | FRA.txt |
| FRA_ban_non_military_aid | FRA_spanish_intervention_category |  | 0 |  |  | FRA.txt |
| FRA_send_non_military_aid_to_FROM | FRA_spanish_intervention_category |  | 0 |  |  | FRA.txt |
| FRA_allow_arms_purchases | FRA_spanish_intervention_category |  | 25 |  |  | FRA.txt |
| FRA_ban_arms_purchases | FRA_spanish_intervention_category |  | 0 |  |  | FRA.txt |
| FRA_allow_sending_weapons | FRA_spanish_intervention_category |  | 25 |  |  | FRA.txt |
| FRA_ban_sending_weapons | FRA_spanish_intervention_category |  | 0 |  |  | FRA.txt |
| FRA_allow_volunteer_work | FRA_spanish_intervention_category |  | 25 |  |  | FRA.txt |
| FRA_ban_volunteer_work | FRA_spanish_intervention_category |  | 0 |  |  | FRA.txt |
| FRA_allow_covert_intervention | FRA_spanish_intervention_category |  | 25 |  |  | FRA.txt |
| FRA_ban_covert_intervention | FRA_spanish_intervention_category |  | 0 |  |  | FRA.txt |
| FRA_intervene_on_side_of_FROM | FRA_spanish_intervention_category |  | 25 |  |  | FRA.txt |
| FRA_revoke_the_matignon_agreements | economy_decisions |  | 50 |  |  | FRA.txt |
| FRA_reorganize_aviation_industry_north | economy_decisions |  | 50 | yes | Arms Against Tyranny | FRA.txt |
| FRA_reorganize_aviation_industry_west | economy_decisions |  | 50 | yes | Arms Against Tyranny | FRA.txt |
| FRA_reorganize_aviation_industry_center | economy_decisions |  | 50 | yes | Arms Against Tyranny | FRA.txt |
| FRA_reorganize_aviation_industry_south_east | economy_decisions |  | 50 | yes | Arms Against Tyranny | FRA.txt |
| FRA_reorganize_aviation_industry_south_west | economy_decisions |  | 50 | yes | Arms Against Tyranny | FRA.txt |
| FRA_rally_the_leagues | political_actions |  |  |  |  | FRA.txt |
| FRA_unleash_la_cagoule | political_actions |  | 25 |  |  | FRA.txt |
| VIC_basing_rights | VIC_concessions_to_the_germans |  | 25 | yes |  | FRA.txt |
| VIC_produce_aircraft_parts | VIC_concessions_to_the_germans |  | 25 | yes |  | FRA.txt |
| VIC_send_guest_workers | VIC_concessions_to_the_germans |  | 25 | yes |  | FRA.txt |
| VIC_recall_guest_workers | VIC_concessions_to_the_germans |  | 0 | yes |  | FRA.txt |
| FRA_promise_independence_to_north_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_prepare_coup_in_north_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_promise_independence_to_syria | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_prepare_coup_in_syria | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_invasion_in_syria | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_promise_independence_to_indochina | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_prepare_coup_in_indochina | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_invasion_in_indochina | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_promise_independence_to_central_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_prepare_coup_in_central_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_invasion_in_central_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_promise_independence_to_west_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_prepare_coup_in_west_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_invasion_in_west_africa | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_promise_independence_to_madagascar | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_prepare_coup_in_madagascar | FRA_intervention_in_overseas_territories |  | 25 | yes |  | FRA.txt |
| FRA_independence_for_syria_mission | FRA_decolonization |  |  |  |  | FRA.txt |
| FRA_independence_for_indochina_mission | FRA_decolonization |  |  |  |  | FRA.txt |
| FRA_independence_for_madagascar_mission | FRA_decolonization |  |  |  |  | FRA.txt |
| FRA_independence_for_north_africa_mission | FRA_decolonization |  |  |  |  | FRA.txt |
| FRA_independence_for_west_africa_mission | FRA_decolonization |  |  |  |  | FRA.txt |
| FRA_independence_for_central_africa_mission | FRA_decolonization |  |  |  |  | FRA.txt |
| DEBUG_Manu | debug_decisions |  |  |  |  | GER.txt |
| DEBUG_DANNE_GER | debug_decisions |  |  |  |  | GER.txt |
| DEBUG_DANNE_change_CG_GER | debug_decisions |  |  |  |  | GER.txt |
| GER_mefo_bills_mission | GER_mefo_bills_category | ger_mefo_bills |  | yes |  | GER.txt |
| GER_cancel_mefos | GER_mefo_bills_category | ger_mefo_bills | 0 |  |  | GER.txt |
| GER_seize_gold_reserves | GER_seize_gold_reserves_cat | GFX_decision_generic_confiscation | 25 | yes |  | GER.txt |
| GER_seize_russian_citites_gold_reserves | GER_seize_gold_reserves_cat | GFX_decision_generic_confiscation | 10 | yes |  | GER.txt |
| GER_operational_planning | GER_operational_planning_category | GFX_decision_hol_draw_up_staff_plans |  |  |  | GER.txt |
| GER_operational_planning_africa | GER_operational_planning_category | GFX_decision_hol_draw_up_staff_plans |  | yes |  | GER.txt |
| GER_guns_before_butter | GER_price_controls_cat | GFX_decision_ger_military_buildup | 30 | yes |  | GER.txt |
| GER_arbeit_und_brot | GER_price_controls_cat | GFX_decision_generic_political_address | 30 | yes |  | GER.txt |
| GER_collect_scrap_metal | GER_price_controls_cat | GFX_decision_steel | 30 | yes |  | GER.txt |
| GER_ersatz_material | GER_price_controls_cat | GFX_decision_generic_consumer_goods | 30 | yes |  | GER.txt |
| GER_import_tariffs | GER_price_controls_cat | GFX_decision_eng_trade_unions_demand | 15 | yes |  | GER.txt |
| GER_implement_rations | GER_price_controls_cat | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_implement_wage_controls | GER_price_controls_cat | GFX_decision_hol_attract_foreign_investors | 15 | yes |  | GER.txt |
| GER_exploit_the_gombos_treaty | GER_price_controls_cat | GFX_decision_generic_fundraising | 30 | yes | Gotterdammerung | GER.txt |
| GER_construct_the_westwall | GER_fortify_the_vaterland_cat | GFX_decision_generic_fortification |  | yes |  | GER.txt |
| GER_construct_the_ostwall | GER_fortify_the_vaterland_cat | GFX_decision_generic_fortification |  | yes |  | GER.txt |
| GER_construct_the_north_atlantikwall | GER_fortify_the_vaterland_cat | GFX_decision_generic_coastal_fortification |  | yes |  | GER.txt |
| GER_construct_the_central_atlantikwall | GER_fortify_the_vaterland_cat | GFX_decision_generic_coastal_fortification |  | yes |  | GER.txt |
| GER_construct_the_west_atlantikwall | GER_fortify_the_vaterland_cat | GFX_decision_generic_coastal_fortification |  | yes |  | GER.txt |
| GER_construct_the_south_atlantikwall | GER_fortify_the_vaterland_cat | GFX_decision_generic_coastal_fortification |  | yes |  | GER.txt |
| GER_construct_the_alpenwall | GER_fortify_the_vaterland_cat | GFX_decision_generic_mountain_fortification |  | yes |  | GER.txt |
| GER_refit_convoys_to_cruisers | GER_hilfskreuzer_cat | GFX_decision_generic_merge_plant_ship | 25 |  | Man the Guns | GER.txt |
| GER_barbarossa_mission | operations | generic_operation |  | yes |  | GER.txt |
| GER_case_anton | GER_case_anton_category | generic_operation | 50 | yes |  | GER.txt |
| GER_reichskommissariat_norwegen | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_niederlande | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_belgien_nordfrankreich | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_ostland | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_ukraine | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_expand_ukraine_adminsitrative_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 10 | yes |  | GER.txt |
| GER_further_expand_ukraine_adminsitrative_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 10 | yes |  | GER.txt |
| GER_reichskommissariat_kaukasien | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_turkestan | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_moskowien | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_the_fate_of_the_volga_german_autonomous_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_send_wehrbauern_to_the_rks | GER_reichskommissariats | GFX_decision_eng_blackshirt_march | 30 |  |  | GER.txt |
| GER_the_fate_of_the_south_ural_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_the_fate_of_the_north_ural_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 20 | yes |  | GER.txt |
| GER_the_fate_of_the_west_yenisei_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 20 | yes |  | GER.txt |
| GER_the_fate_of_greater_finland | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 25 | yes |  | GER.txt |
| GER_generalgouvernement | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_expand_generalgouvernement_adminsitrative_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 10 | yes |  | GER.txt |
| GER_reichsprotektorat_bohemia_moravia | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_iberien | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_reichskommissariat_balkan | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_expand_rkc_adminsitrative_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 10 | yes |  | GER.txt |
| GER_reichskommissariat_grossbritannien | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_the_fate_of_the_greek_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_the_fate_of_the_hungarian_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_the_fate_of_slovakia | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 25 | yes |  | GER.txt |
| GER_the_fate_of_the_irish_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_reichskommissariat_nordafrika | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_reichskommissariat_mittelafrika | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_the_fate_of_the_saf_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 10 | yes |  | GER.txt |
| GER_reichskommissariat_klein_venedig | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_anden | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_kolumbus | GER_reichskommissariats | ger_reichskommissariats | 25 | yes |  | GER.txt |
| GER_reichskommissariat_nordamerika | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_the_fate_of_greenland_and_nfl | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 10 | yes |  | GER.txt |
| GER_the_fate_of_west_coast_america | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 25 | yes |  | GER.txt |
| GER_the_fate_of_the_east_yenisei_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 20 | yes |  | GER.txt |
| GER_the_fate_of_east_turkestan_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 20 | yes |  | GER.txt |
| GER_reichskommissariat_arabien | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_the_fate_of_turkey_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 20 | yes |  | GER.txt |
| GER_the_fate_of_iran_area | GER_reichskommissariats | GFX_decision_eng_trade_unions_support | 20 | yes |  | GER.txt |
| GER_reichskommissariat_hindustan | GER_reichskommissariats | ger_reichskommissariats | 35 | yes |  | GER.txt |
| GER_reichskommissariat_ostasien | GER_reichskommissariats | ger_reichskommissariats | 35 | yes |  | GER.txt |
| GER_reichskommissariat_australasien | GER_reichskommissariats | ger_reichskommissariats | 30 | yes |  | GER.txt |
| GER_democratic_shield_send_support | political_actions | ger_military_buildup |  | yes |  | GER.txt |
| reinstate_wilhelm_iv_succession_rights | political_actions |  | 100 | yes |  | GER.txt |
| modernize_the_succession_laws | political_actions |  | 150 | yes |  | GER.txt |
| recall_von_lettow_vorbeck | political_actions |  | 25 | yes |  | GER.txt |
| GER_sharpen_air_safety_regulations | political_actions |  | 50 | yes |  | GER.txt |
| request_restoration_of_british_titles | foreign_politics |  | 150 | yes |  | GER.txt |
| GER_request_polish_war_participation | foreign_politics | generic_prepare_civil_war | 50 | yes |  | GER.txt |
| GER_install_franz_anton_bach_in_hungary | foreign_politics | GFX_decision_oppression | 25 | yes |  | GER.txt |
| GER_plan_z | GER_military_buildup | generic_naval |  | yes |  | GER.txt |
| GER_jaegernotprogramm | GER_military_buildup | generic_air | 50 | yes |  | GER.txt |
| GER_begin_heavy_water_production | special_projects |  | 0 |  | La Resistance | GER.txt |
| GER_dismantle_maginot | special_projects | generic_construction | 50 | yes |  | GER.txt |
| GER_dismantle_czechoslovakian_forts | special_projects | generic_construction | 50 | yes |  | GER.txt |
| GER_aid_hun_democratic_civil_war | GER_aid_hun_rom_democratic_civil_war | generic_prepare_civil_war | 0 |  |  | GER.txt |
| GER_aid_rom_democratic_civil_war | GER_aid_hun_rom_democratic_civil_war | generic_prepare_civil_war | 0 |  |  | GER.txt |
| GER_reform_austro_hungarian_empire | GER_austro_hungarian_empire |  | 10 | yes |  | GER.txt |
| GER_western_state_development | GER_reich_labor_service_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_northern_state_development | GER_reich_labor_service_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_eastern_state_development | GER_reich_labor_service_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_central_state_development | GER_reich_labor_service_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_southern_state_development | GER_reich_labor_service_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_develop_puppet | GER_integration_of_puppet_economies_dec_cat | GFX_decision_generic_construction | 120 |  |  | GER.txt |
| GER_exploit_puppet | GER_integration_of_puppet_economies_dec_cat | GFX_decision_generic_construction | 120 |  |  | GER.txt |
| GER_state_development_west | GER_rebuild_the_nation_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_state_development_north | GER_rebuild_the_nation_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_state_development_east | GER_rebuild_the_nation_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_state_development_central | GER_rebuild_the_nation_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_state_development_south | GER_rebuild_the_nation_cat | GFX_decision_generic_construction | 50 | yes |  | GER.txt |
| GER_influence_baltics_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_nordics_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_benelux_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_middle_east_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_middle_east_democratic_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_middle_east_neutrality_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_balkans_neutrality_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_balkans_democratic_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_influence_balkans_fascism_decision | GER_influence_countries_cat | GFX_decision_SWI_expand_covert_operations | 25 |  |  | GER.txt |
| GER_invite_to_faction_decision | GER_invite_to_faction_cat | GFX_decision_generic_protection | 25 | yes |  | GER.txt |
| GER_middle_eastern_trade_decision | GER_middle_eastern_trade_cat | GFX_decision_eng_trade_unions_support | 25 | yes |  | GER.txt |
| GER_mitteleuropa_trade_decision | GER_mitteleuropa_allied_trade_cat | GFX_decision_eng_trade_unions_support | 25 | yes |  | GER.txt |
| GER_south_east_asian_construction_push_decision | GER_south_east_asian_natural_wealth_cat | GFX_decision_generic_construction | 75 | yes |  | GER.txt |
| GER_south_east_asian_resources_push_decision | GER_south_east_asian_natural_wealth_cat | GFX_decision_generic_construction | 100 | yes |  | GER.txt |
| GER_destabilize_the_monroe_doctrine_decision | GER_monroe_doctrine_cat | GFX_decision_generic_break_treaty | 100 | yes |  | GER.txt |
| GER_demand_abandon_of_doctrine_decision | GER_monroe_doctrine_cat | GFX_decision_generic_operation | 50 | yes |  | GER.txt |
| GER_doctrine_abandoned_dummy_decision | GER_monroe_doctrine_cat | GFX_decision_generic_GER_flag |  |  |  | GER.txt |
| GER_reinforce_the_monroe_doctrine_decision | GER_monroe_doctrine_cat | GFX_decision_eng_trade_unions_demand | 100 | yes |  | GER.txt |
| GER_demand_adherance_to_doctrine_decision | GER_monroe_doctrine_cat | GFX_decision_eng_trade_unions_support | 50 | yes |  | GER.txt |
| GER_doctrine_reinforced_dummy_decision | GER_monroe_doctrine_cat | GFX_decision_generic_USA_flag |  |  |  | GER.txt |
| GER_monroe_doctrine_USA_sway_ideology | GER_monroe_doctrine_cat | { | 50 | yes |  | GER.txt |
| GER_fourth_silesian_uprising_mission | GER_a_fourth_silesian_uprising_cat | GFX_decision_generic_ignite_civil_war |  | yes |  | GER.txt |
| GER_reestablish_the_black_reichswehr | GER_a_fourth_silesian_uprising_cat | GFX_decision_generic_army_support | 25 | yes |  | GER.txt |
| GER_mobilize_the_selbschutz | GER_a_fourth_silesian_uprising_cat | GFX_decision_oppression | 15 | yes |  | GER.txt |
| GER_kreigsmarine_revolt_mission | GER_waning_patience_within_the_kriegsmarine_cat | GFX_decision_generic_political_discourse |  | yes |  | GER.txt |
| GER_growing_public_dissent_mission | GER_uncertain_future_cat | GFX_decision_revolt |  | yes |  | GER.txt |
| GER_disband_the_schutztruppen | GER_weltpolitik_cat | GFX_decision_eng_blackshirt_march | 5 |  |  | GER.txt |
| GER_reorganize_african_schutztruppe | GER_weltpolitik_cat | GFX_decision_generic_military |  |  |  | GER.txt |
| GER_reorganize_asian_schutztruppe | GER_weltpolitik_cat | GFX_decision_generic_military |  |  |  | GER.txt |
| GER_train_schutztruppe_in_togoland | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_kamerun | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_tanganyika | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_ruanda | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_urundi | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_otjozondjupa | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_kunene | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_khomas | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_karas | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_tsingtao | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_saipan | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_palau | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_karolinen | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_marshallinseln | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_nauru | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_samoa | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_nordlische_salomonen | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_bismarck | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_train_schutztruppe_in_kaiser_wilhelmsland | GER_weltpolitik_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_support_independence_africa_decision | GER_weltpolitik_cat | GFX_decision_eng_propaganda_campaigns | 15 |  |  | GER.txt |
| GER_support_independence_asia_decision | GER_weltpolitik_cat | GFX_decision_eng_propaganda_campaigns | 15 |  |  | GER.txt |
| GER_invite_HOL_to_attack_BEL_decision | GER_realpolitik_cat | GFX_decision_generic_political_discourse | 50 | yes | Gotterdammerung | GER.txt |
| GER_invite_BEL_to_attack_HOL_decision | GER_realpolitik_cat | GFX_decision_generic_political_discourse | 50 | yes | Gotterdammerung | GER.txt |
| GER_sway_the_austrians_decision | GER_realpolitik_cat | GFX_decision_eng_propaganda_campaigns | 50 | yes | Gotterdammerung | GER.txt |
| GER_found_a_baltic_german_state_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 25 | yes |  | GER.txt |
| GER_restore_the_ukrainian_state_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 50 | yes |  | GER.txt |
| GER_found_a_transcacuasian_satellite_state_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 25 | yes |  | GER.txt |
| GER_expand_transcacuasian_administrative_duties_decision | GER_realpolitik_cat | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_establish_a_belarusian_state_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 35 | yes |  | GER.txt |
| GER_establish_greater_flanders_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 25 | yes |  | GER.txt |
| GER_establish_greater_brittany_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 25 | yes |  | GER.txt |
| GER_establish_wales_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 25 | yes |  | GER.txt |
| GER_establish_scotland_decision | GER_realpolitik_cat | GFX_decision_generic_nationalism | 25 | yes |  | GER.txt |
| GER_mitteleuropa_customs_union_decision | GER_mitteleuropa_economic_integration_cat | GFX_decision_gre_investment_decisions | 15 | yes |  | GER.txt |
| GER_mitteleuropa_economic_integration_decision | GER_mitteleuropa_economic_integration_cat | GFX_decision_eng_trade_unions_support | 15 | yes |  | GER.txt |
| GER_further_increase_froms_dependency_decision | GER_mitteleuropa_economic_integration_cat | GFX_decision_eng_trade_unions_demand | 50 | yes |  | GER.txt |
| GER_annex_integrated_puppet_decision | GER_mitteleuropa_economic_integration_cat | GFX_decision_eng_trade_unions_demand | 75 | yes |  | GER.txt |
| GER_imminent_proletarian_revolution_mission | GER_proletarian_revolution_cat | GFX_decision_revolt |  | yes |  | GER.txt |
| GER_expand_the_proletarian_uprisings_decision | GER_proletarian_revolution_cat | GFX_decision_generic_civil_support | 25 | yes |  | GER.txt |
| GER_organize_worker_rally_decision | GER_proletarian_revolution_cat | GFX_decision_generic_political_discourse | 25 | yes |  | GER.txt |
| GER_establish_volkskommissariat_decision | GER_volkskommissariats_cat | GFX_decision_eng_trade_unions_support | 25 | yes |  | GER.txt |
| GER_volkskommissariat_industrial_effort_decision | GER_volkskommissariats_cat | GFX_decision_generic_construction | 15 | yes |  | GER.txt |
| GER_integrate_volkskommissariats_decision | GER_volkskommissariats_cat | GFX_decision_hol_draw_up_staff_plans | 50 | yes |  | GER.txt |
| GER_communist_propaganda_decision | GER_spreading_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | GER.txt |
| GER_communist_propaganda_expanded_decision | GER_spreading_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | GER.txt |
| GER_communist_propaganda_south_america_decision | GER_spreading_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | GER.txt |
| GER_communist_propaganda_middle_east_decision | GER_spreading_the_red_flame_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | GER.txt |
| GER_supporting_the_uprising_decision | GER_spreading_the_red_flame_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_demand_communist_subjugation_decision | GER_spreading_the_red_flame_cat | GFX_decision_eng_trade_unions_demand | 50 | yes |  | GER.txt |
| GER_proletarian_solidarity_decision | GER_spreading_the_red_flame_cat | GFX_decision_SWI_support_humanitarian_efforts | 25 | yes |  | GER.txt |
| GER_industrial_relocation_oil_decision | GER_industrial_relocation_cat | GFX_decision_oil | 50 | yes |  | GER.txt |
| GER_industrial_relocation_tungsten_decision | GER_industrial_relocation_cat | GFX_decision_tungsten | 50 | yes |  | GER.txt |
| GER_industrial_relocation_chromium_decision | GER_industrial_relocation_cat | GFX_decision_chromium | 50 | yes |  | GER.txt |
| GER_support_resistance_decision | GER_anti_colonialism_category | GFX_decision_generic_nationalism |  | yes |  | GER.txt |
| GER_arm_resistance_decision | GER_anti_colonialism_category | GFX_decision_generic_prepare_civil_war |  | yes |  | GER.txt |
| GER_support_independence_decision | GER_anti_colonialism_category | GFX_decision_generic_civil_support | 15 |  |  | GER.txt |
| GER_anti_colonialism_decision | GER_anti_colonialism_category | GFX_decision_eng_propaganda_campaigns | 15 | yes |  | GER.txt |
| GER_occupy_albania_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_montenegro_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_croatia_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_serbia_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_bosnia_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_herzegovina_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_macedonian_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_slovenia_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GER_occupy_kosovo_decision | GER_the_fading_eagle_category | GFX_decision_generic_operation | 50 |  |  | GER.txt |
| GRE_the_election_of_1936 | GRE_1936_election_category | eng_support_imperialist_coup |  | yes |  | GRE.txt |
| GRE_put_the_king_under_house_arrest | GRE_1936_election_category | generic_arrest | 0 | yes |  | GRE.txt |
| GRE_civil_war_imminent | crisis | eng_support_imperialist_coup |  | yes |  | GRE.txt |
| GRE_civil_war_imminent_1 | crisis | eng_support_imperialist_coup |  | yes |  | GRE.txt |
| GRE_civil_war_imminent_2 | crisis | eng_support_imperialist_coup |  | yes |  | GRE.txt |
| GRE_civil_war_imminent_3 | crisis | eng_support_imperialist_coup |  | yes |  | GRE.txt |
| GRE_civil_war_imminent_4 | crisis | eng_support_imperialist_coup |  | yes |  | GRE.txt |
| GRE_invite_politicians_for_investment_talks_in_capital | GRE_investment_decisions_category | generic_factory | 75 |  |  | GRE.txt |
| GRE_hold_national_showcase_for_investors_ger | GRE_investment_decisions_category | generic_factory | 150 |  |  | GRE.txt |
| GRE_exploit_errata_in_schachtplan | GRE_investment_decisions_category | generic_construction | 100 | yes |  | GRE.txt |
| GRE_rebuke_german_investment | GRE_investment_decisions_category | generic_break_treaty | 50 | yes |  | GRE.txt |
| GRE_invite_entrepreneurs_for_investment_talks_in_capital | GRE_investment_decisions_category | generic_factory | 75 |  |  | GRE.txt |
| GRE_hold_national_showcase_for_investors_eng | GRE_investment_decisions_category | generic_factory | 150 |  |  | GRE.txt |
| GRE_trade_manufactured_ship_parts_for_investment | GRE_investment_decisions_category | generic_construction | 100 |  |  | GRE.txt |
| GRE_rebuke_british_investment | GRE_investment_decisions_category | generic_break_treaty | 50 | yes |  | GRE.txt |
| GRE_go_to_paris_to_negotiate_investment_talks | GRE_investment_decisions_category | generic_factory | 75 |  |  | GRE.txt |
| GRE_hold_national_showcase_for_investors_fra | GRE_investment_decisions_category | generic_factory | 150 |  |  | GRE.txt |
| GRE_bribe_french_trade_unions_to_pressure_government_into_investment | GRE_investment_decisions_category | generic_construction | 100 |  |  | GRE.txt |
| GRE_rebuke_french_investment | GRE_investment_decisions_category | generic_break_treaty | 50 | yes |  | GRE.txt |
| GRE_request_italian_assistance_with_industrialisation | GRE_investment_decisions_category | generic_factory | 100 |  |  | GRE.txt |
| GRE_temper_italian_colonial_ambitions_in_greece | GRE_investment_decisions_category | generic_political_discourse | 150 |  |  | GRE.txt |
| GRE_rebuke_italian_investment | GRE_investment_decisions_category | generic_break_treaty | 50 | yes |  | GRE.txt |
| GRE_attend_talks_with_the_presidium | GRE_investment_decisions_category | generic_factory | 75 |  |  | GRE.txt |
| GRE_host_soviet_bureaucrats_in_greece | GRE_investment_decisions_category | generic_political_discourse | 100 |  |  | GRE.txt |
| GRE_invest_back_into_neglected_siberian_regions | GRE_investment_decisions_category | generic_construction | 120 |  |  | GRE.txt |
| GRE_rebuke_soviet_investment | GRE_investment_decisions_category | generic_break_treaty | 50 | yes |  | GRE.txt |
| GRE_small_installment_payment_ENG | GRE_pay_back_debt_to_the_ifc_category | hol_attract_foreign_investors | 25 |  |  | GRE.txt |
| GRE_small_installment_payment_FRA | GRE_pay_back_debt_to_the_ifc_category | hol_attract_foreign_investors | 25 |  |  | GRE.txt |
| GRE_small_installment_payment_ITA | GRE_pay_back_debt_to_the_ifc_category | hol_attract_foreign_investors | 25 |  |  | GRE.txt |
| GRE_large_installment_payment_ENG | GRE_pay_back_debt_to_the_ifc_category | gre_investment_decisions | 50 |  |  | GRE.txt |
| GRE_large_installment_payment_FRA | GRE_pay_back_debt_to_the_ifc_category | gre_investment_decisions | 50 |  |  | GRE.txt |
| GRE_large_installment_payment_ITA | GRE_pay_back_debt_to_the_ifc_category | gre_investment_decisions | 50 |  |  | GRE.txt |
| GRE_restructuring_our_debt | GRE_pay_back_debt_to_the_ifc_category | gre_paying_ifc_debt | 200 | yes |  | GRE.txt |
| GRE_defaulting_on_our_debt | GRE_pay_back_debt_to_the_ifc_category | generic_break_treaty | 300 | yes |  | GRE.txt |
| GRE_anti_german_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_italian_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_french_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_british_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_soviet_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_austro_hungarian_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_romanian_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_bulgarian_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_anti_turkish_stratagems | GRE_hellenic_academy_category | generic_operation |  | yes |  | GRE.txt |
| GRE_befriend_monarchists | GRE_faction_management_category | generic_political_rally | 250 | yes |  | GRE.txt |
| GRE_crush_monarchists | GRE_faction_management_category | generic_police_action | 150 |  |  | GRE.txt |
| GRE_befriend_republicans | GRE_faction_management_category | generic_political_rally | 250 | yes |  | GRE.txt |
| GRE_crush_republicans | GRE_faction_management_category | generic_police_action | 150 |  |  | GRE.txt |
| GRE_befriend_communists | GRE_faction_management_category | generic_political_rally | 250 | yes |  | GRE.txt |
| GRE_crush_communists | GRE_faction_management_category | generic_police_action | 150 |  |  | GRE.txt |
| GRE_befriend_fascists | GRE_faction_management_category | generic_political_rally | 250 | yes |  | GRE.txt |
| GRE_crush_fascists | GRE_faction_management_category | generic_police_action | 150 |  |  | GRE.txt |
| GRE_recommission_the_american_battleships | political_actions | generic_naval | 0 | yes | Battle for the Bosporus | GRE.txt |
| GRE_build_the_salamis | political_actions | generic_naval | 0 | yes | Battle for the Bosporus | GRE.txt |
| GUAY_military_coup_mission | GUAY_military_coup | GFX_decision_revolt |  |  |  | GUAY_decisions.txt |
| GUAY_military_play_arg | GUAY_military_play_cat |  |  | yes |  | GUAY_decisions.txt |
| GUAY_military_play_bra | GUAY_military_play_cat |  |  | yes |  | GUAY_decisions.txt |
| GUAY_meet_with_USA | GUAY_meet_with_the_old_powers_cat | GFX_decision_generic_factory | 0 |  |  | GUAY_decisions.txt |
| GUAY_meet_with_FRA | GUAY_meet_with_the_old_powers_cat | GFX_decision_generic_fortification | 0 |  |  | GUAY_decisions.txt |
| GUAY_meet_with_ENG | GUAY_meet_with_the_old_powers_cat | GFX_decision_hol_draw_up_staff_plans | 0 |  |  | GUAY_decisions.txt |
| GUAY_meet_with_SOV | GUAY_meet_with_the_old_powers_cat | GFX_decision_SWE_set_army_budget | 0 |  |  | GUAY_decisions.txt |
| GUAY_meet_with_GER | GUAY_meet_with_the_old_powers_cat | GFX_decision_ger_reichskommissariats | 0 |  |  | GUAY_decisions.txt |
| GUAY_meet_with_JAP | GUAY_meet_with_the_old_powers_cat | GFX_decision_jap_conquer_china | 0 |  |  | GUAY_decisions.txt |
| GUAY_meet_with_ITA | GUAY_meet_with_the_old_powers_cat | GFX_decision_eng_blackshirt_speech | 0 |  |  | GUAY_decisions.txt |
| GUAY_land_owners_finding_funding | GUAY_laissez_faire_cat | GFX_decision_gre_paying_ifc_debt |  |  |  | GUAY_decisions.txt |
| form_liga_federal_dec | form_liga_federal_cat | generic_form_nation |  |  | Trial of Allegiance | GUAY_decisions.txt |
| HOL_attract_foreign_investors | HOL_obtain_foreign_colonial_investments | hol_attract_foreign_investors | 25 |  |  | HOL.txt |
| HOL_attract_foreign_industry | HOL_obtain_foreign_colonial_investments | generic_construction | 25 |  |  | HOL.txt |
| HOL_attract_west_indies_oil_companies | HOL_obtain_foreign_colonial_investments | oil | 30 |  |  | HOL.txt |
| HOL_attract_east_indies_oil_companies | HOL_obtain_foreign_colonial_investments | oil | 50 |  |  | HOL.txt |
| HOL_inundate_the_water_lines | HOL_prepare_the_inundation_lines | hol_inundate_water_lines | 25 |  |  | HOL.txt |
| HOL_drain_the_water_lines | HOL_prepare_the_inundation_lines | hol_drain_water_lines | 25 |  |  | HOL.txt |
| HOL_crack_down_on_pacifist_movements | HOL_war_on_pacifism | hol_war_on_pacifism | 25 |  |  | HOL.txt |
| HOL_establish_pro_war_labor_indoctrination | HOL_war_on_pacifism | hol_war_on_pacifism | 25 |  |  | HOL.txt |
| HOL_anti_pacifist_propaganda | HOL_war_on_pacifism | hol_war_on_pacifism | 35 |  |  | HOL.txt |
| HOL_request_equipment | HOL_secret_staff_talks | ger_military_buildup | 50 |  |  | HOL.txt |
| HOL_draw_up_combined_staff_plan | HOL_secret_staff_talks | hol_draw_up_staff_plans | 100 | yes |  | HOL.txt |
| HOL_exchange_intelligence_data | HOL_secret_staff_talks | hol_exchange_intelligence_data | 100 | yes |  | HOL.txt |
| HOL_prepare_evacuation_of_gold_reserves | HOL_secret_staff_talks | hol_draw_up_staff_plans | 50 | yes |  | HOL.txt |
| HOL_share_military_knowledge | HOL_secret_staff_talks | hol_draw_up_staff_plans | 75 |  |  | HOL.txt |
| HOL_demand_reduced_dutch_trade_with_germany | HOL_gateway_to_europe_eng_category | eng_trade_unions_demand | 10 |  |  | HOL.txt |
| HOL_demand_increased_dutch_trade_with_germany | HOL_gateway_to_europe_ger_category | eng_trade_unions_demand | 10 |  |  | HOL.txt |
| HOL_placate_the_british | HOL_gateway_to_europe_hol_category | eng_trade_unions_support | 10 |  |  | HOL.txt |
| HOL_placate_the_germans | HOL_gateway_to_europe_hol_category | eng_trade_unions_support | 10 |  | Gotterdammerung | HOL.txt |
| HOL_radio_oranje | HOL_request_allied_favors | hol_radio_oranje | 50 |  |  | HOL.txt |
| HOL_obtain_dockyard_access | HOL_request_allied_favors | generic_naval | 75 |  |  | HOL.txt |
| HOL_assemble_air_squadron | HOL_request_allied_favors | generic_air | 50 |  | By Blood Alone | HOL.txt |
| HOL_request_infantry_equipment | HOL_request_allied_favors | generic_prepare_civil_war | 50 |  | Arms Against Tyranny | HOL.txt |
| HOL_pull_strings_with_british_industrialists | HOL_request_allied_favors | generic_industry | 75 |  |  | HOL.txt |
| HOL_request_aid_for_the_engelandvaarders | HOL_request_allied_favors | hol_engelandvaarders | 50 |  |  | HOL.txt |
| HOL_give_bernhard_generalship | HOL_bernhard | generic_army_support | 25 | yes |  | HOL.txt |
| HOL_pursue_diplomatic_grievances | HOL_bernhard | generic_army_support | 100 | yes |  | HOL.txt |
| HOL_relocate_government_to_batavia | political_actions | eng_trade_unions_support | 0 | yes |  | HOL.txt |
| HOL_propose_benelux_unification | political_actions | eng_trade_unions_support | 300 | yes |  | HOL.txt |
| HUN_establish_new_academy_of_sciences_branches_program_decision | HUN_national_academy_of_sciences_category | GFX_decision_SOV_academy_of_sciences | 75 |  |  | HUN.txt |
| HUN_establish_szekely_academy_of_sciences_decision | HUN_national_academy_of_sciences_category | GFX_decision_SOV_academy_of_sciences | 75 |  |  | HUN.txt |
| HUN_establish_csangos_academy_of_sciences_decision | HUN_national_academy_of_sciences_category | GFX_decision_SOV_academy_of_sciences | 75 |  |  | HUN.txt |
| HUN_establish_leithian_academy_of_sciences_decision | HUN_national_academy_of_sciences_category | GFX_decision_SOV_academy_of_sciences | 75 |  |  | HUN.txt |
| HUN_establish_magyarab_academy_of_sciences_decision | HUN_national_academy_of_sciences_category | GFX_decision_SOV_academy_of_sciences | 100 |  |  | HUN.txt |
| HUN_open_danuvia_ammo_factory_in_veszprem_decision | HUN_gyor_program_initiatives_category | GFX_decision_generic_construction | 75 |  |  | HUN.txt |
| HUN_expand_the_manfred_weiss_armor_plant_decision | HUN_gyor_program_initiatives_category | GFX_decision_generic_merge_plant_tank | 75 |  | No Step Back | HUN.txt |
| HUN_invest_in_the_diosgyor_azsia_plant_decision | HUN_gyor_program_initiatives_category | GFX_decision_gre_investment_decisions | 50 |  |  | HUN.txt |
| HUN_merge_companies_into_the_raba_family_decision | HUN_gyor_program_initiatives_category | GFX_decision_generic_merge_plant_materiel | 50 |  |  | HUN.txt |
| HUN_initiate_the_huba_i_program_decision | HUN_gyor_program_initiatives_category | GFX_decision_eng_trade_unions_support | 50 |  |  | HUN.txt |
| HUN_initiate_huba_ii_program_decision | HUN_gyor_program_initiatives_category | GFX_decision_eng_trade_unions_support | 100 |  |  | HUN.txt |
| HUN_reverse_engineer_skoda_tanks_decision | HUN_gyor_program_initiatives_category | GFX_decision_generic_tank | 50 |  |  | HUN.txt |
| HUN_recusitate_the_hungarian_loyd_airraft_and_engine_factory_decision | HUN_gyor_program_initiatives_category | GFX_decision_hol_attract_foreign_investors | 50 |  |  | HUN.txt |
| HUN_open_the_szekesfehervar_sosto_plant_decision | HUN_gyor_program_initiatives_category | GFX_decision_generic_merge_plant_aircraft | 25 |  |  | HUN.txt |
| HUN_invest_in_dunai_repulogepgyar_decision | HUN_gyor_program_initiatives_category | GFX_decision_generic_air | 35 |  |  | HUN.txt |
| HUN_invest_in_magyar_ruggyantaarugyar_decision | HUN_gyor_program_initiatives_category | GFX_decision_rubber | 50 |  |  | HUN.txt |
| HUN_demand_west_banat | HUN_territorial_revision_category | GFX_decision_generic_operation | 75 |  |  | HUN.txt |
| HUN_reintigrate_southern_slovakia | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_western_slovakia | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_eastern_slovakia | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_carpathian_ruthenia | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_transylvania | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_south_transylvania | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_crisana | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_banat | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_west_banat | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_vojvodina | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_burgenland | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_ukrainian_throne_decision | HUN_territorial_revision_category | GFX_decision_eng_trade_unions_support | 50 |  |  | HUN.txt |
| HUN_reintigrate_croatia | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_reintigrate_dalmatia | HUN_territorial_revision_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_referendum_in_southern_slovakia | HUN_territorial_revision_category | GFX_decision_eng_trade_unions_support | 75 |  |  | HUN.txt |
| HUN_referendum_in_carpathian_ruthenia | HUN_territorial_revision_category | GFX_decision_eng_trade_unions_support | 75 |  |  | HUN.txt |
| HUN_referendum_in_vojvodina | HUN_territorial_revision_category | GFX_decision_eng_trade_unions_support | 75 |  |  | HUN.txt |
| HUN_referendum_in_north_transylvania | HUN_territorial_revision_category | GFX_decision_eng_trade_unions_support | 75 |  |  | HUN.txt |
| HUN_seize_control_of_burgenland_dec | HUN_the_empire_category | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_austrian_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_place_wied_on_the_albanian_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_polish_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_spanish_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_bohemian_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_mexican_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_croatian_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_place_a_habsburg_on_the_lombardo_venetian_throne | HUN_the_empire_category | GFX_decision_eng_trade_unions_support | 10 |  |  | HUN.txt |
| HUN_integrating_an_imperial_subject_decision | HUN_the_empire_category | GFX_decision_generic_monarchy | 150 | yes |  | HUN.txt |
| HUN_integrate_mecklenburg | political_actions | GFX_decision_generic_nationalism | 50 |  |  | HUN.txt |
| HUN_carl_wilhelm_takes_absolute_cotrol_decision | political_actions | GFX_decision_eng_abdication_crisis | 50 |  |  | HUN.txt |
| HUN_royal_decree_decision | political_actions | GFX_decision_eng_abdication_crisis | 100 |  |  | HUN.txt |
| HUN_recall_kocsard_janky_to_active_service | political_actions | GFX_decision_generic_army_support |  |  | Gotterdammerung | HUN.txt |
| HUN_invitations_to_the_balkan_pact_decision | HUN_balkan_pact_category | GFX_decision_generic_protection | 100 | yes |  | HUN.txt |
| HUN_unite_hungary_romania_decision | HUN_balkan_pact_category | GFX_decision_generic_nationalism | 75 |  |  | HUN.txt |
| HUN_the_incoming_fascist_civil_war_mission | HUN_fascist_movements_category | GFX_decision_generic_ignite_civil_war |  | yes |  | HUN.txt |
| HUN_secure_the_ragged_guards | HUN_fascist_movements_category | GFX_decision_generic_army_support | 50 |  |  | HUN.txt |
| HUN_ban_the_volksbund | HUN_fascist_movements_category | GFX_decision_eng_trade_unions_support | 50 |  |  | HUN.txt |
| HUN_dismiss_fascist_generals | HUN_fascist_movements_category | GFX_decision_eng_blackshirt_march | 50 |  |  | HUN.txt |
| HUN_stamp_out_the_arrow_cross_party | HUN_fascist_movements_category | GFX_decision_generic_civil_support | 75 |  |  | HUN.txt |
| HUN_collectivize_society | political_actions | GFX_decision_SOV_place_hq | 120 |  |  | HUN.txt |
| HUN_apostolic_king_goering | political_actions | GFX_decision_generic_political_address | 50 |  |  | HUN.txt |
| HUN_the_danubian_federation_decision | HUN_the_danubian_federation_category | GFX_decision_generic_protection | 100 | yes |  | HUN.txt |
| HUN_unify_the_balkans_decision | HUN_balkan_union_category | generic_form_nation | 100 |  |  | HUN.txt |
| ICE_drilling_for_oil_off_shore | economy_decisions | oil |  |  |  | ICE.txt |
| ICE_incite_communist_uprising_scotland | ICE_infiltrate_the_british_isles_category | GFX_decision_generic_ignite_civil_war | 50 | yes |  | ICE.txt |
| ICE_incite_communist_uprising_wales | ICE_infiltrate_the_british_isles_category | GFX_decision_generic_ignite_civil_war | 50 | yes |  | ICE.txt |
| ICE_incite_communist_uprising_ni | ICE_infiltrate_the_british_isles_category | GFX_decision_generic_ignite_civil_war | 50 | yes |  | ICE.txt |
| ICE_the_wisdom_of_odin | ICE_improve_the_viking_spirit | GFX_decision_eng_puppet_usa | 75 | yes |  | ICE.txt |
| ICE_the_might_of_thor | ICE_improve_the_viking_spirit | GFX_decision_generic_civil_support | 75 | yes |  | ICE.txt |
| ICE_the_guidance_of_aegir_and_ran | ICE_improve_the_viking_spirit | GFX_decision_generic_naval | 75 | yes |  | ICE.txt |
| ICE_the_ferocity_of_the_fenrir | ICE_improve_the_viking_spirit | GFX_decision_eng_imperial_federation | 75 | yes |  | ICE.txt |
| ICE_the_fertility_of_freya | ICE_improve_the_viking_spirit | GFX_decision_eng_propaganda_campaigns | 75 | yes |  | ICE.txt |
| ICE_a_new_yggdrasill | ICE_improve_the_viking_spirit | GFX_decision_generic_construction | 120 | yes |  | ICE.txt |
| ICE_a_monument_to_leif | ICE_improve_the_viking_spirit | GFX_decision_generic_nationalism | 50 | yes |  | ICE.txt |
| IRQ_nationalise_the_oil | political_actions | generic_prepare_civil_war | 50 | yes | Graveyard of Empires | IRQ.txt |
| IRQ_recruit_arab_free_legion | IRQ_arab_free_legion_cat | GFX_decision_generic_prepare_civil_war |  | yes |  | IRQ.txt |
| IRQ_core_state | greater_iraq_decision_cat | GFX_decision_infiltrate_state | 50 | yes |  | IRQ.txt |
| united_arab_rep_core_state | united_arab_republic_cat | GFX_decision_infiltrate_state | 50 | yes |  | IRQ.txt |
| IRQ_invite_to_federation | hashemite_federation_cat | GFX_decision_infiltrate_state | 25 | yes |  | IRQ.txt |
| IRQ_invite_to_federation_africa | hashemite_federation_cat | GFX_decision_infiltrate_state | 25 | yes |  | IRQ.txt |
| IRQ_flood_the_plains | IRQ_flood_the_plains_cat | hol_inundate_water_lines | 50 | yes |  | IRQ.txt |
| KUR_syrian_border_skrimish_decision | KUR_syrian_border_skrimish_cat | border_war | 50 | yes |  | IRQ.txt |
| IRQ_march_on_syrian_kurdistan_mission | KUR_syrian_border_skrimish_cat | border_war |  |  |  | IRQ.txt |
| DEBUG_activate_missiolinis_system | debug_decisions |  |  |  |  | ITA.txt |
| DEBUG_deactivate_missiolinis_system | debug_decisions |  |  |  |  | ITA.txt |
| DEBUG_manu_tests | debug_decisions |  |  |  |  | ITA.txt |
| DEBUG_initiate_BOP | debug_decisions |  |  |  |  | ITA.txt |
| ITA_withdraw_from_ethiopia | ETH_second_italo_ethiopian_war_category | GFX_decision_eng_trade_unions_support | 15 | yes |  | ITA.txt |
| DEBUG_MISSIOLINIS_FASTER_TACK | ITA_missiolinis |  |  |  |  | ITA.txt |
| DEBUG_MISSIOLINIS_BACK_TO_NORMAL | ITA_missiolinis |  |  |  |  | ITA.txt |
| ITA_conquer_the_north_mission | ITA_missiolinis | GFX_decision_generic_operation |  | yes |  | ITA.txt |
| ITA_conquer_the_south_mission | ITA_missiolinis | GFX_decision_generic_operation |  | yes |  | ITA.txt |
| ITA_missiolini_conquer_ethiopia | ITA_missiolinis | GFX_decision_generic_prepare_civil_war |  | yes |  | ITA.txt |
| ITA_missiolini_pacify_ethiopia | ITA_missiolinis | GFX_decision_generic_police_action |  | yes | By Blood Alone | ITA.txt |
| ITA_missiolini_pacify_ethiopia_vanilla | ITA_missiolinis | GFX_decision_generic_police_action |  | yes | By Blood Alone | ITA.txt |
| ITA_missiolini_strengthen_heavy_industry | ITA_missiolinis | GFX_decision_generic_merge_plant_materiel |  |  |  | ITA.txt |
| ITA_missiolini_strengthen_the_army | ITA_missiolinis | GFX_decision_generic_military |  |  |  | ITA.txt |
| ITA_missiolini_stockpile_trucks | ITA_missiolinis | GFX_decision_generic_trucks |  |  |  | ITA.txt |
| ITA_missiolini_stockpile_fuel | ITA_missiolinis | GFX_decision_oil |  |  |  | ITA.txt |
| ITA_missiolini_strengthen_the_airforce | ITA_missiolinis | GFX_decision_generic_merge_plant_aircraft |  |  |  | ITA.txt |
| ITA_missiolini_industrial_research | ITA_missiolinis | GFX_decision_generic_wreckers |  |  |  | ITA.txt |
| ITA_missiolini_expand_intelligence_agency | ITA_missiolinis | GFX_decision_onmap_recruit_operative |  |  |  | ITA.txt |
| ITA_missiolini_occupy_albania | ITA_missiolinis | GFX_decision_infiltrate_state |  |  |  | ITA.txt |
| ITA_missiolini_occupy_dalmatia | ITA_missiolinis | GFX_decision_infiltrate_state |  |  |  | ITA.txt |
| ITA_missiolini_occupy_greece | ITA_missiolinis | GFX_decision_infiltrate_state |  |  |  | ITA.txt |
| ITA_missiolini_occupy_ticino | ITA_missiolinis | GFX_decision_infiltrate_state |  |  |  | ITA.txt |
| ITA_missiolini_bolster_political_cabinet | ITA_missiolinis | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_missiolini_bolster_military_high_command | ITA_missiolinis | GFX_decision_generic_army_support |  |  |  | ITA.txt |
| DEBUG_deactivate_BOP | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_make_decisions_faster_and_free | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_make_decisions_go_back_to_normal | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_absurdly_high_increase_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_high_increase_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_medium_increase_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_low_increase_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_very_low_increase_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_absurdly_high_decrease_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_high_decrease_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_medium_decrease_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_low_decrease_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_bop_very_low_decrease_value | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_mussolini_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_grand_council_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_balbo_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_grandi_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_king_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_king_umberto_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_communism_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_democratic_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_pope_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_max_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| DEBUG_set_min_bop | ITA_balance_of_power_category |  |  |  |  | ITA.txt |
| ITA_bop_take_over_ministry_of_foreign_affairs | ITA_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | ITA.txt |
| ITA_bop_resign_ministry_of_foreign_affairs_position | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_bop_take_over_ministry_of_justice | ITA_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | ITA.txt |
| ITA_bop_resign_ministry_of_justice_position | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_bop_take_over_ministry_of_education | ITA_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | ITA.txt |
| ITA_bop_resign_ministry_of_education_position | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_bop_take_over_ministry_of_corporations | ITA_balance_of_power_category | GFX_decision_eng_trade_unions_demand |  |  |  | ITA.txt |
| ITA_bop_resign_ministry_of_corporations_position | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_bop_slander_the_duce | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  | yes |  | ITA.txt |
| ITA_bop_criticize_the_war | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  | yes |  | ITA.txt |
| ITA_bop_question_the_army | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_bop_question_the_airforce | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_bop_question_the_navy | ITA_balance_of_power_category | GFX_decision_generic_political_discourse |  |  |  | ITA.txt |
| ITA_bop_military_parade | ITA_balance_of_power_category | GFX_decision_generic_military |  |  |  | ITA.txt |
| ITA_bop_send_support | ITA_balance_of_power_category | ger_military_buildup |  | yes |  | ITA.txt |
| ITA_bop_praise_the_army | ITA_balance_of_power_category | GFX_decision_generic_tank |  |  |  | ITA.txt |
| ITA_bop_praise_the_airforce | ITA_balance_of_power_category | GFX_decision_generic_air |  |  |  | ITA.txt |
| ITA_bop_praise_the_navy | ITA_balance_of_power_category | GFX_decision_generic_naval |  |  |  | ITA.txt |
| ITA_bop_constitutional_draft | ITA_balance_of_power_category | GFX_decision_SWI_swiss_democratic_tradition_campaign | 70 | yes |  | ITA.txt |
| ITA_bop_privileges_for_the_elites | ITA_balance_of_power_category | GFX_decision_eng_ally_imperialist_coup | 70 | yes |  | ITA.txt |
| ITA_bop_revoke_the_lateran_treaty | ITA_balance_of_power_category | GFX_decision_generic_break_treaty | 70 | yes |  | ITA.txt |
| ITA_bop_expand_the_lateran_treaty | ITA_balance_of_power_category | GFX_decision_hol_exchange_intelligence_data | 70 | yes |  | ITA.txt |
| ITA_bop_liturgical_reforms | ITA_balance_of_power_category | GFX_decision_eng_trade_unions_support | 70 |  |  | ITA.txt |
| ITA_bop_condemn_fascism | ITA_balance_of_power_category | GFX_decision_eng_propaganda_campaigns | 70 | yes |  | ITA.txt |
| ITA_bop_convoke_ecumenical_council | ITA_balance_of_power_category | GFX_decision_SWI_support_humanitarian_efforts | 100 | yes |  | ITA.txt |
| ITA_bop_cooperation_with_anarchists | ITA_balance_of_power_category | GFX_decision_generic_civil_support | 70 | yes |  | ITA.txt |
| ITA_bop_unify_the_left | ITA_balance_of_power_category | GFX_decision_generic_speech | 70 | yes |  | ITA.txt |
| ITA_bop_concesions_to_the_bourgeoisie | ITA_balance_of_power_category | GFX_decision_generic_fundraising |  | yes |  | ITA.txt |
| ITA_bop_cooperation_with_christian_democrats | ITA_balance_of_power_category | GFX_decision_generic_political_discourse | 70 | yes |  | ITA.txt |
| ITA_bop_utilize_the_mafia | ITA_balance_of_power_category | GFX_decision_generic_assassination | 100 | yes |  | ITA.txt |
| ITA_expand_regional_control | ETH_italian_occupation_category | GFX_decision_oppression | 75 |  |  | ITA.txt |
| ITA_discredit_haile_selassie | ETH_italian_occupation_category | GFX_decision_generic_speech | 35 |  |  | ITA.txt |
| ITA_electrify_state | ETH_italian_occupation_category | GFX_decision_generic_electricity | 25 | yes |  | ITA.txt |
| ITA_train_irregulars | ITA_colonial_management_dec_cat | GFX_decision_generic_prepare_civil_war |  |  |  | ITA.txt |
| ITA_disband_irregulars | ITA_colonial_management_dec_cat | GFX_decision_generic_disband_irregulars | 5 |  |  | ITA.txt |
| ITA_reorganize_irregulars | ITA_colonial_management_dec_cat | GFX_decision_generic_reorganize_irregulars |  |  |  | ITA.txt |
| ITA_reorganize_ascari | ITA_colonial_management_dec_cat | GFX_decision_ITA_reorganize_ascari |  |  | La Resistance | ITA.txt |
| ITA_regional_development_in_state | ITA_colonial_management_dec_cat | GFX_decision_generic_construction |  |  |  | ITA.txt |
| colonial_government_in_east_africa | ITA_colonial_management_dec_cat | GFX_decision_generic_colonial_administration |  | yes | La Resistance | ITA.txt |
| give_somaliland_to_the_aoi | ITA_colonial_management_dec_cat | GFX_decision_infiltrate_state | 25 | yes |  | ITA.txt |
| give_djibouti_to_the_aoi | ITA_colonial_management_dec_cat | GFX_decision_infiltrate_state | 25 | yes |  | ITA.txt |
| give_garissa_to_the_aoi | ITA_colonial_management_dec_cat | GFX_decision_infiltrate_state | 25 | yes |  | ITA.txt |
| send_more_men_to_the_AOI | ITA_colonial_management_dec_cat | GFX_decision_eng_blackshirt_march | 10 |  |  | ITA.txt |
| send_more_weapons_to_the_AOI | ITA_colonial_management_dec_cat | GFX_decision_generic_prepare_civil_war | 10 |  |  | ITA.txt |
| ITA_abolish_the_colonies_dec | ITA_colonial_management_dec_cat | GFX_decision_generic_reorganize_irregulars |  | yes |  | ITA.txt |
| ITA_cooperation_program_with_country | ITA_naval_cooperation_programs_dec_cat | GFX_decision_generic_research | 15 | yes |  | ITA.txt |
| ITA_joint_maneuvers_with_country | ITA_naval_cooperation_programs_dec_cat | GFX_decision_hol_draw_up_staff_plans |  | yes |  | ITA.txt |
| ITA_sell_obsolete_escort_ships_to_country | ITA_naval_cooperation_programs_dec_cat | GFX_decision_generic_naval | 15 |  |  | ITA.txt |
| ITA_cede_aquila_class_destroyers_to_spanish_tag | ITA_naval_cooperation_programs_dec_cat | GFX_decision_generic_naval |  | yes |  | ITA.txt |
| ITA_export_midget_submarines | ITA_naval_cooperation_programs_dec_cat | GFX_decision_generic_construction |  |  |  | ITA.txt |
| ITA_pressure_country_government_balkan | ITA_diplomacy_balkan_decision_category | generic_political_discourse |  |  |  | ITA.txt |
| ITA_promote_ideology_rallies_balkan | ITA_diplomacy_balkan_decision_category | generic_political_rally |  | yes |  | ITA.txt |
| ITA_send_ultimatum_to_country_balkan | ITA_diplomacy_balkan_decision_category | eng_trade_unions_demand |  |  |  | ITA.txt |
| ITA_fight_alongside_country_comrades_balkan | ITA_diplomacy_balkan_decision_category | generic_prepare_civil_war |  |  |  | ITA.txt |
| ITA_coronate_prince_aimone | ITA_diplomacy_balkan_decision_category | GFX_decision_eng_ally_imperialist_coup | 75 |  |  | ITA.txt |
| ITA_demand_tomislavs_absolute_reign | ITA_diplomacy_balkan_decision_category | GFX_decision_eng_abdication_crisis | 75 |  | Together for Victory | ITA.txt |
| ITA_establish_the_regno_albania | ITA_diplomacy_balkan_decision_category | GFX_decision_eng_trade_unions_support | 50 |  | Together for Victory | ITA.txt |
| ITA_establish_the_governato_del_montenegro | ITA_diplomacy_balkan_decision_category | GFX_decision_eng_trade_unions_support | 50 |  | Together for Victory | ITA.txt |
| ITA_demand_recognition_of_the_bashkimi_kombetar | ITA_diplomacy_balkan_decision_category | GFX_decision_generic_operation | 25 |  |  | ITA.txt |
| ITA_demand_dalmatia | ITA_diplomacy_balkan_decision_category | GFX_decision_generic_civil_support | 75 |  |  | ITA.txt |
| ITA_claim_the_montengrin_throne | ITA_diplomacy_balkan_decision_category | GFX_decision_eng_support_imperialist_coup | 100 |  |  | ITA.txt |
| ITA_support_the_hungarians | ITA_diplomacy_balkan_decision_category | GFX_decision_generic_speech | 75 |  |  | ITA.txt |
| ITA_demand_turkish_demilitarization | ITA_diplomacy_balkan_decision_category | GFX_decision_generic_operation | 100 |  |  | ITA.txt |
| ITA_give_the_dodecanese_islands_to_greece_for_an_alliance | ITA_diplomacy_balkan_decision_category | GFX_decision_eng_trade_unions_support | 75 |  |  | ITA.txt |
| ITA_give_the_dodecanese_islands_to_turkey_for_an_alliance | ITA_diplomacy_balkan_decision_category | GFX_decision_eng_trade_unions_support | 75 |  |  | ITA.txt |
| ITA_vallo_alpino_occidentale | ITA_vallo_alpino_del_littorio_dec_cat | GFX_decision_generic_mountain_fortification |  |  |  | ITA.txt |
| ITA_vallo_alpino_settentrionale_west | ITA_vallo_alpino_del_littorio_dec_cat | GFX_decision_generic_mountain_fortification |  |  |  | ITA.txt |
| ITA_vallo_alpino_settentrionale_east | ITA_vallo_alpino_del_littorio_dec_cat | GFX_decision_generic_mountain_fortification |  |  |  | ITA.txt |
| ITA_vallo_alpino_orientale | ITA_vallo_alpino_del_littorio_dec_cat | GFX_decision_generic_mountain_fortification |  |  |  | ITA.txt |
| ITA_vittorio_abdicate | political_actions | GFX_decision_generic_monarchy |  |  |  | ITA.txt |
| ITA_suppress_mafia_in_state | ITA_italian_mafia_dec_cat | GFX_decision_oppression |  |  |  | ITA.txt |
| ITA_human_torpedo_raid | operations | GFX_decision_generic_human_torpedo |  | yes |  | ITA.txt |
| JAP_Danne_debugging | debug_decisions |  |  |  |  | JAP.txt |
| JAP_Danne_imperial_influence_debugging | debug_decisions |  |  |  |  | JAP.txt |
| JAP_Danne_small_army_faction_increase_debugging | debug_decisions | generic_military |  |  |  | JAP.txt |
| JAP_Danne_big_army_faction_increase_debugging | debug_decisions | generic_military |  |  |  | JAP.txt |
| JAP_Danne_small_army_faction_decrease_debugging | debug_decisions | generic_military |  |  |  | JAP.txt |
| JAP_Danne_big_army_faction_decrease_debugging | debug_decisions | generic_military |  |  |  | JAP.txt |
| JAP_Danne_small_navy_faction_increase_debugging | debug_decisions | generic_naval |  |  |  | JAP.txt |
| JAP_Danne_big_navy_faction_increase_debugging | debug_decisions | generic_naval |  |  |  | JAP.txt |
| JAP_Danne_small_navy_faction_decrease_debugging | debug_decisions | generic_naval |  |  |  | JAP.txt |
| JAP_Danne_big_navy_faction_decrease_debugging | debug_decisions | generic_naval |  |  |  | JAP.txt |
| JAP_Danne_small_zaibatsu_faction_increase_debugging | debug_decisions | generic_factory |  |  |  | JAP.txt |
| JAP_Danne_big_zaibatsu_faction_increase_debugging | debug_decisions | generic_factory |  |  |  | JAP.txt |
| JAP_Danne_small_zaibatsu_faction_decrease_debugging | debug_decisions | generic_factory |  |  |  | JAP.txt |
| JAP_Danne_big_zaibatsu_faction_decrease_debugging | debug_decisions | generic_factory |  |  |  | JAP.txt |
| JAP_Danne_small_government_faction_increase_debugging | debug_decisions | generic_political_address |  |  |  | JAP.txt |
| JAP_Danne_big_government_faction_increase_debugging | debug_decisions | generic_political_address |  |  |  | JAP.txt |
| JAP_Danne_small_government_faction_decrease_debugging | debug_decisions | generic_political_address |  |  |  | JAP.txt |
| JAP_Danne_big_government_faction_decrease_debugging | debug_decisions | generic_political_address |  |  |  | JAP.txt |
| JAP_put_hirohito_in_house_arrest_debugging | debug_decisions | generic_political_address |  |  |  | JAP.txt |
| JAP_china_step_up_war_effort | JAP_intervene_in_china | jap_conquer_china | 25 |  |  | JAP.txt |
| JAP_ichi_go | JAP_intervene_in_china | jap_conquer_china |  | yes | No Compromise, No Surrender | JAP.txt |
| JAP_conquer_china | JAP_intervene_in_china | jap_conquer_china |  | yes |  | JAP.txt |
| JAP_sue_for_peace_CHI | foreign_politics |  | 0 | yes |  | JAP.txt |
| JAP_sue_for_peace_MAN | foreign_politics |  | 0 | yes |  | JAP.txt |
| JAP_sue_for_peace_nuke | foreign_politics |  | 0 | yes |  | JAP.txt |
| JAP_sue_for_peace_nuke_mission | foreign_politics |  |  | yes |  | JAP.txt |
| JAP_request_soviet_support | foreign_politics | generic_prepare_civil_war | 50 | yes |  | JAP.txt |
| JAP_demand_soviet_unions_surrender | foreign_politics |  | 50 | yes |  | JAP.txt |
| JAP_core_KOR_state | foreign_politics | GFX_decision_infiltrate_state | 30 | yes |  | JAP.txt |
| JAP_core_MAN_state | foreign_politics | GFX_decision_infiltrate_state | 30 | yes |  | JAP.txt |
| JAP_release_korea | JAP_pacific_guardian | generic_independence |  | yes |  | JAP.txt |
| JAP_guardian_of_INS | JAP_pacific_guardian | jap_pacific_guardian | 50 | yes |  | JAP.txt |
| JAP_guardian_of_MAL | JAP_pacific_guardian | jap_pacific_guardian | 50 | yes |  | JAP.txt |
| JAP_guardian_of_indochina | JAP_pacific_guardian | jap_pacific_guardian | 50 | yes |  | JAP.txt |
| JAP_assume_guardianship_over_asian_subject_decison | JAP_pacific_guardian | GFX_decision_jap_pacific_guardian | 75 | yes |  | JAP.txt |
| JAP_invite_demo_or_na_asian_nation_to_faction_decison | JAP_pacific_guardian | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | JAP.txt |
| JAP_invite_com_south_ame_nation_to_faction_decison | JAP_the_red_sun_over_asia_decisions | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | JAP.txt |
| JAP_communist_core_asian_state | JAP_the_red_sun_over_asia_decisions | GFX_decision_generic_form_nation | 50 | yes |  | JAP.txt |
| JAP_invite_com_middle_eastern_nation_to_faction_decison | JAP_the_red_sun_over_asia_decisions | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | JAP.txt |
| JAP_stir_communist_sentiments_in_the_middle_east_decison | JAP_the_red_sun_over_asia_decisions | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | JAP.txt |
| JAP_stir_communist_sentiments_in_south_asia_decison | JAP_the_red_sun_over_asia_decisions | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | JAP.txt |
| JAP_invite_com_south_asian_nation_to_faction_decison | JAP_the_red_sun_over_asia_decisions | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | JAP.txt |
| JAP_PARF_economic_integration_decision | JAP_the_red_sun_over_asia_decisions | GFX_decision_eng_trade_unions_support | 100 | yes |  | JAP.txt |
| JAP_PARF_develop_member_industry_decision | JAP_the_red_sun_over_asia_decisions | GFX_decision_hol_attract_foreign_investors | 50 | yes |  | JAP.txt |
| JAP_return_manchuria | JAP_colonial_independence | generic_independence | 10 | yes |  | JAP.txt |
| JAP_break_the_london_naval_treaty | political_actions | generic_break_treaty | 25 | yes |  | JAP.txt |
| JAP_promote_hayao_tada_to_lieutenant_general_decision | political_actions | GFX_decision_generic_army_support |  |  |  | JAP.txt |
| JAP_tora_tora_tora | operations | decision_generic_naval |  | yes |  | JAP.txt |
| JAP_test_the_soviets | operations | border_war | 50 | yes |  | JAP.txt |
| JAP_border_conflict_warning_SOV | operations | border_war |  | yes |  | JAP.txt |
| JAP_border_conflict_escalation_warning_SOV | operations | border_war |  | yes |  | JAP.txt |
| JAP_border_incident_forgotten | operations | border_war |  | yes |  | JAP.txt |
| JAP_escalate_incident_to_border_conflict_SOV | operations | border_war |  | yes |  | JAP.txt |
| JAP_border_conflict_time_until_cancelled | operations | border_war |  | yes |  | JAP.txt |
| JAP_border_conflict_escalate_conflict | operations | generic_ignite_civil_war | 200 | yes |  | JAP.txt |
| JAP_border_conflict_escalate_to_war | operations | generic_ignite_civil_war | 150 | yes |  | JAP.txt |
| JAP_border_conflict_back_out_of_conflict | operations |  |  | yes |  | JAP.txt |
| JAP_war_with_soviet_union | operations | generic_ignite_civil_war | 25 | yes |  | JAP.txt |
| JAP_tauran_border_incident_forgotten_1 | operations | border_war |  | yes |  | JAP.txt |
| JAP_assault_tauran_decision | operations | border_war | 5 | yes |  | JAP.txt |
| JAP_tauran_border_conflict_warning_MON | operations | border_war |  | yes |  | JAP.txt |
| JAP_border_conflict_escalation_warning_MON | operations | border_war |  | yes |  | JAP.txt |
| JAP_tauran_border_incident_forgotten | operations | border_war |  | yes |  | JAP.txt |
| JAP_escalate_incident_to_border_conflict_MON | operations | border_war |  | yes |  | JAP.txt |
| JAP_tauran_border_conflict_time_until_cancelled | operations | border_war |  | yes |  | JAP.txt |
| JAP_develop_north_sakhalin_oil_deposits | prospect_for_resources | oil | 25 |  |  | JAP.txt |
| JAP_develop_tunguska_coal_deposits | prospect_for_resources | coal | 25 |  |  | JAP.txt |
| JAP_develop_irkutsk_coal_deposits | prospect_for_resources | coal | 25 |  |  | JAP.txt |
| JAP_develop_luzon_chromium_deposits | prospect_for_resources | chromium | 25 |  |  | JAP.txt |
| JAP_develop_mindanao_steel_deposits | prospect_for_resources | steel | 25 |  |  | JAP.txt |
| JAP_develop_samar_steel_deposits | prospect_for_resources | steel | 25 |  |  | JAP.txt |
| JAP_develop_nauru_tungsten_deposits | prospect_for_resources | tungsten | 25 |  |  | JAP.txt |
| JAP_develop_singapore_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | JAP.txt |
| JAP_develop_riau_oil_deposits | prospect_for_resources | oil | 50 |  |  | JAP.txt |
| JAP_develop_kalimantan_oil_deposits | prospect_for_resources | oil | 25 |  |  | JAP.txt |
| JAP_develop_west_papuan_oil_deposits | prospect_for_resources | oil | 25 |  |  | JAP.txt |
| JAP_develop_tuban_oil_deposits | prospect_for_resources | oil | 30 |  |  | JAP.txt |
| JAP_develop_shandong_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | JAP.txt |
| JAP_develop_suiyuan_steel_deposits | prospect_for_resources | steel | 25 |  |  | JAP.txt |
| JAP_develop_yunnan_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | JAP.txt |
| JAP_develop_sichuan_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | JAP.txt |
| JAP_aizawa_trial_ongoing | JAP_kodoha_insurgency_decisions | GFX_decision_generic_police_action |  | yes |  | JAP.txt |
| JAP_increase_takahashi_korekiyo_security_decision | JAP_kodoha_insurgency_decisions | GFX_decision_SWI_no_elected_president | 40 | yes |  | JAP.txt |
| JAP_increase_jotaro_watanabe_security_decision | JAP_kodoha_insurgency_decisions | GFX_decision_generic_belgian_colonial_helmet | 40 | yes |  | JAP.txt |
| JAP_kwantung_army_impatience | JAP_kwantung_army_decisions | GFX_decision_jap_conquer_china |  | yes |  | JAP.txt |
| JAP_the_suiyuan_offensive_mission | JAP_kwantung_army_decisions | GFX_decision_generic_operation |  | yes |  | JAP.txt |
| JAP_growing_unrest_in_the_shanghai_concession | JAP_kwantung_army_decisions | GFX_decision_jap_conquer_china |  | yes |  | JAP.txt |
| JAP_strike_down_chinese_warlord_decision | JAP_kwantung_army_decisions | GFX_decision_border_war | 30 | yes |  | JAP.txt |
| JAP_launch_an_offensive_in_chinese_state_decision | JAP_kwantung_army_decisions | GFX_decision_border_war |  | yes |  | JAP.txt |
| JAP_luxury_is_the_enemy_decision | JAP_spiritual_mobilization_decisions | GFX_decision_generic_consumer_goods | 75 | yes |  | JAP.txt |
| JAP_form_a_labor_patriot_corps_decision | JAP_spiritual_mobilization_decisions | GFX_decision_generic_merge_plant_materiel | 100 | yes |  | JAP.txt |
| JAP_produce_bullet_stamps_decision | JAP_spiritual_mobilization_decisions | GFX_decision_generic_industry | 75 | yes |  | JAP.txt |
| JAP_distribute_rations_decision | JAP_spiritual_mobilization_decisions | GFX_decision_SWI_support_humanitarian_efforts | 50 | yes |  | JAP.txt |
| JAP_develop_sufu_materials_decision | JAP_spiritual_mobilization_decisions | GFX_decision_generic_confiscation | 50 | yes |  | JAP.txt |
| JAP_collect_civilian_donations_decision | JAP_spiritual_mobilization_decisions | GFX_decision_hol_attract_foreign_investors | 75 | yes |  | JAP.txt |
| JAP_raise_military_moreale_decision | JAP_spiritual_mobilization_decisions | GFX_decision_generic_political_rally | 75 | yes |  | JAP.txt |
| JAP_women_in_military_production_decision | JAP_spiritual_mobilization_decisions | GFX_decision_generic_merge_plant_tank | 50 | yes |  | JAP.txt |
| JAP_incite_increased_tensions_in_the_diet_decision | JAP_imperial_influence_decision_cat | GFX_decision_generic_political_discourse | 50 | yes |  | JAP.txt |
| JAP_conflict_between_faction_reaching_boiling_point_mission | JAP_imperial_influence_decision_cat | GFX_decision_generic_political_address |  | yes |  | JAP.txt |
| JAP_army_faction_demands_military_factories | JAP_imperial_influence_decision_cat | GFX_decision_JAP_army_faction |  |  |  | JAP.txt |
| JAP_army_faction_demands_political_appointment | JAP_imperial_influence_decision_cat | GFX_decision_JAP_army_faction |  |  |  | JAP.txt |
| JAP_army_faction_demands_conscription_law_change | JAP_imperial_influence_decision_cat | GFX_decision_JAP_army_faction |  |  |  | JAP.txt |
| JAP_army_faction_demands_larger_army | JAP_imperial_influence_decision_cat | GFX_decision_JAP_army_faction |  |  |  | JAP.txt |
| JAP_army_faction_demands_more_trucks | JAP_imperial_influence_decision_cat | GFX_decision_JAP_army_faction |  |  |  | JAP.txt |
| JAP_army_faction_demands_more_tanks | JAP_imperial_influence_decision_cat | GFX_decision_JAP_army_faction |  |  |  | JAP.txt |
| JAP_army_faction_demands_more_artillery | JAP_imperial_influence_decision_cat | GFX_decision_JAP_army_faction |  |  |  | JAP.txt |
| JAP_naval_faction_demands_dockyards | JAP_imperial_influence_decision_cat | GFX_decision_JAP_naval_faction |  |  |  | JAP.txt |
| JAP_naval_faction_demands_political_appointment | JAP_imperial_influence_decision_cat | GFX_decision_JAP_naval_faction |  |  |  | JAP.txt |
| JAP_naval_faction_demands_conscription_law_change | JAP_imperial_influence_decision_cat | GFX_decision_JAP_naval_faction |  |  |  | JAP.txt |
| JAP_naval_faction_demands_more_carriers | JAP_imperial_influence_decision_cat | GFX_decision_JAP_naval_faction |  |  |  | JAP.txt |
| JAP_naval_faction_demands_more_carriers_and_battleships | JAP_imperial_influence_decision_cat | GFX_decision_JAP_naval_faction |  |  |  | JAP.txt |
| JAP_naval_faction_demands_more_battleships | JAP_imperial_influence_decision_cat | GFX_decision_JAP_naval_faction |  |  |  | JAP.txt |
| JAP_naval_faction_demands_strike_south_happen_mission | JAP_imperial_influence_decision_cat | GFX_decision_JAP_naval_faction |  |  |  | JAP.txt |
| JAP_zaibatsu_faction_demands_factories | JAP_imperial_influence_decision_cat | GFX_decision_JAP_zaibatsu_faction |  |  |  | JAP.txt |
| JAP_zaibatsu_faction_demands_political_appointment | JAP_imperial_influence_decision_cat | GFX_decision_JAP_zaibatsu_faction |  |  |  | JAP.txt |
| JAP_zaibatsu_faction_demands_economy_law_change | JAP_imperial_influence_decision_cat | GFX_decision_JAP_zaibatsu_faction |  |  |  | JAP.txt |
| JAP_zaibatsu_faction_demands_industrial_company_employment | JAP_imperial_influence_decision_cat | GFX_decision_JAP_zaibatsu_faction |  |  |  | JAP.txt |
| JAP_government_faction_demands_political_appointment | JAP_imperial_influence_decision_cat | GFX_decision_JAP_civic_faction |  |  |  | JAP.txt |
| JAP_government_faction_demands_trade_law_change | JAP_imperial_influence_decision_cat | GFX_decision_JAP_civic_faction |  |  |  | JAP.txt |
| JAP_government_faction_demands_limited_army_influence | JAP_imperial_influence_decision_cat | GFX_decision_JAP_civic_faction |  |  |  | JAP.txt |
| JAP_government_faction_demands_limited_navy_influence | JAP_imperial_influence_decision_cat | GFX_decision_JAP_civic_faction |  |  |  | JAP.txt |
| JAP_government_faction_demands_limited_zaibatsu_influence | JAP_imperial_influence_decision_cat | GFX_decision_JAP_civic_faction |  |  |  | JAP.txt |
| JAP_estabish_contact_with_thubten_kumphela_decision | JAP_the_propaganda_department_decisions | GFX_decision_generic_political_discourse | 50 | yes |  | JAP.txt |
| JAP_estabish_a_trongdra_regiment_in_exile | JAP_the_propaganda_department_decisions | GFX_decision_generic_protection | 25 | yes |  | JAP.txt |
| JAP_influence_tibetan_people_decision | JAP_the_propaganda_department_decisions | GFX_decision_eng_propaganda_campaigns | 50 |  |  | JAP.txt |
| JAP_coup_the_tibetan_government_decision | JAP_the_propaganda_department_decisions | GFX_decision_generic_civil_support | 75 | yes |  | JAP.txt |
| JAP_create_subject_tonarigumi | JAP_the_propaganda_department_decisions | GFX_decision_generic_military | 25 | yes |  | JAP.txt |
| JAP_pull_back_on_fanatiscist_propaganda_decision | JAP_the_propaganda_department_decisions | GFX_decision_hol_war_on_pacifism | 50 | yes |  | JAP.txt |
| JAP_promote_pro_japanese_sentiment_decison | JAP_the_propaganda_department_decisions | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | JAP.txt |
| JAP_invest_in_colonial_resources_decison | JAP_the_propaganda_department_decisions | GFX_decision_gre_investment_decisions | 50 | yes |  | JAP.txt |
| JAP_infiltrate_setsen_khanate_lands_decision | JAP_the_propaganda_department_decisions | GFX_decision_infiltrate_state | 50 | yes |  | JAP.txt |
| JAP_arm_anti_communist_mongol_dissidents_decision | JAP_the_propaganda_department_decisions | GFX_decision_CHL_carabineros | 50 | yes |  | JAP.txt |
| JAP_influence_mongolian_people_decision | JAP_the_propaganda_department_decisions | GFX_decision_eng_propaganda_campaigns | 50 |  |  | JAP.txt |
| JAP_send_jodbajab_to_mongolia_decision | JAP_the_propaganda_department_decisions | GFX_decision_onmap_recruit_operative | 50 | yes |  | JAP.txt |
| JAP_send_jonjurjab_to_mongolia_decision | JAP_the_propaganda_department_decisions | GFX_decision_onmap_recruit_operative | 50 | yes |  | JAP.txt |
| JAP_coup_the_mongolian_government_decision | JAP_the_propaganda_department_decisions | GFX_decision_generic_tank | 75 | yes |  | JAP.txt |
| JAP_jeweled_spear_claim_decision | JAP_the_propaganda_department_decisions | GFX_decision_generic_planted_spear | 10 | yes |  | JAP.txt |
| JAP_core_asian_state | JAP_the_propaganda_department_decisions | GFX_decision_generic_form_nation | 30 | yes |  | JAP.txt |
| JAP_hand_mongol_states_to_mengkukuo_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_SWI_support_humanitarian_efforts | 15 |  |  | JAP.txt |
| JAP_GEACPS_economic_integration_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_eng_trade_unions_support | 100 | yes |  | JAP.txt |
| JAP_GEACPS_develop_member_industry_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_hol_attract_foreign_investors | 50 | yes |  | JAP.txt |
| JAP_annex_developed_puppet_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_eng_trade_unions_demand | 100 | yes |  | JAP.txt |
| JAP_hand_chinese_states_to_the_reorganized_government_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_SWI_support_humanitarian_efforts | 50 |  |  | JAP.txt |
| JAP_merge_our_chinese_puppets_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_eng_trade_unions_support | 100 |  |  | JAP.txt |
| JAP_establish_the_state_of_burma_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_generic_nationalism | 25 |  |  | JAP.txt |
| JAP_establish_the_provisional_government_of_free_india_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_generic_nationalism | 25 |  |  | JAP.txt |
| JAP_establish_the_second_philippine_republic_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_generic_nationalism | 25 |  |  | JAP.txt |
| JAP_establish_kingdoms_of_annam_and_cambodia_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_generic_operation | 30 | yes |  | JAP.txt |
| JAP_establish_empire_of_vietnam_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_JAP_establish_empire_of_vietnam | 10 | yes |  | JAP.txt |
| JAP_establish_kingdom_of_kampuchea_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_JAP_establish_kingdom_of_kampuchea | 10 | yes |  | JAP.txt |
| JAP_establish_kingdom_of_luang_prabang_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_JAP_establish_kingdom_of_luang_prabang | 10 | yes |  | JAP.txt |
| JAP_establish_state_of_ceylon_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_JAP_establish_state_of_ceylon | 10 | yes |  | JAP.txt |
| JAP_organize_timorese_black_columns_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_SWE_set_army_budget | 15 | yes |  | JAP.txt |
| JAP_integrate_northern_karafuto_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_generic_form_nation | 30 | yes |  | JAP.txt |
| JAP_empower_the_yi_dynasty_decision | JAP_the_co_prosperity_sphere_decisions | GFX_decision_generic_monarchy | 25 | yes |  | JAP.txt |
| war_propaganda_manga_industry | propaganda_efforts | generic_prepare_civil_war | 75 | yes |  | JAP.txt |
| war_propaganda_film_industry_2 | propaganda_efforts | generic_prepare_civil_war | 100 | yes |  | JAP.txt |
| JAP_incorporate_imperial_way_buddhism_decision | JAP_state_shintoism_decisions | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | JAP.txt |
| JAP_one_people_united_under_shinto_decision | JAP_state_shintoism_decisions | GFX_decision_generic_civil_support | 50 | yes |  | JAP.txt |
| JAP_relentless_divine_nationalism_decision | JAP_state_shintoism_decisions | GFX_decision_eng_blackshirt_speech | 50 | yes |  | JAP.txt |
| JAP_state_shinto_in_education_decision | JAP_state_shintoism_decisions | GFX_decision_SOV_academy_of_sciences | 75 | yes |  | JAP.txt |
| JAP_open_factory_in_state_decision | economy_decisions | GFX_decision_generic_factory | 50 | yes | No Compromise, No Surrender | JAP.txt |
| JAP_improve_the_category_of_state_decision | economy_decisions | GFX_decision_generic_construction | 35 | yes | No Compromise, No Surrender | JAP.txt |
| JAP_redistribute_wealth_and_collectivize_farms_decision | economy_decisions | GFX_decision_generic_welfare | 75 |  | No Compromise, No Surrender | JAP.txt |
| JAP_implementing_unos_economic_reforms_mission | economy_decisions | GFX_decision_generic_consumer_goods |  |  |  | JAP.txt |
| JAP_secure_control_from_army_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_civil_support |  | yes |  | JAP.txt |
| JAP_sway_general_loyalty_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_army_support | 25 |  |  | JAP.txt |
| JAP_sway_admiral_loyalty_decision | JAP_the_peoples_state_decisions | GFX_decision_SWE_set_navy_budget | 25 |  |  | JAP.txt |
| JAP_hold_speech_in_the_imperial_diet_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_speech | 50 |  |  | JAP.txt |
| JAP_publically_distance_from_sov_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_political_rally | 25 | yes |  | JAP.txt |
| JAP_communist_infiltration_of_state_decision_decision | JAP_the_peoples_state_decisions | GFX_decisions_generic_infiltration |  | yes |  | JAP.txt |
| JAP_spread_socialist_pamphlets_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_political_discourse | 50 |  |  | JAP.txt |
| JAP_spread_socialist_propaganda_in_campuses_decision | JAP_the_peoples_state_decisions | GFX_decision_eng_propaganda_campaigns | 50 | yes |  | JAP.txt |
| JAP_establish_guerilla_units_in_state_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_military |  | yes |  | JAP.txt |
| JAP_move_the_capital_back_to_tokyo_decision | JAP_the_peoples_state_decisions | GFX_decision_eng_propaganda_campaigns | 15 | yes |  | JAP.txt |
| JAP_raid_an_infantry_weapons_depot_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_prepare_civil_war |  | yes |  | JAP.txt |
| JAP_raid_an_artillery_depot_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_industry |  | yes |  | JAP.txt |
| JAP_raid_a_truck_depot_decision | JAP_the_peoples_state_decisions | GFX_decision_generic_trucks |  | yes |  | JAP.txt |
| JAP_launch_an_offensive_in_core_state_decision | JAP_the_peoples_state_decisions | GFX_decision_border_war |  | yes |  | JAP.txt |
| JAP_organize_the_fifth_column_decision | JAP_the_peoples_state_decisions | generic_assassination |  | yes |  | JAP.txt |
| JAP_securing_control_over_osaka_mission | JAP_the_peoples_state_decisions | GFX_decision_gre_faction_management |  | yes |  | JAP.txt |
| JAP_army_politically_purging_disloyal_young_officers_mission | JAP_the_peoples_state_decisions | GFX_decision_SWE_set_army_budget |  | yes |  | JAP.txt |
| JAP_army_recruiting_more_conscripts_mission | JAP_the_peoples_state_decisions | GFX_decision_generic_military |  | yes |  | JAP.txt |
| JAP_army_broadcasting_militarist_propaganda_mission | JAP_the_peoples_state_decisions | GFX_decision_hol_radio_oranje |  | yes |  | JAP.txt |
| JAP_army_smuggling_kwantung_army_units_to_the_home_islands_mission | JAP_the_peoples_state_decisions | GFX_decision_infiltrate_state |  | yes |  | JAP.txt |
| JAP_tokko_arresting_anti_army_disidents_mission | JAP_the_peoples_state_decisions | GFX_decision_generic_arrest |  | yes |  | JAP.txt |
| JAP_army_securing_navy_support_mission | JAP_the_peoples_state_decisions | GFX_decision_SWE_set_navy_budget |  | yes |  | JAP.txt |
| JAP_army_ensuring_loyalty_within_the_regiments_mission | JAP_the_peoples_state_decisions | GFX_decision_generic_army_support |  | yes |  | JAP.txt |
| JAP_army_broadcasting_militarist_propaganda_2_mission | JAP_the_peoples_state_decisions | GFX_decision_hol_radio_oranje |  | yes |  | JAP.txt |
| JAP_army_securing_army_arsenals_mission | JAP_the_peoples_state_decisions | GFX_decision_generic_industry |  | yes |  | JAP.txt |
| JAP_industrial_investment_for_oil_decision | JAP_investing_in_foreign_industries_cat | GFX_decision_oil | 50 | yes |  | JAP.txt |
| JAP_industrial_investment_for_tungsten_decision | JAP_investing_in_foreign_industries_cat | GFX_decision_tungsten | 50 | yes |  | JAP.txt |
| JAP_industrial_investment_for_chromium_decision | JAP_investing_in_foreign_industries_cat | GFX_decision_chromium | 50 | yes |  | JAP.txt |
| JAP_industrial_investment_for_rubber_decision | JAP_investing_in_foreign_industries_cat | GFX_decision_rubber | 50 | yes |  | JAP.txt |
| JAP_attract_foreign_investments_decision | JAP_investing_in_foreign_industries_cat | GFX_decision_gre_investment_decisions | 75 |  |  | JAP.txt |
| JAP_west_pacific_treaty_org_trade_decision | JAP_west_pacific_treaty_org_allied_trade_cat | GFX_decision_eng_trade_unions_support | 25 | yes |  | JAP.txt |
| JAP_west_pacific_treaty_org_currency_union_decision | JAP_west_pacific_treaty_org_economic_integration_cat | GFX_decision_gre_investment_decisions | 15 | yes |  | JAP.txt |
| JAP_west_pacific_treaty_org_economic_integration_decision | JAP_west_pacific_treaty_org_economic_integration_cat | GFX_decision_eng_trade_unions_support | 25 | yes |  | JAP.txt |
| JAP_further_increase_froms_dependency_decision | JAP_west_pacific_treaty_org_economic_integration_cat | GFX_decision_eng_trade_unions_demand | 50 | yes |  | JAP.txt |
| JAP_annex_integrated_puppet_decision | JAP_west_pacific_treaty_org_economic_integration_cat | GFX_decision_eng_trade_unions_demand | 200 | yes |  | JAP.txt |
| JAP_democratic_core_asian_state | JAP_west_pacific_treaty_org_economic_integration_cat | GFX_decision_generic_form_nation | 50 | yes |  | JAP.txt |
| JAP_support_resistance_decision | JAP_anti_colonialism_category | GFX_decision_generic_nationalism |  | yes |  | JAP.txt |
| JAP_arm_resistance_decision | JAP_anti_colonialism_category | GFX_decision_generic_prepare_civil_war |  | yes |  | JAP.txt |
| JAP_expand_banner_recruitment | JAP_ashigaru_category | GFX_decision_generic_military |  |  |  | JAP.txt |
| JAP_raise_the_ashigaru | JAP_ashigaru_category | GFX_decision_generic_prepare_civil_war | 25 |  |  | JAP.txt |
| JAP_demobilize_the_ashigaru | JAP_ashigaru_category | GFX_decision_SWI_dismiss_council | 5 |  |  | JAP.txt |
| JAP_expand_boeitai_recruitment | JAP_boeitai_category | GFX_decision_generic_military |  |  |  | JAP.txt |
| JAP_raise_the_boeitai | JAP_boeitai_category | GFX_decision_generic_prepare_civil_war | 25 |  |  | JAP.txt |
| JAP_demobilize_the_boeitai | JAP_boeitai_category | GFX_decision_SWI_dismiss_council | 5 |  |  | JAP.txt |
| CHI_china_pledging_to_hold_state_mission | war_measures | GFX_decision_generic_prepare_civil_war |  |  |  | JAP.txt |
| BRM_blow_up_the_oil_fields | BRM_burmah_oils_oil_fields | GFX_decision_generic_ignite_civil_war | 25 |  |  | JAP.txt |
| BRM_repair_the_oil_fields | BRM_burmah_oils_oil_fields | GFX_decision_generic_construction | 25 |  |  | JAP.txt |
| KOR_regain_core_on_state_decision | foreign_politics | GFX_decision_infiltrate_state |  | yes |  | KOR.txt |
| recruit_in_europe | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_europe_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| recruit_in_north_america | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_north_america_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| recruit_in_south_america | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_south_america_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| recruit_in_africa | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_africa_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| recruit_in_middle_east | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_middle_east_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| recruit_in_asia | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_asia_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| recruit_in_australia | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_australia_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| recruit_in_india | lar_local_recruitment |  | 50 | yes |  | lar_agent_recruitment_decisions.txt |
| recruit_in_india_state | lar_local_recruitment | onmap_recruit_operative | 0 |  |  | lar_agent_recruitment_decisions.txt |
| LAT_perkonkrust_uprising | LAT_perkonkrust_revolt_category | GFX_decision_revolt |  | yes |  | LAT.txt |
| LAT_equality_campaigns | LAT_delay_perkonkrust_decisions |  | 50 |  |  | LAT.txt |
| LAT_empower_democrats | LAT_delay_perkonkrust_decisions |  |  | yes |  | LAT.txt |
| LAT_support_loyalists | LAT_delay_perkonkrust_decisions |  | 75 | yes |  | LAT.txt |
| LAT_promote_fascism | promote_baltic_fascism_cat | hol_draw_up_staff_plans | 50 |  |  | LAT.txt |
| LAT_promote_falange_militancy | promote_baltic_fascism_cat | hol_draw_up_staff_plans |  |  |  | LAT.txt |
| LAT_ignite_civil_war_in_target | promote_baltic_fascism_cat | hol_draw_up_staff_plans | 75 |  |  | LAT.txt |
| LIT_move_capital_to_vilnius | political_actions |  | 15 | yes |  | LIT.txt |
| LIT_adopt_the_dobuzhinsky_flag_design_decision | political_actions | GFX_decision_eng_trade_unions_support | 25 |  |  | LIT.txt |
| LIT_iron_wolf_partisans | LIT_iron_wolf_coup | ger_mefo_bills |  |  |  | LIT.txt |
| LIT_relocate_iron_wolf_recruitment | LIT_iron_wolf_appeasement |  |  | yes |  | LIT.txt |
| LIT_grant_concessions_to_iron_wolf | LIT_iron_wolf_appeasement |  |  | yes |  | LIT.txt |
| LIT_promote_fascism | support_polish_falange_decisions | hol_draw_up_staff_plans | 50 |  |  | LIT.txt |
| LIT_promote_falange_militancy | support_polish_falange_decisions | hol_draw_up_staff_plans |  |  |  | LIT.txt |
| LIT_ignite_civil_war_in_POL | support_polish_falange_decisions |  | 75 |  |  | LIT.txt |
| MAN_pacify_bandits_in_the_northern_countryside | MAN_banditry_category | GFX_decision_oppression | 0 |  |  | MAN_decisions.txt |
| MAN_hunt_down_northern_bandits | MAN_banditry_category | GFX_decision_generic_prepare_civil_war | 0 | yes |  | MAN_decisions.txt |
| MAN_maintain_northern_control | MAN_banditry_category | generic_civil_support |  |  |  | MAN_decisions.txt |
| MAN_pacify_bandits_in_the_eastern_countryside | MAN_banditry_category | GFX_decision_oppression | 0 |  |  | MAN_decisions.txt |
| MAN_hunt_down_eastern_bandits | MAN_banditry_category | GFX_decision_generic_prepare_civil_war | 0 | yes |  | MAN_decisions.txt |
| MAN_maintain_eastern_control | MAN_banditry_category | generic_civil_support |  |  |  | MAN_decisions.txt |
| MAN_pacify_bandits_in_the_western_countryside | MAN_banditry_category | GFX_decision_oppression | 0 |  |  | MAN_decisions.txt |
| MAN_hunt_down_western_bandits | MAN_banditry_category | GFX_decision_generic_prepare_civil_war | 0 | yes |  | MAN_decisions.txt |
| MAN_maintain_western_control | MAN_banditry_category | generic_civil_support |  |  |  | MAN_decisions.txt |
| MAN_bandit_raids | MAN_banditry_category | GFX_decision_generic_scorched_earth |  |  |  | MAN_decisions.txt |
| MAN_recruit_bandits_north | MAN_banditry_category | generic_civil_support | 50 |  |  | MAN_decisions.txt |
| MAN_recruit_bandits_west | MAN_banditry_category | generic_civil_support | 50 |  |  | MAN_decisions.txt |
| MAN_recruit_bandits_east | MAN_banditry_category | generic_civil_support | 50 |  |  | MAN_decisions.txt |
| MAN_recruit_bandits_generic | MAN_banditry_category | generic_civil_support | 50 | yes |  | MAN_decisions.txt |
| MAN_release_bandits | MAN_banditry_category | generic_civil_support | 0 |  |  | MAN_decisions.txt |
| MAN_recruit_bandits_2_north | MAN_banditry_category | generic_civil_support | 50 |  | No Compromise, No Surrender | MAN_decisions.txt |
| MAN_recruit_bandits_2_west | MAN_banditry_category | generic_civil_support | 50 |  | No Compromise, No Surrender | MAN_decisions.txt |
| MAN_recruit_bandits_2_east | MAN_banditry_category | generic_civil_support | 50 |  | No Compromise, No Surrender | MAN_decisions.txt |
| MAN_recruit_bandits_2_generic | MAN_banditry_category | generic_civil_support | 50 | yes | No Compromise, No Surrender | MAN_decisions.txt |
| MAN_release_bandits_2 | MAN_banditry_category | generic_civil_support | 10 |  |  | MAN_decisions.txt |
| MAN_raise_manchu_banner | MAN_war_preparations |  | 25 |  |  | MAN_decisions.txt |
| MAN_disband_the_banners | MAN_war_preparations |  | 0 |  |  | MAN_decisions.txt |
| MAN_fund_underground_gun_shops | MAN_war_preparations |  | 50 |  |  | MAN_decisions.txt |
| MAN_remove_underground_gun_shops | MAN_war_preparations |  | 0 |  |  | MAN_decisions.txt |
| MAN_divert_machine_tools | MAN_war_preparations |  | 50 |  |  | MAN_decisions.txt |
| MAN_prepare_to_seize_arms | MAN_war_preparations |  | 0 |  |  | MAN_decisions.txt |
| MAN_seize_arms | MAN_war_preparations |  | 0 | yes | No Step Back | MAN_decisions.txt |
| MAN_develop_kirin_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | MAN_decisions.txt |
| MAN_develop_liaotung_iron_ore_deposits | prospect_for_resources | steel | 25 | yes |  | MAN_decisions.txt |
| MAN_establish_the_erdaojiang_special_steel_experimental_plant | prospect_for_resources | steel | 25 | yes |  | MAN_decisions.txt |
| MAN_coring_outer_manchuria_states | MAN_coring_decisions | GFX_decision_generic_form_nation | 50 | yes |  | MAN_decisions.txt |
| MAN_coring_mongolia_tuva | MAN_coring_decisions | GFX_decision_generic_form_nation | 50 | yes |  | MAN_decisions.txt |
| MAN_coring_tibet | MAN_coring_decisions | GFX_decision_generic_form_nation | 50 | yes |  | MAN_decisions.txt |
| MAN_coring_democratic | MAN_coring_decisions | GFX_decision_generic_form_nation | 50 | yes |  | MAN_decisions.txt |
| MAN_import_imperial_way_buddhism_decision | MAN_state_shintoism_decisions | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | MAN_decisions.txt |
| MAN_one_people_united_under_shinto_decision | MAN_state_shintoism_decisions | GFX_decision_generic_civil_support | 50 | yes |  | MAN_decisions.txt |
| MAN_incoporate_manchu_nationalism_decision | MAN_state_shintoism_decisions | GFX_decision_eng_blackshirt_speech | 50 | yes |  | MAN_decisions.txt |
| MAN_state_shinto_in_education_decision | MAN_state_shintoism_decisions | GFX_decision_SOV_academy_of_sciences | 75 | yes |  | MAN_decisions.txt |
| MAN_march_on_hebei_chahar | MAN_march_on_beijing_decisions | border_war | 25 | yes |  | MAN_decisions.txt |
| MAN_march_on_hebei_chahar_mission | MAN_march_on_beijing_decisions | border_war |  |  |  | MAN_decisions.txt |
| MAN_march_on_beijing | MAN_march_on_beijing_decisions | border_war | 25 | yes |  | MAN_decisions.txt |
| MAN_march_on_beijing_mission | MAN_march_on_beijing_decisions | border_war |  |  |  | MAN_decisions.txt |
| MAN_march_on_hebei | MAN_march_on_beijing_decisions | border_war | 25 | yes |  | MAN_decisions.txt |
| MAN_march_on_hebei_mission | MAN_march_on_beijing_decisions | border_war |  |  |  | MAN_decisions.txt |
| MAN_request_full_control_over_china | MAN_china_matters | GFX_decision_jap_conquer_china | 150 | yes |  | MAN_decisions.txt |
| MAN_unify_with_specific_japanese_puppet_decision | MAN_china_matters | GFX_decision_border_war | 75 |  |  | MAN_decisions.txt |
| MAN_warlord_autonomy_drift_decision | MAN_china_matters | GFX_decision_eng_trade_unions_support |  |  |  | MAN_decisions.txt |
| MAN_expand_yong_ying_recruitment | MAN_yong_ying_category | GFX_decision_generic_military |  |  |  | MAN_decisions.txt |
| MAN_raise_the_yong_ying | MAN_yong_ying_category | GFX_decision_generic_prepare_civil_war | 25 |  |  | MAN_decisions.txt |
| MAN_demobilize_the_yong_ying | MAN_yong_ying_category | GFX_decision_SWI_dismiss_council | 5 |  |  | MAN_decisions.txt |
| MEN_core_state | foreign_politics | GFX_decision_infiltrate_state | 25 | yes |  | MEN.txt |
| MEN_expand_banner_recruitment | MEN_mongol_banner_category | GFX_decision_generic_reorganize_irregulars |  |  | No Compromise, No Surrender | MEN.txt |
| MEN_raise_the_banners | MEN_mongol_banner_category | GFX_decision_generic_prepare_civil_war | 75 |  | No Compromise, No Surrender | MEN.txt |
| MEN_demobilize_the_banners | MEN_mongol_banner_category | GFX_decision_SWI_dismiss_council | 5 |  | No Compromise, No Surrender | MEN.txt |
| MEN_move_the_capital_to_zhangbei_decision | political_actions | GFX_decision_eng_trade_unions_support | 75 | yes |  | MEN.txt |
| MEN_move_the_capital_to_kalgan_decision | political_actions | GFX_decision_eng_trade_unions_support | 75 | yes |  | MEN.txt |
| MEN_request_initiation_of_the_suiyuan_campaign_decision | political_actions | GFX_decision_border_war | 50 | yes |  | MEN.txt |
| MEN_army_reform_decision | MEN_army_reform | generic_prepare_civil_war | 0 |  | No Compromise, No Surrender | MEN.txt |
| MEX_join_mexican_faction | foreign_politics | generic_civil_support |  | yes |  | MEX.txt |
| MEX_mission_cedillos_rebellion | MEX_category_military_issues | generic_civil_support |  |  |  | MEX.txt |
| MEX_mission_second_cristiada | MEX_category_military_issues | generic_civil_support |  |  |  | MEX.txt |
| MEX_mission_second_cristiada_dummy | MEX_category_military_issues | generic_civil_support |  |  |  | MEX.txt |
| MEX_mission_second_revolution | MEX_category_military_issues | generic_civil_support |  |  |  | MEX.txt |
| MEX_mission_second_revolution_dummy | MEX_category_military_issues | generic_civil_support |  |  |  | MEX.txt |
| MEX_decision_operation_just_cause | MEX_category_military_issues | generic_nationalism | 25 | yes |  | MEX.txt |
| MEX_decision_support_spanish_loyalists | MEX_category_military_issues | generic_nationalism |  |  |  | MEX.txt |
| MEX_decision_support_spanish_fascists | MEX_category_military_issues | generic_nationalism |  |  |  | MEX.txt |
| MEX_decision_interior_defence_plan | MEX_category_military_issues | generic_operation |  | yes |  | MEX.txt |
| MEX_decision_coastal_defence_plan | MEX_category_military_issues | generic_operation |  | yes |  | MEX.txt |
| MEX_decision_integrate_guatamala | MEX_category_territorial_integration | generic_nationalism | 50 |  |  | MEX.txt |
| MEX_decision_integrate_honduras | MEX_category_territorial_integration | generic_nationalism | 50 |  |  | MEX.txt |
| MEX_decision_integrate_el_salvador | MEX_category_territorial_integration | generic_nationalism | 50 |  |  | MEX.txt |
| MEX_decision_integrate_nicaragua | MEX_category_territorial_integration | generic_nationalism | 50 |  |  | MEX.txt |
| MEX_decision_integrate_costa_rica | MEX_category_territorial_integration | generic_nationalism | 50 |  |  | MEX.txt |
| MEX_decision_integrate_panama | MEX_category_territorial_integration | generic_nationalism | 50 |  |  | MEX.txt |
| MEX_decision_integrate_panama_canal | MEX_category_territorial_integration | generic_nationalism | 25 |  |  | MEX.txt |
| MEX_decision_integrate_belize | MEX_category_territorial_integration | generic_nationalism | 25 |  |  | MEX.txt |
| MEX_decision_integrate_cuba | MEX_category_territorial_integration | generic_nationalism | 25 |  |  | MEX.txt |
| MEX_decision_integrate_haiti | MEX_category_territorial_integration | generic_nationalism | 25 |  |  | MEX.txt |
| MEX_decision_integrate_the_dominican_republic | MEX_category_territorial_integration | generic_nationalism | 25 |  |  | MEX.txt |
| MEX_decision_transfer_lands_to_church | MEX_category_church_power | generic_operation | 75 |  |  | MEX.txt |
| MEX_decision_nationalize_church_lands | MEX_category_church_power | generic_scorched_earth | 75 |  |  | MEX.txt |
| MEX_decision_pardon_cristero_fighter | MEX_category_church_power | generic_army_support | 75 |  |  | MEX.txt |
| MEX_decision_assassinate_cristero_traitor | MEX_category_church_power | generic_prepare_civil_war | 75 |  |  | MEX.txt |
| MEX_decision_attend_public_mass | MEX_category_church_power | generic_nationalism | 75 |  |  | MEX.txt |
| MEX_decision_prosecute_clergyman | MEX_category_church_power | oppression | 75 |  |  | MEX.txt |
| MEX_decision_reconciliation_committee | MEX_category_church_power | generic_political_discourse | 25 |  |  | MEX.txt |
| MEX_decision_incite_tensions | MEX_category_church_power | generic_break_treaty | 25 |  |  | MEX.txt |
| MEX_decision_invite_tag_to_the_hispanic_alliance | MEX_category_hispanic_solidarity | generic_political_discourse | 25 |  |  | MEX.txt |
| rename_ulanbaatar_monarchist_decision | political_actions | GFX_decision_eng_trade_unions_support | 25 | yes |  | MON.txt |
| rename_ulanbaatar_non_monarchist_decision | political_actions | GFX_decision_eng_trade_unions_support | 25 | yes |  | MON.txt |
| reorganize_manchuria_decision | political_actions | GFX_decision_eng_trade_unions_support | 25 | yes |  | MON.txt |
| USA_small_lobby_effort | USA_congress | generic_political_discourse | 0 |  |  | MTG_congress.txt |
| USA_medium_lobby_effort | USA_congress | generic_political_discourse | 0 |  |  | MTG_congress.txt |
| USA_special_measures | USA_congress | ger_mefo_bills | 50 |  |  | MTG_congress.txt |
| USA_use_huac | USA_congress | oppression | 10 |  |  | MTG_congress.txt |
| USA_beat_up_opposition | USA_congress | oppression | 10 |  |  | MTG_congress.txt |
| USA_pay_farm_subsidies | USA_congress | ger_mefo_bills | 0 |  |  | MTG_congress.txt |
| USA_give_tax_break | USA_congress | ger_mefo_bills | 0 |  |  | MTG_congress.txt |
| USA_amend_the_budget | USA_congress | ger_mefo_bills | 25 |  |  | MTG_congress.txt |
| USA_research_grants | USA_congress | ger_mefo_bills | 25 |  |  | MTG_congress.txt |
| USA_invest_in_state_factory | USA_congress | generic_construction |  |  |  | MTG_congress.txt |
| USA_invest_in_state_arms_factory | USA_congress | generic_construction |  |  |  | MTG_congress.txt |
| USA_invest_in_state_dockyard | USA_congress | generic_construction |  |  |  | MTG_congress.txt |
| USA_invest_in_state_infrastructure | USA_congress | generic_construction |  |  |  | MTG_congress.txt |
| USA_statehood_for_alaska | USA_congress | infiltrate_state | 25 | yes |  | MTG_congress.txt |
| USA_statehood_for_hawaii | USA_congress | infiltrate_state | 25 | yes |  | MTG_congress.txt |
| USA_statehood_for_puerto_rico | USA_congress | infiltrate_state | 25 | yes |  | MTG_congress.txt |
| USA_readmit_state | USA_congress | infiltrate_state | 25 |  |  | MTG_congress.txt |
| USA_reshuffle_congress | USA_congress |  | 50 |  |  | MTG_congress.txt |
| MTG_abandon_treaty_democratic | MTG_naval_treaties | generic | 150 | yes |  | MTG_naval_treaty.txt |
| MTG_abandon_treaty_fascist | MTG_naval_treaties | generic | 25 | yes |  | MTG_naval_treaty.txt |
| MTG_abandon_treaty_japanese | MTG_naval_treaties | generic | 25 | yes |  | MTG_naval_treaty.txt |
| MTG_cheat_on_treaty | MTG_naval_treaties | generic | 50 | yes |  | MTG_naval_treaty.txt |
| MTG_invite_FROM_to_treaty | MTG_naval_treaties | generic_naval | 50 | yes |  | MTG_naval_treaty.txt |
| MTG_send_treaty_warning_to_FROM_previous_signatory | MTG_naval_treaties | generic_naval | 50 | yes |  | MTG_naval_treaty.txt |
| MTG_send_treaty_warning_to_FROM | MTG_naval_treaties | generic_naval | 50 | yes |  | MTG_naval_treaty.txt |
| MTG_treaty_reduction_mission | MTG_naval_treaties | generic_naval |  |  |  | MTG_naval_treaty.txt |
| MTG_treaty_reduction_signatory_mission | MTG_naval_treaties | generic_naval |  |  |  | MTG_naval_treaty.txt |
| MTG_treaty_renew_mission | MTG_naval_treaties | generic_naval |  |  |  | MTG_naval_treaty.txt |
| MTG_escalator_clause_invocation_mission | MTG_naval_treaties | generic_naval |  |  |  | MTG_naval_treaty.txt |
| NATO_brussels_treaty | nato_decisions | generic_formable_nations | 25 | yes |  | NATO.txt |
| NATO_suggest_nato | nato_decisions | generic_formable_nations | 25 | yes |  | NATO.txt |
| NOR_add_to_faction | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_remove_all_convoys | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_reset_prep | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| debug_num_convoys | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_debug_add_convoys | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| start_dem_prep | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_start_allied_prep | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| start_comm_prep | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_start_mon_prep | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_start_fas_prep | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| start_defensive_war | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_stop_the_war | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_prep_all_states | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_test_fascist_civil_war | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_test_communist_civil_war | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_debug_nordic_tack | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_debug_vanilla_tack | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_open_NORDIC_debug | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_send_event | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_check_hydro | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_test_mobile_gov | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_test_exile | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_generate_militias | NOR_debug_decisions_category |  |  |  |  | NOR.txt |
| NOR_request_reinstatement | NOR_exile_decisions_category | generic_independence |  |  |  | NOR.txt |
| NOR_lobby_for_parliamentary_support | NOR_exile_decisions_category | eng_install_government |  |  |  | NOR.txt |
| NOR_bring_soldiers_from_norway | NOR_exile_decisions_category | eng_propaganda_campaigns |  |  |  | NOR.txt |
| NOR_weapons_for_the_resistance | NOR_exile_decisions_category | generic_ignite_civil_war |  |  |  | NOR.txt |
| NOR_unity_parade | NOR_exile_decisions_category | generic_nationalism |  | yes |  | NOR.txt |
| NOR_joint_training_exercise | NOR_exile_decisions_category | eng_blackshirt_march |  |  |  | NOR.txt |
| NOR_expand_industrial_capacity | NOR_exile_decisions_category | ger_military_buildup |  |  |  | NOR.txt |
| NOR_foment_resistance_in_state | NOR_exile_decisions_category | GFX_decision_generic_civil_support |  |  |  | NOR.txt |
| NOR_support_rebellion | NOR_exile_decisions_category | GFX_decision_revolt |  | yes |  | NOR.txt |
| NOR_prepare_state_historical | NOR_democratic_preparation_decisions_category | { | 30 |  |  | NOR.txt |
| NOR_focus_on_training | NOR_democratic_preparation_decisions_category |  | 50 |  |  | NOR.txt |
| NOR_public_investment_drive | NOR_democratic_preparation_decisions_category |  | 50 |  |  | NOR.txt |
| NOR_modernize_armed_forces_decision | NOR_democratic_preparation_decisions_category |  |  |  |  | NOR.txt |
| NOR_naval_expanion | NOR_democratic_preparation_decisions_category |  | 50 |  |  | NOR.txt |
| NOR_modernize_armed_forces_decision_wartime | NOR_historical_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_deploy_state_preparation_historical | NOR_historical_deploy_prep_decisions_category | { |  |  |  | NOR.txt |
| NOR_prepare_exile | NOR_historical_deploy_prep_decisions_category | GFX_decision_hol_draw_up_staff_plans |  |  |  | NOR.txt |
| NOR_move_government_headquarters_decision | NOR_historical_deploy_prep_decisions_category |  | 10 |  |  | NOR.txt |
| NOR_expedite_training | NOR_historical_deploy_prep_decisions_category | GFX_decision_generic_prepare_civil_war |  |  |  | NOR.txt |
| NOR_dem_his_integrate_militias | NOR_historical_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_prepare_state_alt_dem | NOR_allied_democratic_preparation_decisions_category | { |  |  |  | NOR.txt |
| NOR_alt_dem_naval_expansion | NOR_allied_democratic_preparation_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_military_industry_expansion | NOR_allied_democratic_preparation_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_economic_relief_measures | NOR_allied_democratic_preparation_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_modernize_armed_forces_decision | NOR_allied_democratic_preparation_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_focus_on_training | NOR_allied_democratic_preparation_decisions_category |  | 50 |  |  | NOR.txt |
| NOR_alt_dem_public_investment_drive | NOR_allied_democratic_preparation_decisions_category |  | 50 |  |  | NOR.txt |
| NOR_alt_dem_modernize_armed_forces_decision_wartime | NOR_allied_democratic_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_expedite_training | NOR_allied_democratic_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_prioritize_production | NOR_allied_democratic_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_offensive_push | NOR_allied_democratic_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_focus_on_defense | NOR_allied_democratic_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_alt_dem_integrate_militias | NOR_allied_democratic_deploy_prep_decisions_category |  |  |  |  | NOR.txt |
| NOR_prepare_state_fascist | NOR_fascist_preparation_decisions_category | { |  |  |  | NOR.txt |
| NOR_invite_fascist_to_invade | NOR_fascist_preparation_decisions_category |  |  |  |  | NOR.txt |
| NOR_deploy_state_preparation_fascist | NOR_fascist_deploy_prep_decisions_category | { |  |  |  | NOR.txt |
| NOR_prepare_state_communist | NOR_communist_preparation_decisions_category | { | 25 |  |  | NOR.txt |
| NOR_communist_propaganda_campaign | NOR_communist_preparation_decisions_category | GFX_decision_eng_propaganda_campaigns | 50 |  |  | NOR.txt |
| NOR_prepare_state_monarchist | NOR_monarchist_preparation_decisions_category | { |  |  |  | NOR.txt |
| NOR_prop_up_the_economy | NOR_monarchist_preparation_decisions_category | GFX_decision_generic_consumer_goods | 40 |  |  | NOR.txt |
| NOR_make_assurances_to_the_people | NOR_monarchist_preparation_decisions_category | GFX_decision_generic_political_address | 50 |  |  | NOR.txt |
| NOR_promote_the_armed_defense_of_the_country | NOR_monarchist_preparation_decisions_category | GFX_decision_generic_protection | 50 |  |  | NOR.txt |
| refit_to_destroyer_nor | economy_decisions | GFX_decision_generic_merge_plant_ship |  |  | Man the Guns | NOR.txt |
| refit_to_destroyer_mass_nor | economy_decisions | GFX_decision_generic_merge_plant_ship |  |  | Man the Guns | NOR.txt |
| NORDIC_remove_all_nordic_stuff | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_toggle_SOV_fin_war | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_increase_participation | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_reset_participation | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_test_array_adding | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_increase_conflict_scale | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_create_democratic_alliance | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_create_commmunist_alliance | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_create_monarchist_alliance | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_show_all_capstones | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_reload_JFT | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_test_platonics | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_test_cooperation_decisions | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_test_on_remove | NORDIC_debug_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_promote_nordic_unity | NORDIC_cooperation_decisions_category |  | 40 |  |  | NORDIC.txt |
| NORDIC_strenghten_ties_decision | NORDIC_cooperation_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_invest_in_nordic | NORDIC_cooperation_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_ask_for_investment_to_nordic | NORDIC_cooperation_decisions_category |  | 50 |  |  | NORDIC.txt |
| NORDIC_economic_cooperation_decisions | NORDIC_cooperation_decisions_category |  | 60 |  |  | NORDIC.txt |
| NORDIC_court_foreign_power | NORDIC_cooperation_decisions_category |  | 100 |  |  | NORDIC.txt |
| NORDIC_decision_limited_war_participation | NORDIC_cooperation_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_decision_risky_war_participation | NORDIC_cooperation_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_decision_dangerous_war_participation | NORDIC_cooperation_decisions_category |  |  |  |  | NORDIC.txt |
| NORDIC_defend_nordic_country | NORDIC_cooperation_decisions_category |  | 100 |  |  | NORDIC.txt |
| NORDIC_send_weapons | NORDIC_cooperation_decisions_category |  | 100 |  |  | NORDIC.txt |
| NORDIC_send_volunteers | NORDIC_cooperation_decisions_category |  | 100 |  |  | NORDIC.txt |
| NORDIC_expand_volunteer_program | NORDIC_cooperation_decisions_category |  | 100 |  |  | NORDIC.txt |
| NORDIC_expand_air_support | NORDIC_cooperation_decisions_category |  | 100 |  |  | NORDIC.txt |
| OMA_restore_order_in_the_interior | political_actions | GFX_decision_oppression | 75 |  |  | OMA.txt |
| OMA_establih_the_sultanate_of_oman | political_actions | GFX_decision_eng_trade_unions_support | 100 | yes |  | OMA.txt |
| PER_sell_oil | PER_profit_from_war_category |  | 0 | yes |  | PER.txt |
| PER_core_conquered_state | PER_integrate_anatolia_decisions_category | GFX_decision_generic_form_nation | 75 | yes |  | PER.txt |
| PER_core_byzantium_state | PER_absorb_byzantines_category | GFX_decision_generic_form_nation | 75 | yes |  | PER.txt |
| PER_core_egypt_state | PER_memphis_initiative_category | GFX_decision_generic_form_nation | 75 | yes |  | PER.txt |
| PER_civil_war_imminent | PER_civil_unrest_category | GFX_decision_revolt |  | yes |  | PER.txt |
| PER_dissolve_parliament | PER_civil_unrest_category | GFX_decision_generic_political_discourse | 100 | yes |  | PER.txt |
| PER_stabilize_economy | PER_civil_unrest_category | GFX_decision_generic_industry | 80 | yes |  | PER.txt |
| PER_prepare_military | PER_civil_unrest_category | GFX_decision_generic_prepare_civil_war | 40 | yes |  | PER.txt |
| PER_organize_protest_in_state | PER_mass_protests | GFX_decision_eng_blackshirt_march | 30 | yes |  | PER.txt |
| PER_establish_cells | PER_mass_protests | GFX_decision_revolt |  | yes |  | PER.txt |
| PER_establish_opposition_hq | PER_mass_protests | GFX_decision_revolt | 10 | yes |  | PER.txt |
| PER_boost_war_support | PER_national_iranian_radio | GFX_decision_generic_military | 30 |  |  | PER.txt |
| PER_promote_communism | PER_national_iranian_radio | GFX_decision_SOV_secure_the_administration | 30 |  |  | PER.txt |
| PER_boost_stability | PER_national_iranian_radio | GFX_decision_generic_political_address | 30 |  |  | PER.txt |
| PER_support_kurds_in_iraq | PER_gulf_decisions_cat | GFX_decision_generic_civil_support |  |  |  | PER.txt |
| PER_send_weapons_to_kurds | PER_gulf_decisions_cat | GFX_decision_generic_prepare_civil_war |  |  |  | PER.txt |
| PER_kurdish_revolt_mission | PER_gulf_decisions_cat | generic_ignite_civil_war |  |  |  | PER.txt |
| PER_pashtuns_in_pakistan | PER_gulf_decisions_cat | GFX_decision_generic_civil_support |  |  |  | PER.txt |
| PER_promote_resistance_in_gulf_states | PER_gulf_decisions_cat | GFX_decision_generic_civil_support |  |  |  | PER.txt |
| PER_clampdown_on_resistance | PER_anti_gulf_decisions_cat | GFX_decision_generic_civil_support |  | yes |  | PER.txt |
| PER_organize_resistance | PER_plant_resistance_cat | GFX_decision_generic_civil_support |  |  |  | PER.txt |
| PER_kur_azr_revolt_mission | PER_kur_azr_independence_cat | generic_ignite_civil_war |  |  |  | PER.txt |
| PHI_american_intervention_declare_war_mission | PHI_american_intervention_category | GFX_decision_generic_prepare_civil_war |  | yes |  | PHI.txt |
| PHI_american_intervention_donate_us_senate | PHI_american_intervention_category | GFX_decision_hol_exchange_intelligence_data | 75 |  |  | PHI.txt |
| PHI_american_intervention_ban_communist_paper | PHI_american_intervention_category | GFX_decision_generic_police_action | 25 |  |  | PHI.txt |
| PHI_american_intervention_forbid_advisor | PHI_american_intervention_category | GFX_decision_generic_arrest | 25 | yes |  | PHI.txt |
| PHI_american_intervention_promise_bases | PHI_american_intervention_category | GFX_decision_SWE_set_army_budget | 100 | yes |  | PHI.txt |
| PHI_american_intervention_host_training_exercise | PHI_american_intervention_category | GFX_decision_generic_military |  | yes |  | PHI.txt |
| PHI_american_intervention_invite_us_communists | PHI_american_intervention_category | GFX_decision_generic_political_rally | 15 | yes |  | PHI.txt |
| PHI_american_intervention_nationalize_railways | PHI_american_intervention_category | GFX_decision_generic_construction | 45 | yes |  | PHI.txt |
| PHI_american_intervention_nationalize_industries | PHI_american_intervention_category | GFX_decision_generic_factory | 55 | yes |  | PHI.txt |
| PHI_american_intervention_recognize_unions | PHI_american_intervention_category | GFX_decision_generic_political_rally | 50 | yes |  | PHI.txt |
| PHI_mineral_prospecting_chromium_small_decision | prospect_for_resources | chromium | 25 | yes |  | PHI.txt |
| PHI_mineral_prospecting_chromium_large_decision | prospect_for_resources | chromium | 25 | yes |  | PHI.txt |
| PHI_mineral_prospecting_steel_repeatable_decision_1 | prospect_for_resources | steel | 25 | yes |  | PHI.txt |
| PHI_mineral_prospecting_steel_repeatable_decision_2 | prospect_for_resources | steel | 50 | yes |  | PHI.txt |
| PHI_convoys_for_infastructure_decision | PHI_convoys_for_infrastructure_decision_cat | GFX_decision_generic_naval |  | yes |  | PHI.txt |
| PHI_convoys_for_consumer_goods | PHI_convoys_for_infrastructure_decision_cat |  |  | yes | Arms Against Tyranny | PHI.txt |
| PHI_convoys_for_guns | PHI_convoys_for_infrastructure_decision_cat | generic_prepare_civil_war |  | yes |  | PHI.txt |
| PHI_convoys_for_trucks | PHI_convoys_for_infrastructure_decision_cat | GFX_decision_generic_trucks |  | yes |  | PHI.txt |
| PHI_convoys_for_artillery | PHI_convoys_for_infrastructure_decision_cat | ger_military_buildup |  | yes |  | PHI.txt |
| PHI_convoys_for_light_tanks | PHI_convoys_for_infrastructure_decision_cat | GFX_decision_generic_tank |  | yes | No Step Back | PHI.txt |
| PHI_sugar_excise_general | PHI_sugar_barons_category |  | 50 | yes |  | PHI.txt |
| PHI_sugar_excise_divisions | PHI_sugar_barons_category |  | 50 | yes |  | PHI.txt |
| PHI_integrate_conquests | PHI_integration_category | GFX_decision_infiltrate_state | 15 | yes |  | PHI.txt |
| PHI_create_faction | PHI_department_of_foreign_affairs_category | GFX_decision_generic_form_nation | 50 | yes |  | PHI.txt |
| PHI_decrease_japanese_ideological_influence | PHI_department_of_foreign_affairs_category | GFX_decision_generic_form_nation | 75 |  |  | PHI.txt |
| PHI_join_other_faction | PHI_department_of_foreign_affairs_category |  | 10 | yes |  | PHI.txt |
| PHI_request_equipment | PHI_government_in_exile_cat | GFX_decision_generic_industry | 50 |  |  | PHI.txt |
| PHI_share_military_experience | PHI_government_in_exile_cat | GFX_decision_hol_exchange_intelligence_data | 50 | yes |  | PHI.txt |
| PHI_peace_with_philippines | political_actions | GFX_decision_eng_trade_unions_support | 25 |  |  | PHI.txt |
| PHI_defend_against_USA | political_actions | generic_operation |  |  |  | PHI.txt |
| PHI_request_indefinite_stay_for_macarthur | political_actions |  | 35 | yes |  | PHI.txt |
| PHI_recall_eisenhower | political_actions |  | 15 | yes |  | PHI.txt |
| PHI_recall_macarthur | political_actions |  |  | yes |  | PHI.txt |
| USA_execute_war_plan_brown | USA_war_plans | generic_operation |  |  |  | PHI.txt |
| PHI_investment_plan_1 | economy_decisions |  |  |  |  | PHI.txt |
| PHI_investment_plan_2 | economy_decisions |  |  |  |  | PHI.txt |
| PHI_investment_plan_3 | economy_decisions |  |  |  |  | PHI.txt |
| PHI_establish_reserve_transport_fleet | economy_decisions | GFX_decision_generic_merge_plant_ship |  |  |  | PHI.txt |
| PHI_establish_new_train_connections | economy_decisions | GFX_decision_generic_train |  |  |  | PHI.txt |
| PHI_inspect_road_network | economy_decisions | GFX_decision_generic_trucks |  |  |  | PHI.txt |
| PHI_propose_treaty_of_mutual_assistance | PHI_relations_with_spanish_america |  | 35 | yes |  | PHI.txt |
| PHI_propose_unification | PHI_relations_with_spanish_america |  | 50 | yes | La Resistance | PHI.txt |
| PHI_force_unification | PHI_relations_with_spanish_america |  | 25 | yes | La Resistance | PHI.txt |
| POL_unification_propaganda | POL_danzig_decisions | infiltrate_state | 75 |  |  | POL.txt |
| POL_military_appeasement | POL_danzig_decisions | infiltrate_state |  |  |  | POL.txt |
| POL_raid_nazi_resistance | POL_danzig_decisions | infiltrate_state |  |  |  | POL.txt |
| POL_tighten_control | POL_danzig_decisions | infiltrate_state |  |  |  | POL.txt |
| POL_sanation_left_irritation | POL_sanation_decisions | { |  | yes |  | POL.txt |
| POL_sanation_right_irritation | POL_sanation_decisions | { |  | yes |  | POL.txt |
| POL_sideline_the_left | POL_sanation_decisions | infiltrate_state | 100 |  |  | POL.txt |
| POL_sideline_the_right | POL_sanation_decisions | infiltrate_state | 100 |  |  | POL.txt |
| POL_looming_peasants_strike_mission | POL_peasant_strike_category | POL_looming_peasants_strike |  | yes |  | POL.txt |
| POL_peasants_strike | POL_peasant_strike_category | POL_organize_strike_two |  | yes |  | POL.txt |
| POL_crackdown_in_lviv | POL_peasant_strike_category | GFX_decision_oppression | 100 | yes |  | POL.txt |
| POL_pacify_zamosc | POL_peasant_strike_category | GFX_decision_oppression | 90 | yes |  | POL.txt |
| POL_pacify_peasants_repeatable | POL_peasant_strike_category | GFX_decision_oppression | 80 |  |  | POL.txt |
| POL_escelate_the_strike | POL_organize_the_peasants_strike | infiltrate_state |  |  |  | POL.txt |
| POL_woo_military_staff | POL_organize_the_peasants_strike | infiltrate_state |  |  |  | POL.txt |
| POL_seize_equipment | POL_organize_the_peasants_strike | infiltrate_state |  |  |  | POL.txt |
| POL_add_state_to_strike | POL_organize_the_peasants_strike | { |  |  |  | POL.txt |
| POL_expand_strikes_to_factories | POL_organize_the_peasants_strike | infiltrate_state | 50 |  |  | POL.txt |
| POL_invite_ford | POL_invite_foreign_motor_decisions | infiltrate_state | 0 | yes | Arms Against Tyranny | POL.txt |
| POL_invite_vauxhall | POL_invite_foreign_motor_decisions | infiltrate_state | 0 | yes | Arms Against Tyranny | POL.txt |
| POL_invite_somua | POL_invite_foreign_motor_decisions | infiltrate_state | 0 | yes | Arms Against Tyranny | POL.txt |
| POL_diplomatic_mission_to_FIN | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_DEN | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_NOR | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_SWE | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_CZE | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_YUG | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_AUS | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_HUN | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_GRE | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_TUR | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_diplomatic_mission_to_ITA | POL_miedzymorze_decisions | infiltrate_state | 10 | yes |  | POL.txt |
| POL_defend_in_east_state | POL_defensive_plans | hol_draw_up_staff_plans | 50 |  |  | POL.txt |
| POL_defend_in_west_state | POL_defensive_plans | hol_draw_up_staff_plans | 50 |  |  | POL.txt |
| POL_purchase_madagascar | POL_reopen_the_maritime_and_colonial_league | decision_generic_nationalism |  | yes |  | POL.txt |
| POL_purchase_gambia | POL_reopen_the_maritime_and_colonial_league | decision_generic_nationalism |  | yes |  | POL.txt |
| POL_purchase_cheap_colony | POL_reopen_the_maritime_and_colonial_league | decision_generic_nationalism |  | yes |  | POL.txt |
| POL_anti_capitalist_revolution | POL_anti_capitalist_decisions | decision_generic_nationalism |  |  |  | POL.txt |
| POL_anti_fascist_military | POL_anti_fascist_revolution_category | decision_generic_nationalism |  |  |  | POL.txt |
| POL_propagandise_monarchist_sentiment | POL_support_monarchy_in_LIT_cat | eng_propaganda_campaigns | 50 |  |  | POL.txt |
| POL_double_propagandise_monarchist_sentiment | POL_support_monarchy_in_LIT_cat | decision_generic_nationalism | 100 |  |  | POL.txt |
| POL_sway_lithuanian_generals | POL_support_monarchy_in_LIT_cat | generic_army_support |  |  |  | POL.txt |
| POL_invest_in_lithuania | POL_support_monarchy_in_LIT_cat | generic_construction |  |  |  | POL.txt |
| POL_arm_monarchist_militants | POL_support_monarchy_in_LIT_cat | generic_prepare_civil_war |  |  |  | POL.txt |
| POL_suppress_monarchist_sentiment | POL_fight_against_monarchy_in_LIT_cat | decision_generic_nationalism | 50 |  |  | POL.txt |
| POL_ban_monarchist_propaganda | POL_fight_against_monarchy_in_LIT_cat | decision_generic_nationalism | 50 |  |  | POL.txt |
| POL_root_out_monarchists | POL_fight_against_monarchy_in_LIT_cat | generic_prepare_civil_war |  |  |  | POL.txt |
| POL_anti_monarchist_purge | POL_fight_against_monarchy_in_LIT_cat | decision_generic_nationalism |  |  |  | POL.txt |
| POL_ban_polish_imports | POL_fight_against_monarchy_in_LIT_cat | generic_break_treaty |  |  |  | POL.txt |
| POL_skirmish_with_monarchist_militants | POL_fight_against_monarchy_in_LIT_cat | generic_prepare_civil_war |  |  |  | POL.txt |
| POL_monarchist_civil_war | POL_fight_against_monarchy_in_LIT_cat | generic_ignite_civil_war | 50 | yes |  | POL.txt |
| POL_ban_monarchists | POL_fight_against_monarchy_in_LIT_cat | eng_propaganda_campaigns | 100 | yes |  | POL.txt |
| POL_restore_don_cossacks | POL_cossack_republic_decisions | generic_form_nation | 100 | yes |  | POL.txt |
| POL_restore_kuban_cossacks | POL_cossack_republic_decisions | generic_form_nation | 100 | yes |  | POL.txt |
| POL_nationwide_fascist_displays | POL_sanacja_falanga_decisions | decision_generic_nationalism | 50 |  |  | POL.txt |
| POL_appoint_nationalist_ministers | POL_sanacja_falanga_decisions | decision_generic_nationalism | 50 |  |  | POL.txt |
| POL_promote_falangism | POL_promote_falangism_decisions | hol_draw_up_staff_plans | 50 |  |  | POL.txt |
| POL_promote_falangism_in_major | POL_promote_falangism_decisions | hol_draw_up_staff_plans | 100 |  |  | POL.txt |
| prepare_for_fascist_civil_war | fascism_on_the_rise | generic_prepare_civil_war | 50 | yes |  | political_decisions.txt |
| expand_civil_fascism_support | fascism_on_the_rise | generic_civil_support | 25 |  |  | political_decisions.txt |
| army_support_for_fascist_civil_war | fascism_on_the_rise | generic_army_support | 50 |  |  | political_decisions.txt |
| ensure_general_loyalty_for_fascist_civil_war | fascism_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| ensure_marshal_loyalty_for_fascist_civil_war | fascism_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| siphon_equipment_stockpiles_for_fascist_civil_war | fascism_on_the_rise | generic_prepare_civil_war | 50 |  |  | political_decisions.txt |
| formulate_surprise_attack_plan_for_fascist_civil_war | fascism_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| ignite_the_fascist_civil_war_single_state | fascism_on_the_rise | generic_ignite_civil_war | 50 | yes |  | political_decisions.txt |
| ignite_the_fascist_civil_war | fascism_on_the_rise | generic_ignite_civil_war | 50 | yes |  | political_decisions.txt |
| rebuild_the_nation_fascism | fascism_on_the_rise | generic_construction | 25 | yes |  | political_decisions.txt |
| open_up_political_discourse_fascism | fascism_on_the_rise | generic_political_discourse | 75 | yes |  | political_decisions.txt |
| discredit_government_fascism | fascism_on_the_rise | generic_political_discourse | 50 | yes |  | political_decisions.txt |
| hold_the_fascist_national_referendum | fascism_on_the_rise | generic_political_discourse | 100 | yes | Trial of Allegiance | political_decisions.txt |
| prepare_for_democratic_civil_war | democratic_on_the_rise | generic_prepare_civil_war | 50 | yes |  | political_decisions.txt |
| expand_civil_democratic_support | democratic_on_the_rise | generic_civil_support | 25 |  |  | political_decisions.txt |
| army_support_for_democratic_civil_war | democratic_on_the_rise | generic_army_support | 50 |  |  | political_decisions.txt |
| ensure_general_loyalty_for_democratic_civil_war | democratic_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| ensure_marshal_loyalty_for_democratic_civil_war | democratic_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| siphon_equipment_stockpiles_for_democratic_civil_war | democratic_on_the_rise | generic_prepare_civil_war | 50 |  |  | political_decisions.txt |
| formulate_surprise_attack_plan_for_democratic_civil_war | democratic_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| ignite_the_democratic_civil_war_single_state | democratic_on_the_rise | generic_ignite_civil_war | 50 | yes |  | political_decisions.txt |
| ignite_the_democratic_civil_war | democratic_on_the_rise | generic_ignite_civil_war | 50 | yes |  | political_decisions.txt |
| rebuild_the_nation_democratic | democratic_on_the_rise | generic_construction | 25 | yes |  | political_decisions.txt |
| open_up_political_discourse_democratic | democratic_on_the_rise | generic_political_discourse | 75 | yes |  | political_decisions.txt |
| discredit_government_democratic | democratic_on_the_rise | generic_political_discourse | 50 | yes |  | political_decisions.txt |
| hold_the_democratic_national_referendum | democratic_on_the_rise | generic_political_discourse | 100 | yes | Arms Against Tyranny | political_decisions.txt |
| prepare_for_communist_civil_war | communism_on_the_rise | generic_prepare_civil_war | 50 | yes |  | political_decisions.txt |
| expand_civil_communist_support | communism_on_the_rise | generic_civil_support | 25 |  |  | political_decisions.txt |
| army_support_for_communist_civil_war | communism_on_the_rise | generic_army_support | 50 |  |  | political_decisions.txt |
| ensure_general_loyalty_for_communist_civil_war | communism_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| ensure_marshal_loyalty_for_communist_civil_war | communism_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| siphon_equipment_stockpiles_for_communist_civil_war | communism_on_the_rise | generic_prepare_civil_war | 50 |  |  | political_decisions.txt |
| formulate_surprise_attack_plan_for_communist_civil_war | communism_on_the_rise | generic_army_support | 50 | yes |  | political_decisions.txt |
| ignite_the_communist_civil_war_single_state | communism_on_the_rise | generic_ignite_civil_war | 50 | yes |  | political_decisions.txt |
| ignite_the_communist_civil_war | communism_on_the_rise | generic_ignite_civil_war | 50 | yes |  | political_decisions.txt |
| rebuild_the_nation_communism | communism_on_the_rise | generic_construction | 25 | yes |  | political_decisions.txt |
| open_up_political_discourse_communist | communism_on_the_rise | generic_political_discourse | 75 | yes |  | political_decisions.txt |
| discredit_government_communism | communism_on_the_rise | generic_political_discourse | 50 | yes |  | political_decisions.txt |
| hold_the_communist_national_referendum | communism_on_the_rise | generic_political_discourse | 100 | yes | Arms Against Tyranny | political_decisions.txt |
| give_refuge_ger | political_actions | generic_research | 100 | yes |  | political_decisions.txt |
| give_refuge_ita | political_actions | generic_research | 100 | yes |  | political_decisions.txt |
| anti_fascist_raids | political_actions | generic_civil_support | 50 |  | Gotterdammerung | political_decisions.txt |
| anti_democratic_raids | political_actions | generic_civil_support | 50 |  |  | political_decisions.txt |
| anti_communist_raids | political_actions | generic_civil_support | 50 |  | No Compromise, No Surrender | political_decisions.txt |
| anti_neutrality_raids | political_actions | generic_civil_support | 50 |  |  | political_decisions.txt |
| ban_fascist_party | political_actions | generic_civil_support | 100 |  | Graveyard of Empires | political_decisions.txt |
| ban_democratic_party | political_actions | generic_civil_support | 100 |  | Battle for the Bosporus | political_decisions.txt |
| ban_communist_party | political_actions | generic_civil_support | 100 |  | Trial of Allegiance | political_decisions.txt |
| ban_neutrality_party | political_actions | generic_civil_support | 100 |  |  | political_decisions.txt |
| institute_press_censorship_fascist_state | political_actions | generic_political_discourse | 150 |  | Battle for the Bosporus | political_decisions.txt |
| institute_press_censorship_democratic_state | political_actions | generic_political_discourse | 150 |  | Battle for the Bosporus | political_decisions.txt |
| institute_press_censorship_communist_state | political_actions | generic_political_discourse | 150 |  | Battle for the Bosporus | political_decisions.txt |
| institute_press_censorship_neutrality_state | political_actions | generic_political_discourse | 150 |  | Battle for the Bosporus | political_decisions.txt |
| POR_angola_overseas_province | POR_overseas_provinces | infiltrate_state | 0 | yes |  | POR.txt |
| POR_mozambique_overseas_territory | POR_overseas_provinces | infiltrate_state | 0 | yes |  | POR.txt |
| POR_buy_artillery_in_britain | POR_arms_purchases | generic_industry | 0 |  | Arms Against Tyranny | POR.txt |
| POR_buy_aa_in_britain | POR_arms_purchases | generic_industry | 0 |  | Arms Against Tyranny | POR.txt |
| POR_buy_at_in_britain | POR_arms_purchases | generic_industry | 0 |  | Arms Against Tyranny | POR.txt |
| POR_buy_ships_britain | POR_arms_purchases | eng_trade_unions_support | 0 |  |  | POR.txt |
| POR_buy_ships_italy | POR_arms_purchases | eng_trade_unions_support | 0 |  |  | POR.txt |
| POR_british_submarines_construction_progress | POR_arms_purchases | generic_naval |  |  | Man the Guns | POR.txt |
| POR_italian_submarines_construction_progress | POR_arms_purchases | generic_naval |  |  | Man the Guns | POR.txt |
| POR_british_destroyers_construction_progress | POR_arms_purchases | generic_naval |  |  | Man the Guns | POR.txt |
| POR_italian_destroyers_construction_progress | POR_arms_purchases | generic_naval |  |  | Man the Guns | POR.txt |
| POR_british_light_cruiser_construction_progress | POR_arms_purchases | generic_naval |  |  | Man the Guns | POR.txt |
| POR_italian_light_cruiser_construction_progress | POR_arms_purchases | generic_naval |  |  | Man the Guns | POR.txt |
| POR_evade_blockade_with_portuguese_convoys | POR_naval_blockade | generic_naval | 25 | yes |  | POR.txt |
| POR_major_cancel_portuguese_blockade_evasion | POR_naval_blockade | generic_break_treaty | 0 | yes |  | POR.txt |
| POR_portugal_cancel_blockade_evasion_for_country | POR_naval_blockade | generic_break_treaty | 0 | yes |  | POR.txt |
| POR_iberian_summit_pro_axis | POR_iberian_summit | eng_trade_unions_support | 50 | yes |  | POR.txt |
| POR_iberian_summit_pro_allies | POR_iberian_summit | eng_trade_unions_support | 50 | yes |  | POR.txt |
| POR_iberian_summit_proposal_delayed | POR_iberian_summit | generic_political_discourse |  |  |  | POR.txt |
| POR_stir_monarchist_sentiment_in_brazil | POR_monarchist_cause | generic_political_discourse | 25 |  | La Resistance | POR.txt |
| POR_portugal_promoting_monarchist_cause_in_brazil | POR_monarchist_cause | generic_civil_support |  |  | La Resistance | POR.txt |
| POR_repress_brazilian_monarchists | POR_monarchist_cause | oppression | 25 |  | La Resistance | POR.txt |
| POR_stir_monarchist_sentiment_in_portugal | POR_monarchist_cause | generic_political_discourse | 25 |  | La Resistance | POR.txt |
| POR_develop_lisbon_tungsten_deposits | POR_prospect_for_resources | tungsten | 25 | yes |  | POR.txt |
| POR_develop_santarem_chromium_deposits | POR_prospect_for_resources | chromium | 25 |  |  | POR.txt |
| POR_fight_alongside_the_republic | POR_the_spanish_civil_war | generic_prepare_civil_war | 0 | yes |  | POR.txt |
| POR_fight_alongside_the_nationalists | POR_the_spanish_civil_war | generic_prepare_civil_war | 0 | yes |  | POR.txt |
| POR_fight_alongside_the_carlists | POR_the_spanish_civil_war | generic_prepare_civil_war | 0 | yes |  | POR.txt |
| debug_DANNES_PRC_decisions | debug_decisions |  |  |  |  | PRC.txt |
| PRC_uprising | PRC_infiltrate_nationalist_areas | generic_ignite_civil_war | 25 | yes |  | PRC.txt |
| PRC_infiltrate_gansu | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_shandong | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_jinan | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_jiangsu | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_henan | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_beijing | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_hebei | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_shanxi | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_suiyuan | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_xian | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_infiltrate_ordos | PRC_infiltrate_nationalist_areas | infiltrate_state | 10 |  |  | PRC.txt |
| PRC_anti_japanese_uprising | PRC_anti_japanese_expedition | revolt | 10 | yes |  | PRC.txt |
| PRC_infiltrate_east_hebei | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_infiltrate_jehol | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_infiltrate_south_chahar | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_infiltrate_chahar | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_infiltrate_heilungkiang | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_infiltrate_liaoning | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_infiltrate_hulunbuir | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_infiltrate_pailingmiao | PRC_anti_japanese_expedition | infiltrate_state | 25 |  |  | PRC.txt |
| PRC_launch_100_regiments_campaign | operations | generic_prepare_civil_war | 0 | yes |  | PRC.txt |
| PRC_provoke_japan | PRC_provoke_japan | generic_ignite_civil_war | 10 |  |  | PRC.txt |
| PRC_return_manchuria_communist | political_actions |  | 25 |  |  | PRC.txt |
| refuse_the_tribute | political_actions | generic_political_actions |  | yes |  | PRC.txt |
| PRC_hold_speech_questioning_tradition | PRC_the_communist_power_struggle_balance_of_power_category |  | 50 |  |  | PRC.txt |
| PRC_emphasize_rural_support | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_criticize_dogmatism | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 |  |  | PRC.txt |
| PRC_send_wang_ming_to_soviet | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_convince_wang_jiaxiang | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_utilizie_political_connections_mao | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_utilizie_political_connections_bo_gu | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_utilizie_political_connections_zhang_guotao | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_guotao_supreme | PRC_the_communist_power_struggle_balance_of_power_category |  | 75 | yes |  | PRC.txt |
| PRC_utilizie_political_connections_otto_braun | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_mao_lectures | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_bo_gu_review | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_bo_gu | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_zhang_guotao | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_wang_ming | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_mao_zedong | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_wang_shiwei | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_chen_changhao | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_liu_shaoqi | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_deng_xiaoping | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_purge_ren_bishi | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_unwilling_diarchy_bop_decision | PRC_the_communist_power_struggle_balance_of_power_category |  | 50 | yes |  | PRC.txt |
| PRC_criticize_leadership_decision | PRC_the_communist_power_struggle_balance_of_power_category |  | 50 |  |  | PRC.txt |
| PRC_reinforce_teachings_from_USSR | PRC_the_communist_power_struggle_balance_of_power_category |  | 75 |  |  | PRC.txt |
| PRC_emphasize_urban_support | PRC_the_communist_power_struggle_balance_of_power_category |  | 25 | yes |  | PRC.txt |
| PRC_emphasize_intellectual_support | PRC_the_communist_power_struggle_balance_of_power_category |  | 50 | yes |  | PRC.txt |
| DEBUG_reset_bop | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_max_mao | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_medium_mao | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_kinda_mao | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_small_mao | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_max_28 | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_medium_28 | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_kinda_28 | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| DEBUG_small_28 | PRC_the_communist_power_struggle_balance_of_power_category |  |  |  |  | PRC.txt |
| PRC_establish_guerilla_cells_start | PRC_guerilla_warfare_sea_cat | { |  |  |  | PRC.txt |
| PRC_establish_guerilla_cells_upgrade | PRC_guerilla_warfare_sea_cat | { |  |  |  | PRC.txt |
| PRC_establish_sabotage_operations | PRC_guerilla_warfare_sea_cat | GFX_decisions_generic_sabotage |  | yes |  | PRC.txt |
| PRC_root_out_guerilla_fighters | PRC_guerilla_suppression_sea_cat | GFX_decision_oppression |  |  |  | PRC.txt |
| PRC_root_out_guerilla_fighters_upgraded | PRC_guerilla_suppression_sea_cat | GFX_decision_oppression |  |  |  | PRC.txt |
| PRC_infiltrate_state | PRC_infiltration_sea_cat | { |  |  |  | PRC.txt |
| CHI_counter_infiltration_measures | CHI_counter_infiltration_sea_cat | { |  |  |  | PRC.txt |
| CHI_counter_infiltration_measures_level_3 | CHI_counter_infiltration_sea_cat | GFX_decisions_generic_infiltration_3 | 100 |  |  | PRC.txt |
| PRC_initialize_five_year_plan_mission | PRC_economic_planning_cat | GFX_decision_generic_factory |  | yes |  | PRC.txt |
| PRC_initialize_shorter_market_plans_mission | PRC_economic_planning_cat | GFX_decision_generic_industry |  | yes |  | PRC.txt |
| PRC_appeal_for_foreign_aid_t34 | PRC_appeal_for_foreign_aid_cat | GFX_decision_SOV_secure_the_administration | 125 | yes |  | PRC.txt |
| PRC_appeal_for_foreign_aid_bt7 | PRC_appeal_for_foreign_aid_cat | GFX_decision_SOV_secure_the_administration | 100 | yes |  | PRC.txt |
| PRC_the_westward_expedition_decision | PRC_border_wars_cat | GFX_decision_generic_fortification |  | yes |  | PRC.txt |
| PRC_assaulting_guyuan | PRC_border_wars_cat | border_war |  |  |  | PRC.txt |
| PRC_the_eastward_expedition_decision | PRC_border_wars_cat | GFX_decision_generic_fortification |  | yes |  | PRC.txt |
| PRC_assaulting_shanxi | PRC_border_wars_cat | border_war |  |  |  | PRC.txt |
| PRC_usurp_control_over_yanan_decision | PRC_border_wars_cat | GFX_decision_generic_fortification |  | yes |  | PRC.txt |
| PRC_assaulting_yanan | PRC_border_wars_cat | border_war |  |  |  | PRC.txt |
| PRC_the_peoples_doubt | PRC_war_of_resistance_cat | GFX_decision_generic_ignite_civil_war |  |  |  | PRC.txt |
| PRC_28_bolshevik_faction_decision_enlai_diplomatic_feelers | PRC_28_bolshevik_faction_cat | GFX_decision_generic_political_discourse |  |  |  | PRC.txt |
| PRC_28_bolshevik_faction_decision_ask_for_support | PRC_28_bolshevik_faction_cat | GFX_decision_generic_speech |  |  |  | PRC.txt |
| PRC_28_bolshevik_faction_decision_backstab | PRC_28_bolshevik_faction_cat | GFX_decisions_generic_infiltration |  | yes |  | PRC.txt |
| PRC_28_bolshevik_faction_decision_legitimize_faction_leader | PRC_28_bolshevik_faction_cat | GFX_decision_eng_propaganda_campaigns |  | yes |  | PRC.txt |
| PRC_rural_surveys | PRC_rural_surveyer_decision_cat |  | 30 |  |  | PRC.txt |
| PRC_integration_decision_tibet | PRC_integration_decision_cat |  | 50 |  |  | PRC.txt |
| PRC_integration_decision_soviet_states | PRC_integration_decision_cat |  | 50 |  |  | PRC.txt |
| PRC_second_thoughts_factions | political_actions |  | 25 | yes |  | PRC.txt |
| PRC_remove_yulin_garrison | political_actions | GFX_decision_generic_prepare_civil_war |  | yes |  | PRC.txt |
| PRU_start_military_conflict_with_ecuador | PRU_pastaza_conflict | GFX_decision_generic_operation | 100 | yes | Trial of Allegiance | PRU.txt |
| PRU_force_peace_ecuador_good | PRU_pastaza_conflict | GFX_decision_generic_nationalism | 25 | yes |  | PRU.txt |
| PRU_force_peace_ecuador_bad | PRU_pastaza_conflict | GFX_decision_eng_trade_unions_support | 10 | yes |  | PRU.txt |
| PSR_core_state | foreign_politics | GFX_decision_infiltrate_state | 150 | yes |  | PSR.txt |
| RAJ_industrialize_state | RAJ_population_decisions | generic_construction | 75 |  |  | RAJ.txt |
| RAJ_industrialize_state_goe | RAJ_population_decisions | generic_construction | 75 |  | Graveyard of Empires | RAJ.txt |
| RAJ_GOE_urge_non_violence | RAJ_GOE_independence_movement | GFX_decision_SWI_swiss_democratic_tradition_campaign | 15 |  |  | RAJ_GOE.txt |
| RAJ_GOE_urge_violence | RAJ_GOE_independence_movement | GFX_decision_revolt | 13 |  |  | RAJ_GOE.txt |
| RAJ_GOE_try_to_arrest_bose | RAJ_GOE_independence_movement |  |  | yes |  | RAJ_GOE.txt |
| RAJ_GOE_foment_independence_tension | RAJ_GOE_independence_movement | GFX_decision_generic_political_rally | 20 |  |  | RAJ_GOE.txt |
| RAJ_GOE_export_tea_subject | RAJ_GOE_tea_exports_cat | generic_construction | 10 |  |  | RAJ_GOE.txt |
| RAJ_GOE_export_tea_free | RAJ_GOE_tea_exports_cat | generic_construction | 70 |  |  | RAJ_GOE.txt |
| RAJ_GOE_sikh_recruitment | RAJ_GOE_sikh_recruitment_cat | GFX_decision_generic_prepare_civil_war | 30 | yes |  | RAJ_GOE.txt |
| RAJ_core_states | RAJ_GOE_india_indivisible_cat | GFX_decision_generic_prepare_civil_war | 30 |  |  | RAJ_GOE.txt |
| RAJ_core_states_eic | RAJ_GOE_india_indivisible_cat | GFX_decision_generic_prepare_civil_war | 120 |  |  | RAJ_GOE.txt |
| RAJ_reveal_famine_timeframe | RAJ_GOE_famine_cat | GFX_decision_generic_prepare_civil_war | 25 |  |  | RAJ_GOE.txt |
| RAJ_ask_for_aid | RAJ_GOE_famine_cat | GFX_decision_generic_prepare_civil_war | 150 |  |  | RAJ_GOE.txt |
| RAJ_deploy_emergency_healthcare | RAJ_GOE_famine_cat | GFX_decision_generic_prepare_civil_war | 10 |  |  | RAJ_GOE.txt |
| RAJ_shut_down_black_markets | RAJ_GOE_famine_cat | GFX_decision_generic_prepare_civil_war | 0 |  |  | RAJ_GOE.txt |
| mughal_west_britain_company_dec | political_actions | generic_form_nation | 50 | yes |  | RAJ_GOE.txt |
| RAJ_GOE_raise_war_taxes | political_actions | GFX_decision_generic_prepare_civil_war | 5 |  |  | RAJ_GOE.txt |
| RAJ_GOE_reduce_war_taxes | political_actions | GFX_decision_generic_prepare_civil_war | 5 |  |  | RAJ_GOE.txt |
| RAJ_GOE_azad_hind_radio_unaligned | political_actions | decision_generic_political_discourse | 25 |  |  | RAJ_GOE.txt |
| RAJ_GOE_azad_hind_radio_fascism | political_actions | decision_generic_political_discourse | 25 |  |  | RAJ_GOE.txt |
| RAJ_GOE_azad_hind_radio_communism | political_actions | decision_generic_political_discourse | 25 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_afg | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_ban | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_nep | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_tib | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_srl | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_princely | RAJ_akhand_bharat_cat | generic_civil_support | 175 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_pak | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_brm | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_mld | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_akhand_bharat_claim_bhu | RAJ_akhand_bharat_cat | generic_civil_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_form_akhand_bharat | RAJ_akhand_bharat_cat | GFX_decision_eng_install_government | 0 | yes |  | RAJ_GOE.txt |
| RAJ_GOE_campaign_against_agrarian_societys | propaganda_efforts | GFX_decision_eng_install_government | 350 |  |  | RAJ_GOE.txt |
| RAJ_GOE_ai_protect_princely_state | RAJ_GOE_partition_cat |  |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_princely_state_timeout | RAJ_GOE_partition_cat |  |  | yes |  | RAJ_GOE.txt |
| RAJ_GOE_eng_is_getting_involved_in_war | RAJ_GOE_partition_cat | GFX_decision_mission_icon |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_cease_hostilities | RAJ_GOE_partition_cat |  | 0 |  |  | RAJ_GOE.txt |
| RAJ_GOE_vie_for_princes | RAJ_GOE_partition_cat | GFX_decision_SWI_swiss_democratic_tradition_campaign | 0 |  |  | RAJ_GOE.txt |
| RAJ_GOE_eic_the_taxman | RAJ_GOE_eic_cat | mission_icon |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_eic_no_more_taxman | RAJ_GOE_eic_cat | mission_icon |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_provide_working_opportunities | RAJ_GOE_eic_cat |  |  | yes |  | RAJ_GOE.txt |
| RAJ_GOE_default_on_debt | RAJ_GOE_eic_cat |  |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_pay_out_dividends_small | RAJ_GOE_eic_cat |  |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_pay_out_dividends_normal | RAJ_GOE_eic_cat |  |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_pay_out_dividends_high | RAJ_GOE_eic_cat |  |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_tax_fraud | RAJ_GOE_eic_cat | eng_propaganda_campaigns |  |  |  | RAJ_GOE.txt |
| RAJ_GOE_hostile_takeover_decision | RAJ_GOE_eic_hostile_takeover_cat | GFX_decision_hol_attract_foreign_investors | 10 |  |  | RAJ_GOE.txt |
| RAJ_GOE_enforced_peace_decision | RAJ_GOE_mughal_independence_category | GFX_decision_revolt |  | yes |  | RAJ_GOE.txt |
| RAJ_GOE_enforced_peace_decision_eng | RAJ_GOE_mughal_independence_category | GFX_decision_revolt |  | yes |  | RAJ_GOE.txt |
| RAJ_communist_unions_promised_worker_safety_mission | RAJ_GOE_communism_infiltration_cat | generic_civil_support |  | yes |  | RAJ_GOE.txt |
| RAJ_communist_unions_promised_minimum_wage_mission | RAJ_GOE_communism_infiltration_cat | generic_civil_support |  | yes |  | RAJ_GOE.txt |
| RAJ_GOE_undermine_gandhis_movement | RAJ_GOE_communism_infiltration_cat | GFX_decision_generic_brainwash | 25 |  |  | RAJ_GOE.txt |
| RAJ_GOE_contact_dissenting_officers | RAJ_GOE_communism_infiltration_cat | GFX_decision_generic_army_support | 30 | yes |  | RAJ_GOE.txt |
| RAJ_GOE_spread_dissent_in_the_army | RAJ_GOE_communism_infiltration_cat | GFX_decision_SWE_set_army_budget | 40 |  |  | RAJ_GOE.txt |
| RAJ_GOE_seek_support_from_the_unions | RAJ_GOE_communism_infiltration_cat | GFX_decision_eng_trade_unions_support | 0 |  |  | RAJ_GOE.txt |
| RAJ_GOE_orchestrate_train_robberies | RAJ_GOE_communism_infiltration_cat | GFX_decision_generic_train | 10 |  |  | RAJ_GOE.txt |
| RAJ_GOE_accept_russian_muhajir_money | RAJ_GOE_communism_infiltration_cat | GFX_decision_gre_paying_ifc_debt | 30 | yes |  | RAJ_GOE.txt |
| RAJ_GOE_meet_with_the_kremlin | RAJ_GOE_communism_infiltration_cat | GFX_decision_eng_trade_unions_support | 30 | yes | Arms Against Tyranny | RAJ_GOE.txt |
| RAJ_GOE_infiltrate_the_national_congress | RAJ_GOE_communism_infiltration_cat | GFX_decision_SWI_expand_covert_operations | 30 |  |  | RAJ_GOE.txt |
| RAJ_GOE_communism_sway_bose | RAJ_GOE_communism_infiltration_cat | generic_civil_support | 25 | yes |  | RAJ_GOE.txt |
| RAJ_secure_west_bengal_decision | RAJ_GOE_communism_border_clashes_cat | GFX_decision_infiltrate_state | 0 | yes |  | RAJ_GOE.txt |
| RAJ_secure_rajahsthan_decision | RAJ_GOE_communism_border_clashes_cat | GFX_decision_generic_reorganize_irregulars | 0 | yes |  | RAJ_GOE.txt |
| RAJ_red_punjab_operation_decision | RAJ_GOE_communism_border_clashes_cat | GFX_decision_hol_war_on_pacifism | 0 | yes |  | RAJ_GOE.txt |
| RAJ_instigate_in_nepal | RAJ_peasant_uprisings_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | RAJ_GOE.txt |
| RAJ_instigate_in_tib | RAJ_peasant_uprisings_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | RAJ_GOE.txt |
| RAJ_instigate_in_brm | RAJ_peasant_uprisings_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | RAJ_GOE.txt |
| RAJ_instigate_in_afg | RAJ_peasant_uprisings_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | RAJ_GOE.txt |
| RAJ_instigate_in_per | RAJ_peasant_uprisings_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | RAJ_GOE.txt |
| RAJ_instigate_in_sia | RAJ_peasant_uprisings_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | RAJ_GOE.txt |
| RAJ_instigate_in_ins | RAJ_peasant_uprisings_cat | GFX_decision_eng_propaganda_campaigns | 25 | yes |  | RAJ_GOE.txt |
| RAJ_propaganda_in_target | RAJ_peasant_uprisings_cat | GFX_decision_POL_organize_strike_two | 25 |  |  | RAJ_GOE.txt |
| RAJ_arm_communist_militants | RAJ_peasant_uprisings_cat | GFX_decision_POL_looming_peasants_strike | 25 |  |  | RAJ_GOE.txt |
| RAJ_communist_coup | RAJ_peasant_uprisings_cat | decision_generic_agriculture | 50 |  |  | RAJ_GOE.txt |
| RAJ_abandon_communist_effort | RAJ_peasant_uprisings_cat | GFX_decision_BOL_reintegrate_litoral_department | 0 |  |  | RAJ_GOE.txt |
| RAJ_return_churchill | political_actions | GFX_decision_generic_political_address |  |  |  | RAJ_GOE.txt |
| RAJ_request_resource_rights_in_burma | prospect_for_resources | GFX_decision_eng_trade_unions_support |  | yes |  | RAJ_GOE.txt |
| develop_southern_madras_rubber_plantations | prospect_for_resources | rubber | 25 | yes | Graveyard of Empires | RAJ_GOE.txt |
| develop_arunachal_pradesh_tungsten_deposits | prospect_for_resources | tungsten | 25 | yes | Graveyard of Empires | RAJ_GOE.txt |
| develop_bombay_tungsten_deposits | prospect_for_resources | tungsten | 25 | yes | Graveyard of Empires | RAJ_GOE.txt |
| develop_west_bengal_iron_mines | prospect_for_resources | steel | 25 | yes | Graveyard of Empires | RAJ_GOE.txt |
| expand_the_mines_in_orissa | prospect_for_resources | steel | 35 | yes | Graveyard of Empires | RAJ_GOE.txt |
| expand_the_mines_in_hyderabad | prospect_for_resources | chromium | 35 | yes | Graveyard of Empires | RAJ_GOE.txt |
| RAJ_investments_from_local_leaders | RAJ_work_with_local_leaders_cat | GFX_decision_generic_construction |  |  |  | RAJ_GOE.txt |
| RAJ_congress_productivity_effort | RAJ_concessions_to_the_congress_cat | generic_factory |  |  |  | RAJ_GOE.txt |
| RAJ_congress_shipbuilding_effort | RAJ_concessions_to_the_congress_cat | generic_naval |  |  |  | RAJ_GOE.txt |
| RAJ_congress_construction_effort | RAJ_concessions_to_the_congress_cat | generic_construction |  |  |  | RAJ_GOE.txt |
| RAJ_congress_war_propaganda | RAJ_concessions_to_the_congress_cat | eng_propaganda_campaigns |  |  |  | RAJ_GOE.txt |
| develop_shandong_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_suiyuan_steel_deposits | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_daqing_deposits | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_daqing_deposits_2 | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_yunnan_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_kirin_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_sichuan_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_nauru_tungsten_deposits | prospect_for_resources | tungsten | 25 | yes |  | resource_prospecting.txt |
| develop_tonkin_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_singapore_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_sirte_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_benghazi_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_tasmania_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_west_africa_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_west_africa_aluminium_deposits_2 | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_madagascar_rubber_plantations | prospect_for_resources | rubber | 25 | yes |  | resource_prospecting.txt |
| develop_madagascar_rubber_plantations_2 | prospect_for_resources | rubber | 25 | yes |  | resource_prospecting.txt |
| develop_sidamo_rubber_plantations | prospect_for_resources | rubber | 25 | yes |  | resource_prospecting.txt |
| develop_nigeria_rubber_plantations | prospect_for_resources | rubber | 25 | yes |  | resource_prospecting.txt |
| develop_ems_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_matzen_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_friesland_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| expand_eregli_steel_works | prospect_for_resources | steel | 25 | yes | Battle for the Bosporus | resource_prospecting.txt |
| develop_newfoundland_steel | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_quebec_steel | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_cuba_steel | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_arkansas_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | resource_prospecting.txt |
| develop_new_york_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | resource_prospecting.txt |
| develop_tennessee_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | resource_prospecting.txt |
| develop_washington_aluminium_deposits | prospect_for_resources | aluminium | 25 |  |  | resource_prospecting.txt |
| develop_idaho_tungsten_deposits | prospect_for_resources | tungsten | 25 |  |  | resource_prospecting.txt |
| develop_california_tungsten_deposits | prospect_for_resources | tungsten | 25 |  |  | resource_prospecting.txt |
| develop_minnesota_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_pennsylvania_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_ohio_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_indiana_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_montana_chromium_deposits | prospect_for_resources | chromium | 25 |  |  | resource_prospecting.txt |
| develop_katanga_cobalt_deposits | prospect_for_resources | chromium | 25 | yes | Gotterdammerung | resource_prospecting.txt |
| develop_katanga_cobalt_deposits_2 | prospect_for_resources | chromium | 25 | yes |  | resource_prospecting.txt |
| develop_california_chromium_deposits | prospect_for_resources | chromium | 25 |  |  | resource_prospecting.txt |
| develop_oregon_chromium_deposits | prospect_for_resources | chromium | 25 |  |  | resource_prospecting.txt |
| develop_alaska_chromium_deposits | prospect_for_resources | chromium | 25 |  |  | resource_prospecting.txt |
| develop_south_sakhalin_oil_deposits | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_palau_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_taiwan_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_taiwan_oil_deposits | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_cornwall_tungsten_deposits_1 | prospect_for_resources | tungsten | 25 | yes |  | resource_prospecting.txt |
| develop_cornwall_tungsten_deposits_2 | prospect_for_resources | tungsten | 25 | yes |  | resource_prospecting.txt |
| develop_leningrad_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_kamensk_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_stalingrad_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| develop_caucasus_tungsten_deposits_1 | prospect_for_resources | tungsten | 25 | yes |  | resource_prospecting.txt |
| develop_caucasus_tungsten_deposits_2 | prospect_for_resources | tungsten | 25 | yes |  | resource_prospecting.txt |
| develop_kyzyl_tungsten_deposits | prospect_for_resources | tungsten | 25 | yes |  | resource_prospecting.txt |
| develop_chelyabinsk_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_zlatoust_steel_deposits_1 | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_zlatoust_steel_deposits_2 | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_kursk_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_kursk_steel_deposits_2 | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_kursk_steel_deposits_3 | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_Belgorod_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_Belgorod_steel_deposits_2 | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_Belgorod_steel_deposits_3 | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_uralsk_chromium_deposits_1 | prospect_for_resources | chromium | 25 | yes |  | resource_prospecting.txt |
| develop_uralsk_chromium_deposits_2 | prospect_for_resources | chromium | 25 | yes |  | resource_prospecting.txt |
| develop_liaotung_iron_ore_deposits | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_chosen_tungsten_deposits | prospect_for_resources | tungsten | 25 |  |  | resource_prospecting.txt |
| develop_abu_dhabi_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_kuwait_oil_fields | prospect_for_resources | oil | 25 |  |  | resource_prospecting.txt |
| develop_omani_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_khuzestan_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_fars_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_baghdad_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_mosul_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_nejd_oil_fields | prospect_for_resources | oil | 25 |  |  | resource_prospecting.txt |
| develop_eastern_desert_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_qatar_oil_fields | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_malatya_chromium_deposits | prospect_for_resources | chromium | 25 | yes |  | resource_prospecting.txt |
| develop_mersin_chromium_mines | prospect_for_resources | chromium | 25 | yes |  | resource_prospecting.txt |
| utilize_diyarbakir_chromium_deposits | prospect_for_resources | chromium | 25 | yes |  | resource_prospecting.txt |
| expand_the_kirikkale_steel_mills | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_the_iron_mines_in_divrigi | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| exploit_the_raman_oil_field | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| drill_in_the_garzan_oil_field | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| expand_the_west_raman_oil_field | prospect_for_resources | oil | 25 | yes |  | resource_prospecting.txt |
| develop_tripoli_oil_fields | prospect_for_resources | oil | 25 |  |  | resource_prospecting.txt |
| develop_tripoli_steel_deposits | prospect_for_resources | steel | 25 |  |  | resource_prospecting.txt |
| develop_transdanubia_aluminium_deposits | prospect_for_resources | aluminium | 25 | yes |  | resource_prospecting.txt |
| expand_the_rudabanya_iron_mine | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| develop_derna_oilfield | prospect_for_resources | oil | 50 | yes |  | resource_prospecting.txt |
| HUN_tap_the_nagylengyel_oil_field | prospect_for_resources | oil | 75 | yes | Gotterdammerung | resource_prospecting.txt |
| HUN_explore_the_oil_fields_around_nagykanizsa | prospect_for_resources | oil | 50 | yes | Gotterdammerung | resource_prospecting.txt |
| deeper_swedish_mines | prospect_for_resources | steel | 50 | yes |  | resource_prospecting.txt |
| expand_greenlands_mines | prospect_for_resources | steel | 50 |  |  | resource_prospecting.txt |
| drill_for_oil_in_chaco_boreal | prospect_for_resources | oil | 50 | yes |  | resource_prospecting.txt |
| drill_for_oil_in_chaco_boreal_2 | prospect_for_resources | oil | 50 | yes |  | resource_prospecting.txt |
| AUS_develop_bleiberger_mines | prospect_for_resources | steel | 25 | yes |  | resource_prospecting.txt |
| CHI_develop_hunan_tungsten_mines | prospect_for_resources | tungsten | 25 | yes | No Compromise, No Surrender | resource_prospecting.txt |
| CHI_develop_jiangxi_tungsten_mines | prospect_for_resources | tungsten | 25 | yes | No Compromise, No Surrender | resource_prospecting.txt |
| CHI_develop_coal_mines | prospect_for_resources | coal | 25 | yes | No Compromise, No Surrender | resource_prospecting.txt |
| develop_rio_grande_sul_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| develop_guapore_casserite_deposits | prospect_for_resources | aluminium | 25 | yes | Trial of Allegiance | resource_prospecting.txt |
| develop_la_libertad_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| develop_western_visayas_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_tomsk_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_sofia_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_north_transdanubia_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_bosnia_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_lima_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_antofagasta_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| develop_mendoza_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| develop_western_slovakia_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_tesinsko_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_german_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_transvaal_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| expand_bihar_coal_mines | prospect_for_resources | coal | 25 | yes |  | resource_prospecting.txt |
| RNG_core_state | foreign_politics | GFX_decision_infiltrate_state | 75 | yes |  | RNG.txt |
| ROM_change_sides_to_allies | ROM_change_sides | decision_generic_nationalism | 0 | yes |  | ROM.txt |
| ROM_change_sides_to_commintern | ROM_change_sides | decision_generic_nationalism | 0 | yes |  | ROM.txt |
| ROM_change_sides_to_axis | ROM_change_sides | decision_generic_nationalism | 0 | yes |  | ROM.txt |
| ROM_present_ultimatum | ROM_dividing_yugo | decision_generic_nationalism | 0 | yes |  | ROM.txt |
| ROM_invite_germany | ROM_dividing_yugo | decision_generic_nationalism | 0 | yes |  | ROM.txt |
| ROM_invite_italy | ROM_dividing_yugo | decision_generic_nationalism | 0 | yes |  | ROM.txt |
| ROM_invite_hungary | ROM_dividing_yugo | decision_generic_nationalism | 0 | yes |  | ROM.txt |
| ROM_claim_vojvodina | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_banat | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_serbia | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_morava | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_kosovo | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_south_serbia | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_macedonia | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_debar | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_montenegro | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_bosnia | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_dalmatia | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_croatia | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_slovenia | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_ljubljana | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| ROM_claim_herzegovina | ROM_dividing_yugo | { | 20 |  |  | ROM.txt |
| liberate_angola | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_mozambique | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_congo | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_zimbabwe | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_kenya | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_madagascar | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_botswana | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_zambia | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_malawi | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_tanzania | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_uganda | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_sudan | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_egypt | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_eritrea | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_ethiopia | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_djibouti | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_somalia | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_rwanda | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_burundi | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_congo_brazzaville | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_gabon | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_equatorial_guinea | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_cameroon | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_central_african_republic | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_chad | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_nigeria | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_niger | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_dahomey | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_togo | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_ghana | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_ivory_coast | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_upper_volta | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_mali | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_sierra_leone | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_guinea | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_guinea_bissau | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_senegal | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_the_gambia | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_liberia | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_mauritania | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_western_sahara | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_algeria | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_morocco | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_tunisia | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| liberate_libya | SAF_anti_colonialist_crusade | generic_independence | 0 | yes |  | SAF.txt |
| SAU_refining_our_national_identity_decision | political_actions | GFX_decision_eng_trade_unions_support | 75 | yes |  | SAU.txt |
| SOV_debug_show_paranoia_system | debug_decisions | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_debug_show_propaganda_system | debug_decisions | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_TEST_ULTIMATE_CONTINENTS | debug_decisions | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_forge_production_reports | SOV_paranoia_system | GFX_decision_eng_trade_unions_support |  |  |  | SOV.txt |
| SOV_inspection_in_the_administration | SOV_paranoia_system | GFX_decision_generic_political_discourse |  |  |  | SOV.txt |
| SOV_inspection_in_the_army | SOV_paranoia_system | GFX_decision_generic_political_discourse |  |  |  | SOV.txt |
| SOV_inspection_in_the_navy | SOV_paranoia_system | GFX_decision_generic_political_discourse |  |  |  | SOV.txt |
| SOV_inspection_in_the_airforce | SOV_paranoia_system | GFX_decision_generic_political_discourse |  |  |  | SOV.txt |
| SOV_loosen_prohibitions_in_military_academies_dec | SOV_paranoia_system | generic_brainwash | 50 |  |  | SOV.txt |
| SOV_reinforce_army_officer_ranks_with_veterans_dec | SOV_paranoia_system | generic_prepare_civil_war |  |  |  | SOV.txt |
| SOV_reinforce_navy_officer_ranks_with_veterans_dec | SOV_paranoia_system | generic_naval |  |  |  | SOV.txt |
| SOV_reinstate_mig_design_bureau | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_reinstate_ilyushin_design_bureau | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_reinstate_tupolev_design_bureau | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_reinstate_yakovlev_design_bureau | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_DEBUG_ACTIVATE_PARANOIA | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_DEACTIVATE_PARANOIA | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_show_debug_purge_decisions | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_hide_debug_purge_decisions | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_MAKE_PURGE_DECISIONS_FASTER_HERE | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_REGULAR_PURGE_DECISIONS_DURATION_HERE | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_great_purge_trial_of_the_generals_dec | SOV_paranoia_system | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_great_purge_army_junior_officers_dec | SOV_paranoia_system | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_random_army_great_purge_dec | SOV_paranoia_system | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_general_accused_dec | SOV_paranoia_system | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_conspiracy_in_the_academy_dec | SOV_paranoia_system | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_anti_saboteur_campaign_dec | SOV_paranoia_system | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_general_accuses_general_dec | SOV_paranoia_system | generic_prepare_civil_war | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_great_purge_moscow_trial_dec | SOV_paranoia_system | eng_trade_unions_support | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_advisor_accused_dec | SOV_paranoia_system | eng_trade_unions_support | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_civil_servants_dec | SOV_paranoia_system | eng_trade_unions_support | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_nkvd_dec | SOV_paranoia_system | eng_trade_unions_support | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_great_purge_trial_of_the_admirals_dec | SOV_paranoia_system | generic_naval | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_great_purge_junior_naval_officers_effect | SOV_paranoia_system | generic_naval | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_admiral_accused_dec | SOV_paranoia_system | generic_naval | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_naval_conspiracy_in_the_academys_dec | SOV_paranoia_system | generic_naval | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_naval_anti_saboteur_campaign_dec | SOV_paranoia_system | generic_naval | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_great_purge_airforce_chiefs_dec | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_great_purge_airforce_design_bureau_dissolved_dec | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_airforce_conspiracy_in_the_academys_dec | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_DEBUG_trigger_regular_purge_airforce_anti_saboteur_campaign_dec | SOV_paranoia_system | generic_air | 0 |  |  | SOV.txt |
| SOV_DEBUG_low_paranoia_increase_dec | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_medium_paranoia_increase_dec | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_high_paranoia_increase_dec | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_low_paranoia_decrease_dec | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_medium_paranoia_decrease_dec | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_high_paranoia_decrease_dec | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_DEBUG_show_all_purged_portraits | SOV_paranoia_system | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_debug_unlock_slot | SOV_propaganda_campaigns | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_debug_MAKE_CAMPAIGNS_FASTER_HERE | SOV_propaganda_campaigns | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_debug_REGULAR_CAMPAIGN_DURATION_HERE | SOV_propaganda_campaigns | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_debug_UNLOCK_ALL_CAMPAIGNS | SOV_propaganda_campaigns | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_propaganda_motherland_calls | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_victory_at_hand | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_defend_moscow | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_fight_to_the_last | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_hit_of_hammer | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_transport | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_oil_for_the_motherland | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_more_metal | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_high_yield | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_for_the_motherland | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_heroes_forward | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_anti_capitalism | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_anti_fascism | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_treacherous_enemy | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  | La Resistance | SOV.txt |
| SOV_propaganda_do_not_blab | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_sweep_scum_out | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_knowledge | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_builders_of_communism | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_glory_to_partisans | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_death_to_invaders | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_stalin | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_rebuild_to_glory | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_peace | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_propaganda_happy_life | SOV_propaganda_campaigns | eng_propaganda_campaigns |  |  |  | SOV.txt |
| SOV_gosproyektstroy_bring_foreign_experts | SOV_gosproyektstroy_decision_category | hol_attract_foreign_investors |  | yes |  | SOV.txt |
| SOV_gosproyektstroy_focus_civ | SOV_gosproyektstroy_decision_category | generic_construction |  | yes |  | SOV.txt |
| SOV_gosproyektstroy_focus_mil | SOV_gosproyektstroy_decision_category | generic_industry |  | yes |  | SOV.txt |
| SOV_gosproyektstroy_focus_dock | SOV_gosproyektstroy_decision_category | GFX_decision_generic_naval |  | yes |  | SOV.txt |
| SOV_organize_covert_depots_poum | SOV_soviet_aid_to_poum_decision_category | ger_military_buildup |  | yes |  | SOV.txt |
| SOV_send_infantry_equipment_poum | SOV_soviet_aid_to_poum_decision_category | generic_industry |  |  |  | SOV.txt |
| SOV_organize_popular_brigades_poum | SOV_soviet_aid_to_poum_decision_category | generic_nationalism |  |  |  | SOV.txt |
| SOV_send_elite_commandos_poum | SOV_soviet_aid_to_poum_decision_category | generic_military |  |  |  | SOV.txt |
| SOV_organize_popular_speeches_poum | SOV_soviet_aid_to_poum_decision_category | eng_propaganda_campaigns | 25 |  |  | SOV.txt |
| SOV_infiltrate_stalinist_plans_in_spain_poum | SOV_soviet_aid_to_poum_decision_category | eng_propaganda_campaigns |  | yes |  | SOV.txt |
| SOV_pressure_country_government_baltic | SOV_diplomacy_baltic_decision_category | generic_political_discourse |  |  |  | SOV.txt |
| SOV_promote_ideology_rallies_baltic | SOV_diplomacy_baltic_decision_category | generic_political_rally |  | yes |  | SOV.txt |
| SOV_send_ultimatum_to_country_baltic | SOV_diplomacy_baltic_decision_category | eng_trade_unions_demand |  |  |  | SOV.txt |
| SOV_fight_alongside_country_comrades_baltic | SOV_diplomacy_baltic_decision_category | generic_prepare_civil_war |  |  |  | SOV.txt |
| SOV_pressure_country_government_nordic | SOV_diplomacy_nordic_decision_category | generic_political_discourse |  |  |  | SOV.txt |
| SOV_promote_ideology_rallies_nordic | SOV_diplomacy_nordic_decision_category | generic_political_rally |  | yes |  | SOV.txt |
| SOV_fight_alongside_country_comrades_nordic | SOV_diplomacy_nordic_decision_category | generic_prepare_civil_war |  |  |  | SOV.txt |
| SOV_pressure_country_government_balkan | SOV_diplomacy_balkan_decision_category | generic_political_discourse |  |  |  | SOV.txt |
| SOV_promote_ideology_rallies_balkan | SOV_diplomacy_balkan_decision_category | generic_political_rally |  | yes |  | SOV.txt |
| SOV_send_ultimatum_to_country_balkan | SOV_diplomacy_balkan_decision_category | eng_trade_unions_demand |  |  |  | SOV.txt |
| SOV_fight_alongside_country_comrades_balkan | SOV_diplomacy_balkan_decision_category | generic_prepare_civil_war |  |  |  | SOV.txt |
| SOV_pressure_country_government_middle_east | SOV_diplomacy_middle_east_decision_category | hol_attract_foreign_investors |  |  |  | SOV.txt |
| SOV_promote_ideology_rallies_middle_east | SOV_diplomacy_middle_east_decision_category | hol_attract_foreign_investors |  | yes |  | SOV.txt |
| SOV_send_ultimatum_to_country_middle_east | SOV_diplomacy_middle_east_decision_category | hol_attract_foreign_investors |  |  |  | SOV.txt |
| SOV_fight_alongside_country_comrades_middle_east | SOV_diplomacy_middle_east_decision_category | generic_prepare_civil_war |  |  |  | SOV.txt |
| SOV_preparations_for_operation_countenance | SOV_diplomacy_middle_east_decision_category | hol_draw_up_staff_plans |  |  |  | SOV.txt |
| SOV_operation_countenance | SOV_diplomacy_middle_east_decision_category | generic_operation |  |  |  | SOV.txt |
| SOV_send_infantry_equipment_asia | SOV_diplomacy_asia_decision_category | generic_industry |  |  |  | SOV.txt |
| SOV_peace_deal_for_south_sakhalin_and_kuril_islands | SOV_diplomacy_asia_decision_category | eng_trade_unions_support |  | yes |  | SOV.txt |
| SOV_peace_deal_for_hokkaido | SOV_diplomacy_asia_decision_category | eng_trade_unions_support |  | yes |  | SOV.txt |
| SOV_cancel_the_japanese_resource_rights_to_sakhalin_decision | SOV_diplomacy_asia_decision_category | GFX_decision_generic_forestry | 50 | yes |  | SOV.txt |
| SOV_sinkiang_mineral_prospection_sik | SOV_diplomacy_asia_decision_category | generic_construction |  |  |  | SOV.txt |
| SOV_sinkiang_oil_prospection_sik | SOV_diplomacy_asia_decision_category | generic_construction |  |  |  | SOV.txt |
| SOV_sinkiang_military_aid_sik | SOV_diplomacy_asia_decision_category | generic_military |  |  |  | SOV.txt |
| SOV_sinkiang_support_expansion_sik | SOV_diplomacy_asia_decision_category | infiltrate_state |  |  |  | SOV.txt |
| SOV_formalize_of_the_soviet_republic_of_sinkiang | SOV_diplomacy_asia_decision_category | generic_nationalism | 100 | yes |  | SOV.txt |
| SOV_sinkiang_mineral_prospection_mission_dummy | SOV_soviet_aid_decision_category | generic_construction |  |  |  | SOV.txt |
| SOV_sinkiang_oil_prospection_mission_dummy | SOV_soviet_aid_decision_category | generic_construction |  |  |  | SOV.txt |
| SOV_sinkiang_military_aid_mission_dummy | SOV_soviet_aid_decision_category | generic_military |  |  |  | SOV.txt |
| SOV_sinkiang_support_expansion_mission_dummy | SOV_soviet_aid_decision_category | infiltrate_state |  |  |  | SOV.txt |
| SOV_sinkiang_mineral_prospection | prospect_for_resources | generic_construction |  |  |  | SOV.txt |
| SOV_sinkiang_oil_prospection | prospect_for_resources | generic_construction |  |  |  | SOV.txt |
| SOV_jiuquan_oil_prospection | prospect_for_resources | generic_construction |  |  |  | SOV.txt |
| SOV_debug_merge_designers_FASTER_AND_FREE | SOV_merge_designers_dec_cat | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_debug_merge_designers_BACK_TO_REGULAR_STUFF | SOV_merge_designers_dec_cat | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_merge_tank_plant | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_tank |  |  |  | SOV.txt |
| SOV_merge_tank_plant_2 | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_tank |  |  |  | SOV.txt |
| SOV_merge_tank_plant_3 | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_tank |  |  |  | SOV.txt |
| SOV_merge_ship_plant_1_baltic | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  | Man the Guns | SOV.txt |
| SOV_merge_ship_plant_2_baltic | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  |  | SOV.txt |
| SOV_merge_ship_plant_3_baltic | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  |  | SOV.txt |
| SOV_merge_ship_plant_4_baltic | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  |  | SOV.txt |
| SOV_merge_ship_plant_1_black_sea | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  | Man the Guns | SOV.txt |
| SOV_merge_ship_plant_2_black_sea | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  |  | SOV.txt |
| SOV_merge_ship_plant_3_black_sea | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  |  | SOV.txt |
| SOV_merge_ship_plant_4_black_sea | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_ship |  |  |  | SOV.txt |
| SOV_merge_aircraft_plant_1 | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_aircraft |  |  |  | SOV.txt |
| SOV_merge_aircraft_plant_2 | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_aircraft |  |  |  | SOV.txt |
| SOV_merge_aircraft_plant_3 | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_aircraft |  |  |  | SOV.txt |
| SOV_merge_materiel_plant_1_artillery | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_materiel |  |  |  | SOV.txt |
| SOV_merge_materiel_plant_1_infantry | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_materiel |  |  |  | SOV.txt |
| SOV_merge_materiel_plant_1_motorized | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_materiel |  |  |  | SOV.txt |
| SOV_merge_materiel_plant_2 | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_materiel |  |  |  | SOV.txt |
| SOV_merge_materiel_plant_3 | SOV_merge_designers_dec_cat | GFX_decision_generic_merge_plant_materiel |  |  |  | SOV.txt |
| SOV_debug_FASTER_AND_FREE | SOV_national_academy_of_sciences_dec_cat | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_debug_BACK_TO_REGULAR_STUFF | SOV_national_academy_of_sciences_dec_cat | eng_ally_imperialist_coup | 0 |  |  | SOV.txt |
| SOV_build_national_academy_of_sciences_independent_republic | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_BLR | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_UKR | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_KAZ | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_GEO | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_ARM | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_AZR | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_UZB | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_TMS | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_KYR | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_TAJ | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_EST | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_LAT | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_LIT | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_POL | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_FIN | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_TAN | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_build_national_academy_of_sciences_integrated_republic_MON | SOV_national_academy_of_sciences_dec_cat | GFX_decision_SOV_academy_of_sciences |  | yes |  | SOV.txt |
| SOV_raid_trotskys_villa | SOV_kill_trotsky_dec_cat | generic_prepare_civil_war | 75 |  |  | SOV.txt |
| SOV_carefully_planned_assassination | SOV_kill_trotsky_dec_cat | GFX_decision_generic_assassination | 100 | yes |  | SOV.txt |
| SOV_generic_industry_relocation | SOV_industry_relocation | generic_construction | 25 |  |  | SOV.txt |
| move_leningrad_aluminium_plant | SOV_industry_relocation | aluminium | 25 | yes |  | SOV.txt |
| SOV_infiltrate_atomic_program | SOV_infiltrate_foreign_atomic_programs_dec_cat | GFX_decision_generic_political_discourse | 100 |  |  | SOV.txt |
| SOV_comecon_industrialization_program | SOV_comecon_dec_cat | GFX_decision_generic_construction | 100 |  |  | SOV.txt |
| SOV_comecon_joint_military_program | SOV_comecon_dec_cat | GFX_decision_generic_construction | 100 |  |  | SOV.txt |
| SOV_raise_penal_units | SOV_great_patriotic_war | GFX_decision_generic_arrest | 50 |  |  | SOV.txt |
| SOV_factory_worker_militias | SOV_great_patriotic_war | generic_prepare_civil_war |  |  |  | SOV.txt |
| SOV_civilian_labor_in_defense | SOV_great_patriotic_war | POL_organize_strike_two |  |  |  | SOV.txt |
| SOV_staggered_retreat | SOV_great_patriotic_war | GFX_decision_generic_military |  |  |  | SOV.txt |
| SOV_order_227 | SOV_great_patriotic_war | generic_army_support |  | yes | No Step Back | SOV.txt |
| SOV_military_offensive_ongoing | SOV_great_patriotic_war | hol_draw_up_staff_plans |  | yes |  | SOV.txt |
| SOV_military_offensive | SOV_great_patriotic_war | GFX_decision_generic_operation |  |  |  | SOV.txt |
| SOV_operation_iskra_ongoing | SOV_great_patriotic_war | hol_draw_up_staff_plans |  | yes |  | SOV.txt |
| SOV_operation_iskra | SOV_great_patriotic_war | GFX_decision_generic_operation |  | yes |  | SOV.txt |
| SOV_the_rush_for_berlin | SOV_great_patriotic_war | GFX_decision_generic_nationalism |  | yes |  | SOV.txt |
| SOV_hold_stalingrad | SOV_great_patriotic_war | generic_civil_support |  | yes |  | SOV.txt |
| SOV_hold_leningrad | SOV_great_patriotic_war | generic_civil_support |  | yes |  | SOV.txt |
| SOV_hold_moscow | SOV_great_patriotic_war | generic_civil_support |  | yes |  | SOV.txt |
| SOV_scorched_earth | SOV_great_patriotic_war | generic_scorched_earth | 50 | yes | No Step Back | SOV.txt |
| SOV_scorched_earth_baltics | SOV_great_patriotic_war | generic_scorched_earth | 50 | yes | No Step Back | SOV.txt |
| SOV_scorched_earth_byelorussia | SOV_great_patriotic_war | generic_scorched_earth | 75 | yes | No Step Back | SOV.txt |
| SOV_scorched_earth_ukraine | SOV_great_patriotic_war | generic_scorched_earth | 75 | yes | No Step Back | SOV.txt |
| SOV_scorched_earth_caucasus | SOV_great_patriotic_war | generic_scorched_earth | 75 | yes | No Step Back | SOV.txt |
| SOV_scorched_earth_stalingrad | SOV_great_patriotic_war | generic_scorched_earth | 75 | yes | No Step Back | SOV.txt |
| SOV_scorched_earth_moscow | SOV_great_patriotic_war | generic_scorched_earth | 75 | yes | No Step Back | SOV.txt |
| SOV_the_head_of_the_nkvd_yezhov | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_political_discourse | 50 | yes |  | SOV.txt |
| SOV_the_head_of_the_nkvd_yagoda | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_political_discourse | 50 | yes |  | SOV.txt |
| SOV_assassinate_stalin | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_political_discourse | 50 |  |  | SOV.txt |
| SOV_send_supporters_abroad | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_political_discourse | 50 |  |  | SOV.txt |
| SOV_wreckers_sabotage_contruction | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_wreckers | 15 |  |  | SOV.txt |
| SOV_wreckers_sabotage_military_production | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_wreckers | 15 |  |  | SOV.txt |
| SOV_wreckers_sabotage_dockyards | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_wreckers | 10 |  |  | SOV.txt |
| SOV_wreckers_sabotage_railways | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_wreckers | 15 |  |  | SOV.txt |
| SOV_secure_moscow_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_revolt | 25 | yes |  | SOV.txt |
| SOV_secure_leningrad_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_revolt | 25 | yes |  | SOV.txt |
| SOV_army_framejob | SOV_soviet_civil_war_dec_cat | generic_police_action |  |  |  | SOV.txt |
| SOV_navy_framejob | SOV_soviet_civil_war_dec_cat | generic_police_action |  |  |  | SOV.txt |
| SOV_recruit_general_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_army_support |  |  |  | SOV.txt |
| SOV_recruit_admiral_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_army_support |  |  |  | SOV.txt |
| SOV_expand_nkvd_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_police_action | 40 |  |  | SOV.txt |
| SOV_influence_army_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_military |  |  |  | SOV.txt |
| SOV_influence_navy_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_naval |  |  |  | SOV.txt |
| SOV_influence_airforce_opposition | SOV_soviet_civil_war_dec_cat | GFX_decision_generic_air |  |  |  | SOV.txt |
| SOV_dismiss_the_counter_revolution | SOV_soviet_civil_war_dec_cat | generic_speech | 75 |  |  | SOV.txt |
| SOV_concessions_japan_vladivostok_SCW | SOV_soviet_civil_war_dec_cat | generic_political_discourse | 25 | yes |  | SOV.txt |
| SOV_concessions_japan_sakhalin_SCW | SOV_soviet_civil_war_dec_cat | generic_political_discourse | 10 | yes |  | SOV.txt |
| SOV_concessions_germany_baku_SCW | SOV_soviet_civil_war_dec_cat | generic_political_discourse | 10 | yes |  | SOV.txt |
| SOV_concessions_germany_ukraininan_oil_SCW | SOV_soviet_civil_war_dec_cat | GFX_decision_revolt | 15 | yes |  | SOV.txt |
| SOV_concessions_uk_belarus_SCW | SOV_soviet_civil_war_dec_cat | generic_political_discourse | 15 | yes |  | SOV.txt |
| SOV_sabotage_behind_enemy_lines_decision | SOV_soviet_civil_war_dec_cat | generic_assassination |  | yes |  | SOV.txt |
| SOV_recruit_manchurian_cavalry_exiles | SOV_soviet_civil_war_dec_cat | generic_cavalry |  | yes |  | SOV.txt |
| SOV_recruit_cavalry_exiles | SOV_soviet_civil_war_dec_cat | generic_cavalry |  | yes |  | SOV.txt |
| SOV_plan_start_of_uprising_archangelsk | SOV_soviet_civil_war_dec_cat | { | 15 | yes |  | SOV.txt |
| SOV_plan_start_of_uprising_odessa | SOV_soviet_civil_war_dec_cat | { | 30 |  |  | SOV.txt |
| SOV_plan_start_of_uprising_omsk | SOV_soviet_civil_war_dec_cat | { | 15 |  |  | SOV.txt |
| SOV_plan_start_of_uprising_tashkent | SOV_soviet_civil_war_dec_cat | { | 15 |  |  | SOV.txt |
| SOV_plan_start_of_uprising_ufa | SOV_soviet_civil_war_dec_cat | { | 10 |  |  | SOV.txt |
| SOV_plan_start_of_uprising_chita | SOV_soviet_civil_war_dec_cat | { | 10 |  |  | SOV.txt |
| SOV_plan_start_of_uprising_irkutsk | SOV_soviet_civil_war_dec_cat | { | 10 |  |  | SOV.txt |
| SOV_align_states_siberia_csw | SOV_soviet_civil_war_dec_cat | { | 5 |  |  | SOV.txt |
| SOV_align_states_far_east_csw | SOV_soviet_civil_war_dec_cat | { | 15 |  |  | SOV.txt |
| SOV_align_states_northern_csw | SOV_soviet_civil_war_dec_cat | { | 15 |  |  | SOV.txt |
| SOV_align_states_ukraine_csw | SOV_soviet_civil_war_dec_cat | { | 25 |  |  | SOV.txt |
| SOV_align_states_steppe_csw | SOV_soviet_civil_war_dec_cat | { | 15 |  |  | SOV.txt |
| SOV_align_states_urals_csw | SOV_soviet_civil_war_dec_cat | { | 15 |  |  | SOV.txt |
| SOV_align_general_stalin | SOV_soviet_civil_war_dec_cat | generic_military |  |  |  | SOV.txt |
| SOV_align_admiral_stalin | SOV_soviet_civil_war_dec_cat | generic_military |  |  |  | SOV.txt |
| SOV_ukraine_crackdown_timer | SOV_soviet_civil_war_dec_cat | generic_ignite_civil_war |  |  |  | SOV.txt |
| SOV_steppe_crackdown_timer | SOV_soviet_civil_war_dec_cat | generic_ignite_civil_war |  |  |  | SOV.txt |
| SOV_northern_crackdown_timer | SOV_soviet_civil_war_dec_cat | generic_ignite_civil_war |  |  |  | SOV.txt |
| SOV_siberian_crackdown_timer | SOV_soviet_civil_war_dec_cat | generic_ignite_civil_war |  |  |  | SOV.txt |
| SOV_urals_crackdown_timer | SOV_soviet_civil_war_dec_cat | generic_ignite_civil_war |  |  |  | SOV.txt |
| SOV_the_stalin_constitution_mission | SOV_soviet_civil_war_dec_cat | SOV_the_stalin_constitution |  | yes |  | SOV.txt |
| SOV_the_zinovyevite_terrorist_center_mission | SOV_soviet_civil_war_dec_cat | SOV_the_zinovyevite_terrorist_center |  | yes |  | SOV.txt |
| SOV_the_anti_soviet_trotskyist_center_mission | SOV_soviet_civil_war_dec_cat | SOV_the_anti_soviet_trotskyist_center |  | yes |  | SOV.txt |
| SOV_the_workers_dictatorship_mission | SOV_soviet_civil_war_dec_cat | SOV_the_workers_dictatorship |  | yes |  | SOV.txt |
| SOV_the_military_conspiracy_mission | SOV_soviet_civil_war_dec_cat | SOV_the_military_conspiracy |  | yes |  | SOV.txt |
| SOV_socialism_in_one_country_mission | SOV_soviet_civil_war_dec_cat | SOV_socialism_in_one_country |  | yes |  | SOV.txt |
| SOV_secure_the_administration_mission | SOV_soviet_civil_war_dec_cat | SOV_secure_the_administration |  | yes |  | SOV.txt |
| SOV_the_bloc_of_rights_and_trotskyites_mission | SOV_soviet_civil_war_dec_cat | SOV_the_bloc_of_rights_and_trotskyites |  | yes |  | SOV.txt |
| SOV_behead_the_snake_mission | SOV_soviet_civil_war_dec_cat | SOV_behead_the_snake |  | yes |  | SOV.txt |
| SOV_organize_fifth_columnists_in_enemy_neighbor | SOV_permanent_revolution_dec_cat | GFX_decision_generic_nationalism | 150 | yes |  | SOV.txt |
| SOV_ignite_revolutionary_uprisings | SOV_permanent_revolution_dec_cat | generic_political_rally | 50 | yes |  | SOV.txt |
| SOV_ignite_uprising_timer_mission | SOV_permanent_revolution_dec_cat | generic_ignite_civil_war |  | yes |  | SOV.txt |
| SOV_seize_manchuria | operations | generic_operation | 25 | yes |  | SOV.txt |
| SOV_return_manchuria | political_actions |  | 0 | yes |  | SOV.txt |
| demand_tribute_from_new_communist_china | political_actions | generic_civil_support | 10 |  |  | SOV.txt |
| demand_full_integration | political_actions | generic_civil_support |  | yes |  | SOV.txt |
| SOV_set_up_puppet_state_in_turkey | political_actions | generic_civil_support | 50 | yes | Battle for the Bosporus | SOV.txt |
| SOV_integrate_czechoslovakia | SOV_panslavic_nationalism | generic_form_nation | 150 | yes |  | SOV.txt |
| SOV_integrate_bulgaria | SOV_panslavic_nationalism | generic_form_nation | 75 | yes |  | SOV.txt |
| SOV_integrate_poland | SOV_panslavic_nationalism | generic_form_nation | 150 | yes |  | SOV.txt |
| SOV_integrate_yugoslavia | SOV_panslavic_nationalism | generic_form_nation | 100 | yes |  | SOV.txt |
| SOV_declare_the_pan_slavic_union | SOV_panslavic_nationalism | generic_form_nation | 25 | yes |  | SOV.txt |
| SOV_return_states_to_poland | SOV_polish_territory | generic_form_nation | 25 | yes |  | SOV.txt |
| SPA_military_plot_nationalists | SPR_the_inevitable_civil_war | generic_ignite_civil_war |  | yes |  | SPR.txt |
| SPR_military_plot_republicans | SPR_the_inevitable_civil_war | generic_ignite_civil_war |  | yes |  | SPR.txt |
| SPA_primo_de_rivera_speech | SPR_the_inevitable_civil_war | eng_propaganda_campaigns | 30 |  |  | SPR.txt |
| SPR_imprison_primo_de_rivera | SPR_the_inevitable_civil_war | generic_independence | 15 | yes |  | SPR.txt |
| SPA_political_assassination | SPR_the_inevitable_civil_war | spr_political_assassination | 30 |  |  | SPR.txt |
| SPR_political_arrest | SPR_the_inevitable_civil_war | generic_independence | 10 |  |  | SPR.txt |
| SPA_sway_leader_loyalty | SPR_the_inevitable_civil_war | generic_army_support | 30 |  |  | SPR.txt |
| SPR_secure_leader_loyalty | SPR_the_inevitable_civil_war | generic_army_support | 30 |  |  | SPR.txt |
| SPR_reassign_disloyal_leader | SPR_the_inevitable_civil_war | generic_army_support | 30 |  |  | SPR.txt |
| SPA_suppress_the_strikes | SPR_the_inevitable_civil_war | oppression | 30 |  |  | SPR.txt |
| SPR_concessions_to_the_left | SPR_the_inevitable_civil_war | eng_trade_unions_support | 30 |  |  | SPR.txt |
| SPA_expand_influence_in_the_galicia_garrison | SPR_the_inevitable_civil_war | { | 171 |  |  | SPR.txt |
| SPA_expand_influence_in_the_asturias_garrison | SPR_the_inevitable_civil_war | { | 790 |  |  | SPR.txt |
| SPA_expand_influence_in_the_leon_garrison | SPR_the_inevitable_civil_war | { | 174 |  |  | SPR.txt |
| SPA_expand_influence_in_the_valladolid_garrison | SPR_the_inevitable_civil_war | { | 791 |  |  | SPR.txt |
| SPA_expand_influence_in_the_burgos_garrison | SPR_the_inevitable_civil_war | { | 176 |  |  | SPR.txt |
| SPA_expand_influence_in_the_pais_vasco_garrison | SPR_the_inevitable_civil_war | { | 792 |  |  | SPR.txt |
| SPA_expand_influence_in_the_navarra_garrison | SPR_the_inevitable_civil_war | { | 172 |  |  | SPR.txt |
| SPA_expand_influence_in_the_western_aragon_garrison | SPR_the_inevitable_civil_war | { | 166 |  |  | SPR.txt |
| SPA_expand_influence_in_the_eastern_aragon_garrison | SPR_the_inevitable_civil_war | { | 794 |  |  | SPR.txt |
| SPA_expand_influence_in_the_catalunya_garrison | SPR_the_inevitable_civil_war | { | 165 |  |  | SPR.txt |
| SPA_expand_influence_in_the_salamanca_garrison | SPR_the_inevitable_civil_war | { | 788 |  |  | SPR.txt |
| SPA_expand_influence_in_the_madrid_garrison | SPR_the_inevitable_civil_war | { | 41 |  |  | SPR.txt |
| SPA_expand_influence_in_the_guadalajara_garrison | SPR_the_inevitable_civil_war | { | 793 |  |  | SPR.txt |
| SPA_expand_influence_in_the_valencia_garrison | SPR_the_inevitable_civil_war | { | 167 |  |  | SPR.txt |
| SPA_expand_influence_in_the_extremadura_garrison | SPR_the_inevitable_civil_war | { | 170 |  |  | SPR.txt |
| SPA_expand_influence_in_the_ciudad_real_garrison | SPR_the_inevitable_civil_war | { | 175 |  |  | SPR.txt |
| SPA_expand_influence_in_the_murcia_garrison | SPR_the_inevitable_civil_war | { | 168 |  |  | SPR.txt |
| SPA_expand_influence_in_the_sevilla_garrison | SPR_the_inevitable_civil_war | { | 169 |  |  | SPR.txt |
| SPA_expand_influence_in_the_cordoba_garrison | SPR_the_inevitable_civil_war | { | 789 |  |  | SPR.txt |
| SPA_expand_influence_in_the_granada_garrison | SPR_the_inevitable_civil_war | { | 173 |  |  | SPR.txt |
| SPA_hand_over_the_ceda_campaign_chest_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPA_negotiate_carlist_support_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPA_the_army_of_africa_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPA_secure_the_northern_garrisons_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPA_sin_paquito_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPA_con_paquito_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPR_secure_the_guardia_de_asalto_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPR_secure_the_guardia_civil_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPR_train_the_union_youth_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPR_enlarge_the_weapon_caches_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPR_distribute_arms_to_the_people_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPR_disband_the_army_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  | yes |  | SPR.txt |
| SPR_primo_de_rivera_speech_mission | SPR_opposition_civil_war_preparations | eng_propaganda_campaigns |  |  |  | SPR.txt |
| SPA_imprison_primo_de_rivera_mission | SPR_opposition_civil_war_preparations | generic_independence |  | yes |  | SPR.txt |
| SPR_political_assassination_mission | SPR_opposition_civil_war_preparations | spr_political_assassination |  |  |  | SPR.txt |
| SPA_political_arrest_mission | SPR_opposition_civil_war_preparations | generic_independence |  |  |  | SPR.txt |
| SPR_sway_leader_loyalty_mission | SPR_opposition_civil_war_preparations | generic_army_support |  |  |  | SPR.txt |
| SPA_reassign_disloyal_leader_mission | SPR_opposition_civil_war_preparations | generic_army_support |  |  |  | SPR.txt |
| SPR_suppress_the_strikes_mission | SPR_opposition_civil_war_preparations | oppression |  |  |  | SPR.txt |
| SPA_concessions_to_the_left_mission | SPR_opposition_civil_war_preparations | eng_trade_unions_support |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_galicia_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_asturias_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_leon_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_valladolid_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_burgos_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_pais_vasco_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_navarra_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_western_aragon_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_eastern_aragon_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_catalunya_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_salamanca_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_madrid_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_guadalajara_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_valencia_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_extremadura_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_ciudad_real_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_murcia_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_sevilla_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_cordoba_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_expand_influence_in_the_granada_garrison_mission | SPR_opposition_civil_war_preparations | generic_prepare_civil_war |  |  |  | SPR.txt |
| SPA_galicia_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_asturias_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_leon_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_valladolid_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_burgos_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_pais_vasco_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_navarra_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_western_aragon_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_eastern_aragon_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_catalunya_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_salamanca_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_madrid_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_guadalajara_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_valencia_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_extremadura_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_ciudad_real_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_murcia_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_sevilla_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_cordoba_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPA_granada_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans | 0 | yes |  | SPR.txt |
| SPR_preparing_offensive | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_galicia_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_asturias_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_leon_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_valladolid_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_burgos_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_pais_vasco_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_navarra_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_western_aragon_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_eastern_aragon_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_catalunya_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_salamanca_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_madrid_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_guadalajara_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_valencia_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_extremadura_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_ciudad_real_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_murcia_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_sevilla_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_cordoba_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_granada_offensive_mission | SPR_civil_war_offensives | hol_draw_up_staff_plans |  | yes |  | SPR.txt |
| SPA_activate_galicia_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_asturias_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_leon_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_valladolid_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_burgos_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_pais_vasco_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_navarra_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_western_aragon_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_eastern_aragon_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_catalunya_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_salamanca_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_madrid_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_guadalajara_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_valencia_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_extremadura_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_ciudad_real_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_murcia_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_sevilla_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_cordoba_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_activate_granada_fifth_columnists | SPR_civil_war_offensives | generic_ignite_civil_war | 25 | yes |  | SPR.txt |
| SPA_carlist_uprising_mission | political_actions | generic_ignite_civil_war |  | yes |  | SPR.txt |
| SPR_anarchist_uprising_mission | political_actions | generic_ignite_civil_war |  | yes |  | SPR.txt |
| SPA_fascist_crackdown_mission | political_actions | generic_ignite_civil_war |  | yes |  | SPR.txt |
| SPR_government_crackdown_mission | political_actions | generic_ignite_civil_war |  | yes |  | SPR.txt |
| SPA_save_the_alcazar_mission | political_actions | eng_propaganda_campaigns |  | yes |  | SPR.txt |
| SPA_reassert_dominance | SPA_reassert_american_dominance | eng_trade_unions_demand |  | yes |  | SPR.txt |
| expand_basque_steel_works | SPR_expand_resource_extraction | steel | 25 | yes |  | SPR.txt |
| expand_western_aragon_steel_works | SPR_expand_resource_extraction | steel | 25 | yes |  | SPR.txt |
| expand_granada_steel_works | SPR_expand_resource_extraction | steel | 25 | yes |  | SPR.txt |
| develop_salamanca_tungsten_deposits | SPR_expand_resource_extraction | tungsten | 25 | yes |  | SPR.txt |
| develop_valladolid_tungsten_deposits | SPR_expand_resource_extraction | tungsten | 35 | yes |  | SPR.txt |
| develop_galicia_tungsten_deposits | SPR_expand_resource_extraction | tungsten | 25 | yes |  | SPR.txt |
| expand_extremadura_tungsten_mines | SPR_expand_resource_extraction | tungsten | 35 | yes |  | SPR.txt |
| expand_madrid_bauxite_mines | SPR_expand_resource_extraction | aluminium | 25 | yes |  | SPR.txt |
| SPA_establish_galicia_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_asturias_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_leon_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_valladolid_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_burgos_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_pais_vasco_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_navarra_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_western_aragon_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_eastern_aragon_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_catalunya_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_salamanca_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_madrid_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_guadalajara_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_valencia_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_extremadura_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_ciudad_real_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_murcia_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_sevilla_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_cordoba_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPA_establish_granada_carlist_cell | SPA_preparing_the_carlist_insurrection | generic_prepare_civil_war | 50 |  |  | SPR.txt |
| SPR_purchase_infantry_equipment | SPR_foreign_arms_purchases | generic_prepare_civil_war | 25 |  |  | SPR.txt |
| SPR_purchase_support_equipment | SPR_foreign_arms_purchases | generic_prepare_civil_war | 25 |  |  | SPR.txt |
| SPR_purchase_artillery_equipment | SPR_foreign_arms_purchases | generic_prepare_civil_war | 25 |  |  | SPR.txt |
| SPR_purchase_aircraft | SPR_foreign_arms_purchases | generic_air | 25 |  | By Blood Alone | SPR.txt |
| SPR_purchase_trucks | SPR_foreign_arms_purchases | generic_prepare_civil_war | 25 |  |  | SPR.txt |
| SPR_purchase_tanks | SPR_foreign_arms_purchases | generic_tank | 25 |  |  | SPR.txt |
| SPR_integrate_commune_1 | SPR_the_seeds_of_revolution | generic_nationalism | 50 | yes |  | SPR.txt |
| SPR_integrate_commune_2 | SPR_the_seeds_of_revolution | generic_nationalism | 150 | yes |  | SPR.txt |
| SPR_ignite_uprising | SPR_the_seeds_of_revolution | generic_ignite_civil_war | 150 | yes |  | SPR.txt |
| SPR_ignite_uprising_timer_mission | SPR_the_seeds_of_revolution | generic_ignite_civil_war |  | yes |  | SPR.txt |
| SPR_concessions_to_the_anarchists | SPR_anti_fascist_unity | eng_trade_unions_support | 150 |  |  | SPR.txt |
| SPR_eliminate_guerrillas | SPR_recovering_from_civil_war | generic_civil_support | 40 | yes |  | SPR.txt |
| SS_recruitment_denmark | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_norway | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_netherlands | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_belgium | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_france | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_estonia | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_latvia | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_lithuania | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_britain | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_scotland | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| SS_recruitment_sweden | SS_recruitment | generic_army_support | 25 | yes |  | SS.txt |
| draft_dodging | crisis | generic_civil_support | 0 |  |  | stability_war_support.txt |
| strikes_1 | crisis | generic_civil_support | 0 |  |  | stability_war_support.txt |
| draft_dodging_mission | crisis | generic_civil_support |  |  |  | stability_war_support.txt |
| strikes_mission | crisis | generic_civil_support |  |  |  | stability_war_support.txt |
| mutiny_1 | crisis | generic_civil_support | 5 |  |  | stability_war_support.txt |
| mutiny_mission | crisis | generic_civil_support |  |  |  | stability_war_support.txt |
| demobilization_economic | demobilization | generic_industry | 50 |  |  | stability_war_support.txt |
| demob_economic_mission | demobilization | revolt |  |  |  | stability_war_support.txt |
| demobilization_manpower | demobilization | generic_prepare_civil_war | 50 |  |  | stability_war_support.txt |
| demob_manpower_mission | demobilization | revolt |  |  |  | stability_war_support.txt |
| SWE_hungershield_dummy | SWE_hungershield_cat | generic_civil_support |  |  |  | SWE.txt |
| SWE_hungershield_worse_dummy | SWE_hungershield_cat | generic_civil_support |  |  |  | SWE.txt |
| SWE_hungershield_mission | SWE_hungershield_cat | generic_civil_support |  |  |  | SWE.txt |
| SWE_gateway_to_peace_decision | SWE_politics | generic_prepare_civil_war | 0 |  |  | SWE.txt |
| SWE_urbanization_decision | SWE_politics | decision_generic_construction | 120 |  |  | SWE.txt |
| restore_radiotjanst_to_democratic | SWE_politics | decision_generic_political_discourse | 50 |  |  | SWE.txt |
| pervert_radiotjanst_fascism | SWE_politics | decision_generic_political_discourse | 50 |  |  | SWE.txt |
| pervert_radiotjanst_communism | SWE_politics | decision_generic_political_discourse | 50 |  |  | SWE.txt |
| pervert_radiotjanst_unaligned | SWE_politics | decision_generic_political_discourse | 50 |  |  | SWE.txt |
| SWE_poverty_reduction | SWE_politics | decision_generic_nationalism | 50 |  |  | SWE.txt |
| SWE_concessions_for_defense_spending | SWE_politics | decision_generic_nationalism | 35 |  |  | SWE.txt |
| SWE_integrate_fin | SWE_politics | decision_eng_install_government | 100 | yes |  | SWE.txt |
| SWE_integrate_nor | SWE_politics | decision_eng_install_government | 100 | yes |  | SWE.txt |
| SWE_integrate_den | SWE_politics | decision_eng_install_government | 80 | yes |  | SWE.txt |
| SWE_integrate_ice | SWE_politics | decision_eng_install_government | 50 | yes |  | SWE.txt |
| SWE_proclaim_eternal_sweden | SWE_politics | decision_eng_install_government |  |  |  | SWE.txt |
| SWE_proclaim_big_power_sweden | SWE_politics | decision_eng_install_government | 0 |  |  | SWE.txt |
| SWE_socialists_reforms_decision_efficiency_gain | SWE_politics | decision_generic_nationalism | 35 |  |  | SWE.txt |
| SWE_train_the_sheltered_decision | SWE_train_the_sheltered_cat | decision_generic_nationalism |  |  |  | SWE.txt |
| SWE_blow_up_the_mines | SWE_mines |  | 15 |  |  | SWE.txt |
| SWE_repair_the_mines | SWE_mines |  |  |  |  | SWE.txt |
| SWE_ebba_add_research | SWE_ebba_palmstierna_cat |  | 60 |  |  | SWE.txt |
| SWE_ebba_add_production | SWE_ebba_palmstierna_cat |  | 60 |  |  | SWE.txt |
| SWE_ebba_political_clout | SWE_ebba_palmstierna_cat |  | 60 |  |  | SWE.txt |
| SWE_swap_herman_eriksson | SWE_rationing_policies | decision_generic_nationalism | 75 |  |  | SWE.txt |
| SWE_seize_civilian_tires | SWE_rationing_policies |  | 0 |  |  | SWE.txt |
| SWE_time_until_can_pick_civilian_tires | SWE_rationing_policies |  |  |  |  | SWE.txt |
| SWE_gengas | SWE_rationing_policies |  | 0 |  |  | SWE.txt |
| SWE_time_until_can_pick_gengas | SWE_rationing_policies |  |  |  |  | SWE.txt |
| SWE_food_stamps | SWE_rationing_policies |  | 0 |  |  | SWE.txt |
| SWE_time_until_can_pick_food_stamps | SWE_rationing_policies |  |  |  |  | SWE.txt |
| SWE_air_raid_shelters | SWE_rationing_policies |  | 0 |  |  | SWE.txt |
| SWE_time_until_can_pick_air_shelters | SWE_rationing_policies |  |  |  |  | SWE.txt |
| SWE_bop_suspend_riksdag | SWE_rationing_policies | GFX_decision_gre_faction_management | 150 |  |  | SWE.txt |
| SWE_rangers_sabotage | SWE_military_matters | decision_generic_nationalism |  |  |  | SWE.txt |
| SWE_set_up_home_guard_forces | SWE_military_matters |  |  |  |  | SWE.txt |
| SWE_activate_home_guard | SWE_military_matters |  |  |  |  | SWE.txt |
| SWE_activate_all_home_guard | SWE_military_matters |  |  |  |  | SWE.txt |
| SWE_trade_ball_bearings | SWE_ball_bearings_cat |  | 30 |  |  | SWE.txt |
| SWE_revoke_food_trade | SWE_ball_bearings_cat |  | 35 |  |  | SWE.txt |
| SWE_revoke_research_exchange | SWE_ball_bearings_cat |  | 0 |  |  | SWE.txt |
| SWE_appeal_to_aristocracy | SWE_appeal_for_support_cat | GFX_decision_generic_political_discourse | 0 |  |  | SWE.txt |
| SWE_appeal_to_industrialists | SWE_appeal_for_support_cat | GFX_decision_category_gre_investment_decisions | 0 |  |  | SWE.txt |
| SWE_appeal_to_military | SWE_appeal_for_support_cat | GFX_decision_generic_military | 0 |  |  | SWE.txt |
| SWE_appeal_to_rural_people | SWE_appeal_for_support_cat | GFX_decision_POL_looming_peasants_strike | 0 |  |  | SWE.txt |
| SWE_implement_aristocracy_reforms_countdown | SWE_appeal_for_support_cat | GFX_decision_generic_political_discourse |  | yes |  | SWE.txt |
| SWE_implement_industrialist_reforms_countdown | SWE_appeal_for_support_cat | GFX_decision_category_gre_investment_decisions |  | yes |  | SWE.txt |
| SWE_implement_military_reforms_countdown | SWE_appeal_for_support_cat | GFX_decision_generic_military |  | yes |  | SWE.txt |
| SWE_implement_rural_reforms_countdown | SWE_appeal_for_support_cat | GFX_decision_POL_looming_peasants_strike |  | yes |  | SWE.txt |
| SWE_implement_aristocracy_reforms | SWE_appeal_for_support_cat | GFX_decision_generic_political_discourse | 100 |  |  | SWE.txt |
| SWE_implement_industrialist_reforms | SWE_appeal_for_support_cat | GFX_decision_category_gre_investment_decisions | 100 |  |  | SWE.txt |
| SWE_implement_military_reforms | SWE_appeal_for_support_cat | GFX_decision_generic_military | 100 |  |  | SWE.txt |
| SWE_implement_rural_reforms | SWE_appeal_for_support_cat | GFX_decision_POL_looming_peasants_strike | 100 |  |  | SWE.txt |
| SWE_royal_visit | SWE_royalist_buildup | GFX_decision_eng_support_imperialist_coup | 20 |  |  | SWE.txt |
| SWE_pull_the_trigger_nor | SWE_communist_foreign_influence | generic_civil_support |  |  |  | SWE.txt |
| SWE_pull_the_trigger_den | SWE_communist_foreign_influence | generic_civil_support |  |  |  | SWE.txt |
| SWE_upgrade_current_trait | SWE_coalition_war_cabinet_cat |  |  |  |  | SWE.txt |
| SWE_upgrade_close_ties_to_the_military | SWE_coalition_war_cabinet_cat |  |  |  |  | SWE.txt |
| SWE_upgrade_landsfader | SWE_coalition_war_cabinet_cat |  |  |  |  | SWE.txt |
| SWE_upgrade_respectful_occupier | SWE_coalition_war_cabinet_cat |  |  |  |  | SWE.txt |
| SWE_upgrade_education_for_all | SWE_coalition_war_cabinet_cat |  |  |  |  | SWE.txt |
| SWE_upgrade_every_barrel_counts | SWE_coalition_war_cabinet_cat |  |  |  |  | SWE.txt |
| SWE_coax_countries_that_rejected | SWE_coax_nordic_defense_council_cat |  | 150 |  |  | SWE.txt |
| SWI_find_biggest_fascist | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_is_FRA_country_to_balance | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_add_dynamic_modifiers | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_remove_dynamic_modifiers | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| start_systems | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_add_100MR | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_test_making_president | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_plus_20_BoP | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_minus_100_BoP | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_make_germany_angry | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_make_germany_happy | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_go_council | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_trigger_elections | SWI_debug_decisions_category |  |  |  |  | SWI.txt |
| SWI_oust_confederation_president | SWI_federal_council_decisions_category | GFX_decision_SWI_dismiss_council | 300 |  |  | SWI.txt |
| SWI_no_elected_president | SWI_federal_council_decisions_category | GFX_decision_SWI_no_elected_president |  |  |  | SWI.txt |
| SWI_elect_a_new_confederation_president | SWI_federal_council_decisions_category | GFX_decision_SWI_elect_confederation_president | 250 |  |  | SWI.txt |
| SWI_no_confederation_councilor | SWI_federal_council_decisions_category | GFX_decision_SWI_no_elected_president |  |  |  | SWI.txt |
| SWI_case_north_decision | SWI_federal_council_decisions_category | GFX_decision_hol_draw_up_staff_plans |  |  |  | SWI.txt |
| SWI_case_west_decision | SWI_federal_council_decisions_category | GFX_decision_hol_draw_up_staff_plans |  |  |  | SWI.txt |
| SWI_decision_remove_councilor_1 | SWI_federal_council_decisions_category | GFX_decision_SWI_dismiss_council | 200 |  |  | SWI.txt |
| SWI_decision_remove_councilor_2 | SWI_federal_council_decisions_category | GFX_decision_SWI_dismiss_council | 200 |  |  | SWI.txt |
| SWI_decision_remove_councilor_3 | SWI_federal_council_decisions_category | GFX_decision_SWI_dismiss_council | 200 |  |  | SWI.txt |
| SWI_influence_future_cantons | SWI_federal_council_decisions_category | GFX_decision_eng_propaganda_campaigns | 65 |  |  | SWI.txt |
| SWI_press_for_future_canton | SWI_federal_council_decisions_category | GFX_decision_eng_trade_unions_demand | 250 |  |  | SWI.txt |
| SWI_invite_to_entente | SWI_federal_council_decisions_category | GFX_decision_hol_exchange_intelligence_data |  |  |  | SWI.txt |
| SWI_buy_ships_from_country | SWI_federal_council_decisions_category | GFX_decision_generic_naval | 50 |  |  | SWI.txt |
| SWI_cancel_fascism_ban | SWI_federal_council_decisions_category | GFX_decision_generic_break_treaty | 250 |  |  | SWI.txt |
| SWI_dismiss_council | SWI_federal_council_decisions_category | GFX_decision_SWI_dismiss_council | 350 |  |  | SWI.txt |
| SWI_embrace_communism | SWI_federal_council_decisions_category | GFX_decision_generic_civil_support | 300 |  |  | SWI.txt |
| SWI_declare_the_alpine_confederation | SWI_federal_council_decisions_category | GFX_decision_generic_form_nation | 100 |  |  | SWI.txt |
| SWI_declare_the_alpine_union | SWI_federal_council_decisions_category | GFX_decision_generic_civil_support | 100 |  |  | SWI.txt |
| SWI_recently_finished_president_initiative_mission | SWI_federal_council_decisions_category | GFX_decision_SWI_elect_confederation_president |  |  |  | SWI.txt |
| SWI_defense_fund_drive | SWI_federal_council_decisions_category | GFX_decision_generic_fundraising |  |  |  | SWI.txt |
| SWI_swiss_democratic_tradition_campaign | SWI_federal_council_decisions_category | GFX_decision_SWI_swiss_democratic_tradition_campaign |  |  |  | SWI.txt |
| SWI_rally_workers | SWI_federal_council_decisions_category | GFX_decision_eng_propaganda_campaigns |  |  |  | SWI.txt |
| SWI_anti_fascist_drive | SWI_federal_council_decisions_category | GFX_decision_generic_civil_support |  |  |  | SWI.txt |
| SWI_focus_on_swiss_unity | SWI_federal_council_decisions_category | GFX_decision_SWI_focus_on_swiss_unity |  |  |  | SWI.txt |
| SWI_isolate_switzerland | SWI_federal_council_decisions_category | GFX_decision_SWI_isolate_switzerland |  |  |  | SWI.txt |
| SWI_militarization_drive | SWI_federal_council_decisions_category | GFX_decision_generic_military |  |  |  | SWI.txt |
| SWI_expand_covert_operations | SWI_federal_council_decisions_category | GFX_decision_SWI_expand_covert_operations |  |  |  | SWI.txt |
| SWI_expand_arms_industry | SWI_federal_council_decisions_category | GFX_decision_generic_industry |  | yes |  | SWI.txt |
| SWI_support_humanitarian_efforts | SWI_federal_council_decisions_category | GFX_decision_SWI_support_humanitarian_efforts |  |  |  | SWI.txt |
| SWI_diplomatic_mission | SWI_federal_council_decisions_category | GFX_decision_hol_exchange_intelligence_data |  |  |  | SWI.txt |
| SWI_spouse_fascism | SWI_federal_council_decisions_category | GFX_decision_hol_radio_oranje |  |  |  | SWI.txt |
| SWI_appease_fascists | SWI_federal_council_decisions_category | GFX_decision_eng_trade_unions_support |  |  |  | SWI.txt |
| SWI_renounce_guiding_principles | SWI_federal_council_decisions_category | GFX_decision_generic_break_treaty | 100 |  |  | SWI.txt |
| SWI_compromise_with_cantons | SWI_centralization_power_balance_decisions | GFX_decision_SWI_focus_on_swiss_unity |  |  |  | SWI.txt |
| SWI_consolidate_council_power | SWI_centralization_power_balance_decisions | GFX_decision_SWI_consolidate_council_power | 80 |  |  | SWI.txt |
| SWI_push_for_centralization | SWI_centralization_power_balance_decisions | GFX_decision_SWI_elect_confederation_president | 100 |  |  | SWI.txt |
| SWI_strengthen_military_high_command | SWI_centralization_power_balance_decisions | GFX_decision_SWI_guisan_speech | 150 |  |  | SWI.txt |
| SWI_rally_cantonal_defense | SWI_centralization_power_balance_decisions | GFX_decision_eng_propaganda_campaigns | 50 |  |  | SWI.txt |
| SWI_council_diplomatic_effort | SWI_centralization_power_balance_decisions | GFX_decision_hol_exchange_intelligence_data |  |  |  | SWI.txt |
| SWI_country_angry_mission | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_tank |  |  |  | SWI.txt |
| SWI_backchannel_negotiations | SWI_absolute_neutrality_decisions_category | decision_hol_exchange_intelligence_data | 90 |  |  | SWI.txt |
| SWI_show_of_defensive_force | SWI_absolute_neutrality_decisions_category | GFX_decision_SWI_swiss_military_tradition_campaign |  |  |  | SWI.txt |
| SWI_ask_for_guarantees | SWI_absolute_neutrality_decisions_category | GFX_decision_hol_attract_foreign_investors | 15 |  |  | SWI.txt |
| SWI_publicly_appease_country | SWI_absolute_neutrality_decisions_category | GFX_decision_eng_trade_unions_support | 50 |  |  | SWI.txt |
| SWI_publicly_reject_country | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_speech | 20 |  |  | SWI.txt |
| SWI_concessions_to_fascists | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_civil_support | 100 |  |  | SWI.txt |
| SWI_concessions_to_democrats | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_civil_support | 100 |  |  | SWI.txt |
| SWI_concessions_to_communists | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_civil_support | 100 |  |  | SWI.txt |
| SWI_concessions_to_monarchists | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_civil_support | 100 |  |  | SWI.txt |
| SWI_cancel_trade_agreement_prematurely | SWI_absolute_neutrality_decisions_category | GFX_decision_hol_attract_foreign_investors |  |  |  | SWI.txt |
| SWI_weapons_production_for_civilian_supplies | SWI_absolute_neutrality_decisions_category | GFX_decision_hol_attract_foreign_investors |  |  |  | SWI.txt |
| SWI_offer_operative | SWI_absolute_neutrality_decisions_category | GFX_decision_recruit_operative | 100 |  |  | SWI.txt |
| SWI_offer_intel_support | SWI_absolute_neutrality_decisions_category | GFX_decision_SWI_expand_covert_operations | 50 |  |  | SWI.txt |
| SWI_support_secret_ally | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_political_discourse | 100 |  |  | SWI.txt |
| SWI_offer_fascist_to_trade_gold | SWI_absolute_neutrality_decisions_category | GFX_decision_hol_attract_foreign_investors | 50 |  |  | SWI.txt |
| SWI_offer_democratic_to_trade_gold | SWI_absolute_neutrality_decisions_category | GFX_decision_hol_attract_foreign_investors | 50 |  |  | SWI.txt |
| SWI_seek_increased_trade | SWI_absolute_neutrality_decisions_category | GFX_decision_hol_attract_foreign_investors | 50 |  |  | SWI.txt |
| SWI_seize_fascist_gold | SWI_absolute_neutrality_decisions_category | GFX_decision_gre_investment_decisions | 50 |  |  | SWI.txt |
| SWI_seize_democratic_gold | SWI_absolute_neutrality_decisions_category | GFX_decision_gre_investment_decisions | 50 |  |  | SWI.txt |
| SWI_purchase_democratic_planes_fighters | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_air | 35 |  |  | SWI.txt |
| SWI_purchase_democratic_planes_cas | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_air | 35 |  |  | SWI.txt |
| SWI_purchase_fascist_planes_fighters | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_air | 35 |  |  | SWI.txt |
| SWI_purchase_fascist_planes_cas | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_air | 35 |  |  | SWI.txt |
| SWI_fund_resistance_decision | SWI_absolute_neutrality_decisions_category | GFX_decision_generic_civil_support | 50 |  |  | SWI.txt |
| SWI_activate_militia | SWI_military_readiness_decisions_category | GFX_decision_generic_civil_support |  |  |  | SWI.txt |
| SWI_deactivate_militia | SWI_military_readiness_decisions_category | GFX_decision_POL_looming_peasants_strike |  |  |  | SWI.txt |
| SWI_militia_active | SWI_military_readiness_decisions_category | GFX_decision_SWI_swiss_military_tradition_campaign |  |  |  | SWI.txt |
| SWI_building_up_military_readiness_mission | SWI_military_readiness_decisions_category | GFX_decision_SWI_swiss_military_tradition_campaign |  |  |  | SWI.txt |
| SWI_confederation_president_speech | SWI_military_readiness_decisions_category | GFX_decision_generic_speech | 100 |  |  | SWI.txt |
| SWI_guisan_speech | SWI_military_readiness_decisions_category | GFX_decision_SWI_guisan_speech |  |  |  | SWI.txt |
| SWI_military_training_drive | SWI_military_readiness_decisions_category | GFX_decision_generic_military |  |  |  | SWI.txt |
| SWI_expand_military_staff | SWI_military_readiness_decisions_category | GFX_decision_generic_army_support |  |  |  | SWI.txt |
| SWI_broaden_militias | SWI_military_readiness_decisions_category | GFX_decision_POL_looming_peasants_strike |  |  |  | SWI.txt |
| SWI_arm_the_population | SWI_military_readiness_decisions_category | generic_prepare_civil_war |  |  |  | SWI.txt |
| SWI_focus_on_the_economy | SWI_military_readiness_decisions_category | GFX_decision_generic_factory |  |  |  | SWI.txt |
| SWI_focus_on_military_production | SWI_military_readiness_decisions_category | GFX_decision_generic_industry |  |  |  | SWI.txt |
| SWI_improve_divisions | SWI_military_readiness_decisions_category | GFX_decision_generic_military |  |  |  | SWI.txt |
| SWI_improve_deployment_speed | SWI_military_readiness_decisions_category | GFX_decision_generic_military |  |  |  | SWI.txt |
| SWI_field_hospital_for_militias | SWI_military_readiness_decisions_category | GFX_decision_generic_research |  | yes |  | SWI.txt |
| SWI_support_for_militias | SWI_military_readiness_decisions_category | GFX_decision_generic_army_support |  | yes |  | SWI.txt |
| unite_hispaniola | hispaniola_category | generic_form_nation |  |  |  | TOA_formable_nation_decisions.txt |
| reunite_peru_bolivia | peru_bolivia_category | generic_form_nation |  |  |  | TOA_formable_nation_decisions.txt |
| unite_guiana | guianas_category | generic_form_nation |  |  |  | TOA_formable_nation_decisions.txt |
| PAR_flip_to_fascism | political_actions | generic_civil_support | 35 |  | Trial of Allegiance | TOA_shared_decisions.txt |
| PAR_appoint_estigarribia_as_leader | political_actions | generic_civil_support | 75 |  | Trial of Allegiance | TOA_shared_decisions.txt |
| JUNO_specialize_in_infantry_tanks | improving_our_army_category | GFX_decision_generic_tank |  |  |  | TOA_shared_decisions.txt |
| JUNO_specialize_in_breakthrough_tanks | improving_our_army_category | GFX_decision_generic_tank |  |  |  | TOA_shared_decisions.txt |
| JUNO_invite_japanese_army_advisors | improving_our_army_category | GFX_decision_generic_army_support | 75 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_american_army_advisors | improving_our_army_category | GFX_decision_generic_army_support | 75 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_soviet_army_advisors | improving_our_army_category | GFX_decision_generic_army_support | 75 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_german_army_advisors | improving_our_army_category | GFX_decision_generic_army_support | 75 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_italian_army_advisors | improving_our_army_category | GFX_decision_generic_army_support | 75 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_british_army_advisors | improving_our_army_category | GFX_decision_generic_army_support | 75 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_french_army_advisors | improving_our_army_category | GFX_decision_generic_army_support | 75 |  |  | TOA_shared_decisions.txt |
| JUNO_purchase_aircraft | improving_our_army_category | generic_air | 50 |  | Trial of Allegiance | TOA_shared_decisions.txt |
| purchase_dreadnoughts_usa | south_american_naval_arms_race_category | GFX_decision_generic_naval | 100 |  |  | TOA_shared_decisions.txt |
| purchase_dreadnoughts_ENG | south_american_naval_arms_race_category | GFX_decision_generic_naval | 100 |  |  | TOA_shared_decisions.txt |
| purchase_dreadnoughts_FRA | south_american_naval_arms_race_category | GFX_decision_generic_naval | 100 |  |  | TOA_shared_decisions.txt |
| purchase_dreadnoughts_ITA | south_american_naval_arms_race_category | GFX_decision_generic_naval | 100 |  |  | TOA_shared_decisions.txt |
| purchase_dreadnoughts_GER | south_american_naval_arms_race_category | GFX_decision_generic_naval | 100 |  |  | TOA_shared_decisions.txt |
| purchase_dreadnoughts_JAP | south_american_naval_arms_race_category | GFX_decision_generic_naval | 100 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_japanese_naval_advisors | south_american_naval_arms_race_category | GFX_decision_generic_army_support | 50 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_american_navy_advisors | south_american_naval_arms_race_category | GFX_decision_generic_army_support | 50 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_soviet_navy_advisors | south_american_naval_arms_race_category | GFX_decision_generic_army_support | 50 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_german_navy_advisors | south_american_naval_arms_race_category | GFX_decision_generic_army_support | 50 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_italian_navy_advisors | south_american_naval_arms_race_category | GFX_decision_generic_army_support | 50 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_british_navy_advisors | south_american_naval_arms_race_category | GFX_decision_generic_army_support | 50 |  |  | TOA_shared_decisions.txt |
| JUNO_invite_french_navy_advisors | south_american_naval_arms_race_category | GFX_decision_generic_army_support | 50 |  |  | TOA_shared_decisions.txt |
| JUNO_promote_immigration_in_state_ITA | JUNO_promote_immigration_cat | GFX_decision_SWI_support_humanitarian_efforts | 150 | yes |  | TOA_shared_decisions.txt |
| JUNO_promote_immigration_in_state_JAP | JUNO_promote_immigration_cat | GFX_decision_SWI_support_humanitarian_efforts | 150 | yes |  | TOA_shared_decisions.txt |
| JUNO_promote_immigration_in_state_POR | JUNO_promote_immigration_cat | GFX_decision_SWI_support_humanitarian_efforts | 150 | yes |  | TOA_shared_decisions.txt |
| JUNO_promote_immigration_in_state_GER | JUNO_promote_immigration_cat | GFX_decision_SWI_support_humanitarian_efforts | 150 | yes |  | TOA_shared_decisions.txt |
| JUNO_promote_immigration_in_state_SPR | JUNO_promote_immigration_cat | GFX_decision_SWI_support_humanitarian_efforts | 150 | yes |  | TOA_shared_decisions.txt |
| JUNO_promote_immigration_in_state_ENG | JUNO_promote_immigration_cat | GFX_decision_SWI_support_humanitarian_efforts | 150 | yes |  | TOA_shared_decisions.txt |
| TOA_blockade_ven | political_actions | generic_naval | 25 |  |  | TOA_shared_decisions.txt |
| TUR_recall_ataturk_to_active_service | political_actions | generic_army_support | 0 | yes | Battle for the Bosporus | TUR.txt |
| TUR_alter_the_royal_laws_of_succession | political_actions | eng_trade_unions_support | 120 | yes |  | TUR.txt |
| TUR_republicanism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 25 |  |  | TUR.txt |
| TUR_secularism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 50 |  |  | TUR.txt |
| TUR_populism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 50 |  |  | TUR.txt |
| TUR_nationalism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 75 |  |  | TUR.txt |
| TUR_etatism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 75 |  |  | TUR.txt |
| TUR_reformism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 75 |  |  | TUR.txt |
| TUR_revolutionism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 75 |  |  | TUR.txt |
| TUR_liberalism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 75 |  |  | TUR.txt |
| TUR_jihad_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 50 |  |  | TUR.txt |
| TUR_fidelity_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 75 |  |  | TUR.txt |
| TUR_absolutism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 120 |  |  | TUR.txt |
| TUR_ultranationalism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 100 |  |  | TUR.txt |
| TUR_socialism_decision | TUR_the_constitutional_arrows_category | tur_the_constitutional_arrows | 75 |  |  | TUR.txt |
| TUR_open_the_nazilli_callico_factory | TUR_industrial_projects_category | generic_factory |  | yes |  | TUR.txt |
| TUR_finance_the_bursa_merinos_factory | TUR_industrial_projects_category | generic_factory |  | yes |  | TUR.txt |
| TUR_fund_the_gemlik_silk_factory | TUR_industrial_projects_category | generic_factory |  | yes |  | TUR.txt |
| TUR_construct_the_zonguldak_coal_refinery | TUR_industrial_projects_category | generic_factory |  | yes |  | TUR.txt |
| TUR_modernise_the_general_directorate_of_military_factories | TUR_industrial_projects_category | generic_factory | 300 | yes |  | TUR.txt |
| TUR_authorise_the_nuri_killigil_factory | TUR_industrial_projects_category | generic_factory |  | yes | Arms Against Tyranny | TUR.txt |
| TUR_sponsor_the_nuri_demirag_besiktas_aircraft_factory | TUR_industrial_projects_category | generic_factory |  | yes | By Blood Alone | TUR.txt |
| TUR_invest_in_malatya_cigarette_factory | TUR_industrial_projects_category | generic_factory |  | yes |  | TUR.txt |
| TUR_bankroll_the_malatya_clothing_factory | TUR_industrial_projects_category | generic_factory |  | yes |  | TUR.txt |
| TUR_subsidise_the_karabuk_iron_steel_factory | TUR_industrial_projects_category | generic_factory |  | yes |  | TUR.txt |
| TUR_sponsor_petrol_olfisis_formation | TUR_industrial_projects_category | generic_construction | 75 | yes |  | TUR.txt |
| TUR_repeal_the_wealth_tax | economy_decisions | generic_political_rally | 50 | yes |  | TUR.txt |
| TUR_repeal_the_faith_tax | economy_decisions | generic_political_rally | 50 | yes |  | TUR.txt |
| TUR_abolish_etatism | economy_decisions | generic_break_treaty | 100 | yes |  | TUR.txt |
| TUR_absorb_the_tpda | economy_decisions | eng_trade_unions_support | 120 | yes |  | TUR.txt |
| TUR_pay_off_our_debts | economy_decisions | hol_exchange_intelligence_data | 120 |  |  | TUR.txt |
| TUR_discuss_investment_possibilities_with_FROM | economy_decisions | generic_construction | 75 |  |  | TUR.txt |
| ROOT_invest_in_turkish_state_building | economy_decisions | generic_construction | 25 |  |  | TUR.txt |
| ROOT_invest_in_turkish_state_light_industry | economy_decisions | generic_construction | 30 |  |  | TUR.txt |
| ROOT_invest_in_turkish_state_heavy_industry | economy_decisions | generic_construction | 50 |  |  | TUR.txt |
| TUR_kurdish_resistance_escalation_mission | TUR_kurdish_state_management_category | tur_unifying_the_country |  |  |  | TUR.txt |
| TUR_counter_the_rebels_in_diyarbakir | TUR_kurdish_state_management_category | faction_tur_kurdish |  |  |  | TUR.txt |
| TUR_counter_the_rebels_in_erzurum | TUR_kurdish_state_management_category | faction_tur_kurdish |  |  |  | TUR.txt |
| TUR_counter_the_rebels_in_van | TUR_kurdish_state_management_category | faction_tur_kurdish |  |  |  | TUR.txt |
| TUR_counter_the_rebels_in_hakkari | TUR_kurdish_state_management_category | faction_tur_kurdish |  |  |  | TUR.txt |
| TUR_offer_conscription_exceptions_to_kurdish_groups | TUR_kurdish_state_management_category | generic_military | 120 |  |  | TUR.txt |
| TUR_integrate_diyarbakir | TUR_kurdish_state_management_category | faction_tur_kurdish | 200 |  |  | TUR.txt |
| TUR_integrate_hakkari | TUR_kurdish_state_management_category | faction_tur_kurdish | 200 |  |  | TUR.txt |
| TUR_integrate_tunceli | TUR_kurdish_state_management_category | faction_tur_kurdish | 200 |  |  | TUR.txt |
| TUR_integrate_van | TUR_kurdish_state_management_category | faction_tur_kurdish | 200 |  |  | TUR.txt |
| TUR_counter_influence_of_fundamentalists_in_state | TUR_fundamentalist_state_management_category | gre_faction_management | 100 |  |  | TUR.txt |
| TUR_hold_a_march_in_state | TUR_fundamentalist_state_management_category | oppression | 150 |  |  | TUR.txt |
| TUR_empower_fundamentalists_in_state | TUR_fundamentalist_state_management_category | generic_political_rally | 200 |  |  | TUR.txt |
| TUR_acquiesce_to_fundamentalists | TUR_fundamentalist_state_management_category | generic_political_discourse | 200 |  |  | TUR.txt |
| TUR_root_out_kemalists_in_state | TUR_kemalist_state_management_category | generic_arrest | 100 |  |  | TUR.txt |
| TUR_traditionalist_infiltration_mission | TUR_the_enemy_within | tur_unifying_the_country |  |  |  | TUR.txt |
| TUR_thwarting_traditionalist_infiltration | TUR_the_enemy_within | generic_assassination |  |  |  | TUR.txt |
| TUR_increase_influence_of_fundamentalists_in_state | TUR_the_enemy_within | eng_propaganda_campaigns | 100 |  |  | TUR.txt |
| TUR_kemalist_infiltration_mission | TUR_the_enemy_within | tur_unifying_the_country |  |  |  | TUR.txt |
| TUR_thwarting_kemalist_infiltration | TUR_the_enemy_within | tur_unifying_the_country |  |  |  | TUR.txt |
| TUR_entrench_kemalism_in_state | TUR_the_enemy_within | hol_radio_oranje | 100 |  |  | TUR.txt |
| TUR_modernize_our_tactics | TUR_reforming_our_armed_forces_category | generic_military | 50 | yes |  | TUR.txt |
| TUR_teach_the_proper_use_of_modern_infrastructure | TUR_reforming_our_armed_forces_category | generic_military | 50 | yes |  | TUR.txt |
| TUR_commence_an_overhaul_of_our_training_methods | TUR_reforming_our_armed_forces_category | generic_military | 50 | yes |  | TUR.txt |
| TUR_streamline_communication_methods_between_ships | TUR_reforming_our_armed_forces_category | generic_naval | 50 | yes |  | TUR.txt |
| TUR_put_new_safety_regulations_regarding_the_operation_of_aircraft_into_effect | TUR_reforming_our_armed_forces_category | generic_air | 50 | yes |  | TUR.txt |
| TUR_ataturk_health_worsening_crisis | TUR_the_fading_father_category | tur_the_constitutional_arrows |  |  |  | TUR.txt |
| TUR_seek_treatment_for_ataturk | TUR_the_fading_father_category | generic_research |  |  |  | TUR.txt |
| TUR_retire_ataturk | TUR_the_fading_father_category | eng_trade_unions_demand |  | yes |  | TUR.txt |
| TUR_etatism_crisis_1 | crisis | generic_political_rally |  |  |  | TUR.txt |
| TUR_etatism_crisis_2 | crisis | generic_political_rally |  |  |  | TUR.txt |
| TUR_etatism_crisis_3 | crisis | generic_political_rally |  |  |  | TUR.txt |
| TUR_etatism_crisis_4 | crisis | generic_political_rally |  |  |  | TUR.txt |
| TUR_kurdish_pacification_debug_decision | category_faction_debug_decisions | faction_tur_kurdish | 0 |  |  | TUR.txt |
| TUR_kurdish_agitation_debug_decision | category_faction_debug_decisions | faction_tur_kurdish | 0 |  |  | TUR.txt |
| TUR_kurdish_integration_debug_decision | category_faction_debug_decisions | faction_tur_kurdish | 0 |  |  | TUR.txt |
| TUR_kurdish_exemptions_debug_decision | category_faction_debug_decisions | faction_tur_kurdish | 0 |  |  | TUR.txt |
| TUR_traditionalist_unrest_debug_decision | category_faction_debug_decisions | faction_tur_traditionalist | 0 |  |  | TUR.txt |
| TUR_traditionalist_succor_debug_decision | category_faction_debug_decisions | faction_tur_traditionalist | 0 |  |  | TUR.txt |
| TUR_kemalist_ideological_entrenchment_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| TUR_kemalist_make_angry_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| TUR_kemalist_make_happy_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| TUR_kemalist_officers_loyal_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| TUR_kemalist_officers_neutral_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| TUR_kemalist_officers_disloyal_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| TUR_kemalist_officers_empower_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| TUR_kemalist_officers_depower_debug_decision | category_faction_debug_decisions | faction_tur_kemalist | 0 |  |  | TUR.txt |
| USA_homeland_defense | war_measures | generic_prepare_civil_war | 50 | yes |  | USA.txt |
| USA_raise_silver_legions | war_measures | generic_prepare_civil_war | 10 |  |  | USA.txt |
| USA_raise_the_free_corps | war_measures | generic_prepare_civil_war | 0 | yes |  | USA.txt |
| USA_CSA_set_up_provisional_government | war_measures |  | 0 |  |  | USA.txt |
| USA_CSA_set_up_provisional_government2 | war_measures |  | 0 |  |  | USA.txt |
| USA_CSA_set_up_provisional_government3 | war_measures |  | 0 |  |  | USA.txt |
| USA_order_weapons_in_USB | war_measures | generic_prepare_civil_war | 25 |  |  | USA.txt |
| USA_order_artillery_in_USB | war_measures | ger_military_buildup | 50 |  |  | USA.txt |
| USA_order_fighters_in_USB | war_measures | generic_air | 50 |  | By Blood Alone | USA.txt |
| USA_order_bombers_in_USB | war_measures | generic_air | 50 |  | By Blood Alone | USA.txt |
| USA_establish_personal_communication_with_former_naval_person | USA_aid_britain | generic_political_discourse | 50 | yes |  | USA.txt |
| USA_battle_domestic_isolationism | USA_aid_britain | generic_civil_support | 50 | yes |  | USA.txt |
| USA_emergency_arms_deliveries | USA_aid_britain | generic_prepare_civil_war | 50 | yes |  | USA.txt |
| USA_arsenal_of_democracy_decision | USA_aid_britain | generic_industry | 50 | yes |  | USA.txt |
| USA_support_the_anti_fascist_war | foreign_support | generic_industry | 25 |  |  | USA.txt |
| USA_guns_for_the_anti_fascist_war | foreign_support | generic_prepare_civil_war | 25 |  |  | USA.txt |
| USA_invite_donations_FROM | USA_foreign_support | ger_mefo_bills | 25 |  |  | USA.txt |
| USA_smuggle_weapons_FROM | USA_foreign_support | generic_prepare_civil_war | 50 |  |  | USA.txt |
| USA_training_camps_in_FROM | USA_foreign_support | generic_prepare_civil_war | 75 |  |  | USA.txt |
| USA_pilot_training_in_FROM | USA_foreign_support | generic_air | 75 |  |  | USA.txt |
| USA_fund_shipyards_FROM | USA_foreign_support | generic_construction | 125 |  |  | USA.txt |
| USA_celebrate_montgomery_convention_day | USA_honor_the_confederacy | generic_nationalism | 25 | yes |  | USA.txt |
| USA_move_government_to_richmond | USA_honor_the_confederacy | generic_nationalism | 25 | yes |  | USA.txt |
| USA_secure_state_rights | USA_honor_the_confederacy | generic_nationalism | 75 | yes |  | USA.txt |
| USA_permit_confederate_flags | USA_honor_the_confederacy | generic_nationalism | 75 | yes |  | USA.txt |
| USA_constitutional_convention | USA_honor_the_confederacy | eng_trade_unions_support | 100 | yes |  | USA.txt |
| USA_communal_domain | economy_decisions | generic_operation | 50 |  |  | USA.txt |
| USA_guns_for_the_anti_bolshevist_war | foreign_politics | generic_prepare_civil_war | 25 |  |  | USA.txt |
| USA_form_defensive_alliance_north_american_dominion | foreign_politics | generic | 25 | yes |  | USA.txt |
| USA_join_defensive_alliance_north_american_dominion | foreign_politics | generic | 25 | yes |  | USA.txt |
| USA_join_the_unions | foreign_politics | infiltrate_state |  | yes |  | USA.txt |
| USA_execute_war_plan_green | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_red | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_silver | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_ruby | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_scarlet_garnet | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_orange | USA_war_plans | generic_operation |  | yes | No Compromise, No Surrender | USA.txt |
| USA_execute_war_plan_yellow | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_crimson | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_gray | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_gold | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_black | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_execute_war_plan_white | USA_war_plans | generic_operation |  | yes |  | USA.txt |
| USA_request_mandate_against_FROM | USA_intervention_mandate |  | 50 |  |  | USA.txt |
| USA_prepare_intervention_in_europe_against_FROM | USA_intervention_mandate | generic_prepare_civil_war | 75 |  |  | USA.txt |
| USA_prepare_intervention_in_asia_against_FROM | USA_intervention_mandate | generic_prepare_civil_war | 75 |  |  | USA.txt |
| USA_protest_anschluss | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_munich | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_molotov_ribbentrop | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_baltic_annexation | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_army_of_aggression | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_albania | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_yugoslavia | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_china | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_indochina | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_protest_panay | USA_intervention_mandate | eng_propaganda_campaigns | 25 | yes |  | USA.txt |
| USA_request_monroe_mandate_against_FROM | USA_intervention_mandate |  | 50 |  |  | USA.txt |
| USA_demand_liberation | USA_intervention_mandate |  | 50 |  |  | USA.txt |
| USA_freedom_for_Papua | USA_decolonisation |  | 25 | yes |  | USA.txt |
| USA_indonesian_liberation | USA_decolonisation |  | 25 | yes |  | USA.txt |
| USA_initiate_the_greenland_patrol | operations | generic_operation | 50 | yes | Arms Against Tyranny | USA.txt |
| HOL_offer_venezuelan_protection | VEN_abc_islands | decision_generic_nationalism | 25 | yes |  | VEN.txt |
| WLS_restore_y_wladfa_decision | political_actions | GFX_decision_generic_nationalism | 75 |  | Trial of Allegiance | WLS.txt |
| WLA_reclaim_the_old_homeland_decision | political_actions | GFX_decision_generic_nationalism | 50 |  | Trial of Allegiance | WLS.txt |
| WTT_border_conflict_initiate_incident | CHI_border_clashes | border_war | 100 |  |  | WTT_border_conflicts.txt |
| WTT_border_conflict_incident_warning_defender | CHI_border_clashes | border_war |  | yes |  | WTT_border_conflicts.txt |
| WTT_border_conflict_escalation_warning_defender | CHI_border_clashes | border_war |  | yes |  | WTT_border_conflicts.txt |
| WTT_escalate_incident_to_border_conflict | CHI_border_clashes | border_war |  | yes |  | WTT_border_conflicts.txt |
| WTT_border_conflict_time_until_cancelled | CHI_border_clashes | border_war |  | yes |  | WTT_border_conflicts.txt |
| WTT_border_conflict_escalate_conflict | CHI_border_clashes | decision_generic_ignite_civil_war | 200 | yes |  | WTT_border_conflicts.txt |
| WTT_border_conflict_escalate_to_war | CHI_border_clashes | decision_generic_ignite_civil_war | 150 | yes |  | WTT_border_conflicts.txt |
| WTT_border_conflict_back_out_of_conflict | CHI_border_clashes |  |  | yes |  | WTT_border_conflicts.txt |
| WTT_national_leadership | CHI_political_power_struggle | generic_nationalism | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_fujian | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_zhejiang | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_shandong | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_jiangsu | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_chongqing | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_wuhan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_nanjing | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_jiangxi | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_xikang | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_hunan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_guizhou | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_sichuan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_anhui | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_henan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_beijing | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_shanghai | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_hebei | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_hubei | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_shanxi | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_suiyuan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_shaanxi | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_gansu | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_qinghai | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_ningxia | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_taklamakan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_urumqi | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_dzungaria | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_yarkand | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_yunnan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_hainan | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_guangzhou | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_guangdong | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_nanning | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_build_support_in_guangxi | CHI_political_power_struggle | generic_political_discourse | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_seek_support_from_warlord | CHI_political_power_struggle | generic_civil_support | 0 | yes |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_pay_for_support_from_warlord_PP | CHI_political_power_struggle | generic_civil_support |  | yes |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_pay_for_support_from_warlord_equipment | CHI_political_power_struggle | generic_civil_support |  | yes |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_pay_for_support_from_warlord_xp | CHI_political_power_struggle | generic_civil_support |  | yes |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_fujian | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_zhejiang | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_shandong | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_jiangsu | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_jiangxi | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_xikang | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_hunan | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_guizhou | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_sichuan | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_anhui | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_henan | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_beijing | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_shanghai | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_hebei | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_hubei | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_shanxi | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_suiyuan | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_shaanxi | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_gansu | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_qinghai | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_ningxia | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_taklamakan | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_urumqi | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_dzungaria | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_yarkand | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_yunnan | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_hainan | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_guangzhou | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_guangdong | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_nanning | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| WTT_remove_opposition_in_guangxi | CHI_political_power_struggle | oppression | 0 |  |  | WTT_politcal_power_struggle_decisions.txt |
| YUG_instigate_in_bulgaria | YUG_peasant_uprisings | decision_generic_nationalism | 25 | yes |  | YUG.txt |
| YUG_instigate_in_albania | YUG_peasant_uprisings | decision_generic_nationalism | 25 | yes |  | YUG.txt |
| YUG_instigate_in_greece | YUG_peasant_uprisings | decision_generic_nationalism | 25 | yes |  | YUG.txt |
| YUG_instigate_in_romania | YUG_peasant_uprisings | decision_generic_nationalism | 25 | yes |  | YUG.txt |
| YUG_instigate_in_hungary | YUG_peasant_uprisings | decision_generic_nationalism | 25 | yes |  | YUG.txt |
| YUG_instigate_in_turkey | YUG_peasant_uprisings | decision_generic_nationalism | 25 | yes |  | YUG.txt |
| YUG_propaganda_in_target | YUG_peasant_uprisings | decision_generic_nationalism | 25 |  |  | YUG.txt |
| YUG_arm_communist_militants | YUG_peasant_uprisings | decision_generic_nationalism | 25 |  |  | YUG.txt |
| YUG_communist_coup | YUG_peasant_uprisings | decision_generic_nationalism | 50 |  |  | YUG.txt |
| YUG_abandon_communist_effort | YUG_peasant_uprisings | decision_generic_nationalism | 0 |  |  | YUG.txt |
| YUG_ustasa_uprising | YUG_crush_ustasa | generic_ignite_civil_war |  | yes |  | YUG.txt |
| YUG_ustasa_crushed_mission | YUG_crush_ustasa | generic_ignite_civil_war |  | yes |  | YUG.txt |
| YUG_croat_concessions | YUG_delay_ustasa_uprising | eng_propaganda_campaigns | 15 |  |  | YUG.txt |
| YUG_positive_discrimination_croat | YUG_delay_ustasa_uprising | eng_propaganda_campaigns | 15 |  |  | YUG.txt |
| YUG_listening_posts_croatia | YUG_delay_ustasa_uprising | eng_propaganda_campaigns | 15 |  |  | YUG.txt |
| YUG_croat_concessions_cooldown | YUG_delay_ustasa_uprising | generic_ignite_civil_war |  | yes |  | YUG.txt |
| YUG_positive_discrimination_croat_cooldown | YUG_delay_ustasa_uprising | generic_ignite_civil_war |  | yes |  | YUG.txt |
| YUG_listening_posts_cooldown | YUG_delay_ustasa_uprising | generic_ignite_civil_war |  | yes |  | YUG.txt |
| YUG_raid_croat_villages | YUG_progress_crushing_decisions | eng_propaganda_campaigns | 15 |  |  | YUG.txt |
| YUG_shut_down_recruitment_centers | YUG_progress_crushing_decisions | eng_propaganda_campaigns | 15 |  |  | YUG.txt |
| YUG_arrest_ustasa_leaders | YUG_progress_crushing_decisions | eng_propaganda_campaigns | 15 |  |  | YUG.txt |
| YUG_croatian_recruitment | YUG_progress_crushing_decisions | eng_propaganda_campaigns | 15 |  |  | YUG.txt |
| YUG_croat_raid_cooldown | YUG_progress_crushing_decisions | generic_ignite_civil_war |  | yes |  | YUG.txt |
| YUG_shut_down_recruitment_centers_cooldown | YUG_progress_crushing_decisions | generic_ignite_civil_war |  | yes |  | YUG.txt |
| YUG_arrest_ustasa_leaders_cooldown | YUG_progress_crushing_decisions | generic_ignite_civil_war |  | yes |  | YUG.txt |
