import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import time

# 1. Khai báo chuỗi kết nối đến két sắt PostgreSQL
DB_URL = "postgresql://vdt_admin:vdt_password123@db:5432/crypto_db"

# 2. Tạo "động cơ" kết nối
engine = create_engine(DB_URL)


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(
        {
            "timestamp": [datetime.now()],
            "bitcoin_usd": [data["bitcoin"]["usd"]],
            "ethereum_usd": [data["ethereum"]["usd"]],
        }
    )
    return df


def save_to_postgres(df):
    # Pandas tự động dịch Dataframe thành lệnh SQL và nhét vào PostgreSQL
    df.to_sql("crypto_prices", engine, if_exists="append", index=False)
    print(f"[{datetime.now()}] Đã hút dữ liệu và lưu vào PostgreSQL thành công!")


if __name__ == "__main__":
    print("Bắt đầu tiến trình ETL hút dữ liệu Crypto tự động...")
    while True:
        try:
            df = fetch_crypto_data()
            save_to_postgres(df)
        except Exception as e:
            print(f"Lỗi hệ thống: {e}")

        # Tự động nghỉ 60 giây rồi hút tiếp
        time.sleep(60)
