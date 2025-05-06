from django.contrib import admin
from .models import Spreadsheet

@admin.register(Spreadsheet)
class SpreadsheetAdmin(admin.ModelAdmin):
    list_display = ('file_or_folder_name', 'related')
    search_fields = ('file_or_folder_name', 'related')
    list_filter = ('related',)
