import streamlit as st
import pandas as pd
import sqlite3

# 1. cấu hình trang web
st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("VDT Crypto Price Tracker")
st.markdown("Dashboard hiển thị giá tiền điện tử trực tiếp từ Database SQLite.")


# 2. Kết nối đến cơ sở dữ liệu SQLite và lấy dữ liệu
@st.cache_data
def load_data():
    conn = sqlite3.connect("crypto_data.db")
    query = "SELECT * FROM crypto_markets"
    df = pd.read_sql_query(query, conn)
    return df


# Lấy dữ liệu ra biến df
df = load_data()

# 3. Hiển trị bảng dữ liệu trên web
st.subheader("Dữ liệu giá tiền điện tử")
st.dataframe(df)

# 4. Trích xuất và vẽ biểu đồ
st.subheader("📈 Top 10 Đồng Coin có Vốn Hóa (Market Cap) lớn nhất")
top_10_df = df.sort_values(by="market_cap", ascending=False).head(10)
display_df = top_10_df.rename(columns={"symbol": "SYMBOL", "market_cap": "MARKET_CAP"})
st.bar_chart(data=display_df, x="SYMBOL", y="MARKET_CAP")
