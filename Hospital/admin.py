from django.contrib import admin
from .models import (
    Doctor, Patient, Appointment, Medicine, Bed, MedicalRecord,
    EmergencyService, LabTest, Surgery, AmbulanceService,
    Outpatient, Visitor, HospitalSystemSetup
)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'email']
    search_fields = ['name', 'specialization']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'phone']
    search_fields = ['name', 'phone']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time']
    list_filter = ['date']
    search_fields = ['patient__name', 'doctor__name']


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock']
    search_fields = ['name']


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['ward', 'bed_number', 'is_occupied']
    list_filter = ['ward', 'is_occupied']


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'record_date']
    list_filter = ['record_date']
    search_fields = ['patient__name']


@admin.register(EmergencyService)
class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ['description', 'contact_number']


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ['test_name', 'patient', 'test_date']
    search_fields = ['test_name', 'patient__name']


@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    list_display = ['surgery_type', 'patient', 'surgery_date']
    list_filter = ['surgery_date']


@admin.register(AmbulanceService)
class AmbulanceServiceAdmin(admin.ModelAdmin):
    list_display = ['driver_name', 'contact_number', 'availability']
    list_filter = ['availability']


@admin.register(Outpatient)
class OutpatientAdmin(admin.ModelAdmin):
    list_display = ['patient', 'visit_date']
    search_fields = ['patient__name']


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'patient', 'visit_date', 'relation']
    list_filter = ['visit_date']


@admin.register(HospitalSystemSetup)
class HospitalSystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name', 'setting_value']
