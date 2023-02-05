from django.contrib import admin
from .models import Uuid
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(Uuid, SimpleHistoryAdmin)

