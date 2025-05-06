from django.db import models
from UserMGMT.models import User

# Create your models here.
class ActivityLog(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('upload', 'Upload'),
        ('edit', 'Edit'),
        ('share', 'Share'),
    ]

    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE_CHOICES)
    module = models.CharField(max_length=50)
    sub_module = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"created by - {self.staff}"