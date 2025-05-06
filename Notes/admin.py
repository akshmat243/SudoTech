from django.contrib import admin
from .models import Notebook

@admin.register(Notebook)
class OneNoteNotebookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)