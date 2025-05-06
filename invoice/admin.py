from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'invoice_id', 'account_type',
        'issue_date', 'due_date', 'total_amount',
        'due_amount', 'status'
    )
    list_filter = ('account_type', 'status')
    search_fields = ('invoice_id',)
    readonly_fields = ('invoice_id',)
