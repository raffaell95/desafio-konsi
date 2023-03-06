from fastapi import APIRouter, Depends
from src.schemas.payload import Payload
from src.services.extratoclube_service import ExtratoClubeService

router = APIRouter()

@router.post('/',tags=["Benefits"], summary='Seek benefit with CPF')
def seek_benefit(payload: Payload, service = Depends(ExtratoClubeService)):
    """
    To carry out a search, the appropriate fields must be filled in.
    - **CPF**: example: 000.000.000-00
    - **login**: The user registered in the search system must be informed
    - **password**: The password registered in the search system must be informed
    """
    return service.seek_benefit_with_cpf(payload)