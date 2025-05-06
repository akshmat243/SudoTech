from rest_framework import serializers
from .models import VehicleSeller, VehicleBuyer, Vehicle, VehicleTrade, PreviousServiceHistory, VehicleSpecification, VehicleCondition, VehicleHistory, VehicleInsuranceHistory, Document, VehicleReport, ExpertInspection, VehicleSetup


class VehicleSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSeller
        fields = ('id', 'name', 'contact', 'email', 'created_at', 'updated_at')


class VehicleBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBuyer
        fields = ('id', 'name', 'contact', 'email', 'created_at', 'updated_at')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'plate_number', 'model', 'manufacturer', 'year', 'color', 'created_at', 'updated_at')


class VehicleTradeSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    seller = VehicleSellerSerializer()
    buyer = VehicleBuyerSerializer()

    class Meta:
        model = VehicleTrade
        fields = ('id', 'vehicle', 'seller', 'buyer', 'trade_date', 'price', 'updated_at')


class PreviousServiceHistorySerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = PreviousServiceHistory
        fields = ('id', 'vehicle', 'service_date', 'description', 'service_center', 'created_at', 'updated_at')


class VehicleSpecificationSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleSpecification
        fields = ('id', 'vehicle', 'key', 'value', 'created_at', 'updated_at')


class VehicleConditionSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleCondition
        fields = ('id', 'vehicle', 'condition', 'reported_on', 'created_at', 'updated_at')


class VehicleHistorySerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleHistory
        fields = ('id', 'vehicle', 'description', 'date_recorded', 'created_at', 'updated_at')


class VehicleInsuranceHistorySerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleInsuranceHistory
        fields = ('id', 'vehicle', 'provider', 'policy_number', 'valid_from', 'valid_to', 'created_at', 'updated_at')


class DocumentSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Document
        fields = ('id', 'vehicle', 'name', 'file', 'uploaded_at', 'updated_at')


class VehicleReportSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = VehicleReport
        fields = ('id', 'vehicle', 'report', 'created_at', 'updated_at')


class ExpertInspectionSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = ExpertInspection
        fields = ('id', 'vehicle', 'expert_name', 'inspection_date', 'findings', 'created_at', 'updated_at')


class VehicleSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSetup
        fields = ('id', 'key', 'value', 'created_at', 'updated_at')
