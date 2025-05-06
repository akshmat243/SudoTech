from django.contrib import admin
from .models import MeasurementProfile, Order, DesignType, WorkType, FabricType, Tailor, Collection

@admin.register(MeasurementProfile)
class MeasurementProfileAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'chest', 'waist', 'hips', 'shoulder_width', 'sleeve_length', 'inseam']
    search_fields = ['customer_name']
    list_filter = ['customer_name']

@admin.register(DesignType)
class DesignTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(FabricType)
class FabricTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Tailor)
class TailorAdmin(admin.ModelAdmin):
    list_display = ['name', 'availability']
    search_fields = ['name']
    list_filter = ['availability']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    date_hierarchy = 'created_at'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'order_date', 'due_date', 'measurement_profile', 'design_type', 'work_type', 'fabric_type', 'tailor_assigned', 'status']
    list_filter = ['status', 'design_type', 'work_type', 'fabric_type', 'tailor_assigned']
    search_fields = ['customer_name']
    date_hierarchy = 'order_date'
