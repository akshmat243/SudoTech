from rest_framework import serializers
from .models import GoogleLead


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleLead
        fields = '__all__'
