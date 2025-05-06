from django.contrib import admin
from .models import Facility, Booking, BookingOrder, BookingReceipt, SystemSetup

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity', 'available']
    search_fields = ['name', 'location']
    list_filter = ['available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['facility', 'customer_name', 'date', 'start_time', 'end_time', 'status']
    list_filter = ['status', 'date']
    search_fields = ['customer_name', 'facility__name']
    date_hierarchy = 'date'

@admin.register(BookingOrder)
class BookingOrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'booking', 'amount', 'order_date', 'payment_status']
    list_filter = ['payment_status']
    search_fields = ['order_number']
    date_hierarchy = 'order_date'

@admin.register(BookingReceipt)
class BookingReceiptAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'order', 'receipt_date']
    date_hierarchy = 'receipt_date'

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name', 'value']
    search_fields = ['setting_name']
