from django.db import models
from django.utils import timezone

class CateringCustomer(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MenuSelection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_person = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EventDetails(models.Model):
    customer = models.ForeignKey(CateringCustomer, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    venue = models.TextField()
    number_of_guests = models.PositiveIntegerField()
    menu = models.ManyToManyField(MenuSelection)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.event_name} - {self.customer.name}"

class CateringInvoice(models.Model):
    event = models.ForeignKey(EventDetails, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number

class FoodSafetyCompliance(models.Model):
    event = models.ForeignKey(EventDetails, on_delete=models.CASCADE)
    inspection_date = models.DateField()
    passed = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Compliance for {self.event}"

class LoyaltyProgram(models.Model):
    customer = models.ForeignKey(CateringCustomer, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    tier = models.CharField(max_length=50, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name} - {self.tier}"

class MarketingCampaigns(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SystemSetup(models.Model):
    company_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
