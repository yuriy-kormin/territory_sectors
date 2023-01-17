from django.contrib import admin
# from .models import House
# # Register your models here.
#
# admin.site.register(House)
from django.contrib.gis.admin import GISModelAdmin
from .models import House


@admin.register(House)
class HouseAdmin(GISModelAdmin):
    list_display = ('address', 'gps_point')
