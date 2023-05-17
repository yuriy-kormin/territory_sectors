import os

from django.conf import settings
from django.http import HttpRequest


def google_analytics(request: HttpRequest):
    return {
        'GA_KEY': settings.GOOGLE_ANALYTICS_KEY,
    }


def mapbox(request: HttpRequest):
    return {
        'MAPBOX_API_KEY': os.environ.get('MAPBOX_API_KEY'),
    }
