from rest_framework import serializers
from .models import Purchase, Warehouse, WarehouseTransfer


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseTransferSerializer(serializers.ModelSerializer):
    from_warehouse = WarehouseSerializer(read_only=True)
    to_warehouse = WarehouseSerializer(read_only=True)

    class Meta:
        model = WarehouseTransfer
        fields = '__all__'
