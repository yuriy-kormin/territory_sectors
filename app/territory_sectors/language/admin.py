from django.contrib import admin
from .models import Language
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(Language, SimpleHistoryAdmin)
