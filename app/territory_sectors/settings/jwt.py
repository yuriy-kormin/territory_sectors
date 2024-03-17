from datetime import timedelta
from .base import DEBUG, ALLOWED_HOSTS
import os

GRAPHENE = {
    'SCHEMA': 'territory_sectors.schema.schema'
}


if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    # CORS_ALLOW_ALL_HEADERS = True
    # CORS_ALLOW_CREDENTIALS = True
    # CORS_ALLOW_METHODS = default_methods
    # CSRF_TRUSTED_ORIGINS = ['*']
    # CORS_ORIGIN_WHITELIST = ['http://localhost:3000']
    # CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']

else:
    # ALLOWED_HOSTS_ENV = os.getenv('CERTBOT_DOMAINS', '*')
    # if ALLOWED_HOSTS_ENV:
    #     ALLOWED_HOSTS = [
    #         host.strip() for host
    #         in ALLOWED_HOSTS_ENV.split(',')
    #     ]

    CORS_ALLOWED_ORIGINS = ALLOWED_HOSTS

TOKEN_EXPIRATION = os.getenv('TOKEN_EXPIRATION', 5 * 60)  # 5 minutes
REFRESH_EXPIRATION = os.getenv('REFRESH_EXPIRATION', 7 * 60 * 60 * 24)  # 7 days default

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": timedelta(seconds=int(TOKEN_EXPIRATION)),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(seconds=int(REFRESH_EXPIRATION)),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
}