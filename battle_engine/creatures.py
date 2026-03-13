from dataclasses import dataclass, field
from typing import List
from battle_engine.skills import Skill
from battle_engine.status_effects import StatusEffect

@dataclass
class Creature:
    name: str
    max_hp: int
    hp: int
    attack: int
    defense: int
    speed: int
    skills: List[Skill]
    status: List[StatusEffect] = field(default_factory=list)

    def is_alive(self) -> bool:
        return self.hp > 0

    def apply_status(self, new_status: StatusEffect) -> str:
        for s in self.status:
            if s.status_type == new_status.status_type:
                s.duration = max(s.duration, new_status.duration)
                return ""
        self.status.append(new_status)
        return f"[{self.name}] foi afligido com {new_status.status_type.value}!"

    def process_status_effects(self) -> list[str]:
        logs = []
        active_status = []
        for s in self.status:
            logs.extend(s.apply_effect(self))
            s.duration -= 1
            if s.duration > 0:
                active_status.append(s)
            else:
                logs.append(f"O efeito {s.status_type.value} de {self.name} passou.")
        self.status = active_status
        return logs

    def can_act_this_turn(self, logs: list[str]) -> bool:
        for s in self.status:
            if not s.can_act(self, logs):
                return False
        return True
