FROM python:3.10-slim

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

RUN apt-get update && apt-get install -y \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxi6 \
    libxtst6 \
    libgtk-3-0 \
    libdrm2 \
    libgbm1 \
    libasound2 \
    sqlite3 \
    libsqlite3-dev 

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install


COPY . .

ENV PYTHONPATH=/app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

