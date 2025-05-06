from django.contrib import admin
from .models import (
    CleaningTeam, BookingRequest, Inspection, Invoice,
    Maintenance, Complaint, Expense, SystemSetup
)

@admin.register(CleaningTeam)
class CleaningTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'supervisor', 'contact_number']
    search_fields = ['name', 'supervisor']

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'date', 'time_slot', 'team', 'status']
    list_filter = ['status', 'date']
    search_fields = ['customer_name']

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ['booking', 'inspector_name', 'inspection_date', 'passed']
    list_filter = ['passed', 'inspection_date']
    search_fields = ['booking__customer_name', 'inspector_name']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount', 'date_issued', 'paid']
    list_filter = ['paid']
    search_fields = ['booking__customer_name']

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['team', 'issue', 'date_reported', 'resolved']
    list_filter = ['resolved']
    search_fields = ['team__name']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['booking', 'complaint_text', 'date_submitted', 'resolved']
    list_filter = ['resolved']
    search_fields = ['booking__customer_name']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'date', 'category']
    list_filter = ['category', 'date']
    search_fields = ['description']

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'support_email', 'contact_number']
    search_fields = ['company_name']
