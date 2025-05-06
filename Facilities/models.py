from django.db import models
from django.utils import timezone

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    purpose = models.CharField(max_length=255, blank=True)
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.facility.name} booking by {self.customer_name} on {self.date}"

class BookingOrder(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(default=timezone.now)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_number}"

class BookingReceipt(models.Model):
    order = models.OneToOneField(BookingOrder, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=50, unique=True)
    receipt_date = models.DateField(default=timezone.now)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Receipt {self.receipt_number}"

class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
