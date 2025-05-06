from rest_framework import serializers
from .models import Item, Customer, DiningTable, TableOrder, SystemSetup


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DiningTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningTable
        fields = '__all__'


class TableOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    dining_table = DiningTableSerializer(read_only=True)
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = TableOrder
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
