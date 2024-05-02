FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

RUN apt-get update && apt-get install -y postgresql-client

# Set environment variables for PostgreSQL connection
ENV POSTGRES_DB=shopclassy
ENV POSTGRES_USER=shopclassy
ENV POSTGRES_PASSWORD=shopclassy
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432

# Run the Python application
CMD ["python", "main.py"]
