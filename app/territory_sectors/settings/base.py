# flake8: noqa

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = os.path.join(BASE_DIR.parent.parent, '.env-compose')
load_dotenv(env_path)

SECRET_KEY = os.getenv('DJANGO_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'True'

CERTBOT_DOMAINS = os.getenv('CERTBOT_DOMAINS', '')

ALLOWED_HOSTS = [domain for domain in CERTBOT_DOMAINS.split(',')] \
    if CERTBOT_DOMAINS else ['*']

ROOT_URLCONF = 'territory_sectors.urls'
# LOGIN_REDIRECT_URL = '/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'territory_sectors.context_processors.google_analytics',
                'territory_sectors.context_processors.mapbox',
            ],
        },
    },
]

WSGI_APPLICATION = 'territory_sectors.wsgi.application'

GOOGLE_ANALYTICS_KEY = os.environ.get("GOOGLE_ANALYTICS_KEY")

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LANGUAGE_CODE = 'ru-ru'
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "territory_sectors", "locale"),
)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Set the maximum file upload size to 20 megabytes
FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520

# Set the maximum request body size to 20 megabytes
DATA_UPLOAD_MAX_MEMORY_SIZE = 20971520
