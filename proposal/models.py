from django.db import models

class Proposal(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('savings', 'Savings'),
        ('current', 'Current'),
        ('business', 'Business'),
    ]

    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('draft', 'Draft'),
        ('declined', 'Declined'),
        ('close', 'Close'),
        ('open', 'Open'),
    ]

    proposal = models.CharField(max_length=255, unique=True, editable=False)
    customer = models.CharField(max_length=255)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    issue_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    updated_at =models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.proposal:
            last_id = Proposal.objects.all().order_by('id').last()
            next_id = last_id.id + 1 if last_id else 1
            self.proposal = f"#PROP{str(next_id).zfill(6)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Proposal #{self.id} - {self.customer}"
