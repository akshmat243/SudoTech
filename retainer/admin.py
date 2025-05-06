from django.contrib import admin
from .models import Retainer

@admin.register(Retainer)
class RetainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'retainer_id', 'customer', 'account_type', 'issue_date', 'due_amount', 'status')
    list_filter = ('account_type', 'status')
    search_fields = ('retainer_id', 'customer')
    readonly_fields = ('retainer_id',)
