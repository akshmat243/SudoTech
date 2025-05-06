from django.contrib import admin
from .models import Animal, Health, Breeding, Weight, DailyMilkSheet, MilkInventory, CumulativeMilkSheet, MilkProduct, FeedManagement, Vaccination, SalesDistribution, ExpenseTracking, CalvingBirthRecord, EquipmentManagement

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'birth_date', 'gender', 'tag_number', 'health_status']
    search_fields = ['name', 'tag_number']
    list_filter = ['gender', 'health_status']

@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = ['animal', 'health_status', 'date_recorded', 'description']
    list_filter = ['health_status', 'date_recorded']

@admin.register(Breeding)
class BreedingAdmin(admin.ModelAdmin):
    list_display = ['animal', 'breeding_date', 'breeding_partner', 'pregnancy_check_date', 'is_pregnant']
    list_filter = ['is_pregnant', 'breeding_date']

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ['animal', 'weight', 'date_recorded']
    search_fields = ['animal__name']
    list_filter = ['date_recorded']

@admin.register(DailyMilkSheet)
class DailyMilkSheetAdmin(admin.ModelAdmin):
    list_display = ['animal', 'milk_quantity', 'date']
    search_fields = ['animal__name']
    list_filter = ['date']

@admin.register(MilkInventory)
class MilkInventoryAdmin(admin.ModelAdmin):
    list_display = ['milk_quantity', 'date_added', 'source']
    search_fields = ['source']
    list_filter = ['date_added']

@admin.register(CumulativeMilkSheet)
class CumulativeMilkSheetAdmin(admin.ModelAdmin):
    list_display = ['animal', 'total_milk', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']

@admin.register(MilkProduct)
class MilkProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_per_unit']
    search_fields = ['name']

@admin.register(FeedManagement)
class FeedManagementAdmin(admin.ModelAdmin):
    list_display = ['animal', 'feed_type', 'quantity', 'feed_date']
    list_filter = ['feed_date']

@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ['animal', 'vaccine_name', 'vaccination_date', 'next_vaccination_date']
    list_filter = ['vaccination_date']

@admin.register(SalesDistribution)
class SalesDistributionAdmin(admin.ModelAdmin):
    list_display = ['milk_product', 'quantity', 'sale_date', 'customer_name']
    list_filter = ['sale_date']

@admin.register(ExpenseTracking)
class ExpenseTrackingAdmin(admin.ModelAdmin):
    list_display = ['expense_type', 'amount', 'expense_date', 'description']
    list_filter = ['expense_date']

@admin.register(CalvingBirthRecord)
class CalvingBirthRecordAdmin(admin.ModelAdmin):
    list_display = ['animal', 'birth_date', 'birth_weight', 'calf_gender']
    list_filter = ['birth_date']

@admin.register(EquipmentManagement)
class EquipmentManagementAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'quantity', 'purchase_date', 'maintenance_date']
    list_filter = ['purchase_date']
