#app/schema/dlc.py
from pydantic import BaseModel

# Pydantic schemas for DLC data, used for API responses and data validation.

# MIO Models:
# Military Idustrial Organization entry in a DLC for lists, contains the name of the MIO and its effects.
class MIOSummary(BaseModel):
    organization_key: str                                 # Unique key for the MIO (e.g. "military_industrial_complex")#
    template_icon: str | None = None             # Icon for the MIO, can be used in UI elements
    template_key: str | None = None              # Key for the MIO template, can be used to link to more details if needed  
    icon: str | None = None                             # Icon for the MIO, can be used in UI elements
    dlc_source: str | None = None                   # Which DLC this MIO comes from (e.g. "La Resistance")
    equipment_types: list[str] = []                    # List of equipment types that benefit from this MIO (e.g. ["infantry_equipment", "artillery_equipment"])       
# End of MIOSummary model

# Entry for a trait bonus provided by an MIO trait, contains the type of bonus and its value.
class MIOTraitBonus(BaseModel):
    key: str                                       # Unique key for the bonus (e.g. "production_efficiency_bonus")  
    category: str | None = None     # Type of bonus (e.g. "production_efficiency", "research_speed")                                            # Value of the bonus (e.g. 0.1 for +10%)
    value: float | None = None           # Human-readable value of the bonus (e.g. "+10%")
# End of MIOTraitBonus model

#  Entry for a trait provided by an MIO, contains the type of bonus and its value.
class MIOTrait(BaseModel):
    trait_token: str                                   # Unique key for the trait
    trait_type: str | None = None            # Type of trait (e.g. "production_efficiency", "research_speed")
    name: str | None = None                  # Human-readable name of the trait (e.g. "+10% Production Efficiency")    
    position_x: int | None = None           # X position for UI display (if needed)
    position_y: int | None = None           # Y position for UI display (if needed)
    bonuses: list[MIOTraitBonus] = []      # List of bonuses provided by this trait (e.g. [{"bonus_type": "production_efficiency", "value": 0.1}])
# End of MIOTrait model

# Detailed information about an MIO, includes all data including the traits it provides.
class MIODetail(MIOSummary):
     traits: list[MIOTrait] = []                                    # List of traits provided by this MIO (e.g. ["+10% production efficiency", "+5% research speed"])
# End of MIODetail model
# -----------------------------------------------

# Operation Models:
# Operation entry in a DLC, contains the name of the operation and its effects. Summary version for lists.
class OperationSummary(BaseModel):
    operation_key: str
    name: str | None = None
    days: int | None = None
    network_strength: int | None = None
    operatives: int | None = None
    risk_chance: float | None = None
    experience: float | None = None
    dlc_source: str | None = None

# Operation equipment entry, contains the name of the equipment and amount needed.
class OperationEquipment(BaseModel):
    equipment_key: str                           # Unique key for the equipment (e.g. "infantry_equipment")#
    amount: int | None = None              # Amount of this equipment needed for the operation, can be used to compare operations
# End of OperationEquipment model

# Phase option, contains the name of the option and its weight.
class PhaseOption(BaseModel):
    phase_key: str
    base_weight: float | None = None

# Phase group, puts  phase options into groups, contains the sequence number of the group and the options in it.
class PhaseGroup(BaseModel):
    sequence_index: int | None = None         # Sequence number of the group, can be used to order the groups
    options: list[PhaseOption] = []                 # List of options in this group
# End of PhaseGroup model

# Full details of an operation, includes all data including the equipment needed and the phase groups.
class OperationDetail(OperationSummary):
    awarded_tokens: list[str] = []                     # List of tokens awarded by this operation (e.g. ["resistance_leader_token", "spy_token"])
    equipment_requirements: list[OperationEquipment] = []     # List of equipment requirements for this operation (e.g. [{"equipment_key": "infantry_equipment", "amount": 100}])
    phase_groups: list[PhaseGroup] = []                 # List of phase groups for this operation, each containing options (e.g. [{"sequence_index": 1, "options": [{"phase_key": "sabotage", "weight": 70}, {"phase_key": "propaganda", "weight": 30}]}])
# End of OperationDetail model
# -----------------------------------------------

# Balance of Power Models:
# Balance of Power entry, contains the name of the mechanic and its effects. Summary version for lists.
class BOPSummary(BaseModel):
    bop_key: str
    initial_value: float | None = None
    left_side: str | None = None
    right_side: str | None = None
    decision_category: str | None = None

# Range modifier entry, contains the key of the modifier and its value.
class BOPRangeModifier(BaseModel):
    modifier_key: str
    modifier_value: float | None = None

#  Range entry, contains the BoP range and the modifiers that apply to it.
class BOPRange(BaseModel):
    range_id: str
    min_value: float | None = None
    max_value: float | None = None
    modifiers: list[BOPRangeModifier] = []

# Entry for a side in a BoP mechanic.
class BOPSide(BaseModel):
    side_id: str
    side_position: str | None = None
    icon: str | None = None                             # Icon for the side, can be used in UI elements
    ranges: list[BOPRange] = []                     # List of BoP ranges for this side, each containing modifiers 
# End of BOPSide model

# Full details of a BoP mechanic, includes all data including the sides and their ranges and modifiers.
class BOPDetail(BOPSummary):
    sides: list[BOPSide] = []                     # List of sides in this BoP mechanic, each containing ranges and modifiers.
# End of BOPDetail model
# -----------------------------------------------

# Faction Models:

class FactionGoal(BaseModel):
    goal_key: str
    name_loc: str | None = None
    category: str | None = None
    goal_group: str | None = None

class FactionRule(BaseModel):
    rule_key: str
    rule_type: str | None = None
    rule_group_key: str | None = None

class FactionMemberUpgrade(BaseModel):
    upgrade_key: str
    bonus: float | None = None
    description_loc: str | None = None

class FactionUpgradeGroup(BaseModel):
    group_key: str
    name_loc: str | None = None
    upgrade_type: str | None = None
    upgrades: list[FactionMemberUpgrade] = []

class FactionSummary(BaseModel):
    template_key: str
    name_loc: str | None = None
    manifest_key: str | None = None
    icon: str | None = None
    can_leader_join_other: bool | None = None
    dlc_source: str | None = None

class FactionDetail(FactionSummary):
    goals: list[FactionGoal] = []
    rules: list[FactionRule] = []
    member_upgrade_groups: list[FactionUpgradeGroup] = []
# ------------------------------------------------

# Special Project Models:

class ProjectReward(BaseModel):
    reward_key: str
    fire_only_once: bool | None = None
    threshold_min: int | None = None
    threshold_max: int | None = None

class SpecialProjectSummary(BaseModel):
    project_key: str
    specialization_key: str
    project_tag: str | None = None
    complexity: str | None = None
    prototype_time: str | None = None
    dlc_source: str | None = None

class SpecialProjectDetail(SpecialProjectSummary):
    rewards: list[ProjectReward] = []

