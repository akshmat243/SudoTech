from rest_framework import serializers
from .models import LaundryRequest, Invoice, Expenses, Machines, SystemSetup


class LaundryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaundryRequest
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'


class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
