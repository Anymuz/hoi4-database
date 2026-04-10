# app/graphql/types.py
# Strawberry GraphQL types mirror the  REST schemas, strawberry types auto-convert snake_case fields to camelCase in GraphQL.
import strawberry
from typing import Optional
from datetime import datetime

# Country related types. use the api_country_detail view:
# Colors are stored as RGB in the database and represented as a nested ColorRGB type in GraphQL.
@strawberry.type
class ColorRGB:
    r: int
    g: int
    b: int
# End of ColorRGB type.

# OwnedState represents a state owned by a country, with its name, controller, and other details. This is nested within the Country type.
@strawberry.type
class OwnedState:
    state_id: int
    state_name_key: Optional[str] = None
    state_name: Optional[str] = None
    controller_tag: Optional[str] = None
# End of OwnedState type.

# Starting technologies are the techs a country has at start,  can differ from the default tech tree based on the country's history or DLC. 
@strawberry.type
class StartingTech:
    technology_key: str
    technology_name: Optional[str] = None
    dlc_source: Optional[str] = None
# End of StartingTech type.

# Country type with nested owned states and starting technologies, and a color field that is a nested RGB object.
@strawberry.type
class Country:
    tag: str
    country_name: Optional[str] = None
    capital_state_id: Optional[int] = None
    stability: Optional[float] = None
    war_support: Optional[float] = None
    graphical_culture: Optional[str] = None
    graphical_culture_2d: Optional[str] = None
    color_rgb: Optional[ColorRGB] = None
    owned_states: list[OwnedState]
    starting_technologies: list[StartingTech]

    # Classmethod to convert a database row (Record) into a Country object, handling nested structures for color, owned states, and starting technologies.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["color_rgb"] = ColorRGB(**d["color_rgb"]) if d.get("color_rgb") else None
        d["owned_states"] = [OwnedState(**s) for s in (d.get("owned_states") or [])]
        d["starting_technologies"] = [StartingTech(**t) for t in (d.get("starting_technologies") or [])]
        return cls(**d)
# End of Country type.
# ------------------------------------------------------

#  State related types, use the api_state_detail view:
# StateResource represents a resource produced by a state, with its key and amount.
@strawberry.type
class StateResource:
    resource_key: str
    amount: int
# End of StateResource type.

# StateBuilding represents a building in a state, with its key and level. This is nested within the State type.
@strawberry.type
class StateBuilding:
    building_key: str
    level: int
# End of StateBuilding type.

# ProvinceBuilding represents a building in a specific province within a state, with the province ID, building key, and level. This is also nested within the State type.
@strawberry.type
class ProvinceBuilding:
    province_id: int
    building_key: str
    level: int
# End of ProvinceBuilding type.

# Province represents a province within a state, with its ID, terrain type, coastal status, and continent. Nested within the State type.
@strawberry.type
class Province:
    province_id: int
    terrain: Optional[str] = None
    is_coastal: Optional[bool] = None
    continent_id: Optional[int] = None
# End of Province type.

# State type with nested resources, buildings, and provinces etc.
@strawberry.type
class State:
    state_id: int
    state_name_key: Optional[str] = None
    state_name: Optional[str] = None
    state_category: Optional[str] = None
    manpower: Optional[int] = None
    local_supplies: Optional[float] = None
    owner_tag: Optional[str] = None
    controller_tag: Optional[str] = None
    resources: list[StateResource]
    state_buildings: list[StateBuilding]
    province_buildings: list[ProvinceBuilding]
    provinces: list[Province]

    # State type has a from_row classmethod to handle the complex nested data structure returned by the database.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["resources"] = [StateResource(**r) for r in (d.get("resources") or [])]
        d["state_buildings"] = [StateBuilding(**b) for b in (d.get("state_buildings") or [])]
        d["province_buildings"] = [ProvinceBuilding(**b) for b in (d.get("province_buildings") or [])]
        d["provinces"] = [Province(**p) for p in (d.get("provinces") or [])]
        return cls(**d)
    # End of from_row class method 
