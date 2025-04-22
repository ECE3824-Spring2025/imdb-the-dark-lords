# ---- Dockerfile ----
FROM python:3.12-slim        # 3.12 has binary wheels; keep 3.13 only if you must

ENV DEBIAN_FRONTEND=noninteractive

# Everything the C extensions need (+ pkg-config so mysqlclient’s setup.py can find them)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential gcc pkg-config \
        libmariadb-dev libmariadb-dev-compat \
        libssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
