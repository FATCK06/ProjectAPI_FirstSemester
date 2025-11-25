FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential libgdal-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
EXPOSE 8501
CMD ["python", "colab_app.py"]