from django.contrib import admin
from .models import (
    VehicleBooking, FuelLog, Incident, MaintenanceRecord,
    VehicleContract, EmergencyContact, Route
)


@admin.register(VehicleBooking)
class VehicleBookingAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "booked_by", "start_datetime", "end_datetime", "purpose")
    list_filter = ("vehicle", "start_datetime")


@admin.register(FuelLog)
class FuelLogAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "date", "liters", "cost", "odometer")


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "reported_by", "date", "resolved")
    list_filter = ("resolved",)


@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "date", "performed_by", "cost")


@admin.register(VehicleContract)
class VehicleContractAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "contract_number", "start_date", "end_date")


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "name", "phone", "relationship")


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "origin", "destination", "distance_km", "estimated_time")
