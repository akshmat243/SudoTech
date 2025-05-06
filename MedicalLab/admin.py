from django.contrib import admin
from .models import (
    LabPatient, PatientCard, LabAppointment, LabTestRequest,
    LabInventory, LabBilling, LabResult, PatientHistory, LabSystemSetting
)

@admin.register(LabPatient)
class LabPatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'gender', 'phone']
    search_fields = ['name', 'phone']


@admin.register(PatientCard)
class PatientCardAdmin(admin.ModelAdmin):
    list_display = ['patient', 'card_number', 'issued_date']
    search_fields = ['card_number', 'patient__name']


@admin.register(LabAppointment)
class LabAppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'appointment_date', 'appointment_time']
    list_filter = ['appointment_date']
    search_fields = ['patient__name']


@admin.register(LabTestRequest)
class LabTestRequestAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'appointment', 'status', 'requested_date']
    list_filter = ['status']
    search_fields = ['test_name', 'appointment__patient__name']


@admin.register(LabInventory)
class LabInventoryAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'quantity', 'unit', 'last_updated']
    search_fields = ['item_name']


@admin.register(LabBilling)
class LabBillingAdmin(admin.ModelAdmin):
    list_display = ['patient', 'bill_date', 'total_amount', 'paid']
    list_filter = ['paid']
    search_fields = ['patient__name']


@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ['lab_test', 'reported_date']
    search_fields = ['lab_test__test_name']


@admin.register(PatientHistory)
class PatientHistoryAdmin(admin.ModelAdmin):
    list_display = ['patient', 'condition', 'record_date']
    search_fields = ['patient__name', 'condition']


@admin.register(LabSystemSetting)
class LabSystemSettingAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ['key']
