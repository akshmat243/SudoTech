from django.contrib import admin
from .models import GoogleSheet

@admin.register(GoogleSheet)
class GoogleSheetAdmin(admin.ModelAdmin):
    list_display = ('sheet_name', 'created_date', 'updated_on')
    search_fields = ('sheet_name',)
    list_filter = ('created_date', 'updated_on')
