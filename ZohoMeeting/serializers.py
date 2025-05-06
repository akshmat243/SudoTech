from rest_framework import serializers
from .models import ZohoMeeting

class ZohoMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZohoMeeting
        fields = '__all__'
