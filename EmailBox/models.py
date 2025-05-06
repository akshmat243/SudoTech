from django.db import models
from UserMGMT.models import User

class EmailBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="email_boxes")
    inbox_count = models.PositiveIntegerField(default=0)
    sent_count = models.PositiveIntegerField(default=0)
    draft_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"EmailBox for {self.user.username}"


class Email(models.Model):
    email_box = models.ForeignKey(EmailBox, on_delete=models.CASCADE, related_name="emails")
    sender = models.EmailField()
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Draft', 'Draft'),
        ('Sent', 'Sent'),
        ('Received', 'Received'),
        ('Failed', 'Failed')
    ], default='Draft')
    
    def __str__(self):
        return f"Email from {self.sender} to {self.recipient} - {self.status}"


class EmailHistory(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    previous_status = models.CharField(max_length=50)
    new_status = models.CharField(max_length=50)
    changed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"History for Email {self.email.id} changed at {self.changed_at}"
