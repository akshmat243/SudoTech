from django.contrib import admin
from .models import ZohoMeeting

@admin.register(ZohoMeeting)
class ZohoMeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'duration', 'status')
    list_filter = ('status', 'date')
    search_fields = ('title', 'invites', 'url')
