import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import time

# 1. Khai báo chìa khóa mở két sắt (Giống hệt bên ingest.py)
DB_URL = "postgresql://vdt_admin:vdt_password123@db:5432/crypto_db"
engine = create_engine(DB_URL)

st.set_page_config(page_title="VDT Crypto Dashboard", layout="wide")
st.title("📈 Biểu đồ Giá Crypto Trực Tuyến (PostgreSQL)")


# 2. Hàm chui xuống hầm lấy dữ liệu
def load_data():
    # Lấy 100 dòng dữ liệu mới nhất
    query = "SELECT * FROM crypto_prices ORDER BY timestamp DESC LIMIT 100"
    df = pd.read_sql(query, engine)
    return df


# Tạo một không gian trống để hình ảnh tự động làm mới
placeholder = st.empty()

# 3. Vòng lặp liên tục cập nhật giao diện
while True:
    try:
        df = load_data()

        # Nếu đã có dữ liệu thì vẽ biểu đồ
        if not df.empty:
            with placeholder.container():
                col1, col2 = st.columns(2)
                col1.metric("Giá Bitcoin (USD)", f"${df['bitcoin_usd'].iloc[0]:,.2f}")
                col2.metric("Giá Ethereum (USD)", f"${df['ethereum_usd'].iloc[0]:,.2f}")

                # Vẽ biểu đồ đường
                st.line_chart(
                    df.set_index("timestamp")[["bitcoin_usd", "ethereum_usd"]]
                )
        else:
            placeholder.warning("Két sắt đang trống. Đợi hệ thống hút dữ liệu...")

    except Exception as e:
        placeholder.error(f"Đang kết nối Database... Vui lòng đợi. Lỗi: {e}")

    time.sleep(5)  # Cứ 5 giây là tải lại giao diện 1 lần
