FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Remove or comment out the collectstatic command
# CMD ["python", "manage.py", "collectstatic", "--noinput"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo_api.wsgi:application"]
