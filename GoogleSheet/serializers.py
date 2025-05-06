from rest_framework import serializers
from .models import GoogleSheet


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleSheet
        fields = '__all__'
