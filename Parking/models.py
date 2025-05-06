from django.db import models
from django.utils import timezone

class Parking(models.Model):
    location = models.CharField(max_length=100)
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Parking at {self.location}"

class Payment(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=50)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status_choices = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    payment_status = models.CharField(max_length=10, choices=payment_status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment for {self.vehicle_number} - {self.payment_status}"

class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.setting_name
