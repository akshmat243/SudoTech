from rest_framework import serializers
from .models import Vehicle, Service, JobCard, Item, Warranty, SystemSetup


class VehicleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Vehicle
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Service
        fields = '__all__'


class JobCardSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    service = ServiceSerializer(many=True, read_only=True)  # Nested Service serializer
    job_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = JobCard
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    jobcard = JobCardSerializer(read_only=True)  # Nested JobCard serializer
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Item
        fields = '__all__'


class WarrantySerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    start_date = serializers.DateField(format="%Y-%m-%d")
    end_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Warranty
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SystemSetup
        fields = '__all__'
