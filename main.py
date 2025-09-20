from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import random

app = FastAPI(
    title="Garagem de Carros API",
    version="1.0",
    description="API de revenda de carros - CRUD em memória"
)

class Carro(BaseModel):
    marca: str
    modelo: str
    ano: int
    disponivel: bool = True

db: Dict[int, Carro] = {}

@app.get("/helloworld")
async def root():
    return {"message": "Bem-vindo à Garagem de Carros!"}

@app.get("/fila")
async def senha():
    return {"senha": True, "num_aleatorio": random.randint(0, 5000)}

@app.post("/carros/", response_model=Carro)
async def criar_carro(carro: Carro):
    carro_id = len(db) + 1
    db[carro_id] = carro
    return carro

@app.get("/carros/{carro_id}", response_model=Carro)
async def obter_carro(carro_id: int):
    if carro_id not in db:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return db[carro_id]

@app.get("/carros/", response_model=dict)
async def listar_carros():
    return db

@app.put("/carros/{carro_id}", response_model=Carro)
async def atualizar_carro(carro_id: int, carro: Carro):
    if carro_id not in db:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    db[carro_id] = carro
    return carro

@app.delete("/carros/{carro_id}")
async def deletar_carro(carro_id: int):
    if carro_id not in db:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    del db[carro_id]
    return {"message": f"Carro {carro_id} removido da garagem com sucesso"}
