#   Crypto Data API

A production-style FastAPI project that provides cryptocurrency data through a RESTful API.  
The project simulates a real-world data engineering workflow with database integration, filtering, pagination, and structured responses.

---

##   Features

- FastAPI-based REST API
- PostgreSQL database integration
- Pagination (limit & offset)
- Filtering (min_price)
- Sorting (price, market_cap, volume)
- Structured JSON responses (metadata included)
- Logging system for monitoring
- Health check endpoint

---

##   Tech Stack

- Python
- FastAPI
- PostgreSQL
- Git

---

##   API Endpoints

### Get all cryptos
GET /api/v1/cryptos?limit=10&offset=0

### Filter + Sort
GET /api/v1/cryptos?min_price=1000&sort_by=price&order=asc

### Get by symbol
GET /api/v1/cryptos/BTC

### Health check
GET /api/v1/health

---

##   Response Example

```json
{
  "total": 100,
  "limit": 10,
  "offset": 0,
  "data": [...]
<<<<<<< HEAD
}
{
  "max_price": 68817,
  "min_price": 0.091549,
  "avg_price": 7162.257828100001,
  "total_market_cap": 2171923413716
}
[
  {
    "id": "bitcoin",
    "symbol": "btc",
    "name": "Bitcoin",
    "price": 68817,
    "market_cap": 1376087523900,
    "volume": 28382152890
  }
]
=======
}
>>>>>>> df67633 (Initial commit - Crypto Data API)
