from django.db import models

class Invoice(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('business', 'Business'),
    ]

    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('draft', 'Draft'),
    ]

    invoice_id = models.CharField(max_length=20, unique=True, editable=False)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpaid')
    updated_at =models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            last = Invoice.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.invoice_id = f"#INV{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_id
