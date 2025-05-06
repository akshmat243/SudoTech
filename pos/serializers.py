from rest_framework import serializers
from .models import POS, POSOrder, Product, PrintBarcode, Report


class POSSerializer(serializers.ModelSerializer):
    class Meta:
        model = POS
        fields = '__all__'


class POSOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSOrder
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PrintBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintBarcode
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
