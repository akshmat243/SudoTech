from django.db import models

class ZohoMeeting(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('waiting', 'Waiting'),
    ]

    title = models.CharField(max_length=100)
    invites = models.CharField(max_length=255, help_text="Comma-separated list of invitee emails or names")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField(help_text="Duration in minutes")
    url = models.URLField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.date}"
