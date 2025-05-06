from django.db import models
from django.utils import timezone


class CleaningTeam(models.Model):
    name = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BookingRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    team = models.ForeignKey(CleaningTeam, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.date}"


class Inspection(models.Model):
    booking = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    inspector_name = models.CharField(max_length=100)
    notes = models.TextField()
    inspection_date = models.DateField(default=timezone.now)
    passed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inspection for {self.booking.customer_name}"


class Invoice(models.Model):
    booking = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField(default=timezone.now)
    paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.booking.customer_name}"


class Maintenance(models.Model):
    team = models.ForeignKey(CleaningTeam, on_delete=models.CASCADE)
    issue = models.TextField()
    date_reported = models.DateField(default=timezone.now)
    resolved = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team.name} - Maintenance"


class Complaint(models.Model):
    booking = models.ForeignKey(BookingRequest, on_delete=models.CASCADE)
    complaint_text = models.TextField()
    date_submitted = models.DateField(default=timezone.now)
    resolved = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Complaint by {self.booking.customer_name}"


class Expense(models.Model):
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - ${self.amount}"


class SystemSetup(models.Model):
    company_name = models.CharField(max_length=255)
    support_email = models.EmailField()
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
