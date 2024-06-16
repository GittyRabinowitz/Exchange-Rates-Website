# backend/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container for the backend
WORKDIR /app

# Install CA certificates and any necessary dependencies
RUN apt-get update && apt-get install -y ca-certificates

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the backend code into the container
COPY . .

# Set environment variable
ENV EXCHANGE_RATE_API_KEY=a1304752dc74c2929fd62678

# Expose the port that your FastAPI server runs on
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
