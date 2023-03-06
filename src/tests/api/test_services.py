from src.services.extratoclube_service import ExtratoClubeService
from src.schemas.payload import Payload
from src.config.env_config import Env

service = ExtratoClubeService()

def test_post_generate_headers_status_ok():
    response = service.generate_headers(
        login=Env('LOGIN_TEST').get(), password=Env('PASSWORD_TEST').get())
    assert response.status_code == 200

def test_post_seek_benefit_with_cpf_ok_or_not_found():
    payload = Payload(
        cpf=Env('CPF_TEST').get(), 
        login=Env('LOGIN_TEST').get(), 
        password=Env('PASSWORD_TEST').get()
    )
    response = service.seek_benefit_with_cpf(payload)
    assert response == { 'benefit': '1734164104' or 'Matrícula não encontrada!' }