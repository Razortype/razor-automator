# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Copy the contents of the pattern_macro directory into the container at /app
COPY ./pattern_macro /app/pattern_macro

# Install required dependencies
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

# Install project dependencies (if you have a requirements.txt file)
COPY ./pattern_macro/requirements.txt /app/pattern_macro/requirements.txt
RUN pip3 install -r /app/pattern_macro/requirements.txt

# Set the entry point to run the application
CMD ["python3", "/app/pattern_macro/app.py"]
