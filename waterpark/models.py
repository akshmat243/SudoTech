from django.db import models
from django.utils import timezone


class RideManagement(models.Model):
    ride_name = models.CharField(max_length=255)
    ride_type = models.CharField(max_length=100, choices=[('rollercoaster', 'Rollercoaster'), ('water_slide', 'Water Slide'), ('carousel', 'Carousel'), ('ferris_wheel', 'Ferris Wheel')])
    max_capacity = models.PositiveIntegerField()
    operational_status = models.BooleanField(default=True)  # True = Open, False = Closed
    location = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ride_name


class Maintenance(models.Model):
    ride = models.ForeignKey(RideManagement, on_delete=models.CASCADE, related_name="maintenance")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    maintenance_type = models.CharField(max_length=255)
    description = models.TextField()
    maintenance_status = models.CharField(max_length=100, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed')], default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ride.ride_name} Maintenance"


class SeasonalPromotion(models.Model):
    promotion_code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(help_text="Discount in %")
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.promotion_code


class EventManagement(models.Model):
    event_name = models.CharField(max_length=255)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    tickets_available = models.PositiveIntegerField()
    price_per_ticket = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name


class ClothingSales(models.Model):
    item_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('t-shirt', 'T-Shirt'), ('hat', 'Hat'), ('towel', 'Towel'), ('sunglasses', 'Sunglasses')])
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name


class WaterParkBooking(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    number_of_tickets = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(default=timezone.now)
    seasonal_promotion = models.ForeignKey(SeasonalPromotion, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.number_of_tickets} Tickets"


class SystemSetup(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
