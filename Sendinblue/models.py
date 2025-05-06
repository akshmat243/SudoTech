from django.db import models
from django.contrib.auth.models import User

class SendinblueMail(models.Model):
    subject = models.CharField(max_length=255)
    sender_email = models.EmailField()
    recipient_email = models.EmailField()
    content = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
        ('Failed', 'Failed')
    ], default='Pending')
    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mail from {self.sender_email} to {self.recipient_email} - {self.status}"


class SendinblueTemplate(models.Model):
    name = models.CharField(max_length=255)
    template_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SendinblueContact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
