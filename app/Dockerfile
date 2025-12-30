#This give us an operating system + Python without building them ourselves.
FROM python:3.13-slim
#Set the working directory INSIDE the container
WORKDIR /app
#Copy only requirements.txt from local machine.
#into the container's /app directory
#This is done so Docker can cache dependency installation.
COPY requirements.txt .
#Install Python dependencies INSIDE the container.
RUN pip install --no-cache-dir -r requirements.txt
#Copy the rest of your application files into the container.
COPY . .

# Define the command that runs WHEN the container starts.
# This tells Docker how to start your application.
# Uvicorn runs the FastAPI app called "app" inside main.py
# 0.0.0.0 allows traffic from outside the container
# Port 8000 is where the service listens
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]