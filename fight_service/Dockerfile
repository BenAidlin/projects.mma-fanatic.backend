# Use the official Python image as a base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 
# Set the working directory in the container
WORKDIR /app


# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn separately (not in requirements.txt for flexibility)
RUN pip install gunicorn[uvicorn]

# Copy the application code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# Command to run Gunicorn with Uvicorn workers
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "app.main:app"]
