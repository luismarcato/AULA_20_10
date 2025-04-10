from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Minha API de Investimentos",
    description="API para calcular retorno de ações",
    version="1.0.0",
    docs_url="/docs",       
    redoc_url="/redoc", 
)

class InfoPrevisao(BaseModel):
    empresa: str
    volume: float
    prev_fechamento: float

@app.get("/")
async def principal():
    return {"status" : True, 
            "message": "Hello World"}

@app.get("/previsoes")
def previsoes(infoPrevisao: InfoPrevisao):
    w0, w1, w2 = [-15.3, 1.0, -3.2]

    if (infoPrevisao.empresa == 'aapl'):
        previsao = w0 + w1 * infoPrevisao.prev_fechamento + w2 * infoPrevisao.volume
    else :
        previsao = 0

    return {"profecia": previsao}