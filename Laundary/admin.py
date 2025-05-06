from django.contrib import admin
from .models import LaundryRequest, Invoice, Expenses, Machines, SystemSetup

@admin.register(LaundryRequest)
class LaundryRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'contact_number', 'weight_in_kg', 'status', 'requested_at']
    search_fields = ['customer_name', 'contact_number']
    list_filter = ['status', 'requested_at']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'laundry_request', 'amount', 'is_paid', 'issued_at']
    search_fields = ['invoice_number']
    list_filter = ['is_paid', 'issued_at']

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date']
    search_fields = ['title']
    list_filter = ['date']

@admin.register(Machines)
class MachinesAdmin(admin.ModelAdmin):
    list_display = ['name', 'machine_type', 'purchase_date', 'status']
    search_fields = ['name']
    list_filter = ['status', 'purchase_date']

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_email', 'contact_phone', 'tax_percentage']
    search_fields = ['company_name', 'contact_email']
