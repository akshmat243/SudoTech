from django.db import models
from django.utils import timezone

class Membership(models.Model):
    name = models.CharField(max_length=100)
    duration_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    client_name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    staff = models.CharField(max_length=100)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client_name} - {self.service} at {self.date_time}"

class BookingOrder(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.booking.client_name} - {self.item_name}"

class BeautyReceipt(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(default=timezone.now)
    payment_method = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Receipt #{self.id} - {self.booking.client_name}"

class Training(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    trainer = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    staff_name = models.CharField(max_length=100)
    certificate_name = models.CharField(max_length=100)
    date_issued = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.staff_name} - {self.certificate_name}"

class GiftCard(models.Model):
    code = models.CharField(max_length=20, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    is_redeemed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

class Resource(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BookingReminder(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reminder for {self.booking.client_name}"

class LoyaltyProgram(models.Model):
    client_name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.points} points"

class BeautySpaSystemSetup(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
