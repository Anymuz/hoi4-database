-- HOI4 PostgreSQL API Views & Functions
--
-- 2 functions (date-parameterised) + 14 views across 3 slices.
--
-- Slice A — Country & State:   api_country_detail (function),
--                              api_state_detail (function)
-- Slice B — Domain Catalogs:   api_country_technologies, api_technology_tree,
--                              api_country_characters, api_country_divisions,
--                              api_country_naval, api_country_air,
--                              api_focus_tree_detail, api_equipment_catalog,
--                              api_ideas_detail
-- Slice C — DLC Systems:       api_mio_organization_detail, api_operation_detail,
--                              api_bop_detail, api_faction_detail,
--                              api_special_project_detail

-- ============================================================
-- Slice A — Country & State Detail
-- ============================================================

-- This is a FUNCTION, not a view. The difference:
--   VIEW  = a saved query, always runs the same way, no parameters.
--   FUNCTION = a saved query that accepts parameters (like a date).
--
-- p_date is the parameter. DEFAULT means "use 1936-01-01 if nothing is passed".
-- RETURNS TABLE lists every column the function outputs (same columns the old view had).
-- LANGUAGE sql means the body is plain SQL (not a different language).
-- STABLE tells PostgreSQL "this function only reads data, never changes it"
--    (helps the query planner optimise).
-- $$ ... $$ is just the way PostgreSQL wraps the function body — think of $$
--    as opening and closing quotes around the SQL.
--
-- How to call it:
--   SELECT * FROM api_country_detail('1936-01-01');       -- 1936 start
--   SELECT * FROM api_country_detail('1939-08-14');       -- 1939 start
--   SELECT * FROM api_country_detail();                   -- defaults to 1936

CREATE OR REPLACE FUNCTION api_country_detail(p_date DATE DEFAULT '1936-01-01')
RETURNS TABLE (
    tag              CHAR(3),
    country_name     TEXT,
    capital_state_id INT,
    stability        NUMERIC,
    war_support      NUMERIC,
    graphical_culture    VARCHAR,
    graphical_culture_2d VARCHAR,
    color_rgb            JSONB,
    owned_states         JSONB,
    starting_technologies JSONB
)
LANGUAGE sql STABLE AS $$
    WITH ownership AS (
        SELECT soh.state_id, soh.owner_tag, COALESCE(soh.controller_tag, soh.owner_tag) AS controller_tag
        FROM state_ownership_history soh
        WHERE soh.effective_date <= p_date
    ),
    tech AS (
        SELECT cst.country_tag, cst.technology_key, cst.dlc_source
        FROM country_starting_technologies cst
        WHERE cst.effective_date <= p_date
    )
    SELECT
        c.tag,
        COALESCE(cl.loc_value, c.tag) AS country_name,
        c.capital_state_id,
        c.stability,
        c.war_support,
        c.graphical_culture,
        c.graphical_culture_2d,
        jsonb_build_object('r', c.color_r, 'g', c.color_g, 'b', c.color_b) AS color_rgb,
        COALESCE((
            SELECT jsonb_agg(
                jsonb_build_object(
                    'state_id', o.state_id,
                    'state_name_key', s.state_name_key,
                    'state_name', COALESCE(sl.loc_value, s.state_name_key),
                    'controller_tag', o.controller_tag
                )
                ORDER BY o.state_id
            )
            FROM ownership o
            JOIN states s ON s.state_id = o.state_id
            LEFT JOIN localisation sl ON sl.loc_key = s.state_name_key
            WHERE o.owner_tag = c.tag
        ), '[]'::jsonb) AS owned_states,
        COALESCE((
            SELECT jsonb_agg(
                jsonb_build_object(
                    'technology_key', t.technology_key,
                    'technology_name', COALESCE(tl.loc_value, t.technology_key),
                    'dlc_source', t.dlc_source
                )
                ORDER BY t.technology_key, t.dlc_source
            )
            FROM tech t
            LEFT JOIN localisation tl ON tl.loc_key = t.technology_key
            WHERE t.country_tag = c.tag
        ), '[]'::jsonb) AS starting_technologies
    FROM countries c
    LEFT JOIN localisation cl ON cl.loc_key = c.tag;
