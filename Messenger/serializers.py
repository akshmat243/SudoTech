from rest_framework import serializers
from .models import Messenger

class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        fields = '__all__'
