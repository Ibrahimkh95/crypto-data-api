from ..db.connection import get_connection
from fastapi import HTTPException
from api.core.logger import logger
 
 
logger.info("Executing query: get_cryptos")
 
def get_cryptos(limit=10, offset=0, min_price=None, sort_by="market_cap", order="desc"):
    conn = get_connection()
    cur = conn.cursor()

    # protection
    allowed_sort_fields = ["price", "market_cap", "volume"]
    if sort_by not in allowed_sort_fields:
        sort_by = "market_cap"

    order = order.lower()
    if order not in ["asc", "desc"]:
        order = "desc"

    # count total
    count_query = """
        SELECT COUNT(*) FROM crypto_prices
        WHERE (%s IS NULL OR price >= %s)
    """
    cur.execute(count_query, (min_price, min_price))
    total = cur.fetchone()[0]

    # main query
    query = f"""
        SELECT * FROM crypto_prices
        WHERE (%s IS NULL OR price >= %s)
        ORDER BY {sort_by} {order}
        LIMIT %s OFFSET %s
    """

    cur.execute(query, (min_price, min_price, limit, offset))
    data = cur.fetchall()

    cur.close()
    conn.close()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "data": data
    }



def get_crypto(symbol: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM crypto_prices
        WHERE LOWER(symbol) = LOWER(%s)
        """,
        (symbol,)
    )

    data = cur.fetchone()

    cur.close()
    conn.close()

    return data
	
def search_cryptos(query: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM crypto_prices
        WHERE LOWER(name) LIKE LOWER(%s) OR LOWER(symbol) LIKE LOWER(%s)
        """,
        (f"%{query}%", f"%{query}%")
    )
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_cryptos_stats():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT
            MAX(price) as max_price,
            MIN(price) as min_price,
            AVG(price) as avg_price,
            SUM(market_cap) as total_market_cap
        FROM crypto_prices
        """
    )
    stats = cur.fetchone()
    cur.close()
    conn.close()
    return stats

def get_top_cryptos(limit=5):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT name, price, market_cap
        FROM crypto_prices
        ORDER BY market_cap DESC
        LIMIT %s
        """,
        (limit,)
    )

    data = cur.fetchall()

    cur.close()
    conn.close()

    return data