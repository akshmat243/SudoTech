from django.contrib import admin
from .models import (
    Driver, Customer, Vehicle, LogBook, Booking, Availability,
    Insurance, Maintenance, FuelHistory, Report, SystemSetup
)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("name", "license_number", "phone", "email")
    search_fields = ("name", "license_number")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("plate_number", "model", "year", "driver")
    search_fields = ("plate_number", "model")
    list_filter = ("year",)


@admin.register(LogBook)
class LogBookAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "date", "distance_traveled")
    date_hierarchy = "date"
    search_fields = ("vehicle__plate_number",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer", "vehicle", "start_date", "end_date", "driver")
    date_hierarchy = "start_date"
    search_fields = ("customer__name", "vehicle__plate_number")


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "available_from", "available_to")
    search_fields = ("vehicle__plate_number",)


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "provider", "policy_number", "valid_from", "valid_to")
    date_hierarchy = "valid_from"
    search_fields = ("vehicle__plate_number", "policy_number")


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "date", "cost")
    date_hierarchy = "date"
    search_fields = ("vehicle__plate_number",)


@admin.register(FuelHistory)
class FuelHistoryAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "date", "liters", "cost")
    date_hierarchy = "date"


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    date_hierarchy = "created_at"


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
