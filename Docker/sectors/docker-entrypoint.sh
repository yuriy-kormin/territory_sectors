#!/bin/bash

cd /app/
echo "Apply database migrations"
python manage.py migrate --noinput

echo "collect static"
python manage.py collectstatic --noinput

echo "createsuperuser"
python manage.py createsuperuser --noinput \
      --username $DJANGO_SUPERUSER_USERNAME \
      --email $DJANGO_SUPERUSER_EMAIL


echo "run crontab"
service cron start

echo "Starting jango app"

gunicorn territory_sectors.wsgi:application --bind 0.0.0.0:8000
