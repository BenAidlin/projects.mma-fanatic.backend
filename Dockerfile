# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Install Gunicorn
RUN pip install gunicorn

ENV PYTHONPATH="${PYTHONPATH}:/app"
# Expose the port the app runs on
EXPOSE 8000


