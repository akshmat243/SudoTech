from django.contrib import admin
from .models import (
    SLAPolicy, ServiceContract, PendingRequest, 
    ServiceRequest, ServiceHistory, SystemSetup
)

@admin.register(SLAPolicy)
class SLAPolicyAdmin(admin.ModelAdmin):
    list_display = ['name', 'response_time_hours', 'resolution_time_hours']
    search_fields = ['name']

@admin.register(ServiceContract)
class ServiceContractAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'start_date', 'end_date', 'sla_policy', 'active']
    list_filter = ['active', 'sla_policy']
    search_fields = ['customer_name']

@admin.register(PendingRequest)
class PendingRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'contact', 'date_requested']
    search_fields = ['customer_name']

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'status', 'date_requested', 'sla_policy']
    list_filter = ['status']
    search_fields = ['customer_name']

@admin.register(ServiceHistory)
class ServiceHistoryAdmin(admin.ModelAdmin):
    list_display = ['service_request', 'technician_name', 'date_serviced']
    search_fields = ['technician_name', 'service_request__customer_name']

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'support_email', 'phone']
    search_fields = ['company_name']
