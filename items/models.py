import uuid
from django.db import models

def generate_sku():
    return f"BC{uuid.uuid4().hex[:6].upper()}"

class Items(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('physical', 'Physical'),
        ('digital', 'Digital'),
        ('service', 'Service'),
    ]

    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True, default=generate_sku)
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2, help_text="Tax %")
    category = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, help_text="e.g. pcs, kg, liter")
    quantity = models.PositiveIntegerField()
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)


    def __str__(self):
        return self.name
