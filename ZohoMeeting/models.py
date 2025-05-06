from django.db import models

class ZohoMeeting(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('waiting', 'Waiting'),
    ]

    title = models.CharField(max_length=100)
    invites = models.CharField(max_length=255, help_text="Comma-separated invitee emails or names")
    date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    url = models.URLField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.date}"
