# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /task

# Copy the requirements file into the container at /app
COPY requirements.txt /task/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /task/

# Expose port 8085
EXPOSE 8085

# Start the Django development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8085"]
