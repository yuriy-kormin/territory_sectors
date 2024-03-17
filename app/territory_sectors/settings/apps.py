DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'bootstrap4',
    'simple_history',
    "qr_code",
    'graphene_django',
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
    'graphene_gis',
    'corsheaders',
    'dbbackup',
    'debug_toolbar',
]

PROJECT_APPS = [
    'territory_sectors',
    'territory_sectors.flat',
    'territory_sectors.house',
    'territory_sectors.sector',
    'territory_sectors.language',
    'territory_sectors.uuid_qr',
    "territory_sectors.issue",
    "territory_sectors.status",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
