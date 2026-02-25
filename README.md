# 🚀 Crypto ETL Pipeline & Dashboard
**A personal project for Viettel Digital Talent 2026 - Data Engineer Track**

## 📌 Project Overview
This project is an automated ETL (Extract, Transform, Load) pipeline that tracks real-time cryptocurrency prices. It demonstrates the ability to handle data flows from APIs to a local database and visualize it through a web dashboard.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas (using Vectorization for performance)
* **Database:** SQLite
* **Visualization:** Streamlit
* **API:** CoinGecko API

## ✨ Key Features
* **Extract:** Automatically fetch top 10 cryptocurrencies' prices (BTC, ETH, etc.) via Requests.
* **Transform:** Clean and format data using Pandas (handling Market Cap, Volume).
* **Load:** Store historical data into a structured SQLite database.
* **Visualize:** Interactive dashboard showing real-time price tables and Market Cap bar charts.

## ⚙️ How to Run
1. **Clone the repository:**
   git clone git@github.com:nguyenphucptitd24/vdt-crypto-etl.git
Install dependencies:
pip install requests pandas streamlit

Run the ingestion script (Collect data):
python ingest.py

Launch the Dashboard:
streamlit run app.py

👨‍💻 Author
Nguyen Phuc - 2nd year IT Student at PTIT (High-quality Program)
Expected Graduation: 2028
Target: Viettel Digital Talent 2026