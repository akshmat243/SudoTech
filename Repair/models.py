from django.db import models
from django.utils import timezone

class RepairTechnician(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    expertise = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Repair(models.Model):
    item_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    issue_description = models.TextField()
    received_date = models.DateTimeField(default=timezone.now)
    assigned_technician = models.ForeignKey(RepairTechnician, on_delete=models.SET_NULL, null=True, blank=True)
    status_choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} - {self.serial_number} ({self.status})"

class RepairOrderRequest(models.Model):
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=timezone.now)
    requested_by = models.CharField(max_length=100)
    urgency_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order Request - {self.repair.serial_number}"

class RepairInvoice(models.Model):
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice #{self.id} for {self.repair.serial_number}"

class Warranty(models.Model):
    item_serial_number = models.CharField(max_length=100)
    warranty_provider = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    terms = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Warranty for {self.item_serial_number}"
