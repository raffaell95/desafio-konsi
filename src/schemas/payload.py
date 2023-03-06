from pydantic import BaseModel, validator


class Payload(BaseModel):
    cpf: str
    login: str
    password: str

    @validator('login', 'password', allow_reuse=True)
    def not_empty(cls, value: str):
        if value == '':
            raise ValueError('Field cannot be empty')
        return value
    
    @validator('cpf', allow_reuse=True)
    def not_str(cls, value: str):
        if len(value) < 14:
            raise ValueError('Invalid field value, ' + 
                             'example: 000.000.000-00')
        return value