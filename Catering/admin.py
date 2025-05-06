from django.contrib import admin
from .models import (
    CateringCustomer, MenuSelection, EventDetails, CateringInvoice,
    FoodSafetyCompliance, LoyaltyProgram, MarketingCampaigns, SystemSetup
)

@admin.register(CateringCustomer)
class CateringCustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_number', 'email']
    search_fields = ['name', 'email']
    list_filter = ['name']

@admin.register(MenuSelection)
class MenuSelectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_per_person']
    search_fields = ['name']

@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'customer', 'event_date', 'venue', 'number_of_guests']
    search_fields = ['event_name', 'customer__name']
    list_filter = ['event_date']

@admin.register(CateringInvoice)
class CateringInvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'event', 'total_amount', 'is_paid', 'issued_date']
    list_filter = ['is_paid', 'issued_date']
    search_fields = ['invoice_number']

@admin.register(FoodSafetyCompliance)
class FoodSafetyComplianceAdmin(admin.ModelAdmin):
    list_display = ['event', 'inspection_date', 'passed']
    list_filter = ['passed', 'inspection_date']

@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ['customer', 'points', 'tier']
    list_filter = ['tier']
    search_fields = ['customer__name']

@admin.register(MarketingCampaigns)
class MarketingCampaignsAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'budget']
    list_filter = ['start_date', 'end_date']

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_email', 'contact_phone']
