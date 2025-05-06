from django.db import models
from purchases.models import Warehouse

class Quotation(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('business', 'Business'),
    ]

    QUOTATION_TYPE_CHOICES = [
        ('pos', 'Pos'),
        ('invoice', 'Invoice'),
    ]

    quotation_id = models.CharField(max_length=20, unique=True, editable=False)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    customer = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quotation_type = models.CharField(max_length=20, choices=QUOTATION_TYPE_CHOICES)
    quotation_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.quotation_id:
            last = Quotation.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.quotation_id = f"#QUO{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.quotation_id
