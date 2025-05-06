from rest_framework import serializers
from .models import GoToMeeting
from UserMGMT.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class GoToMeetingSerializer(serializers.ModelSerializer):
    invitees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = GoToMeeting
        fields = '__all__'
