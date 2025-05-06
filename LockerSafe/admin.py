from django.contrib import admin
from .models import (
    Locker, Customer, BookingAssignment,
    DepositKeyAccess, Renewal, MaintenanceRepair, Membership
)


@admin.register(Locker)
class LockerAdmin(admin.ModelAdmin):
    list_display = ("locker_number", "size", "is_available", "location")
    list_filter = ("size", "is_available")
    search_fields = ("locker_number", "location")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    search_fields = ("full_name", "email", "phone")


@admin.register(BookingAssignment)
class BookingAssignmentAdmin(admin.ModelAdmin):
    list_display = ("customer", "locker", "booking_date", "end_date", "status")
    list_filter = ("status",)
    search_fields = ("customer__full_name", "locker__locker_number")


@admin.register(DepositKeyAccess)
class DepositKeyAccessAdmin(admin.ModelAdmin):
    list_display = ("booking", "key_number", "access_card_number", "deposited_on")
    search_fields = ("key_number", "access_card_number")


@admin.register(Renewal)
class RenewalAdmin(admin.ModelAdmin):
    list_display = ("booking", "renewed_on", "new_end_date")
    search_fields = ("booking__customer__full_name",)


@admin.register(MaintenanceRepair)
class MaintenanceRepairAdmin(admin.ModelAdmin):
    list_display = ("locker", "issue_reported", "reported_on", "resolved")
    list_filter = ("resolved",)
    search_fields = ("locker__locker_number", "issue_reported")


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("customer", "membership_type", "start_date", "end_date", "is_active")
    list_filter = ("membership_type", "is_active")
    search_fields = ("customer__full_name",)
