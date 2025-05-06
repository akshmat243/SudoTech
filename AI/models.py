from django.db import models
from django.utils import timezone

class AI(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AIDocument(models.Model):
    ai = models.ForeignKey(AI, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=200)
    content = models.TextField()
    uploaded_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AIImage(models.Model):
    ai = models.ForeignKey(AI, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ai_images/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class History(models.Model):
    ai = models.ForeignKey(AI, on_delete=models.CASCADE, related_name='history')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ai.name} - {self.action} at {self.timestamp}"
