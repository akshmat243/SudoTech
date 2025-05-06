from django.db import models
from django.utils import timezone


class InstagramInteraction(models.Model):
    TYPE_CHOICES = [
        ('dm', 'Direct Message'),
        ('comment', 'Comment'),
        ('mention', 'Mention'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    username = models.CharField(max_length=255, help_text="Instagram username")
    content = models.TextField()
    instagram_id = models.CharField(max_length=100, unique=True, help_text="Instagram post/comment/message ID")
    created_at = models.DateTimeField(default=timezone.now)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type.capitalize()} from @{self.username} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class InstagramPost(models.Model):
    post_id = models.CharField(max_length=100, unique=True, help_text="Instagram post ID")
    username = models.CharField(max_length=255, help_text="Instagram account username")
    caption = models.TextField(blank=True, help_text="Text caption of the post")
    image_url = models.URLField(blank=True, help_text="Direct link to the image or video")
    post_type = models.CharField(
        max_length=20,
        choices=[('image', 'Image'), ('video', 'Video'), ('reel', 'Reel'), ('carousel', 'Carousel')],
        default='image'
    )
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return f"@{self.username} - {self.caption[:40]}"