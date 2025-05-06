from rest_framework import serializers
from .models import Driver, Customer, Vehicle, LogBook, Booking, Availability, Insurance, Maintenance, FuelHistory, Report, SystemSetup


class DriverSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Driver
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Customer
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)  # Nested Driver serializer
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Vehicle
        fields = '__all__'


class LogBookSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = LogBook
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)  # Nested Customer serializer
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    driver = DriverSerializer(read_only=True)  # Nested Driver serializer
    start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Booking
        fields = '__all__'


class AvailabilitySerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    available_from = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    available_to = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Availability
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    valid_from = serializers.DateField(format="%Y-%m-%d")
    valid_to = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Insurance
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Maintenance
        fields = '__all__'


class FuelHistorySerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)  # Nested Vehicle serializer
    date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FuelHistory
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Report
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SystemSetup
        fields = '__all__'
