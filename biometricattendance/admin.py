from django.contrib import admin
from .models import BiometricAttendance, BiometricDevice

@admin.register(BiometricDevice)
class BiometricDeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'location', 'serial_number')
    search_fields = ('device_name', 'serial_number')


@admin.register(BiometricAttendance)
class BiometricAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in', 'check_out', 'total_hours', 'status', 'device')
    list_filter = ('status', 'date', 'device')
    search_fields = ('employee__username', 'employee__email')
