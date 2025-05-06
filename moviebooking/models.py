from django.db import models
from django.utils import timezone


class MovieCast(models.Model):
    movie_title = models.CharField(max_length=255)
    cast_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cast_name} in {self.movie_title}"


class SeatingLayout(models.Model):
    theater_name = models.CharField(max_length=255)
    total_seats = models.PositiveIntegerField()
    rows = models.PositiveIntegerField()
    columns = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.theater_name} Layout"


class MovieShow(models.Model):
    movie_title = models.CharField(max_length=255)
    show_time = models.DateTimeField()
    theater = models.ForeignKey(SeatingLayout, on_delete=models.CASCADE)
    price_per_seat = models.DecimalField(max_digits=8, decimal_places=2)
    available_seats = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie_title} at {self.show_time.strftime('%Y-%m-%d %H:%M')}"


class MovieOrder(models.Model):
    customer_name = models.CharField(max_length=255)
    show = models.ForeignKey(MovieShow, on_delete=models.CASCADE)
    seats_booked = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.show}"


class FoodOrder(models.Model):
    movie_order = models.ForeignKey(MovieOrder, on_delete=models.CASCADE, related_name="food_orders")
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} x{self.quantity} for {self.movie_order.customer_name}"


class BookingHistory(models.Model):
    customer_name = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    show_time = models.DateTimeField()
    seats = models.PositiveIntegerField()
    booked_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} booked {self.movie_title}"


class SystemSetup(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
