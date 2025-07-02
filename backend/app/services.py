import httpx

VIA_CEP_URL = "https://viacep.com.br/ws/{cep}/json/"

async def fetch_cep_data(cep: str) -> dict:
    """
    Consulta o ViaCEP para obter informações do CEP fornecido
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(VIA_CEP_URL.format(cep=cep))
        response.raise_for_status()
        return response.json()