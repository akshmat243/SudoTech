from django.contrib import admin
from .models import (
    EyeCarePatient, EyeTestPrescription, EyeCareAppointment,
    EyewearCustomization, EyewearOrder
)

@admin.register(EyeCarePatient)
class EyeCarePatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'phone']
    search_fields = ['name', 'phone']


@admin.register(EyeTestPrescription)
class EyeTestPrescriptionAdmin(admin.ModelAdmin):
    list_display = ['patient', 'test_date', 'right_eye_power', 'left_eye_power']
    list_filter = ['test_date']
    search_fields = ['patient__name']


@admin.register(EyeCareAppointment)
class EyeCareAppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date', 'time']
    list_filter = ['date']
    search_fields = ['patient__name']


@admin.register(EyewearCustomization)
class EyewearCustomizationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'frame_type', 'lens_type', 'color']
    search_fields = ['patient__name', 'frame_type', 'lens_type']


@admin.register(EyewearOrder)
class EyewearOrderAdmin(admin.ModelAdmin):
    list_display = ['patient', 'order_date', 'customization', 'total_cost', 'status']
    list_filter = ['status', 'order_date']
    search_fields = ['patient__name']
