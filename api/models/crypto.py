from pydantic import BaseModel

class Crypto(BaseModel):
    id: str
    symbol: str
    name: str
    price: float
    market_cap: float
    volume: float

class TopCrypto(BaseModel):
    name: str
    price: float
    market_cap: float