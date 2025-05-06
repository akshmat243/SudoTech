from django.db import models
from django.utils import timezone


class PettyCashCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class PettyCash(models.Model):
    title = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    available_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - Available: {self.available_amount}"


class PettyCashExpense(models.Model):
    petty_cash = models.ForeignKey(PettyCash, related_name="expenses", on_delete=models.CASCADE)
    category = models.ForeignKey(PettyCashCategory, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent_on = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.category.name} - {self.amount}"


class PettyCashRequest(models.Model):
    requester = models.CharField(max_length=100)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.TextField()
    requested_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.requester} - {self.amount_requested} - {'Approved' if self.approved else 'Pending'}"


class PettyCashReimbursement(models.Model):
    petty_cash = models.ForeignKey(PettyCash, related_name="reimbursements", on_delete=models.CASCADE)
    reimbursed_by = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reimbursed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reimbursed_by} - {self.amount}"
