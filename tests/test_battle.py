import pytest
from battle_engine.creatures import Creature
from battle_engine.skills import Skill
from battle_engine.battle import calculate_damage, perform_attack

@pytest.fixture
def char1():
    tackle = Skill("Tackle", 40, 100)
    return Creature("C1", 100, 100, 50, 50, 50, [tackle])

@pytest.fixture
def char2():
    tackle = Skill("Tackle", 40, 100)
    return Creature("C2", 100, 100, 50, 50, 50, [tackle])

def test_calculate_damage(char1, char2):
    tackle = char1.skills[0]
    dmg = calculate_damage(char1, char2, tackle)
    
    assert dmg > 0
    assert isinstance(dmg, int)

def test_perform_attack_misses(char1, char2, mocker):
    mocker.patch("battle_engine.battle.calculate_hit", return_value=False)
    
    logs = perform_attack(char1, char2, char1.skills[0])
    
    assert len(logs) == 2
    assert "falhou" in logs[1]
    assert char2.hp == 100 # Sem dano

def test_perform_attack_hits(char1, char2, mocker):
    mocker.patch("battle_engine.battle.calculate_hit", return_value=True)
    mocker.patch("battle_engine.battle.calculate_damage", return_value=20)
    
    logs = perform_attack(char1, char2, char1.skills[0])
    
    assert len(logs) == 2
    assert "recebe 20 de dano" in logs[1]
    assert char2.hp == 80
