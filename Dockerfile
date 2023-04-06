# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install Git
RUN apt-get update && apt-get install -y git

# Install curl and dnsutils packages
RUN apt-get update && apt-get install -y curl dnsutils

# Install Ping
RUN apt-get update && apt-get install -y iputils-ping && \
    useradd -ms /bin/bash appuser && \
    chown -R appuser /app

USER appuser

# Clone the GitHub repository
RUN git clone https://github.com/TheWation/CiCeSandbox

# Set the working directory to the root directory of the cloned repository
WORKDIR /app/CiCeSandbox

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set the PATH environment variable to include the directory containing the uvicorn executable
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Expose the port that the application will run on
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]