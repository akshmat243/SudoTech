from rest_framework import serializers
from .models import (
    CommissionPlan,
    Commission,
    CommissionReceipt,
    BankTransferRequest
)


class CommissionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionPlan
        fields = '__all__'


class CommissionSerializer(serializers.ModelSerializer):
    plan = CommissionPlanSerializer(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=CommissionPlan.objects.all(), source='plan', write_only=True
    )

    class Meta:
        model = Commission
        fields = '__all__'


class CommissionReceiptSerializer(serializers.ModelSerializer):
    commission = CommissionSerializer(read_only=True)
    commission_id = serializers.PrimaryKeyRelatedField(
        queryset=Commission.objects.all(), source='commission', write_only=True
    )

    class Meta:
        model = CommissionReceipt
        fields = '__all__'


class BankTransferRequestSerializer(serializers.ModelSerializer):
    commission = CommissionSerializer(read_only=True)
    commission_id = serializers.PrimaryKeyRelatedField(
        queryset=Commission.objects.all(), source='commission', write_only=True
    )

    class Meta:
        model = BankTransferRequest
        fields = '__all__'
