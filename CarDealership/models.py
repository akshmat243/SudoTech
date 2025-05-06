from django.db import models
from django.utils import timezone


class DealershipProduct(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.brand}"


class CarInventory(models.Model):
    product = models.ForeignKey(DealershipProduct, on_delete=models.CASCADE)
    vin = models.CharField(max_length=100, unique=True)  # Vehicle Identification Number
    color = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vin} - {self.product.name}"


class CarPurchase(models.Model):
    buyer_name = models.CharField(max_length=100)
    inventory = models.ForeignKey(CarInventory, on_delete=models.CASCADE)
    purchase_date = models.DateField(default=timezone.now)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Purchase by {self.buyer_name} - {self.inventory.vin}"


class SalesManagement(models.Model):
    salesperson = models.CharField(max_length=100)
    sale = models.ForeignKey(CarPurchase, on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sales - {self.sale.inventory.vin} by {self.salesperson}"


class Service(models.Model):
    car = models.ForeignKey(CarInventory, on_delete=models.CASCADE)
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service on {self.car.vin} - {self.service_date}"


class TestDrive(models.Model):
    car = models.ForeignKey(CarInventory, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    feedback = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} test drive - {self.car.vin}"


class Warranty(models.Model):
    car = models.ForeignKey(CarInventory, on_delete=models.CASCADE)
    warranty_provider = models.CharField(max_length=100)
    warranty_start = models.DateField()
    warranty_end = models.DateField()
    coverage_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Warranty for {self.car.vin}"


class Insurance(models.Model):
    car = models.ForeignKey(CarInventory, on_delete=models.CASCADE)
    insurance_company = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    insured_from = models.DateField()
    insured_to = models.DateField()
    premium_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Insurance - {self.car.vin}"
