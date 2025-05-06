from django.db import models

class LivestormMeeting(models.Model):
    no = models.IntegerField()
    owner_name = models.CharField(max_length=100)
    invites = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    session_count = models.IntegerField()
    scheduling_status = models.CharField(
        max_length=100,
        choices=[
            ('ended', 'Ended'),
            ('not scheduled', 'Not Scheduled'),
            ('not started', 'Not Started')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.owner_name}"
