from src.schemas.payload import Payload
import pytest

def test_schema_valid():
    Payload(cpf='000.000.000-00', login='login', password='password')

def test_cpf_invalid():
    with pytest.raises(ValueError, 
                       match='Invalid field value, example: 000.000.000-00'):
        Payload(cpf='', login='login', password='password')

def test_login_and_password_not_empty():
    with pytest.raises(ValueError, 
                       match='Field cannot be empty'):
        Payload(cpf='000.000.000-00', login='', password='')