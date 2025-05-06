from django.db import models
from django.utils import timezone
from UserMGMT.models import User 

class GoogleMeet(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    invitees = models.ManyToManyField(User, related_name='meet_invites')
    meeting_datetime = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    url = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
