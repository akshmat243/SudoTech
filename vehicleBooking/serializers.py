from rest_framework import serializers
from .models import VehicleBooking, FuelLog, Incident, MaintenanceRecord, VehicleContract, EmergencyContact, Route
from vehicleTrade.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'plate_number', 'model', 'make', 'year', 'color', 'vin', 'created_at', 'updated_at')


class VehicleBookingSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleBooking
        fields = ('id', 'vehicle', 'booked_by', 'start_datetime', 'end_datetime', 'purpose', 'created_at', 'updated_at')


class FuelLogSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = FuelLog
        fields = ('id', 'vehicle', 'date', 'liters', 'cost', 'odometer', 'created_at', 'updated_at')


class IncidentSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Incident
        fields = ('id', 'vehicle', 'reported_by', 'date', 'description', 'resolved', 'created_at', 'updated_at')


class MaintenanceRecordSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = MaintenanceRecord
        fields = ('id', 'vehicle', 'date', 'description', 'cost', 'performed_by', 'created_at', 'updated_at')


class VehicleContractSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleContract
        fields = ('id', 'vehicle', 'contract_number', 'start_date', 'end_date', 'terms', 'created_at', 'updated_at')


class EmergencyContactSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = EmergencyContact
        fields = ('id', 'vehicle', 'name', 'phone', 'relationship', 'created_at', 'updated_at')


class RouteSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Route
        fields = ('id', 'vehicle', 'origin', 'destination', 'distance_km', 'estimated_time', 'created_at', 'updated_at')