$$;

-- Same pattern as api_country_detail above — function with a date parameter.
-- See the comments on that function for explanation of the syntax.

CREATE OR REPLACE FUNCTION api_state_detail(p_date DATE DEFAULT '1936-01-01')
RETURNS TABLE (
    state_id           INT,
    state_name_key     VARCHAR,
    state_name         TEXT,
    state_category     VARCHAR,
    manpower           INT,
    local_supplies     NUMERIC,
    owner_tag          CHAR(3),
    controller_tag     CHAR(3),
    resources          JSONB,
    state_buildings    JSONB,
    province_buildings JSONB,
    provinces          JSONB
)
LANGUAGE sql STABLE AS $$
    WITH ownership AS (
        SELECT soh.state_id, soh.owner_tag, COALESCE(soh.controller_tag, soh.owner_tag) AS controller_tag
        FROM state_ownership_history soh
        WHERE soh.effective_date <= p_date
    ),
    resources_at_date AS (
        SELECT sr.state_id,
               jsonb_agg(
                   jsonb_build_object('resource_key', sr.resource_key, 'amount', sr.amount)
                   ORDER BY sr.resource_key
               ) AS resources
        FROM state_resources sr
        WHERE sr.effective_date <= p_date
        GROUP BY sr.state_id
    ),
    state_buildings_at_date AS (
        SELECT sb.state_id,
               jsonb_agg(
                   jsonb_build_object('building_key', sb.building_key, 'level', sb.level)
                   ORDER BY sb.building_key
               ) AS buildings
        FROM state_buildings sb
        WHERE sb.effective_date <= p_date
        GROUP BY sb.state_id
    ),
    province_buildings_at_date AS (
        SELECT pb.state_id,
               jsonb_agg(
                   jsonb_build_object(
                       'province_id', pb.province_id,
                       'building_key', pb.building_key,
                       'level', pb.level
                   )
                   ORDER BY pb.province_id, pb.building_key
               ) AS province_buildings
        FROM province_buildings pb
        WHERE pb.effective_date <= p_date
        GROUP BY pb.state_id
    ),
    state_province_list AS (
        SELECT sp.state_id,
               jsonb_agg(
                   jsonb_build_object(
                       'province_id', p.province_id,
                       'terrain', p.terrain,
                       'is_coastal', p.is_coastal,
                       'continent_id', p.continent_id
                   )
                   ORDER BY p.province_id
               ) AS provinces
        FROM state_provinces sp
        JOIN provinces p ON p.province_id = sp.province_id
        GROUP BY sp.state_id
    )
    SELECT
        s.state_id,
        s.state_name_key,
        COALESCE(sl.loc_value, s.state_name_key) AS state_name,
        s.state_category,
        s.manpower,
        s.local_supplies,
        o.owner_tag,
        o.controller_tag,
        COALESCE(r.resources, '[]'::jsonb) AS resources,
        COALESCE(sb.buildings, '[]'::jsonb) AS state_buildings,
        COALESCE(pb.province_buildings, '[]'::jsonb) AS province_buildings,
        COALESCE(pl.provinces, '[]'::jsonb) AS provinces
    FROM states s
    LEFT JOIN localisation sl ON sl.loc_key = s.state_name_key
    LEFT JOIN ownership o ON o.state_id = s.state_id
    LEFT JOIN resources_at_date r ON r.state_id = s.state_id
    LEFT JOIN state_buildings_at_date sb ON sb.state_id = s.state_id
    LEFT JOIN province_buildings_at_date pb ON pb.state_id = s.state_id
    LEFT JOIN state_province_list pl ON pl.state_id = s.state_id;
$$;

-- ============================================================
-- Slice B — Technologies
-- ============================================================

