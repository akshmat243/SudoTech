from django.db import models
from django.utils import timezone


class Locker(models.Model):
    locker_number = models.CharField(max_length=50, unique=True)
    size = models.CharField(max_length=50, choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")])
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Locker {self.locker_number}"


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    id_proof = models.CharField(max_length=100, help_text="Govt. ID Number")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class BookingAssignment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    booking_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("expired", "Expired")])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.full_name} -> {self.locker.locker_number}"


class DepositKeyAccess(models.Model):
    booking = models.ForeignKey(BookingAssignment, on_delete=models.CASCADE)
    key_number = models.CharField(max_length=100)
    access_card_number = models.CharField(max_length=100, blank=True, null=True)
    deposited_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Key/Card for {self.booking}"


class Renewal(models.Model):
    booking = models.ForeignKey(BookingAssignment, on_delete=models.CASCADE)
    renewed_on = models.DateTimeField(auto_now_add=True)
    new_end_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Renewal for {self.booking}"


class MaintenanceRepair(models.Model):
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    issue_reported = models.TextField()
    reported_on = models.DateTimeField(default=timezone.now)
    resolved = models.BooleanField(default=False)
    resolution_notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Maintenance for Locker {self.locker.locker_number}"


class Membership(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    membership_type = models.CharField(max_length=100, choices=[("monthly", "Monthly"), ("yearly", "Yearly")])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.full_name} ({self.membership_type})"
