# Peace Cost Modifiers

Source: `common/peace_conference/cost_modifiers/*.txt`

| modifier_key | category_key | peace_action_type | cost_multiplier | dlc_source | source_file |
|---|---|---|---|---|---|
| generic_is_core | is_core | take_states | 0.25 |  | 00_generic_peace.txt |
| generic_is_core_of_puppet | is_core | take_states | 0.5 |  | 00_generic_peace.txt |
| generic_is_not_losers_core | is_core | take_states | 0.95 |  | 00_generic_peace.txt |
| generic_has_claim | has_claim | take_states | 0.9 |  | 00_generic_peace.txt |
| generic_occupies_state | occupation | take_states puppet liberate force_government | 0.80 |  | 00_generic_peace.txt |
| fascism_take_state | ideology | take_states | 0.9 |  | 00_generic_peace.txt |
| fascism_liberate | ideology | liberate | 1.3 |  | 00_generic_peace.txt |
| fascism_puppet | ideology | puppet | 0.95 |  | 00_generic_peace.txt |
| communism_take_state | ideology | take_states | 1.0 |  | 00_generic_peace.txt |
| communism_liberate | ideology | liberate | 1.3 |  | 00_generic_peace.txt |
| communism_puppet | ideology | puppet | 0.9 |  | 00_generic_peace.txt |
| democracy_take_state | ideology | take_states | 1.3 |  | 00_generic_peace.txt |
| democracy_liberate | ideology | liberate | 0.9 |  | 00_generic_peace.txt |
| democracy_force_government_on_evil_fascism | ideology | force_government | 0.9 |  | 00_generic_peace.txt |
| democracy_force_government_on_evil_communism | ideology | force_government | 0.9 |  | 00_generic_peace.txt |
| democracy_puppet | ideology | puppet | 1.2 |  | 00_generic_peace.txt |
| generic_major_participant_has_core | core_of_ally | take_states puppet force_government | 3.0 |  | 00_generic_peace.txt |
| defensive_war_liberate | defensive_war | liberate force_government | 0.95 |  | 00_generic_peace.txt |
| defensive_war_take_state | defensive_war | take_state | 1.1 |  | 00_generic_peace.txt |
| belonged_to_someone_else | belonged_to_someone_else | take_states puppet force_government | 1.05 |  | 00_generic_peace.txt |
| dormant_national_identity |  | liberate | 1.25 |  | 00_generic_peace.txt |
| war_of_independence | other | take_states puppet force_government liberate | 1.25 |  | 00_generic_peace.txt |
| war_of_independence_crushed | other | take_states | 0.5 |  | 00_generic_peace.txt |
| eat_the_rich | ideology | take_states puppet force_government liberate | 0.80 |  | 00_generic_peace.txt |
| democracy_major_force_gov | ideology | force_government | 0.70 |  | 00_generic_peace.txt |
| continuous_force_gov | continuous_political_action | force_government | 0.85 |  | 00_generic_peace.txt |
| continuous_puppet | continuous_political_action | puppet | 0.85 |  | 00_generic_peace.txt |
| AFG_agreed_state_peace_cost_modifier | treaties_or_conferences | take_states | 0.55 |  | AFG_peace.txt |
| CHI_re_re_organization | events_or_focuses | take_states | 0.75 |  | CHI_peace.txt |
| DEN_puppet_former_overlord | events_or_focuses | puppet | 0.75 |  | DEN_peace.txt |
| DEN_take_former_overlords_state | events_or_focuses | take_states | 0.75 |  | DEN_peace.txt |
| DEN_topple_former_overlords_government | events_or_focuses | force_government liberate | 0.7 |  | DEN_peace.txt |
| ENG_operation_fork |  | puppet | 0.15 |  | ENG_peace.txt |
| ETH_agreed_state_peace_cost_modifier | treaties_or_conferences | take_states | 0.55 |  | ETH_peace.txt |
| ETH_end_of_civil_war_cost_modifier_low | treaties_or_conferences | take_states | 0.2 |  | ETH_peace.txt |
| faction_rule_modifier_encourage_puppet |  | puppet | 0.8 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_discourage_puppet |  | puppet | 2 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_encourage_liberate |  | liberate | 0.8 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_encourage_force_government |  | force_government | 0.8 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_encourage_take_states |  | take_states | 0.9 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_encourage_take_claimed_states |  | take_states | 0.8 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_encourage_chinese_states |  | take_states puppet | 0.95 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_extra_cost_take_states |  | take_states | 1.05 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_extra_cost_puppet |  | puppet | 1.05 |  | faction_peace_action_modifiers.txt |
| faction_rule_modifier_extra_cost_liberate |  | liberate | 1.05 |  | faction_peace_action_modifiers.txt |
| FIN_expansionist_policies | events_or_focuses | take_states | 0.75 |  | FIN_peace.txt |
| FIN_finnish_irredentism_desires | events_or_focuses | take_states | 0.65 |  | FIN_peace.txt |
| FIN_crown_prince_of_finland_baltic_cores | events_or_focuses | take_states | 0.25 |  | FIN_peace.txt |
| FIN_crown_prince_of_finland_annex | events_or_focuses | take_states | 0.75 |  | FIN_peace.txt |
| FRA_retake_french_territory_modifier | is_core | take_states | 0.25 |  | FRA_peace.txt |
| GER_sphere_of_influencee | events_or_focuses | take_states | 1.15 |  | GER_peace.txt |
| GER_SOV_sphere_of_influence | events_or_focuses | take_states | 1.15 |  | GER_peace.txt |
| GER_asian_sphere_of_influencee | events_or_focuses | take_states | 1.15 |  | GER_peace.txt |
| GER_CHI_sphere_of_influence | events_or_focuses | take_states | 1.15 |  | GER_peace.txt |
| GER_liberate_oppressed_peoples | events_or_focuses | liberate | 0.6 |  | GER_peace.txt |
| GER_air_quotations_liberate_oppressed_peoples | events_or_focuses | puppet | 0.8 |  | GER_peace.txt |
| GER_silesia_is_ours_i_tell_ypu | events_or_focuses | take_states | 0.25 |  | GER_peace.txt |
| ITA_proclaim_the_empire | events_or_focuses | take_states | 0.85 |  | ITA_peace.txt |
| italy_catholic_dominion | events_or_focuses | puppet | 0.75 |  | ITA_peace.txt |
| italy_sol_dell_avvenire | events_or_focuses | take_states force_government | 0.75 |  | ITA_peace.txt |
| ITA_forced_peace_with_ethiopia | treaties_or_conferences | take_states | 1.5 |  | ITA_peace.txt |
| JAP_spiritual_mobilization | events_or_focuses | take_states | 1.5 |  | JAP_peace.txt |
| USA_the_baddies_no_broadcast | events_or_focuses | puppet | 0.6 |  | JAP_peace.txt |
| USA_the_baddies_broadcast | events_or_focuses | puppet | 0.25 |  | JAP_peace.txt |
| USA_the_baddies_take_japanese_islands | events_or_focuses | take_states | 0.75 |  | JAP_peace.txt |
| JAP_sea_greater_east_asian_co_properity_sphere_peace_puppeting | events_or_focuses | puppet liberate | 0.75 |  | JAP_peace.txt |
| PHI_re_re_organization | events_or_focuses | take_states | 0.75 |  | PHI_peace.txt |
| PRC_infiltrated_states_cheaper_to_take | treaties_or_conferences | take_states | 0.5 |  | PRC_peace.txt |
| RAJ_get_off_my_lawn_peace_cost_modifier | treaties_or_conferences | take_states | 0.05 |  | RAJ_peace.txt |
| GER_RK_cost_reduction_RKU | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKO | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKG | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKN | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKB | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKK | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKT | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKM | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKL | events_or_focuses | take_states | 0.25 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKH | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_GEN | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKI | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKC | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RGB | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RNA | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKA | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RKV | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RAN | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RCO | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RUS | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RAR | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RHD | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_ROA | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| GER_RK_cost_reduction_RAA | events_or_focuses | take_states | 0.5 |  | RK_peace.txt |
| yalta_pls_poland_into_space | treaties_or_conferences | take_states | 0.1 |  | yalta_peace.txt |
| yalta_pls_leave_poland_alone | treaties_or_conferences | take_states puppet liberate force_government | 3.0 |  | yalta_peace.txt |
| yalta_pls_leave_wgr_alone | treaties_or_conferences | take_states puppet liberate force_government | 4.0 |  | yalta_peace.txt |
| yalta_pls_leave_ddr_alone | treaties_or_conferences | take_states puppet liberate force_government | 4.0 |  | yalta_peace.txt |
| yalta_wgr | treaties_or_conferences | puppet | 0.5 |  | yalta_peace.txt |
| yalta_wgr_other_majors | treaties_or_conferences | puppet | 0.5 |  | yalta_peace.txt |
| yalta_wgr_force_government | treaties_or_conferences | force_government | 2 |  | yalta_peace.txt |
| yalta_ddr | treaties_or_conferences | puppet | 0.5 |  | yalta_peace.txt |
| yalta_ddr_force_government | treaties_or_conferences | force_government | 2 |  | yalta_peace.txt |
| yalta_reinstate_austria | treaties_or_conferences | liberate | 0.5 |  | yalta_peace.txt |
| yalta_aus_force_government | treaties_or_conferences | force_government | 0.5 |  | yalta_peace.txt |
| FRA_yalta_puppet_mosel_germany | events_or_focuses | puppet | 0.3 |  | yalta_peace.txt |
