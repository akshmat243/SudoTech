from django.contrib import admin
from .models import (
    Medicine, Stock, DiscountPromotion, Bill, Invoice,
    ReturnRefund, Manufacturing, PharmacySystemSetup
)

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'batch_number', 'price', 'expiry_date']
    search_fields = ['name', 'brand', 'batch_number']
    list_filter = ['expiry_date']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['medicine', 'quantity', 'last_updated']
    search_fields = ['medicine__name']


@admin.register(DiscountPromotion)
class DiscountPromotionAdmin(admin.ModelAdmin):
    list_display = ['medicine', 'discount_percent', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'date', 'total_amount', 'final_amount']
    search_fields = ['customer_name']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['bill', 'medicine', 'quantity', 'rate', 'total']
    search_fields = ['medicine__name', 'bill__customer_name']


@admin.register(ReturnRefund)
class ReturnRefundAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'reason', 'refund_amount', 'date']
    search_fields = ['invoice__id']


@admin.register(Manufacturing)
class ManufacturingAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'batch_code', 'manufacture_date', 'expiry_date', 'quantity_produced']
    search_fields = ['product_name', 'batch_code']


@admin.register(PharmacySystemSetup)
class PharmacySystemSetupAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ['key']
