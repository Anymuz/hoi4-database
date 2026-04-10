# app/schemas/military.py
from pydantic import BaseModel

# Pydantic schemas for military data, used for API responses and data validation.

# Division models:
# Regiment entry in a division template (e.g. {"unit_type_key": "infantry", "grid_x": 0, "grid_y": 0})
class Regiment(BaseModel):
    unit_type_key: str
    grid_x: int | None = None
    grid_y: int | None = None
# End of Regiment model

# Support company entry in a division template (e.g. {"unit_type_key": "engineer_company", "grid_x": 3, "grid_y": 0})
class SupportCompany(BaseModel):
    unit_type_key: str
    grid_x: int | None = None
    grid_y: int | None = None
# End of SupportCompany model

# Deployed division entry (e.g. {"location_province_id": 123, "start_experience_factor": 0.5})
class Deployed(BaseModel):
    location_province_id: int | None = None
    start_experience_factor: float | None = None
# End of Deployed model

# Division details for a single division template, includes all data including which country it belongs to and where it's deployed.
class DivisionDetail(BaseModel):
    country_tag: str
    division_template_id: int
    template_name: str
    oob_file: str | None = None
    regiments: list[Regiment] = []
    support: list[SupportCompany] = []
    deployed_divisions: list[Deployed] = []
# End of DivisionDetail model
# ----------------------------------------------

# Naval models:
# Ship entry in a task force, contains ship name, definition, hull equipment, and whether it's pride of the fleet.
class Ship(BaseModel):
    ship_name: str
    definition: str
    hull_equipment_key: str
    version_name: str | None = None
    pride_of_the_fleet: bool | None = None
# End of Ship model

# Task force entry in a fleet, contains task force name, location, and list of ships.
class TaskForce(BaseModel):
    task_force_id: int
    task_force_name: str
    location_province_id: int | None = None
    ships: list[Ship] = []
# End of TaskForce model

# Naval details for a single fleet, includes all data including which country it belongs to and its task forces.
class NavalDetail(BaseModel):
    country_tag: str
    fleet_id: int
    fleet_name: str
    naval_base_province_id: int | None = None
    oob_file: str | None = None
    task_forces: list[TaskForce] = []
# End of NavalDetail model
# ----------------------------------------------

# Air models:
# Air wing entry, contains location, equipment type and amount, and optional wing name and version.
class AirWingItem(BaseModel):
    country_tag: str
    location_state_id: int
    state_name_key: str
    equipment_type: str
    amount: int
    wing_name: str | None = None
    version_name: str | None = None
    oob_file: str | None = None
# End of AirWingItem model
# -----------------------------------------------