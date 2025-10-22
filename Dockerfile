FROM efreidevopschina.azurecr.io/cache/library/python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app/
COPY tests/ ./tests/

CMD ["python", "app/app.py"]