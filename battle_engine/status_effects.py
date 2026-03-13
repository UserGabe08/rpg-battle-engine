from enum import Enum
from dataclasses import dataclass
from typing import Any

class StatusType(Enum):
    BURN = "Burn"
    POISON = "Poison"
    STUN = "Stun"
    WET = "Wet"
    FREEZE = "Freeze"

@dataclass
class StatusEffect:
    status_type: StatusType
    duration: int
    
    def apply_effect(self, creature: Any) -> list[str]:
        logs = []
        if self.status_type == StatusType.BURN:
            damage = max(1, int(creature.max_hp * 0.0625))
            creature.hp = max(0, creature.hp - damage)
            logs.append(f"[{creature.name}] sofre {damage} de dano devido a {self.status_type.value}!")
        elif self.status_type == StatusType.POISON:
            damage = max(1, int(creature.max_hp * 0.125))
            creature.hp = max(0, creature.hp - damage)
            logs.append(f"[{creature.name}] sofre {damage} de dano devido a {self.status_type.value}!")
        return logs
            
    def can_act(self, creature: Any, logs: list[str]) -> bool:
        if self.status_type == StatusType.STUN:
            logs.append(f"[{creature.name}] esta paralisado e nao pode se mover!")
            return False
        elif self.status_type == StatusType.FREEZE:
            logs.append(f"[{creature.name}] esta congelado e nao pode se mover!")
            return False
        return True
