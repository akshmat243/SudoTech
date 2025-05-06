from rest_framework import serializers
from .models import CollectionRequest, Trip, Inspection, CollectionSchedule, DisposalFacility, Recycling, SystemSetup


class CollectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionRequest
        fields = ['id', 'customer_name', 'address', 'collection_date', 'status', 'request_date', 'created_at', 'updated_at']


class TripSerializer(serializers.ModelSerializer):
    collection_request = CollectionRequestSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'collection_request', 'driver_name', 'vehicle_number', 'start_time', 'end_time', 'status', 'created_at', 'updated_at']


class InspectionSerializer(serializers.ModelSerializer):
    trip = TripSerializer(read_only=True)

    class Meta:
        model = Inspection
        fields = ['id', 'trip', 'inspector_name', 'inspection_date', 'findings', 'status', 'created_at', 'updated_at']


class CollectionScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionSchedule
        fields = ['id', 'day_of_week', 'start_time', 'end_time', 'assigned_driver', 'created_at', 'updated_at']


class DisposalFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DisposalFacility
        fields = ['id', 'name', 'location', 'capacity', 'contact_info', 'created_at', 'updated_at']


class RecyclingSerializer(serializers.ModelSerializer):
    recycling_center = DisposalFacilitySerializer(read_only=True)

    class Meta:
        model = Recycling
        fields = ['id', 'material_type', 'quantity_collected', 'collection_date', 'recycling_center', 'created_at', 'updated_at']


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = ['id', 'system_name', 'configuration_details', 'setup_date']