CREATE OR REPLACE VIEW api_country_technologies AS
SELECT
    cst.country_tag,
    cst.technology_key,
    COALESCE(l.loc_value, cst.technology_key) AS technology_name,
    t.start_year,
    t.research_cost,
    t.folder_name,
    cst.dlc_source,
    cst.effective_date
FROM country_starting_technologies cst
JOIN technologies t ON t.technology_key = cst.technology_key
LEFT JOIN localisation l ON l.loc_key = cst.technology_key;

CREATE OR REPLACE VIEW api_technology_tree AS
SELECT
    t.technology_key,
    COALESCE(l.loc_value, t.technology_key) AS technology_name,
    t.start_year,
    t.research_cost,
    t.folder_name,
    COALESCE((
        SELECT jsonb_agg(tp.prerequisite_key ORDER BY tp.prerequisite_key)
        FROM technology_prerequisites tp
        WHERE tp.technology_key = t.technology_key
    ), '[]'::jsonb) AS prerequisites,
    COALESCE((
        SELECT jsonb_agg(tc.category_key ORDER BY tc.category_key)
        FROM technology_categories_junction tc
        WHERE tc.technology_key = t.technology_key
    ), '[]'::jsonb) AS categories,
    COALESCE((
        SELECT jsonb_agg(te.equipment_key ORDER BY te.equipment_key)
        FROM technology_enables_equipment te
        WHERE te.technology_key = t.technology_key
    ), '[]'::jsonb) AS enables_equipment,
    COALESCE((
        SELECT jsonb_agg(tu.unit_type_key ORDER BY tu.unit_type_key)
        FROM technology_enables_units tu
        WHERE tu.technology_key = t.technology_key
    ), '[]'::jsonb) AS enables_units
FROM technologies t
LEFT JOIN localisation l ON l.loc_key = t.technology_key;

-- ============================================================
-- Slice B — Characters
-- ============================================================

CREATE OR REPLACE VIEW api_country_characters AS
SELECT
    ch.character_id,
    ch.name_key,
    ch.country_tag,
    ch.gender,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'role_type', cr.role_type,
                'sub_ideology_key', cr.sub_ideology_key,
                'skill', cr.skill,
                'attack_skill', cr.attack_skill,
                'defense_skill', cr.defense_skill,
                'planning_skill', cr.planning_skill,
                'logistics_skill', cr.logistics_skill,
                'maneuvering_skill', cr.maneuvering_skill,
                'coordination_skill', cr.coordination_skill,
                'dlc_source', cr.dlc_source,
                'traits', COALESCE((
                    SELECT jsonb_agg(crt.trait_key ORDER BY crt.trait_key)
                    FROM character_role_traits crt
                    WHERE crt.character_role_id = cr.character_role_id
                ), '[]'::jsonb)
            )
            ORDER BY cr.role_type
        )
        FROM character_roles cr
        WHERE cr.character_id = ch.character_id
    ), '[]'::jsonb) AS roles
FROM characters ch;

-- ============================================================
-- Slice B — Land OOB
-- ============================================================

CREATE OR REPLACE VIEW api_country_divisions AS
SELECT
    dt.country_tag,
    dt.division_template_id,
    dt.template_name,
    dt.oob_file,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'unit_type_key', r.unit_type_key,
                'grid_x', r.grid_x,
                'grid_y', r.grid_y
            )
            ORDER BY r.grid_y, r.grid_x
        )
        FROM division_template_regiments r
        WHERE r.division_template_id = dt.division_template_id
    ), '[]'::jsonb) AS regiments,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'unit_type_key', s.unit_type_key,
                'grid_x', s.grid_x,
                'grid_y', s.grid_y
            )
            ORDER BY s.grid_y, s.grid_x
        )
        FROM division_template_support s
        WHERE s.division_template_id = dt.division_template_id
    ), '[]'::jsonb) AS support,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'location_province_id', d.location_province_id,
                'start_experience_factor', d.start_experience_factor
            )
        )
        FROM divisions d
        WHERE d.division_template_id = dt.division_template_id
    ), '[]'::jsonb) AS deployed_divisions
