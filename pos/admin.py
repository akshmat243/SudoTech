from django.contrib import admin
from .models import POS, POSOrder, Product, PrintBarcode, Report


@admin.register(POS)
class POSAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'active')
    search_fields = ('name', 'location')
    list_filter = ('active',)


@admin.register(POSOrder)
class POSOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'pos', 'total_amount', 'order_datetime')
    search_fields = ('order_number', 'pos__name')
    list_filter = ('order_datetime',)
    autocomplete_fields = ('pos',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price')
    search_fields = ('name', 'sku')


@admin.register(PrintBarcode)
class PrintBarcodeAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    search_fields = ('product__name',)
    autocomplete_fields = ('product',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('pos', 'report_date', 'total_orders', 'total_sales')
    search_fields = ('pos__name',)
    list_filter = ('report_date',)
    autocomplete_fields = ('pos',)
