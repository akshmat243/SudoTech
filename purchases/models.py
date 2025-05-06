from django.db import models

class Purchase(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('business', 'Business'),
    ]

    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('partialypaid', 'partialy Paid'),
        ('draft', 'Draft'),
    ]

    purchase_id = models.CharField(max_length=20, unique=True, editable=False)
    vendor = models.CharField(max_length=255)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    category = models.CharField(max_length=100)
    purchase_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.purchase_id:
            last = Purchase.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.purchase_id = f"#PUR{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.purchase_id


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WarehouseTransfer(models.Model):
    from_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='transfers_out')
    to_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='transfers_in')
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} from {self.from_warehouse.name} to {self.to_warehouse.name}"