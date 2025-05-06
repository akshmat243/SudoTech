from django.db import models

class Advocate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CaseInitiator(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourtCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LegalCase(models.Model):
    title = models.CharField(max_length=255)
    advocate = models.ForeignKey(Advocate, on_delete=models.SET_NULL, null=True)
    initiator = models.ForeignKey(CaseInitiator, on_delete=models.SET_NULL, null=True)
    court_category = models.ForeignKey(CourtCategory, on_delete=models.SET_NULL, null=True)
    case_number = models.CharField(max_length=100)
    filing_date = models.DateField()
    status = models.CharField(max_length=100, choices=[("Open", "Open"), ("Closed", "Closed"), ("Pending", "Pending")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.case_number})"


class Expense(models.Model):
    legal_case = models.ForeignKey(LegalCase, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"


class FeeReceive(models.Model):
    legal_case = models.ForeignKey(LegalCase, on_delete=models.CASCADE)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    received_date = models.DateField()
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"₹{self.amount_received} on {self.received_date}"
