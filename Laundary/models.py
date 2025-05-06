from django.db import models
from django.utils import timezone

class LaundryRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    item_description = models.TextField()
    weight_in_kg = models.FloatField()
    requested_at = models.DateTimeField(default=timezone.now)
    status_choices = [
        ('pending', 'Pending'),
        ('in_process', 'In Process'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"

class Invoice(models.Model):
    laundry_request = models.ForeignKey(LaundryRequest, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issued_at = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number

class Expenses(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Machines(models.Model):
    name = models.CharField(max_length=100)
    machine_type = models.CharField(max_length=100)
    purchase_date = models.DateField()
    status_choices = [
        ('working', 'Working'),
        ('maintenance', 'Under Maintenance'),
        ('out_of_order', 'Out of Order')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='working')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SystemSetup(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    tax_percentage = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
