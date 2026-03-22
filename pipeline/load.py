 
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="crypto_db",
        user="postgres",
        password="123456"
    )

def create_table(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS crypto_prices (
        id TEXT PRIMARY KEY,
        symbol TEXT,
        name TEXT,
        price FLOAT,
        market_cap FLOAT,
        volume FLOAT
    )
    """)

def load_data():
    try:
        print("Reading data...")
        df = pd.read_csv("C:\Projects\crypto-data-pipeline/data/crypto_clean.csv")

        conn = get_connection()
        cur = conn.cursor()

        print("Creating table if not exists...")
        create_table(cur)

        print("Inserting data...")

        values = [
            (row.id, row.symbol, row.name, row.price, row.market_cap, row.volume)
            for row in df.itertuples()
        ]

        query = """
        INSERT INTO crypto_prices (id, symbol, name, price, market_cap, volume)
        VALUES %s
        ON CONFLICT (id) DO UPDATE SET
            price = EXCLUDED.price,
            market_cap = EXCLUDED.market_cap,
            volume = EXCLUDED.volume;
        """

        execute_values(cur, query, values)

        conn.commit()

        print(f"{len(values)} rows loaded successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    load_data()
 