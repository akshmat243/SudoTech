from rest_framework import serializers
from .models import LivestormMeeting

class LivestormMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestormMeeting
        fields = '__all__'
