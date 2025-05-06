from rest_framework import serializers
from .models import (
    Product,
    Consignment,
    PurchaseOrder,
    PurchaseOrderItem,
    SaleOrder,
    SaleOrderItem,
    Shipping,
    Returns,
    QualityControl,
    Contract,
    Compliance
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ConsignmentSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = Consignment
        fields = '__all__'


class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(source='purchaseorderitem_set', many=True, read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class SaleOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = SaleOrderItem
        fields = '__all__'


class SaleOrderSerializer(serializers.ModelSerializer):
    items = SaleOrderItemSerializer(source='saleorderitem_set', many=True, read_only=True)

    class Meta:
        model = SaleOrder
        fields = '__all__'


class ShippingSerializer(serializers.ModelSerializer):
    sale_order = SaleOrderSerializer(read_only=True)
    sale_order_id = serializers.PrimaryKeyRelatedField(queryset=SaleOrder.objects.all(), source='sale_order', write_only=True)

    class Meta:
        model = Shipping
        fields = '__all__'


class ReturnsSerializer(serializers.ModelSerializer):
    sale_order = SaleOrderSerializer(read_only=True)
    sale_order_id = serializers.PrimaryKeyRelatedField(queryset=SaleOrder.objects.all(), source='sale_order', write_only=True)

    class Meta:
        model = Returns
        fields = '__all__'


class QualityControlSerializer(serializers.ModelSerializer):
    consignment = ConsignmentSerializer(read_only=True)
    consignment_id = serializers.PrimaryKeyRelatedField(queryset=Consignment.objects.all(), source='consignment', write_only=True)

    class Meta:
        model = QualityControl
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    consignment = ConsignmentSerializer(read_only=True)
    consignment_id = serializers.PrimaryKeyRelatedField(queryset=Consignment.objects.all(), source='consignment', write_only=True)

    class Meta:
        model = Contract
        fields = '__all__'


class ComplianceSerializer(serializers.ModelSerializer):
    consignment = ConsignmentSerializer(read_only=True)
    consignment_id = serializers.PrimaryKeyRelatedField(queryset=Consignment.objects.all(), source='consignment', write_only=True)

    class Meta:
        model = Compliance
        fields = '__all__'
