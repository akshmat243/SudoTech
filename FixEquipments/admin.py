from django.contrib import admin
from .models import FixEquipment, EquipmentMaintenance, EquipmentAudit, EquipmentSystemSetup

@admin.register(FixEquipment)
class FixEquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_id', 'name', 'equipment_type', 'status', 'location', 'purchase_date')
    search_fields = ('equipment_id', 'name', 'equipment_type', 'location')
    list_filter = ('equipment_type', 'status')

@admin.register(EquipmentMaintenance)
class EquipmentMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'maintenance_date', 'maintenance_type', 'status')
    search_fields = ('equipment__equipment_id', 'maintenance_type', 'status')
    list_filter = ('maintenance_type', 'status')

@admin.register(EquipmentAudit)
class EquipmentAuditAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'audit_date', 'auditor_name', 'audit_status')
    search_fields = ('equipment__equipment_id', 'audit_status', 'auditor_name')
    list_filter = ('audit_status',)

@admin.register(EquipmentSystemSetup)
class EquipmentSystemSetupAdmin(admin.ModelAdmin):
    list_display = ('setting_name', 'value')
    search_fields = ('setting_name',)
