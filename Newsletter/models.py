from django.db import models
from UserMGMT.models import User

class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Mail(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    recipient_email = models.EmailField()
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Sent', 'Sent'),
        ('Failed', 'Failed')
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.recipient_email} - {self.status}"


class MailHistory(models.Model):
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)
    status_changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    previous_status = models.CharField(max_length=50)
    new_status = models.CharField(max_length=50)
    changed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mail {self.mail.id} status changed at {self.changed_at}"
