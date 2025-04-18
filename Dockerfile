# Use official Python image
FROM python:3.12.9-slim

# Set work directory
WORKDIR /app

# Install system packages needed for mysqlclient and other compiled dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libmysqlclient-dev \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Set environment variables (optional)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start app
CMD ["flask", "run"]
