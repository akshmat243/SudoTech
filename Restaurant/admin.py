from django.contrib import admin
from .models import Item, Customer, DiningTable, TableOrder, SystemSetup

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available']
    search_fields = ['name']
    list_filter = ['available']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'is_available']
    list_filter = ['is_available']
    search_fields = ['table_number']

@admin.register(TableOrder)
class TableOrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'dining_table', 'order_time', 'total_price', 'order_status']
    list_filter = ['order_status', 'dining_table']
    search_fields = ['customer__first_name', 'customer__last_name']
    date_hierarchy = 'order_time'

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name', 'value']
    search_fields = ['setting_name']
