# Microserviço de Consulta de CEP

Um microserviço simples para consulta de endereços a partir de CEPs, utilizando Python (FastAPI) no backend e Vue.js no frontend, containerizado com Docker.

## Funcionalidades

- Consulta de endereço completo a partir de um CEP
- Validação de formato de CEP
- Tratamento de erros para CEPs inválidos ou não encontrados
- Interface web amigável

## Tecnologias utilizadas

- **Backend**: Python 3.9 + FastAPI
- **Frontend**: Vue.js 3
- **API de CEP**: ViaCEP
- **Containerização**: Docker + Docker Compose

## Como executar

1. Certifique-se de ter o Docker e Docker Compose instalados
2. Clone este repositório
3. Execute o comando:
   ```bash
   docker-compose up --build