FROM division_templates dt;

-- ============================================================
-- Slice B — Naval OOB
-- ============================================================

CREATE OR REPLACE VIEW api_country_naval AS
SELECT
    f.country_tag,
    f.fleet_id,
    f.fleet_name,
    f.naval_base_province_id,
    f.oob_file,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'task_force_id', tf.task_force_id,
                'task_force_name', tf.task_force_name,
                'location_province_id', tf.location_province_id,
                'ships', COALESCE((
                    SELECT jsonb_agg(
                        jsonb_build_object(
                            'ship_name', sh.ship_name,
                            'definition', sh.definition,
                            'hull_equipment_key', sh.hull_equipment_key,
                            'version_name', sh.version_name,
                            'pride_of_the_fleet', sh.pride_of_the_fleet
                        )
                        ORDER BY sh.ship_name
                    )
                    FROM ships sh
                    WHERE sh.task_force_id = tf.task_force_id
                ), '[]'::jsonb)
            )
            ORDER BY tf.task_force_name
        )
        FROM task_forces tf
        WHERE tf.fleet_id = f.fleet_id
    ), '[]'::jsonb) AS task_forces
FROM fleets f;

-- ============================================================
-- Slice B — Air OOB
-- ============================================================

CREATE OR REPLACE VIEW api_country_air AS
SELECT
    aw.country_tag,
    aw.location_state_id,
    s.state_name_key,
    aw.equipment_type,
    aw.amount,
    aw.wing_name,
    aw.version_name,
    aw.oob_file
FROM air_wings aw
JOIN states s ON s.state_id = aw.location_state_id;

-- ============================================================
-- Slice B — Focus Trees
-- ============================================================

CREATE OR REPLACE VIEW api_focus_tree_detail AS
SELECT
    ft.focus_tree_id,
    ft.country_tag,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'focus_id', f.focus_id,
                'cost', f.cost,
                'x_pos', f.x_pos,
                'y_pos', f.y_pos,
                'icon', f.icon,
                'dlc_source', f.dlc_source,
                'prerequisites', COALESCE((
                    SELECT jsonb_agg(
                        jsonb_build_object(
                            'group', fp.prerequisite_group,
                            'required_focus_id', fp.required_focus_id
                        )
                    )
                    FROM focus_prerequisites fp
                    WHERE fp.focus_id = f.focus_id
                ), '[]'::jsonb),
                'mutually_exclusive', COALESCE((
                    SELECT jsonb_agg(
                        CASE WHEN me.focus_a_id = f.focus_id THEN me.focus_b_id
                             ELSE me.focus_a_id END
                    )
                    FROM focus_mutually_exclusive me
                    WHERE me.focus_a_id = f.focus_id OR me.focus_b_id = f.focus_id
                ), '[]'::jsonb)
            )
            ORDER BY f.y_pos, f.x_pos
        )
        FROM focuses f
        WHERE f.focus_tree_id = ft.focus_tree_id
    ), '[]'::jsonb) AS focuses
FROM focus_trees ft;

-- ============================================================
-- Slice B — Equipment Catalog
-- ============================================================

CREATE OR REPLACE VIEW api_equipment_catalog AS
SELECT
    ed.equipment_key,
    ed.is_archetype,
    ed.archetype_key,
    ed.parent_key,
    ed.year,
    ed.build_cost_ic,
    ed.reliability,
    ed.maximum_speed,
    ed.defense,
    ed.breakthrough,
    ed.soft_attack,
    ed.hard_attack,
    ed.ap_attack,
    ed.air_attack,
    ed.armor_value,
    ed.hardness,
    ed.dlc_source,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object('resource_key', er.resource_key, 'amount', er.amount)
            ORDER BY er.resource_key
        )
        FROM equipment_resources er
        WHERE er.equipment_key = ed.equipment_key
    ), '[]'::jsonb) AS resources
FROM equipment_definitions ed;

-- ============================================================
-- Slice B — Ideas & National Spirits
-- ============================================================

