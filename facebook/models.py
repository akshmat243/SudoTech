from django.db import models
from django.utils import timezone


class FacebookInteraction(models.Model):
    TYPE_CHOICES = [
        ('post', 'Post'),
        ('message', 'Message'),
        ('comment', 'Comment'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    sender_name = models.CharField(max_length=255)
    content = models.TextField()
    facebook_id = models.CharField(max_length=100, unique=True, help_text="Facebook post/message/comment ID")
    created_at = models.DateTimeField(default=timezone.now)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type.capitalize()} from {self.sender_name} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class FacebookPost(models.Model):
    post_id = models.CharField(max_length=100, unique=True, help_text="Facebook post ID")
    page_name = models.CharField(max_length=255, help_text="Name of the Facebook page")
    message = models.TextField(help_text="Text content of the post")
    link = models.URLField(blank=True, help_text="Optional link shared in the post")
    image_url = models.URLField(blank=True, help_text="Optional image URL")
    created_at = models.DateTimeField(default=timezone.now)
    scheduled = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.page_name}: {self.message[:50]}"
