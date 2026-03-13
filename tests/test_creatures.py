import pytest
from battle_engine.creatures import Creature
from battle_engine.skills import Skill
from battle_engine.status_effects import StatusEffect, StatusType

@pytest.fixture
def mock_creature():
    tackle = Skill(name="Tackle", power=40, accuracy=100)
    return Creature("Tester", 100, 100, 50, 50, 50, [tackle])

def test_creature_initialization(mock_creature):
    assert mock_creature.name == "Tester"
    assert mock_creature.hp == 100
    assert mock_creature.is_alive()

def test_creature_takes_damage(mock_creature):
    mock_creature.hp -= 30
    assert mock_creature.hp == 70
    assert mock_creature.is_alive()
    
    mock_creature.hp -= 70
    assert not mock_creature.is_alive()

def test_creature_apply_status(mock_creature):
    burn = StatusEffect(StatusType.BURN, 3)
    log = mock_creature.apply_status(burn)
    
    assert len(mock_creature.status) == 1
    assert "foi afligido com Burn" in log
    
    # Verifica a lógica de duração máxima
    burn2 = StatusEffect(StatusType.BURN, 5)
    mock_creature.apply_status(burn2)
    assert len(mock_creature.status) == 1
    assert mock_creature.status[0].duration == 5

def test_creature_process_status(mock_creature):
    poison = StatusEffect(StatusType.POISON, 2)
    mock_creature.apply_status(poison)
    
    logs = mock_creature.process_status_effects()
    
    assert mock_creature.hp < 100 # Veneno causa dano
    assert mock_creature.status[0].duration == 1
    assert len(logs) == 1
    assert "Poison" in logs[0]
