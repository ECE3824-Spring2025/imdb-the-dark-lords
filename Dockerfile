# Use Python 3.12 with slim OS layer
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    libssl-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip wheel
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
