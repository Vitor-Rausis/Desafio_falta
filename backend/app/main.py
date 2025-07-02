from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import httpx
from .services import fetch_cep_data

app = FastAPI(title="CEP Microservice", version="1.0.0")

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CEPResponse(BaseModel):
    cep: str
    logradouro: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    localidade: str
    uf: str
    ibge: Optional[str]
    gia: Optional[str]
    ddd: Optional[str]
    siafi: Optional[str]

@app.get("/cep/{cep}", response_model=CEPResponse)
async def get_cep_info(cep: str):
    """
    Endpoint para consulta de CEP
    Formato esperado: 00000000 ou 00000-000
    """
    # Remove caracteres não numéricos
    cleaned_cep = "".join(filter(str.isdigit, cep))
    
    if len(cleaned_cep) != 8:
        raise HTTPException(
            status_code=400,
            detail="CEP deve conter 8 dígitos"
        )
    
    try:
        cep_data = await fetch_cep_data(cleaned_cep)
        if cep_data.get("erro"):
            raise HTTPException(
                status_code=404,
                detail="CEP não encontrado"
            )
        return cep_data
    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Erro ao consultar serviço de CEP"
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}