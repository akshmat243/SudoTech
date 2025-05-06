from django.db import models
from django.utils import timezone


class WhatsAppMessage(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('delivered', 'Delivered'),
        ('read', 'Read'),
    ]

    recipient_number = models.CharField(max_length=20)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    external_id = models.CharField(max_length=100, blank=True, help_text="ID from WhatsApp API, if available")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"To: {self.recipient_number} | Status: {self.status}"
