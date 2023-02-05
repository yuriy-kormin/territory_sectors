from django.contrib import admin
from .models import Flat
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Flat,SimpleHistoryAdmin)