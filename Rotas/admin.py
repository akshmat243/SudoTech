from django.contrib import admin
from .models import Rota, WorkSchedule, Availability


@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ("name", "created_on")
    search_fields = ("name",)


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "rota", "shift_start", "shift_end", "role")
    list_filter = ("rota",)
    search_fields = ("employee_name", "role")


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "date", "is_available")
    list_filter = ("is_available", "date")
    search_fields = ("employee_name",)
