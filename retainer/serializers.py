from rest_framework import serializers
from .models import Retainer


class RetainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retainer
        fields = '__all__'
