DOCUMENTAÇÃO FEITA COM USO DE IA
# RPG Battle Engine

Um motor de batalha no estilo clássico de RPG (inspirado em Pokémon) escrito puramente em Python, fornecendo tanto um executor em linha de comando quanto uma API REST.

## Estrutura do Projeto
- `battle_engine/`: Módulo core que contém toda a lógica de dano, RNG, habilidades e criaturas.
- `api/`: Pacote contendo a aplicação FastAPI para interagir com o motor.
- `tests/`: Suíte de testes `pytest` para a lógica core.

## Executando o Projeto

Você tem três opções para rodar o motor:

### 1. Terminal Principal
Se deseja apenas ver uma batalha de demonstração simulada no console:
```bash
python3 main.py
```

### 2. Rodar a API (Localmente)
Para subir o servidor FastAPI e interagir na porta 8000:
```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Acesse a documentação Swagger em http://localhost:8000/docs.

### 3. Rodar a API (via Docker)
Para subir a API sem configurar o Python localmente:
```bash
docker build -t rpg-engine .
docker run -p 8000:8000 rpg-engine
```

## Testes
Para rodar a bateria de testes automatizados, instale os requirements e execute:
```bash
pytest
```
