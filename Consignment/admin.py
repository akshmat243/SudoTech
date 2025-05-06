from django.contrib import admin
from .models import Product, Consignment, PurchaseOrder, SaleOrder, Shipping, Returns, QualityControl, Contract, Compliance

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity_in_stock']
    search_fields = ['name']
    list_filter = ['price']

@admin.register(Consignment)
class ConsignmentAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'date_received', 'status']
    list_filter = ['status', 'date_received']
    search_fields = ['product__name']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['supplier_name', 'order_date', 'total_price']
    search_fields = ['supplier_name']
    list_filter = ['order_date']

@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'order_date', 'total_price']
    search_fields = ['customer_name']
    list_filter = ['order_date']

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['sale_order', 'shipping_address', 'shipping_date', 'tracking_number']
    search_fields = ['sale_order__customer_name', 'tracking_number']

@admin.register(Returns)
class ReturnsAdmin(admin.ModelAdmin):
    list_display = ['sale_order', 'return_reason', 'return_date', 'status']
    search_fields = ['sale_order__customer_name']
    list_filter = ['status', 'return_date']

@admin.register(QualityControl)
class QualityControlAdmin(admin.ModelAdmin):
    list_display = ['consignment', 'inspection_date', 'inspector_name', 'status']
    list_filter = ['status', 'inspection_date']
    search_fields = ['consignment__product__name']

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['consignment', 'contract_number', 'contract_date']
    search_fields = ['contract_number']

@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    list_display = ['consignment', 'compliance_document', 'compliance_date', 'status']
    list_filter = ['status', 'compliance_date']
    search_fields = ['consignment__product__name']
