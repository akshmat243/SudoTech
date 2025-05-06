from django.db import models

class Retainer(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('business', 'Business'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('paid', 'Paid'),
        ('accepted', 'Accepted'),
    ]

    retainer_id = models.CharField(max_length=20, unique=True, editable=False)
    customer = models.CharField(max_length=255)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    issue_date = models.DateField()
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.retainer_id:
            last = Retainer.objects.order_by('id').last()
            next_id = last.id + 1 if last else 1
            self.retainer_id = f"#RETAINER{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.retainer_id
