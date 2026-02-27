FROM python:3.9-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

COPY . .

RUN pip install streamlit pandas requests sqlalchemy psycopg2-binary

CMD ["streamlit", "run", "app.py"]