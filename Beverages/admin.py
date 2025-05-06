from django.contrib import admin
from .models import (
    Beverage, CollectionCenter, RawMaterial, BillOfMaterial,
    Manufacturing, Packaging, QualityControl, Maintenance, WasteRecord
)

@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'volume_ml', 'price']
    search_fields = ['name', 'category']

@admin.register(CollectionCenter)
class CollectionCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'manager_name']
    search_fields = ['name', 'location']

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'quantity', 'collection_center']
    list_filter = ['collection_center']
    search_fields = ['name']

@admin.register(BillOfMaterial)
class BillOfMaterialAdmin(admin.ModelAdmin):
    list_display = ['beverage', 'raw_material', 'quantity_required']
    search_fields = ['beverage__name']

@admin.register(Manufacturing)
class ManufacturingAdmin(admin.ModelAdmin):
    list_display = ['beverage', 'batch_number', 'date', 'quantity_produced']
    search_fields = ['batch_number']
    date_hierarchy = 'date'

@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ['manufacturing', 'packaging_type', 'packaged_units', 'date']
    search_fields = ['packaging_type']
    date_hierarchy = 'date'

@admin.register(QualityControl)
class QualityControlAdmin(admin.ModelAdmin):
    list_display = ['manufacturing', 'tested_by', 'test_date', 'passed']
    list_filter = ['passed']
    date_hierarchy = 'test_date'

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'last_maintenance_date', 'next_due_date']
    date_hierarchy = 'last_maintenance_date'

@admin.register(WasteRecord)
class WasteRecordAdmin(admin.ModelAdmin):
    list_display = ['manufacturing', 'waste_type', 'quantity', 'date']
    date_hierarchy = 'date'
