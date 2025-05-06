from rest_framework import serializers
from .models import (
    RideManagement, Maintenance, SeasonalPromotion,
    EventManagement, ClothingSales, WaterParkBooking, SystemSetup
)


class RideManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideManagement
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    ride = RideManagementSerializer()

    class Meta:
        model = Maintenance
        fields = '__all__'


class SeasonalPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalPromotion
        fields = '__all__'


class EventManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventManagement
        fields = '__all__'


class ClothingSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingSales
        fields = '__all__'


class WaterParkBookingSerializer(serializers.ModelSerializer):
    seasonal_promotion = SeasonalPromotionSerializer()

    class Meta:
        model = WaterParkBooking
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
