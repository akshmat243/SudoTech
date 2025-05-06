from rest_framework import serializers
from .models import WhereByMeeting

class WhereByMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhereByMeeting
        fields = '__all__'
