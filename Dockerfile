FROM python:3.8-slim

# Set a directory for the app
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV VAR=DefaultValue

# Run app.py when the container launches
CMD ["python", "./app.py"]
