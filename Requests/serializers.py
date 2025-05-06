from rest_framework import serializers
from .models import Request, RequestSystemSetup

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class RequestSystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestSystemSetup
        fields = '__all__'
