from rest_framework import serializers
from .models import Channel, Category, Video, Playlist, ViewerActivity
from UserMGMT.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ChannelSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Channel
        fields = ('id', 'name', 'description', 'created_by', 'created_on', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategorySerializer()

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file', 'thumbnail', 'channel', 'category', 'upload_date', 'is_published', 'updated_at')


class PlaylistSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    videos = VideoSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('id', 'title', 'videos', 'created_by', 'created_on', 'updated_at')


class ViewerActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    video = VideoSerializer()

    class Meta:
        model = ViewerActivity
        fields = ('id', 'user', 'video', 'watched_on', 'liked', 'updated_at')
