from django.contrib import admin
from .models import PettyCash, PettyCashExpense, PettyCashRequest, PettyCashReimbursement, PettyCashCategory

@admin.register(PettyCashCategory)
class PettyCashCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(PettyCash)
class PettyCashAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_amount', 'available_amount', 'created_on')
    search_fields = ('title',)

@admin.register(PettyCashExpense)
class PettyCashExpenseAdmin(admin.ModelAdmin):
    list_display = ('petty_cash', 'category', 'amount', 'spent_on')
    list_filter = ('category',)
    search_fields = ('description',)

@admin.register(PettyCashRequest)
class PettyCashRequestAdmin(admin.ModelAdmin):
    list_display = ('requester', 'amount_requested', 'requested_on', 'approved')
    list_filter = ('approved',)
    search_fields = ('requester',)

@admin.register(PettyCashReimbursement)
class PettyCashReimbursementAdmin(admin.ModelAdmin):
    list_display = ('petty_cash', 'reimbursed_by', 'amount', 'reimbursed_on')
    search_fields = ('reimbursed_by',)
