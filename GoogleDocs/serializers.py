from rest_framework import serializers
from .models import GoogleDoc


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleDoc
        fields = '__all__'
