from rest_framework import serializers
from .models import UpcomingChallenge, NewCreativity, InnovationSystemSetup


class UpcomingChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingChallenge
        fields = '__all__'


class NewCreativitySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCreativity
        fields = '__all__'
        read_only_fields = ['submitted_on']


class InnovationSystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InnovationSystemSetup
        fields = '__all__'
