from django.db import models

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('meeting', 'Meeting'),
        ('appointment', 'Appointment'),
        ('reminder', 'Reminder'),
        ('holiday', 'Holiday'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='other')
    location = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_time']
