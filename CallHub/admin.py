from django.contrib import admin
from .models import CallList, CallHistory, Report, SystemSetup

@admin.register(CallList)
class CallListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')
    search_fields = ('name',)
    list_filter = ('created_on',)


@admin.register(CallHistory)
class CallHistoryAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'phone_number', 'call_time', 'duration', 'status')
    list_filter = ('status', 'call_time')
    search_fields = ('contact_name', 'phone_number')
    date_hierarchy = 'call_time'


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('call_list', 'generated_on', 'total_calls', 'successful_calls', 'failed_calls')
    list_filter = ('generated_on',)
    search_fields = ('call_list__name',)
    date_hierarchy = 'generated_on'


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ('setting_name', 'setting_value')
    search_fields = ('setting_name',)
