from django.contrib import admin
from .models import Commission, CommissionPlan, CommissionReceipt, BankTransferRequest


@admin.register(CommissionPlan)
class CommissionPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ("agent_name", "plan", "amount", "earned_on")
    list_filter = ("earned_on", "plan")
    search_fields = ("agent_name",)


@admin.register(CommissionReceipt)
class CommissionReceiptAdmin(admin.ModelAdmin):
    list_display = ("receipt_number", "commission", "issued_date", "paid")
    list_filter = ("paid",)
    search_fields = ("receipt_number", "commission__agent_name")


@admin.register(BankTransferRequest)
class BankTransferRequestAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "commission", "requested_on", "approved")
    list_filter = ("approved",)
    search_fields = ("transaction_id", "commission__agent_name")
