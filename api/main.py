from fastapi import FastAPI
from api.routes import creatures, battles

app = FastAPI(
    title="API - Motor de Batalha RPG",
    description="Um motor de batalha RPG completo inspirado em Pokémon com interface REST",
    version="1.0.0"
)

app.include_router(creatures.router)
app.include_router(battles.router)

@app.get("/")
def root():
    return {"mensagem": "Bem-vindo à API do Motor de Batalha RPG. Acesse /docs para ver os endpoints!"}
