from django.db import models

class FreightCustomer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FreightBooking(models.Model):
    customer = models.ForeignKey(FreightCustomer, on_delete=models.CASCADE)
    booking_date = models.DateField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    cargo_description = models.TextField()
    weight_kg = models.DecimalField(max_digits=10, decimal_places=2)
    volume_cbm = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("In Transit", "In Transit"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ], default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer.name}"


class FreightShipping(models.Model):
    booking = models.ForeignKey(FreightBooking, on_delete=models.CASCADE)
    vessel_name = models.CharField(max_length=255)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    container_number = models.CharField(max_length=100)
    tracking_status = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shipping for {self.booking}"


class FreightInvoice(models.Model):
    booking = models.ForeignKey(FreightBooking, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100, unique=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number


class FreightSystemSetup(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
