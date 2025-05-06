from rest_framework import serializers
from .models import InstagramInteraction, InstagramPost


class InstagramInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramInteraction
        fields = '__all__'
        read_only_fields = ['received_at']


class InstagramPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramPost
        fields = '__all__'
