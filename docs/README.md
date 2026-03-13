# Documentação RPG Battle Engine

Esta pasta serve como base para documentação extra (diagramas, arquitetura aprofundada).

Para saber como rodar a API, referenciar o [README principal da raiz](../README.md).

## Endpoints Úteis
* `GET /creatures/` - Lista os pokémons disponíveis.
* `GET /creatures/{name}` - Pega os stats de um pokémon específico.
* `POST /battles/` - Recebe `creature1` e `creature2` no payload (ex: `"Charizard"` e `"Venusaur"`) e retorna as logs detalhadas turno-a-turno declarando um vencedor.
