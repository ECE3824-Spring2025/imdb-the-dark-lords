# --- Dockerfile (unix line‑endings) -----------------
FROM python:3.12-slim       

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# OS‑level build deps (no editors, no docs, no cache)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential gcc pkg-config \
        libssl-dev libffi-dev \
        default-libmysqlclient-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
