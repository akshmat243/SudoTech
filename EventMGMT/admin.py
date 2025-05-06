from django.contrib import admin
from .models import Event, EventBooking, EventBookingOrder, SystemSetup


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start_datetime", "end_datetime", "capacity", "price")
    list_filter = ("start_datetime",)
    search_fields = ("title", "location")


@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ("event", "customer_name", "email", "number_of_tickets", "booking_date")
    search_fields = ("customer_name", "email", "event__title")


@admin.register(EventBookingOrder)
class EventBookingOrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "booking", "payment_status", "amount_paid", "order_date")
    list_filter = ("payment_status",)
    search_fields = ("order_id", "booking__customer_name")


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("setting_name", "setting_value")
    search_fields = ("setting_name",)
