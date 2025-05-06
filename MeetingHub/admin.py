from django.contrib import admin
from .models import MeetingType, Meeting, MeetingMinutes, MeetingReport


@admin.register(MeetingType)
class MeetingTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('subject', 'start_time', 'end_time', 'meeting_type', 'location')
    search_fields = ('subject', 'location')
    list_filter = ('meeting_type', 'start_time')


@admin.register(MeetingMinutes)
class MeetingMinutesAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'created_at')
    search_fields = ('meeting__subject',)


@admin.register(MeetingReport)
class MeetingReportAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'created_at', 'report_file')
    search_fields = ('meeting__subject',)
