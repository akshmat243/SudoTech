from django.db import models

class RoadMap(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=[
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='planned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Idea(models.Model):
    roadmap = models.ForeignKey(RoadMap, on_delete=models.CASCADE, related_name='ideas')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    submitted_by = models.CharField(max_length=255, blank=True, null=True)
    submission_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=[
        ('new', 'New'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='new')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
