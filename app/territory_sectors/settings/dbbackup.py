from .base import BASE_DIR

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': f'{BASE_DIR.parent}/dbbackup/'}