# End of State type.
# ------------------------------------------------------

# Technology related types, use the api_technology_detail view:
# Technology type represents a technology in the game, with its key, name, research cost, prerequisites, and what it enables.
@strawberry.type
class Technology:
    technology_key: str
    technology_name: Optional[str] = None
    start_year: Optional[int] = None
    research_cost: Optional[float] = None
    folder_name: Optional[str] = None
    prerequisites: list[str]
    categories: list[str]
    enables_equipment: list[str]
    enables_units: list[str]

    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["prerequisites"] = d.get("prerequisites") or []
        d["categories"] = d.get("categories") or []
        d["enables_equipment"] = d.get("enables_equipment") or []
        d["enables_units"] = d.get("enables_units") or []
        return cls(**d)
# End of Technology type.
# ------------------------------------------------------

# Character related types, use the api_character_detail view:
# CharacterRole represents a role a character can have (leader, general, admiral, advisor), with associated skills and traits. Nested within the Character type.
@strawberry.type
class CharacterRole:
    role_type: str
    sub_ideology_key: Optional[str] = None
    skill: Optional[int] = None
    attack_skill: Optional[int] = None
    defense_skill: Optional[int] = None
    planning_skill: Optional[int] = None
    logistics_skill: Optional[int] = None
    maneuvering_skill: Optional[int] = None
    coordination_skill: Optional[int] = None
    dlc_source: Optional[str] = None
    traits: list[str]
    # Classmethod to convert a dictionary (from database) into a CharacterRole object, handling the traits list which may be null in the database.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["traits"] = d.get("traits") or []
        return cls(**d)
    # End of from_dict class method.
# End of CharacterRole type.

