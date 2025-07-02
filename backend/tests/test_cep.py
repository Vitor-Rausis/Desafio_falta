import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_valid_cep():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/cep/01001000")
        assert response.status_code == 200
        data = response.json()
        assert data["cep"] == "01001-000"
        assert data["localidade"] == "São Paulo"
        assert data["uf"] == "SP"

@pytest.mark.asyncio
async def test_invalid_cep_format():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/cep/123")
        assert response.status_code == 400
        assert response.json()["detail"] == "CEP deve conter 8 dígitos"

@pytest.mark.asyncio
async def test_nonexistent_cep():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/cep/00000000")
        assert response.status_code == 404
        assert response.json()["detail"] == "CEP não encontrado"

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}