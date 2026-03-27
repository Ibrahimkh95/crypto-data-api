from fastapi import APIRouter
from api.services.crypto_service import get_top_cryptos
from api.models.crypto import TopCrypto
from typing import List

router = APIRouter()

@router.get("/top", response_model=List[TopCrypto])
def read_top_cryptos():
    """
    top 5 Market Cap.
    """
    return get_top_cryptos()