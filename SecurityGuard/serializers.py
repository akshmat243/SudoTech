from rest_framework import serializers
from .models import SecurityGuard, SecurityRequest, GuardBooking, Payment, IncidentReport, EquipmentTracking, SystemSetup


class SecurityGuardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityGuard
        fields = '__all__'


class SecurityRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityRequest
        fields = '__all__'


class GuardBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardBooking
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class IncidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentReport
        fields = '__all__'


class EquipmentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTracking
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
