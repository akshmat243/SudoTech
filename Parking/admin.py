from django.contrib import admin
from .models import Parking, Payment, SystemSetup

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ['location', 'total_slots', 'available_slots', 'price_per_hour']
    search_fields = ['location']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['parking', 'customer_name', 'vehicle_number', 'entry_time', 'exit_time', 'total_amount', 'payment_status']
    list_filter = ['payment_status', 'parking']
    search_fields = ['vehicle_number', 'customer_name']
    date_hierarchy = 'entry_time'

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name', 'value']
    search_fields = ['setting_name']
