#!/bin/sh

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files (optional)
# python manage.py collectstatic --noinput

# Start the Gunicorn server with the specified configuration
exec gunicorn todo_api.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120
