 
from fastapi import HTTPException
from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from api.core.logger import logger
from api.services.crypto_service import (
    get_cryptos,
    get_crypto,
    get_top_cryptos,
    search_cryptos,
    get_cryptos_stats)
	
from api.models.crypto import Crypto



router = APIRouter()


@router.get("/cryptos")
def read_cryptos(imit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    min_price: Optional[float] = Query(None, ge=0),
    sort_by: str = Query("market_cap"),
    order: str = Query("desc")
):
    logger.info(f"Request: /cryptos | limit={limit}, offset={offset}")
    result = get_cryptos(
        limit=limit,
        offset=offset,
        min_price=min_price,
        sort_by=sort_by,
        order=order
    )
	

    if not result["data"]:
        logger.warning("No cryptos found")
        raise HTTPException(status_code=404, detail="No cryptos found")

    return result

# GET /cryptos/search?query=
@router.get("/cryptos/search", response_model=List[Crypto])
def search_cryptos_endpoint(query: str):
    data = search_cryptos(query)
    if not data:
        raise HTTPException(status_code=404, detail="No matching cryptos found")
    return data

# GET /cryptos/stats
@router.get("/cryptos/stats")
def cryptos_stats_endpoint():
    stats = get_cryptos_stats()
    if not stats:
        raise HTTPException(status_code=404, detail="No data found")
    return stats

@router.get("/cryptos/{symbol}")
def get_crypto_by_symbol(symbol: str):
    logger.info(f"GET /cryptos/{symbol}")

    data = get_crypto(symbol)

    if not data:
        logger.error(f"Crypto not found: {symbol}")
        raise HTTPException(status_code=404, detail="Crypto not found")

    return data


@router.get("/health")
def health():
    logger.info("Health check called")
    return {"status": "ok"}