from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    ambiente = os.getenv("AMBIENTE", "Desenvolvimento")
    return {"mensagem": "API FastAPI no ar!", "ambiente": ambiente}

@app.get("/health")
def health_check():
    return {"status": "ok"}