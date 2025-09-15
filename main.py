from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,20000)}