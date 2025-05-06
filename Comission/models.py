from django.db import models
from django.utils import timezone


class CommissionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Commission(models.Model):
    agent_name = models.CharField(max_length=100)
    plan = models.ForeignKey(CommissionPlan, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    earned_on = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.agent_name} - ${self.amount}"


class CommissionReceipt(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=100, unique=True)
    issued_date = models.DateTimeField(default=timezone.now)
    paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Receipt {self.receipt_number} - {self.commission.agent_name}"


class BankTransferRequest(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    requested_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transfer {self.transaction_id} - {self.commission.agent_name}"
