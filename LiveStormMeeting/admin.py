from django.contrib import admin
from .models import LivestormMeeting

@admin.register(LivestormMeeting)
class LivestormMeetingAdmin(admin.ModelAdmin):
    list_display = ('no', 'title', 'owner_name', 'event', 'scheduling_status')
    search_fields = ('title', 'owner_name', 'event')
