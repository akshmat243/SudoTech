from django.contrib import admin
from .models import Purchase, Warehouse, WarehouseTransfer

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'purchase_id', 'vendor', 'account_type', 
        'category', 'purchase_date', 'status'
    )
    list_filter = ('account_type', 'status', 'category')
    search_fields = ('purchase_id', 'vendor', 'category')
    readonly_fields = ('purchase_id',)

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city', 'zip_code')
    search_fields = ('name', 'city', 'zip_code')
    

@admin.register(WarehouseTransfer)
class WarehouseTransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_warehouse', 'to_warehouse', 'product', 'quantity', 'date')
    list_filter = ('from_warehouse', 'to_warehouse', 'date')
    search_fields = ('product',)