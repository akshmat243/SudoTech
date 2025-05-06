from django.db import models
from UserMGMT.models import User

class Project(models.Model):
    STAGE_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('onhold', 'OnHold'),
        ('finished', 'Finished'),
    ]

    name = models.CharField(max_length=255)
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_project')
    updated_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProjectTemplate(models.Model):
    name = models.CharField(max_length=255)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectReport(models.Model):
    STAGE_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('onhold', 'OnHold'),
        ('finished', 'Finished'),
    ]

    name = models.CharField(max_length=255)
    start_date = models.DateField()
    due_date = models.DateField()
    project_members = models.ForeignKey(User, on_delete=models.CASCADE)
    progress = models.PositiveIntegerField(help_text="Enter progress as a percentage (0–100)")
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name