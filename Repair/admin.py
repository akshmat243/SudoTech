from django.contrib import admin
from .models import Repair, RepairOrderRequest, RepairInvoice, RepairTechnician, Warranty

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'serial_number', 'status', 'assigned_technician', 'received_date']
    list_filter = ['status']
    search_fields = ['item_name', 'serial_number']

@admin.register(RepairOrderRequest)
class RepairOrderRequestAdmin(admin.ModelAdmin):
    list_display = ['repair', 'request_date', 'requested_by', 'urgency_level']
    list_filter = ['urgency_level']
    search_fields = ['repair__serial_number', 'requested_by']

@admin.register(RepairInvoice)
class RepairInvoiceAdmin(admin.ModelAdmin):
    list_display = ['repair', 'invoice_date', 'amount', 'paid']
    list_filter = ['paid']
    search_fields = ['repair__serial_number']

@admin.register(RepairTechnician)
class RepairTechnicianAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_number', 'email', 'expertise']
    search_fields = ['name', 'expertise']

@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['item_serial_number', 'warranty_provider', 'start_date', 'end_date']
    search_fields = ['item_serial_number', 'warranty_provider']
