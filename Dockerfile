# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install Git
RUN apt-get update && apt-get install -y git

# Clone the GitHub repository
RUN git clone https://github.com/TheWation/CiCeSandbox

# Set the working directory to the cloned repository
WORKDIR /app/CiCeSandbox

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will run on
EXPOSE 8000

# Start the application
CMD ["python", "app.py"]