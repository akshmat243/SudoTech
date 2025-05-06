from rest_framework import serializers
from .models import GoogleMeet
from UserMGMT.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class GoogleMeetSerializer(serializers.ModelSerializer):
    invitees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = GoogleMeet
        fields = '__all__'
