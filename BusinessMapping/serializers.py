from rest_framework import serializers
from .models import BusinessMapping


class BusinessMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessMapping
        fields = '__all__'
