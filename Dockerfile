# This starts us with a clean Linux environment with Python 3.9 installed.
FROM python:3.9-slim

# Set the working directory inside the container
# All subsequent commands will run from /app
WORKDIR /app

# Set the PYTHONPATH environment variable inside the container
ENV PYTHONPATH=/app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy our application's source code into the container
COPY ./src .

# Copy the data folder into the container
COPY ./data ./data

# Run the training script to generate the .pkl model files inside the container
RUN python book_service/train.py

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run when the container starts
CMD ["uvicorn", "book_service.api.main:app", "--host", "0.0.0.0", "--port", "8000"]