#!/bin/bash

#python manage.py initadmin
######################################
#### planning to write initadmin  ####
######################################


# Apply database migrations
echo "Apply database migrations"
python /app/manage.py migrate --noinput
#poetry run python manage.py createsuperuser --noinput
#collect static
python /app/manage.py collectstatic --noinput

# Start server
echo "Starting jango app"
cd /app/
gunicorn territory_sectors.wsgi:application --bind 0.0.0.0:8000
