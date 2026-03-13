import copy
from fastapi import APIRouter, HTTPException
from api.schemas.battle_schema import BattleRequest, BattleResult
from api.routes.creatures import AVAILABLE_CREATURES
from battle_engine.battle import run_battle

router = APIRouter(prefix="/battles", tags=["Battles"])

@router.post("/", response_model=BattleResult)
def start_battle(request: BattleRequest):
    """Simula um combate até uma criatura desmaiar e retorna os logs."""
    if request.creature1 not in AVAILABLE_CREATURES or request.creature2 not in AVAILABLE_CREATURES:
        raise HTTPException(status_code=404, detail="Uma ou ambas as criaturas não foram encontradas")
        
    c1 = copy.deepcopy(AVAILABLE_CREATURES[request.creature1])
    c2 = copy.deepcopy(AVAILABLE_CREATURES[request.creature2])
    
    logs = run_battle(c1, c2)
    
    winner = c1.name if c1.is_alive() else c2.name
    loser = c2.name if c1.is_alive() else c1.name
    
    return BattleResult(winner=winner, loser=loser, logs=logs)
