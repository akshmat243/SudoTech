from django.contrib import admin
from .models import (
    PropertyManage, Property, Unit, Listing, Tenant, Invoice, MaintenanceRequest,
    DocumentType, TenantRequest, ExpenseTracking, Inspection, TenantCommunication,
    Utility, Contractor
)

@admin.register(PropertyManage)
class PropertyManageAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_email']
    search_fields = ['name']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'manager']
    search_fields = ['name']
    list_filter = ['manager']


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['unit_number', 'property', 'size_sqft', 'available']
    list_filter = ['property', 'available']


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['unit', 'price', 'is_active', 'listed_date']
    list_filter = ['is_active']


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'unit']
    search_fields = ['name', 'email']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'amount', 'due_date', 'is_paid']
    list_filter = ['is_paid']
    search_fields = ['tenant__name']


@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ['unit', 'status', 'request_date']
    list_filter = ['status']


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(TenantRequest)
class TenantRequestAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'subject', 'submitted_at']
    search_fields = ['tenant__name', 'subject']


@admin.register(ExpenseTracking)
class ExpenseTrackingAdmin(admin.ModelAdmin):
    list_display = ['property', 'category', 'amount', 'expense_date']
    list_filter = ['property']


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ['unit', 'inspector_name', 'inspection_date']


@admin.register(TenantCommunication)
class TenantCommunicationAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'subject', 'date_sent']


@admin.register(Utility)
class UtilityAdmin(admin.ModelAdmin):
    list_display = ['unit', 'type', 'reading', 'bill_amount', 'billing_date']


@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type']
    search_fields = ['name', 'service_type']
