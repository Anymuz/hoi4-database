# app/schemas/ideology.py
from pydantic import BaseModel # For defining data models and validation

# Pydantic schemas (response models) for ideologies and sub-ideologies.

# SubIdeology represents a sub-ideology nested under an ideology (e.g. nazism under fascism).
class SubIdeology(BaseModel):
    sub_ideology_key: str
# End of SubIdeology model

# ColorRGB represents the RGB color assigned to an ideology in the game UI.
class ColorRGB(BaseModel):
    r: int
    g: int
    b: int
# End of ColorRGB model

# Ideology represents a top-level ideology with its color and nested sub-ideologies.
class Ideology(BaseModel):
    ideology_key: str
    color_rgb: ColorRGB
    sub_ideologies: list[SubIdeology] = []
# End of Ideology model