CREATE OR REPLACE VIEW api_ideas_detail AS
SELECT
    i.idea_key,
    i.slot,
    i.is_law,
    i.cost,
    i.removal_cost,
    i.is_default,
    i.dlc_source,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object('modifier_key', im.modifier_key, 'modifier_value', im.modifier_value)
            ORDER BY im.modifier_key
        )
        FROM idea_modifiers im
        WHERE im.idea_key = i.idea_key
    ), '[]'::jsonb) AS modifiers
FROM ideas i;

-- ============================================================
-- Slice C — DLC: Military-Industrial Organizations
-- ============================================================

CREATE OR REPLACE VIEW api_mio_organization_detail AS
SELECT
    mo.organization_key,
    mo.template_key,
    mo.icon,
    mo.dlc_source,
    mt.icon AS template_icon,
    COALESCE((
        SELECT jsonb_agg(oet.equipment_type ORDER BY oet.equipment_type)
        FROM mio_organization_equipment_types oet
        WHERE oet.owner_key = mo.organization_key AND oet.owner_type = 'organization'
    ), COALESCE((
        SELECT jsonb_agg(oet.equipment_type ORDER BY oet.equipment_type)
        FROM mio_organization_equipment_types oet
        WHERE oet.owner_key = mo.template_key AND oet.owner_type = 'template'
    ), '[]'::jsonb)) AS equipment_types,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'trait_token', t.trait_token,
                'trait_type', t.trait_type,
                'name', t.name,
                'position_x', t.position_x,
                'position_y', t.position_y,
                'bonuses', COALESCE((
                    SELECT jsonb_agg(
                        jsonb_build_object(
                            'category', tb.bonus_category,
                            'key', tb.bonus_key,
                            'value', tb.bonus_value
                        )
                    )
                    FROM mio_trait_bonuses tb
                    WHERE tb.trait_token = t.trait_token
                ), '[]'::jsonb)
            )
            ORDER BY t.position_y, t.position_x
        )
        FROM mio_traits t
        WHERE (t.owner_key = mo.organization_key AND t.owner_type = 'organization')
           OR (t.owner_key = mo.template_key AND t.owner_type = 'template')
    ), '[]'::jsonb) AS traits
FROM mio_organizations mo
LEFT JOIN mio_templates mt ON mt.template_key = mo.template_key;

-- ============================================================
-- Slice C — DLC: Espionage Operations
-- ============================================================

CREATE OR REPLACE VIEW api_operation_detail AS
SELECT
    op.operation_key,
    op.name,
    op.days,
    op.network_strength,
    op.operatives,
    op.risk_chance,
    op.experience,
    op.dlc_source,
    COALESCE((
        SELECT jsonb_agg(oat.token_key ORDER BY oat.token_key)
        FROM operation_awarded_tokens oat
        WHERE oat.operation_key = op.operation_key
    ), '[]'::jsonb) AS awarded_tokens,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object('equipment_key', oer.equipment_key, 'amount', oer.amount)
        )
        FROM operation_equipment_requirements oer
        WHERE oer.operation_key = op.operation_key
    ), '[]'::jsonb) AS equipment_requirements,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'sequence_index', pg.sequence_index,
                'options', COALESCE((
                    SELECT jsonb_agg(
                        jsonb_build_object(
                            'phase_key', po.phase_key,
                            'base_weight', po.base_weight
                        )
                        ORDER BY po.base_weight DESC
                    )
                    FROM operation_phase_options po
                    WHERE po.operation_key = pg.operation_key
                      AND po.sequence_index = pg.sequence_index
                ), '[]'::jsonb)
            )
            ORDER BY pg.sequence_index
        )
        FROM operation_phase_groups pg
        WHERE pg.operation_key = op.operation_key
    ), '[]'::jsonb) AS phase_groups
FROM operations op;

-- ============================================================
-- Slice C — DLC: Balance of Power
-- ============================================================

