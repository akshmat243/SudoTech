from django.db import models

class BusinessMapping(models.Model):
    no = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    related = models.CharField(max_length=255, blank=True, null=True)
    related_to = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.no} - {self.title}"
