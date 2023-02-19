from django.contrib import admin
from .models import Issue, Comment
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(Issue, Comment, SimpleHistoryAdmin)
