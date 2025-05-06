from django.contrib import admin
from .models import Machine, RepairRequest, RepairHistory, ServiceAgreement

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'name', 'manufacturer', 'purchase_date', 'location']
    search_fields = ['serial_number', 'name', 'location']

@admin.register(ServiceAgreement)
class ServiceAgreementAdmin(admin.ModelAdmin):
    list_display = ['machine', 'provider', 'start_date', 'end_date']
    search_fields = ['machine__name', 'provider']

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ['machine', 'issue_description', 'request_date', 'status']
    list_filter = ['status']
    search_fields = ['machine__serial_number', 'issue_description']

@admin.register(RepairHistory)
class RepairHistoryAdmin(admin.ModelAdmin):
    list_display = ['machine', 'repair_date', 'cost', 'repaired_by']
    list_filter = ['repair_date']
    search_fields = ['machine__serial_number', 'repaired_by']
