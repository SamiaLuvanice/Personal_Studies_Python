from fastapi import FastAPI

app = FastAPI()
#Dicionáio de jogadores
jogadores = {
    1: {"nome": "Luiz", "idade": 25, "time": "Brasil"},
    2: {"nome": "Vini", "idade": 30, "time": "Argentina"},
    3: {"nome": "Antonio", "idade": 28, "time": "França"},
}

# localhost:8000/
@app.get("/")
def inicio():
    return {"message": "Olá, mundo!"}

@app.get("/jogadores")
def lista_jogadores():
    return jogadores

# Path parameter  
@app.get("/busca-jogador-id/{jogador_id}")
def busca_jogador_id(jogador_id: int):
    return jogadores[jogador_id]

# Query parameter 
@app.get("/busca-jogador-nome")
def busca_jogador_nome(nome: str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["nome"] == nome:
            return jogadores[jogador_id]
    return {"message": "Jogador não encontrado"}