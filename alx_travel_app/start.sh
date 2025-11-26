#!/bin/bash
set -e

# Create Django project if missing (inside /app folder)
if [ ! -f "/app/manage.py" ]; then
    echo "Creating Django project..."
    django-admin startproject alx_travel_app /app
fi

# Create listings app if missing
if [ ! -d "/app/listings" ]; then
    echo "Creating listings app..."
    python /app/manage.py startapp listings
fi

echo "Applying migrations..."
python /app/manage.py migrate

echo "Starting Django server..."
python /app/manage.py runserver 0.0.0.0:8000
