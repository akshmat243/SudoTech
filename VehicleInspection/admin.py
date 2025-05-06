from django.contrib import admin
from .models import (
    Vehicle, InspectionRequest, InspectionList,
    InspectionReminder, InspectionSchedule,
    InspectionHistory, ComplianceRegulation
)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['registration_number', 'model', 'manufacturer', 'year', 'owner_name']
    search_fields = ['registration_number', 'owner_name']

@admin.register(InspectionRequest)
class InspectionRequestAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'reason', 'request_date', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['vehicle__registration_number']

@admin.register(InspectionList)
class InspectionListAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(InspectionSchedule)
class InspectionScheduleAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'inspection_date', 'assigned_inspector']
    list_filter = ['inspection_date']
    search_fields = ['vehicle__registration_number', 'assigned_inspector']

@admin.register(InspectionReminder)
class InspectionReminderAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'reminder_date']
    search_fields = ['vehicle__registration_number']

@admin.register(InspectionHistory)
class InspectionHistoryAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'inspection_date', 'passed', 'inspector_name']
    list_filter = ['passed']
    search_fields = ['vehicle__registration_number', 'inspector_name']

@admin.register(ComplianceRegulation)
class ComplianceRegulationAdmin(admin.ModelAdmin):
    list_display = ['title', 'effective_date']
    search_fields = ['title']
