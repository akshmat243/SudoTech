from django.contrib import admin
from .models import (
    Booking, Item, Package, Customer, Appointment, Staff, SystemSetup
)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'phone']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'contact']
    search_fields = ['name', 'role']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_minutes']
    search_fields = ['name']

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_price']
    filter_horizontal = ['items']
    search_fields = ['name']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_time', 'staff']
    search_fields = ['customer__name']
    list_filter = ['staff']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'item', 'package', 'appointment', 'status', 'created_at']
    search_fields = ['customer__name']
    list_filter = ['status', 'created_at']

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ['key']
