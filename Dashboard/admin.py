from django.contrib import admin
from .models import Dashboard

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'is_active', 'created_at')
    list_filter = ('module', 'is_active')
    search_fields = ('name',)
