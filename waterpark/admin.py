from django.contrib import admin
from .models import (
    RideManagement, Maintenance, SeasonalPromotion,
    EventManagement, ClothingSales, WaterParkBooking, SystemSetup
)


@admin.register(RideManagement)
class RideManagementAdmin(admin.ModelAdmin):
    list_display = ("ride_name", "ride_type", "max_capacity", "operational_status", "location")
    list_filter = ("ride_type", "operational_status")
    search_fields = ("ride_name",)


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("ride", "start_date", "end_date", "maintenance_type", "maintenance_status")
    list_filter = ("maintenance_status", "start_date")
    search_fields = ("ride__ride_name",)


@admin.register(SeasonalPromotion)
class SeasonalPromotionAdmin(admin.ModelAdmin):
    list_display = ("promotion_code", "discount_percent", "valid_from", "valid_until", "is_active")
    list_filter = ("is_active", "valid_from")
    search_fields = ("promotion_code",)


@admin.register(EventManagement)
class EventManagementAdmin(admin.ModelAdmin):
    list_display = ("event_name", "event_date", "location", "tickets_available", "price_per_ticket")
    list_filter = ("event_date",)
    search_fields = ("event_name",)


@admin.register(ClothingSales)
class ClothingSalesAdmin(admin.ModelAdmin):
    list_display = ("item_name", "category", "price", "available_stock")
    list_filter = ("category",)
    search_fields = ("item_name",)


@admin.register(WaterParkBooking)
class WaterParkBookingAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_email", "number_of_tickets", "total_amount", "booking_date", "seasonal_promotion")
    list_filter = ("booking_date",)
    search_fields = ("customer_name", "customer_email")


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)
