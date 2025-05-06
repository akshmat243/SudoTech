from django.contrib import admin
from .models import CollectionRequest, Trip, Inspection, CollectionSchedule, DisposalFacility, Recycling, SystemSetup

@admin.register(CollectionRequest)
class CollectionRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'address', 'collection_date', 'status', 'request_date']
    search_fields = ['customer_name', 'address']
    list_filter = ['status', 'collection_date']

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['collection_request', 'driver_name', 'vehicle_number', 'start_time', 'end_time', 'status']
    list_filter = ['status', 'start_time']
    search_fields = ['collection_request__customer_name']

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ['trip', 'inspector_name', 'inspection_date', 'status']
    list_filter = ['status', 'inspection_date']
    search_fields = ['trip__collection_request__customer_name']

@admin.register(CollectionSchedule)
class CollectionScheduleAdmin(admin.ModelAdmin):
    list_display = ['day_of_week', 'start_time', 'end_time', 'assigned_driver']
    list_filter = ['day_of_week']

@admin.register(DisposalFacility)
class DisposalFacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity', 'contact_info']
    search_fields = ['name', 'location']
    list_filter = ['capacity']

@admin.register(Recycling)
class RecyclingAdmin(admin.ModelAdmin):
    list_display = ['material_type', 'quantity_collected', 'collection_date', 'recycling_center']
    list_filter = ['material_type', 'collection_date']
    search_fields = ['material_type']

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['system_name', 'configuration_details', 'setup_date']
    search_fields = ['system_name']
