from django.contrib import admin
from .models import (
    Membership, MembershipPlan, Booking, Amenity, ResponseSetup, CoworkingSpaceSetup
)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "email", "membership_start_date", "membership_end_date", "status")
    search_fields = ("customer_name", "email")
    list_filter = ("status",)


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_month", "duration_months")
    search_fields = ("name",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer", "start_time", "end_time", "space_booked", "booking_status")
    list_filter = ("booking_status", "start_time")
    search_fields = ("customer__customer_name", "space_booked")


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_use", "available")
    list_filter = ("available",)
    search_fields = ("name",)


@admin.register(ResponseSetup)
class ResponseSetupAdmin(admin.ModelAdmin):
    list_display = ("question", "response_type", "is_active")
    list_filter = ("is_active",)
    search_fields = ("question",)


@admin.register(CoworkingSpaceSetup)
class CoworkingSpaceSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)
