from rest_framework import serializers
from .models import CustomField


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomField
        fields = '__all__'
