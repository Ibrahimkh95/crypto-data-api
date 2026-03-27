from fastapi import FastAPI
from api.routes import cryptos, top
from api.core.logger import logger
 
 
app = FastAPI()
app = FastAPI(
    title="Crypto Data API",
    description="API show data professionally ",
    version="1.0.0"
)
app.include_router(cryptos.router, prefix="/api/v1")
# add routes
app.include_router(cryptos.router)
app.include_router(top.router)

@app.get("/")
def root():
    return {"message": "Crypto API is running"}