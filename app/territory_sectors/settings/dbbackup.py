# flake8: noqa
from .base import BASE_DIR

BACKUP_SUBDIR = 'dbbackup'

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': f'{BASE_DIR.parent}/{BACKUP_SUBDIR}/'}
