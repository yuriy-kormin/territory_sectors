from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import House
from simple_history.admin import SimpleHistoryAdmin


# @admin.register(House, SimpleHistoryAdmin)
class HouseAdmin(GISModelAdmin, SimpleHistoryAdmin):
    list_display = ('address', 'gps_point')


admin.site.register(House, SimpleHistoryAdmin)
