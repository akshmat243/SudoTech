from django.contrib import admin
from .models import (
    FreightCustomer, FreightBooking, FreightShipping, FreightInvoice, FreightSystemSetup
)

@admin.register(FreightCustomer)
class FreightCustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']


@admin.register(FreightBooking)
class FreightBookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'booking_date', 'origin', 'destination', 'status']
    list_filter = ['status', 'booking_date']
    search_fields = ['customer__name', 'origin', 'destination']


@admin.register(FreightShipping)
class FreightShippingAdmin(admin.ModelAdmin):
    list_display = ['booking', 'vessel_name', 'departure_date', 'arrival_date', 'container_number']
    search_fields = ['vessel_name', 'container_number']


@admin.register(FreightInvoice)
class FreightInvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'booking', 'issue_date', 'due_date', 'amount', 'paid']
    list_filter = ['paid', 'issue_date', 'due_date']
    search_fields = ['invoice_number']


@admin.register(FreightSystemSetup)
class FreightSystemSetupAdmin(admin.ModelAdmin):
    list_display = ['key']
    search_fields = ['key']
