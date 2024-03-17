# flake8: noqa

import os
import dj_database_url
from .base import CERTBOT_DOMAINS

db_conf = {
    'username': os.environ.get("POSTGRES_USER", None),
    'password': os.environ.get("POSTGRES_PASSWORD", None),
    'db_name': os.environ.get("POSTGRES_DB", None),
    'db_port': os.environ.get("POSTGRES_PORT", 5432),
}
docker_db_host = os.environ.get("DOCKER_DB_HOST", 'localhost')
db_conf['hostname'] = docker_db_host \
    if docker_db_host else CERTBOT_DOMAINS.split(',')[0]

if all(db_conf.values()):
    database_url = f"postgis://{db_conf['username']}:{db_conf['password']}@" \
                   f"{db_conf['hostname']}:{db_conf['db_port']}/{db_conf['db_name']}"
else:
    database_url = 'spatialite:///db.sqlite3'
os.environ['DATABASE_URL'] = database_url

DATABASES = {
    'default': dj_database_url.config(
        # default='spatialite:///db.sqlite3',
        # conn_max_age=600,
    )
}
