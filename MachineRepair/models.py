from django.db import models
from django.utils import timezone


class Machine(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    purchase_date = models.DateField()
    location = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class ServiceAgreement(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    terms = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.provider} - {self.machine.name}"


class RepairRequest(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    issue_description = models.TextField()
    request_date = models.DateTimeField(default=timezone.now)
    status_choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Repair Request for {self.machine.serial_number} - {self.status}"


class RepairHistory(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    repair_date = models.DateTimeField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    repaired_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.machine.serial_number} - {self.repair_date.date()}"
