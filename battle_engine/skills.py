from dataclasses import dataclass
from typing import Optional
from battle_engine.status_effects import StatusType

@dataclass
class Skill:
    name: str
    power: int
    accuracy: int = 100
    status_effect: Optional[StatusType] = None
    status_chance: int = 0
