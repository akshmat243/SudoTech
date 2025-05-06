from django.db import models
from django.utils import timezone


class YouTubeChannel(models.Model):
    channel_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class YouTubePlaylist(models.Model):
    playlist_id = models.CharField(max_length=100, unique=True)
    channel = models.ForeignKey(YouTubeChannel, on_delete=models.CASCADE, related_name='playlists')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class YouTubeVideo(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    playlist = models.ForeignKey(YouTubePlaylist, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    channel = models.ForeignKey(YouTubeChannel, on_delete=models.CASCADE, related_name='videos')
    published_at = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return self.title


class YouTubeActivity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('upload', 'Upload'),
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('subscribe', 'Subscribe'),
        ('share', 'Share'),
    ]

    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE_CHOICES)
    video = models.ForeignKey(YouTubeVideo, on_delete=models.SET_NULL, null=True, blank=True)
    channel = models.ForeignKey(YouTubeChannel, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    occurred_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.activity_type.capitalize()} - {self.channel.name}"
