from django.contrib import admin
from .models import Vehicle, Service, JobCard, Item, Warranty, SystemSetup

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['registration_number', 'owner_name', 'make', 'model', 'year']
    search_fields = ['registration_number', 'owner_name', 'make', 'model']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    search_fields = ['name']


@admin.register(JobCard)
class JobCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicle', 'job_date', 'status']
    list_filter = ['status', 'job_date']
    search_fields = ['vehicle__registration_number']
    filter_horizontal = ['service']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['jobcard', 'name', 'quantity', 'unit_price']
    search_fields = ['name', 'jobcard__vehicle__registration_number']


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'start_date', 'end_date']
    search_fields = ['vehicle__registration_number']


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['key']
    search_fields = ['key']