# Character type with nested roles, and a from_row classmethod to handle the complex nested data structure returned by the database.
@strawberry.type
class Character:
    character_id: str
    name_key: Optional[str] = None
    country_tag: Optional[str] = None
    gender: Optional[str] = None
    roles: list[CharacterRole]

    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["roles"] = [CharacterRole.from_dict(r) for r in (d.get("roles") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Character type.
# ------------------------------------------------------

# Military (ground based) related types, use the api_military_detail view:
# Regiment represents a regiment in a division, with its unit type and position in the division template. Nested within the Division type.
@strawberry.type
class Regiment:
    unit_type_key: str
    grid_x: Optional[int] = None
    grid_y: Optional[int] = None
# End of Regiment type.

# SupportCompany represents a support company in a division, with its unit type and position in the division template. Nested within the Division type.
@strawberry.type
class SupportCompany:
    unit_type_key: str
    grid_x: Optional[int] = None
    grid_y: Optional[int] = None
# End of SupportCompany type.

# Deployed represents a deployed division, with its location and experience factor. Nested within the Division type.
@strawberry.type
class Deployed:
    location_province_id: Optional[int] = None
    start_experience_factor: Optional[float] = None
# End of Deployed type.

# Division type with nested regiments, support companies, and deployed divisions.
@strawberry.type
class Division:
    country_tag: str
    division_template_id: int
    template_name: str
    oob_file: Optional[str] = None
    regiments: list[Regiment]
    support: list[SupportCompany]
    deployed_divisions: list[Deployed]

    # Classmethod to handle the complex nested data structure returned by the database.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["regiments"] = [Regiment(**r) for r in (d.get("regiments") or [])]
        d["support"] = [SupportCompany(**s) for s in (d.get("support") or [])]
        d["deployed_divisions"] = [Deployed(**dd) for dd in (d.get("deployed_divisions") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Division type.

# Naval and air force types, use the api_military_detail view:
# Ship represents a ship in a task force, with its name, definition, and equipment. Nested within the TaskForce type.
@strawberry.type
class Ship:
    ship_name: str
    definition: str
    hull_equipment_key: str
    version_name: Optional[str] = None
    pride_of_the_fleet: Optional[bool] = None
# End of Ship type.

# TaskForce represents a naval task force, with its name, location, and the ships it contains. Nested within the Fleet type.
@strawberry.type
class TaskForce:
    task_force_id: int
    task_force_name: str
    location_province_id: Optional[int] = None
    ships: list[Ship]
    # Classmethod to handle the nested ships list in the database result.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["ships"] = [Ship(**s) for s in (d.get("ships") or [])]
        return cls(**d)
    # End of from_dict class method.
# End of TaskForce type.

# Fleet represents a naval fleet, with its name, location, and the task forces it contains. Nested within the Country type.
@strawberry.type
class Fleet:
    country_tag: str
    fleet_id: int
    fleet_name: str
    naval_base_province_id: Optional[int] = None
    oob_file: Optional[str] = None
    task_forces: list[TaskForce]

    # Classmethod to handle the nested task forces list in the database result.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["task_forces"] = [TaskForce.from_dict(t) for t in (d.get("task_forces") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Fleet type.

# AirWing represents an air wing, with its location, equipment type, and other details. Nested within the Country type.
@strawberry.type
class AirWing:
    country_tag: str
    location_state_id: int
    state_name_key: Optional[str] = None
    equipment_type: str
    amount: int
    wing_name: Optional[str] = None
    version_name: Optional[str] = None
    oob_file: Optional[str] = None
# End of AirWing type.
# ------------------------------------------------------

# Focus tree types, use the api_focus_tree_detail view:
# FocusPrereq represents a prerequisite for a national focus, which can be either required or mutually exclusive. Nested within the Focus type.
@strawberry.type
class FocusPrereq:
    group: Optional[int] = None
    required_focus_id: str
# End of FocusPrereq type.

# Focus represents a national focus, with its cost, position in the focus tree, prerequisites, and mutually exclusive focuses. Nested within the FocusTree type.
@strawberry.type
class Focus:
    focus_id: str
    cost: Optional[float] = None
    x_pos: Optional[int] = None
    y_pos: Optional[int] = None
    icon: Optional[str] = None
    dlc_source: Optional[str] = None
    completion_reward: Optional[str] = None
    prerequisites: list[FocusPrereq]
    mutually_exclusive: list[str]

    # Classmethod to convert from a dictionary (from the database) into a Focus object, handling the prerequisites and mutually exclusive lists which may be null in the database.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["prerequisites"] = [FocusPrereq(**p) for p in (d.get("prerequisites") or [])]
        d["mutually_exclusive"] = d.get("mutually_exclusive") or []
        return cls(**d)
    # End of from_dict class method.
# End of Focus type.

# FocusTree represents a national focus tree, with its country tag and the list of focuses it contains. Nested within the Country type.
@strawberry.type
class FocusTree:
    focus_tree_id: str
    country_tag: Optional[str] = None
    focuses: list[Focus]

    # Classmethod to convert from a database row into a FocusTree object, handling the nested focuses list.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["focuses"] = [Focus.from_dict(f) for f in (d.get("focuses") or [])]
        return cls(**d)
    # End of from_row class method.
# End of FocusTree type.
# ------------------------------------------------------

# Equipment related types, use the api_equipment_detail view:
# EquipmentResource represents a resource required to build a piece of equipment, with its key and amount. Nested within the Equipment type.
@strawberry.type
class EquipmentResource:
    resource_key: str
    amount: Optional[float] = None
# End of EquipmentResource type.

# Equipment represents a piece of equipment in the game, with its stats, resources required, and other details.
@strawberry.type
class Equipment:
    equipment_key: str
    is_archetype: bool
    archetype_key: Optional[str] = None
    parent_key: Optional[str] = None
    year: Optional[int] = None
    build_cost_ic: Optional[float] = None
    reliability: Optional[float] = None
    maximum_speed: Optional[float] = None
    defense: Optional[float] = None
    breakthrough: Optional[float] = None
    soft_attack: Optional[float] = None
    hard_attack: Optional[float] = None
    ap_attack: Optional[float] = None
    air_attack: Optional[float] = None
    armor_value: Optional[float] = None
    hardness: Optional[float] = None
    dlc_source: Optional[str] = None
    resources: list[EquipmentResource]

    # Classmethod to handle the complex nested data structure returned by the database.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["resources"] = [EquipmentResource(**r) for r in (d.get("resources") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Equipment type.

# EquipmentVariant represents a specific variant of a piece of equipment, with modules and upgrades. Uses the api_equipment_variant_detail view.
@strawberry.type
class EquipmentVariantModule:
    slot_name: str
    module_key: str
# End of EquipmentVariantModule type.

# EquipmentVariantUpgrade represents an upgrade for an equipment variant, with its key and level. Nested within the EquipmentVariant type.
@strawberry.type
class EquipmentVariantUpgrade:
    upgrade_key: str
    upgrade_level: int
# End of EquipmentVariantUpgrade type.

# EquipmentVariant represents a specific variant of a piece of equipment, with its owner country, base equipment, modules, and upgrades.
@strawberry.type
class EquipmentVariant:
    equipment_variant_id: int
    owner_tag: str
    base_equipment_key: str
    version_name: Optional[str] = None
    effective_date: str = "1936-01-01"
    modules: list[EquipmentVariantModule]
    upgrades: list[EquipmentVariantUpgrade]
# End of EquipmentVariant type.
# ------------------------------------------------------

# Idea related types, use the api_ideas_detail view:
# IdeaModifier represents a modifier provided by an idea, with its key and value. Nested within the Idea type.
@strawberry.type
class IdeaModifier:
    modifier_key: str
    modifier_value: Optional[float] = None
# End of IdeaModifier type.

#  Idea represents a national spirit, law, or modifier that provides bonuses or penalties to countries, with its cost, whether it's a law, and the modifiers it provides.
@strawberry.type
class Idea:
    idea_key: str
    slot: Optional[str] = None
    is_law: bool
    cost: Optional[float] = None
    removal_cost: Optional[float] = None
    is_default: bool
    dlc_source: Optional[str] = None
    on_add_effect: Optional[str] = None
    on_remove_effect: Optional[str] = None
    allowed_condition: Optional[str] = None
    modifiers: list[IdeaModifier]

    # Classmethod to handle the complex nested data structure returned by the database.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["modifiers"] = [IdeaModifier(**m) for m in (d.get("modifiers") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Idea type.
# ------------------------------------------------------

# DLC: MIOs (Military Industry Organizations) related types, use the api_mio_organization_detail view:
# MIOTraitBonus represents a bonus provided by an MIO trait, with its key, category, and value. Nested within the MIOTrait type.
@strawberry.type
class MIOTraitBonus:
    key: str
    category: Optional[str] = None
    value: Optional[float] = None
# End of MIOTraitBonus type.

# MIOTrait represents a trait of an MIO, with its type, name, position in the MIO interface, and the bonuses it provides. Nested within the Mio type.
@strawberry.type
class MIOTrait:
    trait_token: str
    trait_type: Optional[str] = None
    name: Optional[str] = None
    position_x: Optional[int] = None
    position_y: Optional[int] = None
    bonuses: list[MIOTraitBonus]

    # Classmethod to convert from a dictionary (from the database) into an MIOTrait object, handling the bonuses list which may be null.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["bonuses"] = [MIOTraitBonus(**b) for b in (d.get("bonuses") or [])]
        return cls(**d)
    # End of from_dict class method.
# End of MIOTrait type.

# Mio represents a Military Industry Organization (MIO), with its key, template, icon, DLC source, equipment types, and traits.
@strawberry.type
class Mio:
    organization_key: str
    template_key: Optional[str] = None
    icon: Optional[str] = None
    dlc_source: Optional[str] = None
    template_icon: Optional[str] = None
    equipment_types: list[str]
    traits: list[MIOTrait]

    # Classmethod to convert from a database row into a Mio object, handling the nested equipment types and traits lists.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["equipment_types"] = d.get("equipment_types") or []
        d["traits"] = [MIOTrait.from_dict(t) for t in (d.get("traits") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Mio type.
# ------------------------------------------------------

# DLC: Operations related types, use the api_operation_detail view:
# OperationEquipment represents a piece of equipment required for an operation, with its key and amount. Nested within the Operation type.
@strawberry.type
class OperationEquipment:
    equipment_key: str
    amount: Optional[int] = None
# End of OperationEquipment type.

# PhaseOption represents an option for a phase in an operation, with its key and base weight. Nested within the PhaseGroup type.
@strawberry.type
class PhaseOption:
    phase_key: str
    base_weight: Optional[float] = None
# End of PhaseOption type.

# PhaseGroup represents a group of phases in an operation, with its sequence index and the options it contains. Nested within the Operation type.
@strawberry.type
class PhaseGroup:
    sequence_index: Optional[int] = None
    options: list[PhaseOption]

    # Classmethod to convert from a dictionary (from the database) into a PhaseGroup object, handling the options list which may be null.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["options"] = [PhaseOption(**o) for o in (d.get("options") or [])]
        return cls(**d)
    # End of from_dict class method.
# End of PhaseGroup type.

# Operation represents a military operation, with its key, name, duration, risk, rewards, equipment requirements, and the phases it contains.
@strawberry.type
class Operation:
    operation_key: str
    name: Optional[str] = None
    days: Optional[int] = None
    network_strength: Optional[int] = None
    operatives: Optional[int] = None
    risk_chance: Optional[float] = None
    experience: Optional[float] = None
    dlc_source: Optional[str] = None
    awarded_tokens: list[str]
    equipment_requirements: list[OperationEquipment]
    phase_groups: list[PhaseGroup]

    # Classmethod to convert from a database row into an Operation object, handling the nested lists.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["awarded_tokens"] = d.get("awarded_tokens") or []
        d["equipment_requirements"] = [OperationEquipment(**e) for e in (d.get("equipment_requirements") or [])]
        d["phase_groups"] = [PhaseGroup.from_dict(p) for p in (d.get("phase_groups") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Operation type.
# ------------------------------------------------------

# DLC: BOP (Balance of Power) related types, use the api_bop_detail view:
# BOPRangeModifier represents a modifier applied to a BOP range, with its key and value. Nested within the BOPRange type.
@strawberry.type
class BOPRangeModifier:
    modifier_key: str
    modifier_value: Optional[float] = None
# End of BOPRangeModifier type.

# BOPRange represents a range of values for a BOP side, with its ID, minimum and maximum values, and modifiers applied. Nested within the BOPSide type.
@strawberry.type
class BOPRange:
    range_id: str
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    modifiers: list[BOPRangeModifier]
    # Classmethod to convert from a dictionary (from the database) into a BOPRange object, handling the modifiers list which may be null.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["modifiers"] = [BOPRangeModifier(**m) for m in (d.get("modifiers") or [])]
        return cls(**d)
    # End of from_dict class method.
# End of BOPRange type.

# BOPSide represents a side in a Balance of Power scenario, with its ID, position, icon, and the ranges that define its strength. Nested within the Bop type.
@strawberry.type
class BOPSide:
    side_id: str
    side_position: Optional[str] = None
    icon: Optional[str] = None
    ranges: list[BOPRange]

    # Classmethod to convert from a dictionary (from the database) into a BOPSide object, handling the ranges list which may be null.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["ranges"] = [BOPRange.from_dict(r) for r in (d.get("ranges") or [])]
        return cls(**d)
    # End of from_dict class method.
# End of BOPSide type.

# Bop represents a Balance of Power scenario, with its key, initial value, sides, and other details.
@strawberry.type
class Bop:
    bop_key: str
    initial_value: Optional[float] = None
    left_side: Optional[str] = None
    right_side: Optional[str] = None
    decision_category: Optional[str] = None
    sides: list[BOPSide]

    # Classmethod to convert from a database row into a Bop object, handling the nested sides list.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["sides"] = [BOPSide.from_dict(s) for s in (d.get("sides") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Bop type.
# ------------------------------------------------------

# DLC: Factions related types, use the api_faction_detail view:
# FactionGoal represents a goal of a faction, with its key, name, category, and group. Nested within the Faction type.
@strawberry.type
class FactionGoal:
    goal_key: str
    name_loc: Optional[str] = None
    category: Optional[str] = None
    goal_group: Optional[str] = None
# End of FactionGoal type.

# FactionRule represents a rule of a faction, with its key, type, and group. Nested within the Faction type.
@strawberry.type
class FactionRule:
    rule_key: str
    rule_type: Optional[str] = None
    rule_group_key: Optional[str] = None
# End of FactionRule type.

# FactionMemberUpgrade represents an upgrade for a faction member, with its key, bonus value, and description. Nested within the FactionUpgradeGroup type.
@strawberry.type
class FactionMemberUpgrade:
    upgrade_key: str
    bonus: Optional[float] = None
    description_loc: Optional[str] = None
# End of FactionMemberUpgrade type.

# FactionUpgradeGroup represents a group of upgrades for faction members, with its key, name, type, and the list of upgrades. Nested within the Faction type.
@strawberry.type
class FactionUpgradeGroup:
    group_key: str
    name_loc: Optional[str] = None
    upgrade_type: Optional[str] = None
    upgrades: list[FactionMemberUpgrade]

    # Classmethod to convert from a dictionary (from the database) into a FactionUpgradeGroup object, handling the upgrades list which may be null.
    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        d["upgrades"] = [FactionMemberUpgrade(**u) for u in (d.get("upgrades") or [])]
        return cls(**d)
    # End of from_dict class method.
# End of FactionUpgradeGroup type.

# Faction represents a faction in the game, with its template key, name, icon, goals, rules, and member upgrade groups.
@strawberry.type
class Faction:
    template_key: str
    name_loc: Optional[str] = None
    manifest_key: Optional[str] = None
    icon: Optional[str] = None
    can_leader_join_other: Optional[bool] = None
    dlc_source: Optional[str] = None
    goals: list[FactionGoal]
    rules: list[FactionRule]
    member_upgrade_groups: list[FactionUpgradeGroup]

    # Classmethod to convert from a database row into a Faction object, handling the nested lists for goals, rules, and member upgrade groups.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["goals"] = [FactionGoal(**g) for g in (d.get("goals") or [])]
        d["rules"] = [FactionRule(**r) for r in (d.get("rules") or [])]
        d["member_upgrade_groups"] = [FactionUpgradeGroup.from_dict(g) for g in (d.get("member_upgrade_groups") or [])]
        return cls(**d)
    # End of from_row class method.
# End of Faction type.
# ------------------------------------------------------

# DLC: Projects related types, use the api_project_detail view:
# ProjectReward represents a reward for completing a project, with its key, whether it can only be earned once, and thresholds for earning it. Nested within the SpecialProject type.
@strawberry.type
class ProjectReward:
    reward_key: str
    fire_only_once: Optional[bool] = None
    threshold_min: Optional[int] = None
    threshold_max: Optional[int] = None
# End of ProjectReward type.

# SpecialProject represents a special project in the game, with its key, specialization, rewards, and other details.
@strawberry.type
class SpecialProject:
    project_key: str
    specialization_key: str
    project_tag: Optional[str] = None
    complexity: Optional[str] = None
    prototype_time: Optional[str] = None
    dlc_source: Optional[str] = None
    rewards: list[ProjectReward]

    # Classmethod to convert from a database row into a SpecialProject object, handling the nested rewards list.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        d["rewards"] = [ProjectReward(**r) for r in (d.get("rewards") or [])]
        return cls(**d)
    # End of from_row class method.
# End of SpecialProject type.
# ------------------------------------------------------

# Annotation related types, use the api_annotation_detail view:
# Annotation is a more generic type that represents a user-created annotation for an entity in the game, with its ID, type, key, note content, and creation timestamp. 
@strawberry.type
class Annotation:
    annotation_id: int
    entity_type: str
    entity_key: str
    note: str
    created_at: datetime

    # Classmethod to convert from a database row into an Annotation object.
    @classmethod
    def from_row(cls, row):
        return cls(**dict(row))
    # End of from_row class method.
# End of Annotation type.
# ------------------------------------------------------

# Wargoal related types, use the api_wargoal_detail view:
# Wargoal represents a wargoal in the game, with its key, name, costs, threat, and other details. 
@strawberry.type
class Wargoal:
    wargoal_key: str
    war_name_key: Optional[str] = None
    generate_base_cost: Optional[int] = None
    generate_per_state_cost: Optional[int] = None
    take_states_limit: Optional[int] = None
    take_states_cost: Optional[int] = None
    puppet_cost: Optional[int] = None
    force_government_cost: Optional[int] = None
    expire: Optional[int] = None
    threat: Optional[float] = None
    take_states_threat_factor: Optional[float] = None
    allowed_block: Optional[str] = None
    available_block: Optional[str] = None
    source_file: Optional[str] = None

    # Classmethod to convert from a database row into a Wargoal object.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        # Convert Decimal to float for numeric fields
        for k in ("threat", "take_states_threat_factor"):
            if d.get(k) is not None:
                d[k] = float(d[k])
        return cls(**d)
    # End of from_row class method.
# End of Wargoal type.
# ------------------------------------------------------

# Diplomacy and faction related types, use the api_diplomatic_relation_detail view:
# DiplomaticRelation represents a diplomatic relation between two countries, with its type, autonomy level, freedom level, effective date, and other details.
@strawberry.type
class DiplomaticRelation:
    diplomatic_relation_id: int
    country_tag: str
    target_tag: str
    relation_type: str
    autonomy_type: Optional[str] = None
    freedom_level: Optional[float] = None
    effective_date: Optional[str] = None
    dlc_source: Optional[str] = None
    source_file: Optional[str] = None

    # Classmethod to convert from a database row into a DiplomaticRelation object, handling the conversion of numeric fields and date fields.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        if d.get("freedom_level") is not None:
            d["freedom_level"] = float(d["freedom_level"])
        if d.get("effective_date") is not None:
            d["effective_date"] = str(d["effective_date"])
        return cls(**d)
    # End of from_row class method.
# End of DiplomaticRelation type.

# StartingFactionMember represents a member of a starting faction, with their tag and name. Nested within the StartingFaction type.
@strawberry.type
class StartingFactionMember:
    member_tag: str
    member_name: Optional[str] = None
# End of StartingFactionMember type.

# StartingFaction represents a faction that exists at the start of the game, with its ID, template key, leader, effective date, and members.
@strawberry.type
class StartingFaction:
    starting_faction_id: int
    faction_template_key: str
    leader_tag: str
    leader_name: Optional[str] = None
    effective_date: Optional[str] = None
    members: list[StartingFactionMember] = strawberry.field(default_factory=list)

    # Classmethod to convert from a database row into a StartingFaction object, handling the conversion of date fields and the nested members list.
    @classmethod
    def from_row(cls, row):
        d = dict(row)
        if d.get("effective_date") is not None:
            d["effective_date"] = str(d["effective_date"])
        members_raw = d.pop("members", [])
        import json
        if isinstance(members_raw, str):
            members_raw = json.loads(members_raw)
        d["members"] = [StartingFactionMember(**m) for m in members_raw]
        return cls(**d)
    # End of from_row class method.
# End of StartingFaction type.
# ------------------------------------------------------