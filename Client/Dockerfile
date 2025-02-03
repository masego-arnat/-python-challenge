# # Use an official Python runtime as the base image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

 
# # Command to run the script
# CMD ["python", "train.py"] 

FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the script
CMD ["python", "train.py"]