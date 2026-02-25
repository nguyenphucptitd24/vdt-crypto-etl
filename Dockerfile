From python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir requests pandas streamlit
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]