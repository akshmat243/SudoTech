from django.db import models
from django.utils import timezone


class Vehicle(models.Model):
    registration_number = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    owner_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration_number


class ComplianceRegulation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    effective_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InspectionRequest(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    reason = models.TextField()
    request_date = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request for {self.vehicle.registration_number}"


class InspectionList(models.Model):
    title = models.CharField(max_length=100)
    checklist_items = models.TextField(help_text="Separate items with a comma.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InspectionSchedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    inspection_date = models.DateTimeField()
    assigned_inspector = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Schedule for {self.vehicle.registration_number} on {self.inspection_date.date()}"


class InspectionReminder(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reminder for {self.vehicle.registration_number}"


class InspectionHistory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    inspection_date = models.DateTimeField()
    findings = models.TextField()
    passed = models.BooleanField(default=False)
    inspector_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle.registration_number} - {self.inspection_date.date()}"
