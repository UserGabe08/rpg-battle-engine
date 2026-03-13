from fastapi import APIRouter, HTTPException
from typing import List
from api.schemas.creature_schema import CreatureSchema
from battle_engine.skills import Skill
from battle_engine.status_effects import StatusType
from battle_engine.creatures import Creature

router = APIRouter(prefix="/creatures", tags=["Creatures"])

# Banco de dados simulado
tackle = Skill(name="Tackle", power=40, accuracy=100)
ember = Skill(name="Ember", power=40, accuracy=100, status_effect=StatusType.BURN, status_chance=10)
flamethrower = Skill(name="Flamethrower", power=90, accuracy=100, status_effect=StatusType.BURN, status_chance=10)
water_gun = Skill(name="Water Gun", power=40, accuracy=100)
hydro_pump = Skill(name="Hydro Pump", power=110, accuracy=80, status_effect=StatusType.WET, status_chance=30)
vine_whip = Skill(name="Vine Whip", power=45, accuracy=100)
sludge_bomb = Skill(name="Sludge Bomb", power=90, accuracy=100, status_effect=StatusType.POISON, status_chance=30)
spark = Skill(name="Spark", power=65, accuracy=100, status_effect=StatusType.STUN, status_chance=30)
thunderbolt = Skill(name="Thunderbolt", power=90, accuracy=100, status_effect=StatusType.STUN, status_chance=10)
ice_beam = Skill(name="Ice Beam", power=90, accuracy=100, status_effect=StatusType.FREEZE, status_chance=10)

AVAILABLE_CREATURES = {
    "Charizard": Creature("Charizard", 78, 78, 84, 78, 100, [tackle, ember, flamethrower]),
    "Blastoise": Creature("Blastoise", 79, 79, 83, 100, 78, [tackle, water_gun, hydro_pump]),
    "Venusaur": Creature("Venusaur", 80, 80, 82, 83, 80, [tackle, vine_whip, sludge_bomb]),
    "Pikachu": Creature("Pikachu", 35, 35, 55, 40, 90, [tackle, spark, thunderbolt]),
    "Lapras": Creature("Lapras", 130, 130, 85, 80, 60, [water_gun, ice_beam]),
}

@router.get("/", response_model=List[CreatureSchema])
def list_creatures():
    """Lista todas as criaturas disponíveis no jogo."""
    return list(AVAILABLE_CREATURES.values())

@router.get("/{name}", response_model=CreatureSchema)
def get_creature(name: str):
    """Pega os detalhes de uma criatura específica pelo nome."""
    if name not in AVAILABLE_CREATURES:
        raise HTTPException(status_code=404, detail="Criatura não encontrada")
    return AVAILABLE_CREATURES[name]
