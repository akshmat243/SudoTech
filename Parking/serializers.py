from rest_framework import serializers
from .models import Parking, Payment, SystemSetup


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    parking_location = serializers.CharField(source='parking.location', read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
