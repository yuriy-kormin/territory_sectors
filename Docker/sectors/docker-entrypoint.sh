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

echo "creating log dir if not exist"
mkdir -p /var/log/gunocorn

echo "Starting jango app"
gunicorn territory_sectors.wsgi:application --bind 0.0.0.0:8000 \
    --access-logfile /var/log/gunicorn/access.log \
    --error-logfile /var/log/gunicorn/error.log
