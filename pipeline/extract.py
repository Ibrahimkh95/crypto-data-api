import requests
import json

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)

data = response.json()

with open("C:\Projects\crypto-data-pipeline/data/crypto_raw.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data saved successfully")