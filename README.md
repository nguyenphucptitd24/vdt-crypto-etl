# 🪙 Real-time Crypto ETL Pipeline & Dashboard

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

## 📖 Table of Contents

- [About The Project](#-about-the-project)
- [Architecture](#-architecture)
- [Built With](#-built-with)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Run](#installation--run)
- [Usage](#-usage)
- [Future Scope](#-future-scope)
- [Contact](#-contact)

## 🚀 About The Project

This project is a containerized microservices application designed to track live cryptocurrency prices. It continuously extracts data from the CoinGecko API, processes it, and loads it into a relational database. A real-time web dashboard is then used to visualize the price fluctuations.

This pipeline demonstrates fundamental **Data Engineering** concepts, including data extraction, database management, and containerized deployment using Docker.

## 🏗 Architecture

The system is built on a microservices architecture with three main components:

1. **ETL Worker:** A Python script running in the background, continuously fetching data.
2. **Database:** A PostgreSQL instance storing the historical and real-time pricing data safely via Docker Volumes.
3. **Dashboard:** A Streamlit UI that queries the database and displays interactive charts.

```text
[CoinGecko API] ---> (Extract/Transform) ---> [Python ETL Worker]
                                                      |
                                                   (Load)
                                                      |
                                                      v
[Streamlit UI]  <--- (Query/Visualize) ------ [PostgreSQL DB]
```

## 🛠 Built With

- **Language:** Python 3
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **Frontend/UI:** Streamlit
- **Data Source:** CoinGecko Free API

## ⚙️ Getting Started

### Prerequisites

Make sure you have the following installed on your local machine:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Installation & Run

1. Clone the repository:

```bash
git clone [https://github.com/nguyenphucptitd24/vdt-crypto-etl.git](https://github.com/nguyenphucptitd24/vdt-crypto-etl.git)
cd vdt-crypto-etl
```

2. Build and start the containers using Docker Compose:

```bash
docker-compose up -d --build
```

3. Verify that all 3 containers (`etl-worker`, `postgres-db`, `streamlit-ui`) are running successfully:

```bash
docker ps
```

## 📊 Usage

Once the containers are up and running:

- The **ETL Worker** will automatically start fetching and inserting data into the database.
- Open your web browser and navigate to `http://localhost:8501` to view the **Streamlit Dashboard**.
- To stop the application and remove containers, simply run:

```bash
docker-compose down
```

## 🔭 Future Scope

- **Message Broker:** Integrate **Apache Kafka** to decouple the data extraction from the database loading process, enabling better scalability.
- **Cloud Deployment:** Deploy the Docker containers to **AWS EC2** or a VPS for a 24/7 production environment.
- **Workflow Orchestration:** Implement **Apache Airflow** to schedule and monitor the ETL jobs.

## 📬 Contact

**Nguyen Hong Phuc** - [LinkedIn Profile](https://www.linkedin.com/in/thay-bang-link-cua-ban)
Project Link: [https://github.com/nguyenphucptitd24/vdt-crypto-etl](https://github.com/nguyenphucptitd24/vdt-crypto-etl)
