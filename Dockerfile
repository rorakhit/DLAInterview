# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 8080/tcp

# Set the working directory in the container
COPY . /app
COPY templates /app/
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY project.py .

# Specify the command to run on container start
CMD [ "python", "/app/project.py" ]