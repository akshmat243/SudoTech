from django.contrib import admin
from .models import (
    SecurityGuard, SecurityRequest, Payment,
    GuardBooking, IncidentReport, EquipmentTracking, SystemSetup
)


@admin.register(SecurityGuard)
class SecurityGuardAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "license_number", "is_active", "date_joined")
    search_fields = ("name", "phone", "license_number")
    list_filter = ("is_active",)


@admin.register(SecurityRequest)
class SecurityRequestAdmin(admin.ModelAdmin):
    list_display = ("requester_name", "location", "requested_date", "duration_hours", "status")
    list_filter = ("status",)
    search_fields = ("requester_name", "location")


@admin.register(GuardBooking)
class GuardBookingAdmin(admin.ModelAdmin):
    list_display = ("guard", "security_request", "shift_start", "shift_end", "assigned_on")
    search_fields = ("guard__name", "security_request__location")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("security_request", "amount", "paid_on", "payment_method", "status")
    list_filter = ("payment_method", "status")
    search_fields = ("security_request__requester_name",)


@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ("guard", "location", "incident_date", "reported_on")
    list_filter = ("incident_date",)
    search_fields = ("guard__name", "location")


@admin.register(EquipmentTracking)
class EquipmentTrackingAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "issued_to", "issue_date", "return_date", "status")
    list_filter = ("status",)
    search_fields = ("name", "serial_number")


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)
