from fastapi import FastAPI
from src.routers import extratoclube

app = FastAPI()

app.title = 'Desafio Konsi'
app.version = '0.0.1'

app.include_router(extratoclube.router)
