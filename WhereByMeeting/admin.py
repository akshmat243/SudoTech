from django.contrib import admin
from .models import WhereByMeeting

@admin.register(WhereByMeeting)
class WhereByMeetingAdmin(admin.ModelAdmin):
    list_display = ('room_name_prefix', 'date', 'start_time', 'end_time', 'room_mode', 'status')
    search_fields = ('room_name_prefix', 'invites')
    list_filter = ('room_mode', 'status', 'date')
