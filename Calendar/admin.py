from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_time', 'end_time', 'location')
    search_fields = ('title', 'description', 'location')
    list_filter = ('event_type',)
    ordering = ('-start_time',)
