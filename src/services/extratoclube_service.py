from fastapi import HTTPException, status
import requests
import json
from src.schemas.payload import Payload
from src.config.env_config import Env


class ExtratoClubeService:

    def seek_benefit_with_cpf(self, payload: Payload):
        response = requests.get(
            url='{}/{}'.format(Env('SEEK_URL').get(), payload.cpf),
            headers=self.generate_headers(payload.login, payload.password).headers
        )
        if response.status_code is not status.HTTP_200_OK:
            raise HTTPException(status_code=response.status_code)
        return { 'benefit': beneficio['nb'] for beneficio in response.json()['beneficios']}

    def generate_headers(self, login: str, password: str):
        payload = json.dumps({ "login": login, "senha": password })
        response = requests.post(url=Env('LOGIN_URL').get(), data=payload)

        if response.status_code is not status.HTTP_200_OK:
            raise HTTPException(status_code=response.status_code)
        return response
