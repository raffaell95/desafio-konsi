from fastapi import status
from fastapi.testclient import TestClient
from src.config.env_config import Env


def test_post_seek_benefit_status_ok(client: TestClient) -> None:
    payload = {
        'cpf': Env('CPF_TEST').get(), 
        'login': Env('LOGIN_TEST').get(), 
        'password': Env('PASSWORD_TEST').get()
    }
    respose = client.post('/', json=payload)
    assert respose.status_code == status.HTTP_200_OK


def test_post_benefit_ok_or_not_found(client: TestClient) -> None:
    payload = {
        'cpf': Env('CPF_TEST').get(), 
        'login': Env('LOGIN_TEST').get(), 
        'password': Env('PASSWORD_TEST').get()
    }
    respose = client.post('/', json=payload)
    assert respose.json() == { 'benefit': '1734164104' or 'Matrícula não encontrada!' }