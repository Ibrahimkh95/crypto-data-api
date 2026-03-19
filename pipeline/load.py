import pandas as pd
import psycopg2

# read data
df = pd.read_csv("../data/crypto_clean.csv")

# connect wit Postres
conn = psycopg2.connect(
    host="localhost",
    database="crypto_db",
    user="postgres",
    password="password"
)

cur = conn.cursor()

# CREATE TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS crypto_prices (
    id TEXT,
    symbol TEXT,
    name TEXT,
    price FLOAT,
    market_cap FLOAT,
    volume FLOAT
)
""")

# INSERT INTO crypto_prices
for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO crypto_prices (id, symbol, name, price, market_cap, volume)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("Data loaded into PostgreSQL!")