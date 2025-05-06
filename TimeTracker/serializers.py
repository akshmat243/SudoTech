from rest_framework import serializers
from .models import Timetracker

class TimetrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetracker
        fields = '__all__'
