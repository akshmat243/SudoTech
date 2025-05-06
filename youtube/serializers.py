from rest_framework import serializers
from .models import YouTubeChannel, YouTubePlaylist, YouTubeVideo, YouTubeActivity


class YouTubeChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeChannel
        fields = ['id', 'channel_id', 'name', 'description', 'created_at']


class YouTubePlaylistSerializer(serializers.ModelSerializer):
    channel = YouTubeChannelSerializer(read_only=True)

    class Meta:
        model = YouTubePlaylist
        fields = ['id', 'playlist_id', 'channel', 'title', 'description', 'created_at']


class YouTubeVideoSerializer(serializers.ModelSerializer):
    playlist = YouTubePlaylistSerializer(read_only=True)
    channel = YouTubeChannelSerializer(read_only=True)

    class Meta:
        model = YouTubeVideo
        fields = ['id', 'video_id', 'title', 'description', 'playlist', 'channel', 'published_at', 'url']


class YouTubeActivitySerializer(serializers.ModelSerializer):
    video = YouTubeVideoSerializer(read_only=True)
    channel = YouTubeChannelSerializer(read_only=True)

    class Meta:
        model = YouTubeActivity
        fields = ['id', 'activity_type', 'video', 'channel', 'description', 'occurred_at', 'created_at', 'updated_at']
