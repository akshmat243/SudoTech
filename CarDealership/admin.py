from django.contrib import admin
from .models import (
    DealershipProduct, CarInventory, CarPurchase, SalesManagement,
    Service, TestDrive, Warranty, Insurance
)


@admin.register(DealershipProduct)
class DealershipProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category")


@admin.register(CarInventory)
class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ("vin", "product", "color", "year", "price", "is_sold")
    list_filter = ("is_sold", "year")


@admin.register(CarPurchase)
class CarPurchaseAdmin(admin.ModelAdmin):
    list_display = ("buyer_name", "inventory", "purchase_date", "total_price")
    date_hierarchy = "purchase_date"


@admin.register(SalesManagement)
class SalesManagementAdmin(admin.ModelAdmin):
    list_display = ("salesperson", "sale", "commission")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("car", "service_date", "cost")


@admin.register(TestDrive)
class TestDriveAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "car", "date")


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ("car", "warranty_provider", "warranty_start", "warranty_end")


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ("car", "insurance_company", "policy_number", "insured_from", "insured_to", "premium_amount")
