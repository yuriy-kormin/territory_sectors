from .base import DEBUG
# from .apps import INSTALLED_APPS


if DEBUG:
    # INSTALLED_APPS.append("")
    INTERNAL_IPS = ('127.0.0.1',)