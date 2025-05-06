from rest_framework import serializers
from .models import SideMenuBuilder

class SideMenuBuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideMenuBuilder
        fields = '__all__'
