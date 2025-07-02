from pydantic import BaseModel

class CEPResponse(BaseModel):
    cep: str
    logradouro: str | None
    complemento: str | None
    bairro: str | None
    localidade: str
    uf: str
    ibge: str | None
    gia: str | None
    ddd: str | None
    siafi: str | None