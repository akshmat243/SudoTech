from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.location}"


class TourBooking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_people = models.PositiveIntegerField()
    booking_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking for {self.customer_name} - {self.tour.name}"


class TouristInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    inquiry_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inquiry from {self.name}"


class Guide(models.Model):
    name = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    experience_years = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount_percentage = models.FloatField()
    valid_from = models.DateField()
    valid_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TravelInsurance(models.Model):
    provider = models.CharField(max_length=255)
    coverage_details = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.provider


class SystemSetup(models.Model):
    setting_name = models.CharField(max_length=255)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_name
