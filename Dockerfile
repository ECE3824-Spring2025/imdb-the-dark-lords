# Dockerfile  (only the two lines changed)
FROM python:3.12-slim           # ← switch to 3.12

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        libffi-dev libssl-dev libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
