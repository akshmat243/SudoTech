from rest_framework import serializers
from .models import MeetingType, Meeting, MeetingMinutes, MeetingReport
from UserMGMT.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MeetingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingType
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    meeting_type = MeetingTypeSerializer()
    attendees = UserSerializer(many=True)

    class Meta:
        model = Meeting
        fields = '__all__'


class MeetingMinutesSerializer(serializers.ModelSerializer):
    meeting = MeetingSerializer()

    class Meta:
        model = MeetingMinutes
        fields = '__all__'


class MeetingReportSerializer(serializers.ModelSerializer):
    meeting = MeetingSerializer()

    class Meta:
        model = MeetingReport
        fields = '__all__'
