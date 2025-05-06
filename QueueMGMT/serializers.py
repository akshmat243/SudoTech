from rest_framework import serializers
from .models import Service, Counter, Call, Report

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class CounterSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = Counter
        fields = '__all__'


class CallSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    counter = CounterSerializer()

    class Meta:
        model = Call
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = Report
        fields = '__all__'
