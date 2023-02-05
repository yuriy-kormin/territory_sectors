from django.contrib import admin
from .models import Sector
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.


admin.site.register(Sector, SimpleHistoryAdmin)