from django.contrib import admin
from .models import FormEntry


@admin.register(FormEntry)
class FormEntryAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'response', 'submitted_at')
    search_fields = ('name', 'response')
    list_filter = ('submitted_at',)
    ordering = ('no',)
