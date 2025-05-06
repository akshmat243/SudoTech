from rest_framework import serializers
from .models import RoadMap, Idea


class RoadMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMap
        fields = '__all__'


class IdeaSerializer(serializers.ModelSerializer):
    roadmap = RoadMapSerializer(read_only=True)

    class Meta:
        model = Idea
        fields = '__all__'
