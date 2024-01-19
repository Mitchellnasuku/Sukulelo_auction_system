# Use an official Python runtime as a parent image
FROM python:3.9


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in docker_requirements.txt
#RUN pip install --no-cache-dir -r docker_requirements.txt
RUN pip install --no-cache-dir --prefer-binary -r docker_requirements.txt


# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run Django migrations and start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]








