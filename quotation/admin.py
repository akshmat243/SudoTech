from django.contrib import admin
from .models import Quotation

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'quotation_id', 'customer', 'account_type',
        'warehouse', 'quotation_type', 'quotation_date'
    )
    list_filter = ('account_type', 'quotation_type', 'warehouse')
    search_fields = ('quotation_id', 'customer')
    readonly_fields = ('quotation_id',)
