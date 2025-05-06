from django.contrib import admin
from .models import ActivityLog

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'module', 'sub_module', 'staff', 'created_at')
    list_filter = ('activity_type', 'module', 'sub_module', 'created_at')
    search_fields = ('description', 'staff__username', 'module', 'sub_module')
