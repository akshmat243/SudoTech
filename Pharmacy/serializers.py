from rest_framework import serializers
from .models import (
    Medicine, Stock, DiscountPromotion, Bill, Invoice,
    ReturnRefund, Manufacturing, PharmacySystemSetup
)


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'


class DiscountPromotionSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)

    class Meta:
        model = DiscountPromotion
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)
    bill_customer_name = serializers.CharField(source='bill.customer_name', read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class ReturnRefundSerializer(serializers.ModelSerializer):
    invoice_id = serializers.IntegerField(source='invoice.id', read_only=True)

    class Meta:
        model = ReturnRefund
        fields = '__all__'


class ManufacturingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturing
        fields = '__all__'


class PharmacySystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacySystemSetup
        fields = '__all__'
