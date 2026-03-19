import json
import pandas as pd

# readin raw data
with open("C:\Projects\crypto-data-pipeline/data/crypto_raw.json") as f:
    data = json.load(f)

# transform into DataFrame
df = pd.DataFrame(data)

# select top coloumns
df = df[[
    "id",
    "symbol",
    "name",
    "current_price",
    "market_cap",
    "total_volume"
]]

# rename coloums
df.columns = [
    "id",
    "symbol",
    "name",
    "price",
    "market_cap",
    "volume"
]

# ??? ???????? ???????
df.to_csv("C:\Projects\crypto-data-pipeline/data/crypto_clean.csv", index=False)

print("Transformed data saved!")