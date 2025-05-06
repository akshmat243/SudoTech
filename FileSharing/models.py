from django.db import models
from UserMGMT.models import User

class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='shared_files/')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_trashed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTION_CHOICES = [
        ('upload', 'Upload'),
        ('download', 'Download'),
        ('delete', 'Delete'),
        ('verify', 'Verify'),
    ]
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.file.name}"


class Trash(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE)
    trashed_at = models.DateTimeField(auto_now_add=True)
    trashed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.file.name


class FileVerification(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE)
    verifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='verified_files')
    verified_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.file.name} verified by {self.verifier}"
