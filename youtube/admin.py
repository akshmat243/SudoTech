from django.contrib import admin
from .models import YouTubeChannel, YouTubePlaylist, YouTubeVideo, YouTubeActivity


@admin.register(YouTubeChannel)
class YouTubeChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "channel_id", "created_at")
    search_fields = ("name", "channel_id")


@admin.register(YouTubePlaylist)
class YouTubePlaylistAdmin(admin.ModelAdmin):
    list_display = ("title", "playlist_id", "channel", "created_at")
    search_fields = ("title", "playlist_id")
    list_filter = ("channel",)


@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "video_id", "channel", "published_at")
    search_fields = ("title", "video_id")
    list_filter = ("channel", "playlist")


@admin.register(YouTubeActivity)
class YouTubeActivityAdmin(admin.ModelAdmin):
    list_display = ("activity_type", "channel", "video", "occurred_at")
    list_filter = ("activity_type", "channel")
    search_fields = ("description",)
