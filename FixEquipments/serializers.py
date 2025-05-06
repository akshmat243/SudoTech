from rest_framework import serializers
from .models import FixEquipment, EquipmentMaintenance, EquipmentAudit, EquipmentSystemSetup


class FixEquipmentSerializer(serializers.ModelSerializer):
    equipment_type = serializers.ChoiceField(choices=FixEquipment.EQUIPMENT_TYPE_CHOICES)
    purchase_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FixEquipment
        fields = '__all__'


class EquipmentMaintenanceSerializer(serializers.ModelSerializer):
    equipment = FixEquipmentSerializer(read_only=True)  # Nested FixEquipment serializer
    maintenance_date = serializers.DateField(format="%Y-%m-%d")
    next_service_due = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = EquipmentMaintenance
        fields = '__all__'


class EquipmentAuditSerializer(serializers.ModelSerializer):
    equipment = FixEquipmentSerializer(read_only=True)  # Nested FixEquipment serializer
    audit_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = EquipmentAudit
        fields = '__all__'


class EquipmentSystemSetupSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = EquipmentSystemSetup
        fields = '__all__'
