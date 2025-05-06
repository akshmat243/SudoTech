from rest_framework import serializers
from .models import Location, Supplier, Component, WorkOrder, PMs, PO


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True
    )
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), source='supplier', write_only=True, required=False
    )

    class Meta:
        model = Component
        fields = '__all__'


class WorkOrderSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True
    )
    component = ComponentSerializer(read_only=True)
    component_id = serializers.PrimaryKeyRelatedField(
        queryset=Component.objects.all(), source='component', write_only=True, required=False
    )

    class Meta:
        model = WorkOrder
        fields = '__all__'


class PMsSerializer(serializers.ModelSerializer):
    component = ComponentSerializer(read_only=True)
    component_id = serializers.PrimaryKeyRelatedField(
        queryset=Component.objects.all(), source='component', write_only=True
    )

    class Meta:
        model = PMs
        fields = '__all__'


class POSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), source='supplier', write_only=True
    )

    class Meta:
        model = PO
        fields = '__all__'
