from django.contrib import admin
from .models import (
    GardenBed, Plant, WateringSchedule,
    MaintenanceLog, SeasonalPlan, PestAndDisease
)


@admin.register(GardenBed)
class GardenBedAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "size_sq_meters")
    search_fields = ("name", "location")


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ("name", "bed", "planted_on", "plant_type")
    list_filter = ("plant_type",)
    search_fields = ("name",)


@admin.register(WateringSchedule)
class WateringScheduleAdmin(admin.ModelAdmin):
    list_display = ("plant", "frequency_days", "last_watered", "next_due")
    search_fields = ("plant__name",)


@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ("bed", "performed_on", "activity")
    list_filter = ("performed_on",)
    search_fields = ("activity", "bed__name")


@admin.register(SeasonalPlan)
class SeasonalPlanAdmin(admin.ModelAdmin):
    list_display = ("season", "year")
    list_filter = ("season", "year")
    search_fields = ("planned_crops",)


@admin.register(PestAndDisease)
class PestAndDiseaseAdmin(admin.ModelAdmin):
    list_display = ("plant", "issue_type", "date_detected")
    list_filter = ("issue_type",)
    search_fields = ("description", "plant__name")