CREATE OR REPLACE VIEW api_bop_detail AS
SELECT
    bop.bop_key,
    bop.initial_value,
    bop.left_side,
    bop.right_side,
    bop.decision_category,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'side_id', bs.side_id,
                'side_position', bs.side_position,
                'icon', bs.icon,
                'ranges', COALESCE((
                    SELECT jsonb_agg(
                        jsonb_build_object(
                            'range_id', br.range_id,
                            'min_value', br.min_value,
                            'max_value', br.max_value,
                            'modifiers', COALESCE((
                                SELECT jsonb_agg(
                                    jsonb_build_object(
                                        'modifier_key', brm.modifier_key,
                                        'modifier_value', brm.modifier_value
                                    )
                                )
                                FROM bop_range_modifiers brm
                                WHERE brm.range_id = br.range_id
                            ), '[]'::jsonb)
                        )
                        ORDER BY br.min_value
                    )
                    FROM bop_ranges br
                    WHERE br.bop_key = bs.bop_key AND br.side_id = bs.side_id
                ), '[]'::jsonb)
            )
        )
        FROM bop_sides bs
        WHERE bs.bop_key = bop.bop_key
    ), '[]'::jsonb) AS sides
FROM balance_of_power_definitions bop;

-- ============================================================
-- Slice C — DLC: Factions (Götterdämmerung)
-- ============================================================

CREATE OR REPLACE VIEW api_faction_detail AS
SELECT
    ft.template_key,
    ft.name_loc,
    ft.manifest_key,
    ft.icon,
    ft.can_leader_join_other,
    ft.dlc_source,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'goal_key', fg.goal_key,
                'name_loc', fg.name_loc,
                'category', fg.category,
                'goal_group', fg.goal_group
            )
            ORDER BY fg.goal_key
        )
        FROM faction_template_goals ftg
        JOIN faction_goals fg ON fg.goal_key = ftg.goal_key
        WHERE ftg.template_key = ft.template_key
    ), '[]'::jsonb) AS goals,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'rule_key', fr.rule_key,
                'rule_type', fr.rule_type,
                'rule_group_key', fr.rule_group_key
            )
            ORDER BY fr.rule_key
        )
        FROM faction_template_rules ftr
        JOIN faction_rules fr ON fr.rule_key = ftr.rule_key
        WHERE ftr.template_key = ft.template_key
    ), '[]'::jsonb) AS rules,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'group_key', mug.group_key,
                'name_loc', mug.name_loc,
                'upgrade_type', mug.upgrade_type,
                'upgrades', COALESCE((
                    SELECT jsonb_agg(
                        jsonb_build_object(
                            'upgrade_key', mu.upgrade_key,
                            'bonus', mu.bonus,
                            'description_loc', mu.description_loc
                        )
                        ORDER BY mu.upgrade_key
                    )
                    FROM faction_member_upgrades mu
                    WHERE mu.group_key = mug.group_key
                ), '[]'::jsonb)
            )
            ORDER BY mug.group_key
        )
        FROM faction_member_upgrade_groups mug
    ), '[]'::jsonb) AS member_upgrade_groups
FROM faction_templates ft;

-- ============================================================
-- Slice C — DLC: Special Projects (Götterdämmerung)
-- ============================================================

CREATE OR REPLACE VIEW api_special_project_detail AS
SELECT
    sp.project_key,
    sp.specialization_key,
    sp.project_tag,
    sp.complexity,
    sp.prototype_time,
    sp.dlc_source,
    COALESCE((
        SELECT jsonb_agg(
            jsonb_build_object(
                'reward_key', spr.reward_key,
                'fire_only_once', spr.fire_only_once,
                'threshold_min', spr.threshold_min,
                'threshold_max', spr.threshold_max
            )
            ORDER BY spr.reward_key
        )
        FROM special_project_reward_links sprl
        JOIN special_project_rewards spr ON spr.reward_key = sprl.reward_key
        WHERE sprl.project_key = sp.project_key
    ), '[]'::jsonb) AS rewards
FROM special_projects sp;
