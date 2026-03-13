from pydantic import BaseModel
from typing import List
from api.schemas.creature_schema import CreatureSchema

class BattleRequest(BaseModel):
    creature1: str
    creature2: str

class BattleResult(BaseModel):
    winner: str
    loser: str
    logs: List[str]
