from pydantic import BaseModel
from typing import List, Optional
from battle_engine.status_effects import StatusType

class SkillSchema(BaseModel):
    name: str
    power: int
    accuracy: int
    status_effect: Optional[StatusType] = None
    status_chance: int = 0

class CreatureSchema(BaseModel):
    name: str
    max_hp: int
    hp: int
    attack: int
    defense: int
    speed: int
    skills: List[SkillSchema]
