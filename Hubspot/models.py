from django.db import models

class HubSpotTicket(models.Model):
    TICKET_PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    TICKET_STAGE_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    TICKET_STATUS_CHOICES = [
        ('open', 'Open'),
        ('pending', 'Pending'),
        ('waiting_on_customer', 'Waiting on Customer'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    ticket_id = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=255)
    priority = models.CharField(max_length=20, choices=TICKET_PRIORITY_CHOICES, default='medium')
    owner = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    stage = models.CharField(max_length=20, choices=TICKET_STAGE_CHOICES, default='new')
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='open')
    description = models.TextField()

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.subject}"
