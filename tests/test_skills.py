import pytest
from battle_engine.skills import Skill
from battle_engine.status_effects import StatusType

def test_skill_initialization():
    basic_skill = Skill(name="Punch", power=50)
    assert basic_skill.name == "Punch"
    assert basic_skill.power == 50
    assert basic_skill.accuracy == 100
    assert basic_skill.status_effect is None
    
    effect_skill = Skill(name="Ember", power=40, status_effect=StatusType.BURN, status_chance=10)
    assert effect_skill.status_effect == StatusType.BURN
    assert effect_skill.status_chance == 10
