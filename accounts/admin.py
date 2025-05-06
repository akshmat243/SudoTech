from django.contrib import admin
from .models import Customer, Vendor, BankAccount, ChartAccount, Transfer, TransactionRecord, Revenue, CreditNotes, BillRecord, PaymentRecord, DebitNotes, Budget, FinancialGoal

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'name', 'contact', 'email', 'balance')
    search_fields = ('customer_id', 'name', 'contact', 'email')
    readonly_fields = ('customer_id',)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor_id', 'name', 'contact', 'email', 'balance')
    search_fields = ('vendor_id', 'name', 'contact', 'email')
    readonly_fields = ('vendor_id',)
    
@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'chart_of_account', 'name', 'bank', 'account_number',
        'current_balance', 'contact_number', 'bank_branch', 'swift'
    )
    search_fields = ('name', 'bank', 'account_number', 'swift')
    list_filter = ('bank', 'bank_branch')

@admin.register(ChartAccount)
class ChartAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'type', 'parent_account', 'balance', 'status')
    list_filter = ('type', 'status')
    search_fields = ('code', 'name', 'parent_account__name')
    
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'from_account', 'to_account', 'amount', 'reference')
    list_filter = ('created_at', 'from_account', 'to_account')
    search_fields = ('reference', 'description', 'from_account__name', 'to_account__name')

@admin.register(TransactionRecord)
class TransactionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_date', 'transaction_name', 'transaction_amount', 'transaction_status')
    list_filter = ('transaction_status', 'transaction_date')
    search_fields = ('transaction_name',)
    
@admin.register(Revenue)
class RevenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'amount', 'account', 'customer', 'category', 'reference')
    list_filter = ('created_at', 'account', 'customer', 'category')
    search_fields = ('reference', 'description', 'account__name', 'customer__name')

@admin.register(CreditNotes)
class CreditNotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice_number', 'customer', 'date', 'amount', 'status')
    list_filter = ('status', 'date')
    search_fields = ('invoice_number', 'customer__name', 'description')
    readonly_fields = ('invoice_number',)

@admin.register(BillRecord)
class BillRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'bill_number', 'vendor', 'account_type',
        'bill_date', 'due_date', 'due_amount', 'status'
    )
    list_filter = ('status', 'account_type', 'bill_date', 'due_date')
    search_fields = ('bill_number', 'vendor__name')
    readonly_fields = ('bill_number',)

@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'date', 'amount', 'account',
        'vendor', 'category', 'reference'
    )
    list_filter = ('date', 'account', 'vendor', 'category')
    search_fields = ( 'reference', 'description', 'vendor__name')
    readonly_fields = ('id',)

@admin.register(DebitNotes)
class DebitNotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill_number', 'vendor', 'date', 'amount', 'status')
    list_filter = ('status', 'date')
    search_fields = ('bill_number', 'vendor__name', 'description')
    readonly_fields = ('bill_number',)

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'from_date', 'budget_period')
    search_fields = ('name',)
    list_filter = ('budget_period',)
    readonly_fields = ('id',)
    
@admin.register(FinancialGoal)
class FinancialGoalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'goal_no', 'name', 'type', 'from_date', 'to_date', 'amount', 'is_dashboard_display'
    )
    list_filter = ('type', 'from_date', 'to_date', 'is_dashboard_display')
    search_fields = ('goal_no', 'name', 'type')
    readonly_fields = ('goal_no',)