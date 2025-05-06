from rest_framework import serializers
from .models import ZoomMeeting
from UserMGMT.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ZoomMeetingSerializer(serializers.ModelSerializer):
    invites = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ZoomMeeting
        fields = '__all__'
