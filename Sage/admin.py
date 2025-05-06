from django.contrib import admin
from .models import LedgerAccount

@admin.register(LedgerAccount)
class LedgerAccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'account_type', 'is_active')
    search_fields = ('name', 'code')
    list_filter = ('account_type', 'is_active')
