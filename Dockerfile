# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for PostgreSQL
ENV POSTGRES_URL=postgres://suraj:b88jwwC8aulZmvgoRHdf9RWB8YvJkpcf@dpg-chlgi9m4dadfmsmdcbo0-a.oregon-postgres.render.com/suraj_n9u9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Install application dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Expose the port your Django app is running on (change this if necessary)
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
