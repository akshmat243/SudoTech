from rest_framework import serializers
from .models import FormEntry


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormEntry
        fields = '__all__'
