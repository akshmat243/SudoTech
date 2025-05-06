from django.contrib import admin
from .models import GoToMeeting

@admin.register(GoToMeeting)
class GoToMeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'meeting_datetime', 'duration_minutes', 'status')
    list_filter = ('status', 'meeting_datetime')
    search_fields = ('title', 'url')
