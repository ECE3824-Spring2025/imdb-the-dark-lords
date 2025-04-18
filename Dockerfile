# Use a lightweight Python base image
FROM python:3.13.1-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . /app

EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "app.py"]
