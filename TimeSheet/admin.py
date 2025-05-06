from django.contrib import admin
from .models import Timesheet

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'project', 'task', 'types', 'date', 'hours', 'minutes', 'total_time')
    search_fields = ('name', 'project', 'task', 'types')
    list_filter = ('date', 'project', 'types')
