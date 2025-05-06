from django.contrib import admin
from .models import (
    ElderlyResident, Caretaker, CareRequest, DailyActivitySchedule,
    HealthCheckup, MealPlan
)

@admin.register(ElderlyResident)
class ElderlyResidentAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth', 'emergency_contact']
    search_fields = ['name', 'emergency_contact']


@admin.register(Caretaker)
class CaretakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'assigned_resident']
    list_filter = ['assigned_resident']
    search_fields = ['name']


@admin.register(CareRequest)
class CareRequestAdmin(admin.ModelAdmin):
    list_display = ['resident', 'request_date', 'status']
    list_filter = ['status']
    search_fields = ['resident__name']


@admin.register(DailyActivitySchedule)
class DailyActivityScheduleAdmin(admin.ModelAdmin):
    list_display = ['resident', 'activity_name', 'time']
    search_fields = ['activity_name', 'resident__name']


@admin.register(HealthCheckup)
class HealthCheckupAdmin(admin.ModelAdmin):
    list_display = ['resident', 'checkup_date']
    search_fields = ['resident__name']


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ['resident', 'date', 'breakfast', 'lunch', 'dinner']
    list_filter = ['date']
    search_fields = ['resident__name']
