from django.contrib import admin
from .models import CustomField

@admin.register(CustomField)
class CustomFieldAdmin(admin.ModelAdmin):
    list_display = ['name', 'field_type', 'module', 'rule']
    list_filter = ['field_type', 'module']
    search_fields = ['name', 'module']
