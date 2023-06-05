# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

ENV MySQL_db_host="xxx"
ENV MySQL_db_user="xxx" 
ENV MySQL_db_pass="xxx"
ENV MySQL_db_name="xxx"

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT 8080

# Run main.py when the container launches
CMD exec gunicorn --bind :$PORT main:app