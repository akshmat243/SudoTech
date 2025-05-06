from rest_framework import serializers
from .models import ZulipMessage


class ZulipMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZulipMessage
        fields = '__all__'
