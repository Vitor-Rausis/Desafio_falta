# Microserviço de Consulta de CEP

Um microserviço simples para consulta de endereços a partir de CEPs, utilizando Python (FastAPI) no backend e Vue.js no frontend, containerizado com Docker.

## Funcionalidades

- Consulta de endereço completo a partir de um CEP
- Validação de formato de CEP
- Tratamento de erros para CEPs inválidos ou não encontrados
- Interface web amigável
- **Nova funcionalidade**: Adição e salvamento de complemento quando não informado

## Tecnologias utilizadas

- **Backend**: Python 3.9 + FastAPI
- **Frontend**: Vue.js 3
- **API de CEP**: ViaCEP
- **Containerização**: Docker + Docker Compose

## Como executar

1. Certifique-se de ter o Docker e Docker Compose instalados
2. Clone este repositório:
   ```bash
   git clone https://github.com/Vitor-Rausis/Desafio_falta.git
   cd Desafio_falta
   ```
3. Execute o comando:
   ```bash
   docker-compose up --build
   ```

## Como usar

1. Acesse a aplicação no navegador: `http://localhost:8080`
2. Digite um CEP no formato 00000-000 ou 00000000
3. Clique em "Consultar" para obter as informações do endereço
4. Se o complemento não estiver informado, você pode adicionar um e salvá-lo

## Estrutura do projeto

```
Desafio_falta/
├── backend/          # API FastAPI
├── frontend/         # Interface Vue.js
├── docker-compose.yml
└── README.md
```

## Endpoints da API

- `GET /cep/{cep}` - Consulta informações do CEP
- `POST /cep/{cep}/complemento` - Salva complemento para um CEP
- `GET /health` - Verificação de saúde da API