import requests
import pandas as pd
import sqlite3

# Bước 1: Lấy dữ liệu từ API CoinGecko
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False,
}

response = requests.get(url, params=params)
data = response.json()

# Bước 2: Làm sạch dữ liệu và chọn các cột cần thiết
df = pd.DataFrame(data)
df_clean = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume"]]
print("Dữ liệu sau khi làm sạch:")
print(df_clean)

# Lưu dữ liệu vào cơ sở dữ liệu SQLite
conn = sqlite3.connect("crypto_data.db")
df_clean.to_sql("crypto_markets", conn, if_exists="replace", index=False)
conn.close()
print("Dữ liệu đã được lưu vào cơ sở dữ liệu SQLite.")
