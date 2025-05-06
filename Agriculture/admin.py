from django.contrib import admin
from .models import *

@admin.register(Agriculture)
class AgricultureAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name', 'location']


@admin.register(Fleet)
class FleetAdmin(admin.ModelAdmin):
    list_display = ['name', 'vehicle_type', 'registration_number', 'status']
    search_fields = ['name', 'registration_number']
    list_filter = ['vehicle_type', 'status']


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status']
    list_filter = ['category', 'status']
    search_fields = ['name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'head']
    search_fields = ['name', 'head']


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name']


@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):
    list_display = ['name', 'length_km']
    search_fields = ['name']


@admin.register(ServiceProduct)
class ServiceProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ['name', 'season']
    list_filter = ['season']
    search_fields = ['name']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'contact']
    search_fields = ['name', 'role', 'contact']


@admin.register(Cultivation)
class CultivationAdmin(admin.ModelAdmin):
    list_display = ['crop', 'area', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    date_hierarchy = 'start_date'
    search_fields = ['crop__name']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'cultivation', 'performed_by', 'date']
    date_hierarchy = 'date'
    search_fields = ['name', 'performed_by']
    list_filter = ['date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider', 'date']
    date_hierarchy = 'date'
    search_fields = ['name', 'provider']


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit']
    search_fields = ['name']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['name', 'partner', 'start_date', 'end_date']
    date_hierarchy = 'start_date'
    search_fields = ['name', 'partner']


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['borrower', 'amount', 'issued_date', 'due_date']
    date_hierarchy = 'issued_date'
    search_fields = ['borrower']


@admin.register(PestDisease)
class PestDiseaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'crop']
    search_fields = ['name', 'crop__name']


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'temperature', 'rainfall', 'humidity']
    date_hierarchy = 'date'
    list_filter = ['date']


@admin.register(SoilAnalysis)
class SoilAnalysisAdmin(admin.ModelAdmin):
    list_display = ['location', 'ph_level', 'date']
    search_fields = ['location']
    date_hierarchy = 'date'


@admin.register(IrrigationSystem)
class IrrigationSystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'coverage_area']
    search_fields = ['name', 'type']


@admin.register(ResearchDevelopment)
class ResearchDevelopmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'lead_scientist', 'date']
    search_fields = ['title', 'lead_scientist']
    date_hierarchy = 'date'


@admin.register(ComplianceReport)
class ComplianceReportAdmin(admin.ModelAdmin):
    list_display = ['report_name', 'submitted_by', 'date']
    search_fields = ['report_name', 'submitted_by']
    date_hierarchy = 'date'


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name']
    search_fields = ['setting_name']
