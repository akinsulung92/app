# Base image
FROM ubuntu:18.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget curl build-essential git vim && \
    pip3 install Flask

# Copy the app.py file into the container
COPY app.py /app/

# Set the working directory
WORKDIR /app

# Expose the port that the Flask app will run on
EXPOSE 5000

# Start the Flask app when the container starts
CMD ["python3", "app.py"]
