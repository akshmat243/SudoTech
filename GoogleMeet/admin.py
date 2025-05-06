from django.contrib import admin
from .models import GoogleMeet

@admin.register(GoogleMeet)
class GoogleMeetAdmin(admin.ModelAdmin):
    list_display = ('title', 'meeting_datetime', 'duration_minutes', 'status')
    list_filter = ('status', 'meeting_datetime')
    search_fields = ('title', 'url')
