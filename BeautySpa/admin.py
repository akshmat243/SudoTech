from django.contrib import admin
from .models import (
    Booking, BookingOrder, BeautyReceipt, Training, Certification,
    GiftCard, Resource, BookingReminder, LoyaltyProgram, Membership,
    BeautySpaSystemSetup
)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'service', 'date_time', 'staff', 'membership']
    search_fields = ['client_name', 'service']
    list_filter = ['date_time', 'staff']

@admin.register(BookingOrder)
class BookingOrderAdmin(admin.ModelAdmin):
    list_display = ['booking', 'item_name', 'price']
    search_fields = ['item_name', 'booking__client_name']

@admin.register(BeautyReceipt)
class BeautyReceiptAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount_paid', 'date_paid', 'payment_method']
    search_fields = ['booking__client_name']

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'trainer']
    search_fields = ['title', 'trainer']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['staff_name', 'certificate_name', 'date_issued']
    search_fields = ['staff_name', 'certificate_name']

@admin.register(GiftCard)
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ['code', 'value', 'issue_date', 'expiry_date', 'is_redeemed']
    search_fields = ['code']
    list_filter = ['is_redeemed']

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'quantity', 'last_updated']
    search_fields = ['name']

@admin.register(BookingReminder)
class BookingReminderAdmin(admin.ModelAdmin):
    list_display = ['booking', 'reminder_time', 'sent']
    list_filter = ['sent']

@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'points', 'last_updated']
    search_fields = ['client_name']

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_days', 'price']
    search_fields = ['name']

@admin.register(BeautySpaSystemSetup)
class BeautySpaSystemSetupAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ['key']
