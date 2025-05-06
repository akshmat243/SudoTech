from django.db import models

class WhereByMeeting(models.Model):
    ROOM_MODE_CHOICES = [
        ('normal', 'Normal'),
        ('locked', 'Locked'),
    ]

    room_name_prefix = models.CharField(max_length=100)
    invites = models.CharField(max_length=255, help_text="Comma-separated list of invitees")
    room_mode = models.CharField(max_length=100, choices=ROOM_MODE_CHOICES, default='normal')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('active', 'Active'), ('ended', 'Ended')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Whereby Meeting: {self.room_name_prefix} on {self.date}"
