# Desafio-konsi - Crawler Extratoclube

## Tecnologias usadas

- Python: 3.10
- FastAPI: 0.92.0
- Pydantic: 1.10.5
- Pytest: 7.2.2
- Docker: 23.0.1

## Instalação com docker

1. basta entrar na pasta desafio-konsi e digitar `docker-compose up -d` via linha de comando, apos o build o backend estará rodando na porta `http://localhost:8000`


## Instalação local

1. basta entrar na pasta desafio-konsi, e criar o ambiente virtual com o seguinte comando: `python -m venv .venv` ou `python3 -m venv .venv`
2. em seguida vamos ativar o ambiente virtual no caso do linux e mac seria `source .venv/bin/activate` e para windows `.venv\Scripts\activate`
3. com ambiente ativado vamos instalar as libs e dependencias do projeto com o comando `pip install -r requirements.txt`
4. com tudo instalado agora é so executar o comando `uvicorn src.server:app --reload` e pronto, o projeto estará rodando na porta `http://localhost:8000`.


## Testes Unitarios

- **Com ambiente docker** os tests automatizados são executados na primeira vez que o projeto é buildado, para executar novamente basta rodar o comando `docker-compose up -d --build`,
tambem é possivel rodar os testes entrando no container com o comando `docker container exec -it desafio-konsi-app bash` e em seguida rodar `pytest`.

- **Com ambiente local** basta entrar na pasta  desafio-konsi e rodar o comando `pytest`.


## Documentação

Para acessar a documentação da api é so entrar em: `http://localhost:8000/docs` ou `http://localhost:8000/redoc`.
