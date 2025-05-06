from rest_framework import serializers
from .models import GardenBed, Plant, WateringSchedule, MaintenanceLog, SeasonalPlan, PestAndDisease


class GardenBedSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = GardenBed
        fields = '__all__'


class PlantSerializer(serializers.ModelSerializer):
    bed = GardenBedSerializer(read_only=True)  # Nested GardenBed serializer
    planted_on = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Plant
        fields = '__all__'


class WateringScheduleSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)  # Nested Plant serializer
    last_watered = serializers.DateField(format="%Y-%m-%d")
    next_due = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = WateringSchedule
        fields = '__all__'


class MaintenanceLogSerializer(serializers.ModelSerializer):
    bed = GardenBedSerializer(read_only=True)  # Nested GardenBed serializer
    performed_on = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = MaintenanceLog
        fields = '__all__'


class SeasonalPlanSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SeasonalPlan
        fields = '__all__'


class PestAndDiseaseSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)  # Nested Plant serializer
    date_detected = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = PestAndDisease
        fields = '__all__'
