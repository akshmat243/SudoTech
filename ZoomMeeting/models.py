from django.db import models
from UserMGMT.models import User

class ZoomMeeting(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('waiting', 'Waiting'),
    ]

    title = models.CharField(max_length=100)
    invites = models.ManyToManyField(User, related_name='zoom_meeting_invites') 
    name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField(help_text="Duration in minutes")
    url = models.URLField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.date})"
