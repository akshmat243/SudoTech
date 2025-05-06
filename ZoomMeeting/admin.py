from django.contrib import admin
from .models import ZoomMeeting

@admin.register(ZoomMeeting)
class ZoomMeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'duration', 'status')
    list_filter = ('status', 'date')
    search_fields = ('title', 'name', 'url')
