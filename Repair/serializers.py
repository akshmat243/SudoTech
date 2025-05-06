from rest_framework import serializers
from .models import RepairTechnician, Repair, RepairOrderRequest, RepairInvoice, Warranty


class RepairTechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairTechnician
        fields = '__all__'


class RepairSerializer(serializers.ModelSerializer):
    assigned_technician = RepairTechnicianSerializer(read_only=True)

    class Meta:
        model = Repair
        fields = '__all__'


class RepairOrderRequestSerializer(serializers.ModelSerializer):
    repair = RepairSerializer(read_only=True)

    class Meta:
        model = RepairOrderRequest
        fields = '__all__'


class RepairInvoiceSerializer(serializers.ModelSerializer):
    repair = RepairSerializer(read_only=True)

    class Meta:
        model = RepairInvoice
        fields = '__all__'


class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'
