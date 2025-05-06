from django.db import models
from django.utils import timezone


class Membership(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    membership_start_date = models.DateTimeField(default=timezone.now)
    membership_end_date = models.DateTimeField()
    plan = models.ForeignKey("MembershipPlan", on_delete=models.CASCADE, related_name="memberships")
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} ({self.plan.name})"


class MembershipPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_per_month = models.DecimalField(max_digits=8, decimal_places=2)
    duration_months = models.PositiveIntegerField(help_text="Duration in months")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(Membership, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_status = models.CharField(max_length=50, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed')
    space_booked = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.customer_name} - {self.space_booked} ({self.start_time.strftime('%Y-%m-%d %H:%M')})"


class Amenity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_per_use = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ResponseSetup(models.Model):
    question = models.CharField(max_length=255)
    response_type = models.CharField(max_length=50, choices=[('text', 'Text'), ('select', 'Select'), ('boolean', 'Boolean')], default='text')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class CoworkingSpaceSetup(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
