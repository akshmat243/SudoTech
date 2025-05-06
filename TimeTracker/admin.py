from django.contrib import admin
from .models import Timetracker

@admin.register(Timetracker)
class TimetrackerAdmin(admin.ModelAdmin):
    list_display = ('description', 'project', 'task', 'workspace', 'start_time', 'end_time', 'total_time')
    search_fields = ('description', 'project', 'task', 'workspace')
