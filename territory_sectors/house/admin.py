from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import House



@admin.register(House)
class HouseAdmin(GISModelAdmin):
    list_display = ('address', 'gps_point')
