from rest_framework import serializers
from .models import Vehicle, ComplianceRegulation, InspectionRequest, InspectionList, InspectionSchedule, InspectionReminder, InspectionHistory


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'registration_number', 'model', 'manufacturer', 'year', 'owner_name', 'created_at', 'updated_at']


class ComplianceRegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceRegulation
        fields = ['id', 'title', 'description', 'effective_date', 'created_at', 'updated_at']


class InspectionRequestSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = InspectionRequest
        fields = ['id', 'vehicle', 'reason', 'request_date', 'is_approved', 'updated_at']


class InspectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionList
        fields = ['id', 'title', 'checklist_items', 'created_at', 'updated_at']


class InspectionScheduleSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = InspectionSchedule
        fields = ['id', 'vehicle', 'inspection_date', 'assigned_inspector', 'created_at', 'updated_at']


class InspectionReminderSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = InspectionReminder
        fields = ['id', 'vehicle', 'reminder_date', 'message', 'created_at', 'updated_at']


class InspectionHistorySerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(read_only=True)

    class Meta:
        model = InspectionHistory
        fields = ['id', 'vehicle', 'inspection_date', 'findings', 'passed', 'inspector_name', 'created_at', 'updated_at']
