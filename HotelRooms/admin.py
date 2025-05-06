from django.contrib import admin
from .models import (
    Hotel, Room, Facility, Booking, Coupon, CustomPage,
    HotelCustomer, CustomerReview, BankTransferRequest
)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "contact_email", "contact_phone")
    search_fields = ("name", "city")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("hotel", "room_number", "room_type", "price_per_night", "is_available")
    list_filter = ("hotel", "room_type", "is_available")
    search_fields = ("room_number",)


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("hotel", "name")
    search_fields = ("name", "hotel__name")


@admin.register(HotelCustomer)
class HotelCustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    search_fields = ("full_name", "email")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer", "room", "check_in", "check_out", "is_paid")
    list_filter = ("is_paid",)
    search_fields = ("customer__full_name", "room__room_number")


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "discount_percent", "valid_from", "valid_to", "is_active")
    list_filter = ("is_active",)
    search_fields = ("code",)


@admin.register(CustomPage)
class CustomPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title",)


@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ("hotel", "customer", "rating", "review_date")
    list_filter = ("rating",)
    search_fields = ("customer__full_name", "hotel__name")


@admin.register(BankTransferRequest)
class BankTransferRequestAdmin(admin.ModelAdmin):
    list_display = ("customer", "amount", "transaction_id", "requested_on", "is_approved")
    list_filter = ("is_approved",)
    search_fields = ("transaction_id", "customer__full_name")
