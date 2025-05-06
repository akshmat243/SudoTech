from rest_framework import serializers
from .models import ActivityLog
from UserMGMT.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ActivityLogSerializer(serializers.ModelSerializer):
    staff = UserSerializer(read_only=True)

    class Meta:
        model = ActivityLog
        fields = '__all__'
