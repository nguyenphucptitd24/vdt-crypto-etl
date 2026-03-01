# 🚀 Real-time Crypto ETL Pipeline & Dashboard

A complete and automated Data Pipeline system that extracts live cryptocurrency prices, transforms the data, ensures persistent storage, and visualizes the trends through an interactive dashboard. The entire project is containerized using Docker, adhering to a Microservices architecture.

## 🛠️ Tech Stack & Architecture

The system is designed with independent services communicating within a containerized network:

- **Core Language:** Python 3
- **Extract & Transform (ETL):** `pandas` and `requests` (Interacting with CoinGecko REST API).
- **Load (Database):** PostgreSQL (Configured with Docker Volumes to ensure data persistence).
- **Visualization (BI/Dashboard):** Streamlit.
- **Deployment & Infrastructure:** Docker & Docker Compose.

## ⚙️ How to Run (Local Environment)

Since the entire application is containerized, you do not need to manually install Python dependencies or configure a local database server. Ensure you have **Docker** and **Docker Compose** installed on your machine.

1. **Clone this repository:**
   git clone https://github.com/nguyenphucptitd24/vdt-crypto-etl.git
   cd vdt-crypto-etl

2. **Build and spin up the microservices:**

docker-compose up -d --build

3. **Access the application:**

- Open your web browser and navigate to the Streamlit Dashboard: `http://localhost:8501`
- The background worker will continuously fetch and update the live crypto data into the database.

4. **Tear down the system:**

docker-compose down

## 📈 Future Scope & Roadmap

This project currently serves as an MVP (Minimum Viable Product) to demonstrate a functional data engineering pipeline. To meet Enterprise-level standards, the following architectural upgrades are planned:

- **Workflow Orchestration:** Integrate **Apache Airflow** to replace background scripts, enabling robust DAG scheduling, failure retries, and automated alerting.
- **Real-time Streaming:** Introduce **Apache Kafka** as a Message Broker to decouple data ingestion and processing, handling high-throughput streams efficiently.
- **AI & Sentiment Analysis:** Utilize a local LLM (e.g., Ollama) to scrape and summarize market news, combining sentiment scores with price data for predictive analytics.
- **Cloud Migration:** Deploy the infrastructure to AWS (EC2, RDS) or GCP for High Availability (HA) and better scalability.

## 👨‍💻 Author

**Nguyen Hong Phuc**
