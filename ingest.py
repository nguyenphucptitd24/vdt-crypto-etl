import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_crypto_data():
    api_key = os.getenv("CRYPTO_API_KEY")

    if not api_key:
        print("Lỗi: Không tìm thấy CRYPTO_API_KEY trong file .env hoặc hệ thống!")
        return None

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False,
    }

    headers = {"x-access-token": api_key, "accept": "application/json"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        print("Dữ liệu đã được tải thành công!")
        return data

    except requests.exceptions.RequestException as e:
        print(f"Đã xảy ra lỗi khi gọi API: {e}")
        return None


if __name__ == "__main__":
    data = get_crypto_data()
    if data:
        print(data[:1])
