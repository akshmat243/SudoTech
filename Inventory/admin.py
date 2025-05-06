from django.contrib import admin
from .models import InventoryItem

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'quantity', 'unit_price', 'location', 'is_active')
    search_fields = ('sku', 'name', 'category', 'location')
    list_filter = ('category', 'is_active')
