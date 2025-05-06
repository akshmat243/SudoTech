from rest_framework import serializers
from .models import PropertyManage, Property, Unit, Listing, Tenant, Invoice, MaintenanceRequest, DocumentType, TenantRequest, ExpenseTracking, Inspection, TenantCommunication, Utility, Contractor

class PropertyManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyManage
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    manager = PropertyManageSerializer()

    class Meta:
        model = Property
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = Unit
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Listing
        fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Tenant
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'


class MaintenanceRequestSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = MaintenanceRequest
        fields = '__all__'


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class TenantRequestSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()

    class Meta:
        model = TenantRequest
        fields = '__all__'


class ExpenseTrackingSerializer(serializers.ModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = ExpenseTracking
        fields = '__all__'


class InspectionSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Inspection
        fields = '__all__'


class TenantCommunicationSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()

    class Meta:
        model = TenantCommunication
        fields = '__all__'


class UtilitySerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Utility
        fields = '__all__'


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'
