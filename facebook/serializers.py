from rest_framework import serializers
from .models import FacebookInteraction, FacebookPost


class FacebookInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookInteraction
        fields = '__all__'


class FacebookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookPost
        fields = '__all__'
