#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# Start server
echo "Starting jango app"
gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000