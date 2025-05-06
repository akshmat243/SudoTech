from django.db import models
from django.utils import timezone


class ZulipMessage(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('stream', 'Stream'),
        ('private', 'Private'),
    ]

    message_id = models.CharField(max_length=100, unique=True, help_text="Zulip message ID")
    sender_email = models.EmailField(help_text="Email of the message sender")
    recipient = models.CharField(max_length=255, help_text="Stream name or recipient email")
    topic = models.CharField(max_length=255, blank=True, help_text="Topic for stream messages")
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPE_CHOICES)
    content = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender_email} to {self.recipient} ({self.message_type})"
