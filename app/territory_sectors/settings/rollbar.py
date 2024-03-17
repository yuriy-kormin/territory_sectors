import os
from .base import DEBUG, BASE_DIR


ROLLBAR = {
    'access_token': os.getenv('ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}
