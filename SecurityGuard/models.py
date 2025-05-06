from django.db import models
from django.utils import timezone


class SecurityGuard(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    license_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SecurityRequest(models.Model):
    requester_name = models.CharField(max_length=255)
    requester_contact = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    requested_date = models.DateTimeField()
    duration_hours = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.requester_name} - {self.location}"


class GuardBooking(models.Model):
    guard = models.ForeignKey(SecurityGuard, on_delete=models.CASCADE)
    security_request = models.ForeignKey(SecurityRequest, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(default=timezone.now)
    shift_start = models.DateTimeField()
    shift_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.guard.name} booked for {self.security_request.location}"


class Payment(models.Model):
    security_request = models.ForeignKey(SecurityRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('card', 'Card'), ('online', 'Online')])
    status = models.CharField(max_length=50, choices=[('paid', 'Paid'), ('pending', 'Pending')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for {self.security_request}"


class IncidentReport(models.Model):
    guard = models.ForeignKey(SecurityGuard, on_delete=models.SET_NULL, null=True)
    incident_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    reported_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Incident at {self.location} on {self.incident_date.date()}"


class EquipmentTracking(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    issued_to = models.ForeignKey(SecurityGuard, on_delete=models.SET_NULL, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('issued', 'Issued'), ('returned', 'Returned')], default='issued')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SystemSetup(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
