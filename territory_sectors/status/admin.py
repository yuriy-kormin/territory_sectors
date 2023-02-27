from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Status

admin.site.register(Status, SimpleHistoryAdmin)
