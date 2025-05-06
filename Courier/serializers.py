from rest_framework import serializers
from .models import (
    CourierAgent, PendingCourier, Courier,
    Payment, ServiceAgreement, CourierReturn,
    Contract, SystemSetup
)


class CourierAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierAgent
        fields = '__all__'


class PendingCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingCourier
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    agent = CourierAgentSerializer(read_only=True)
    agent_id = serializers.PrimaryKeyRelatedField(queryset=CourierAgent.objects.all(), source='agent', write_only=True)

    class Meta:
        model = Courier
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    courier = CourierSerializer(read_only=True)
    courier_id = serializers.PrimaryKeyRelatedField(queryset=Courier.objects.all(), source='courier', write_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


class ServiceAgreementSerializer(serializers.ModelSerializer):
    agent = CourierAgentSerializer(read_only=True)
    agent_id = serializers.PrimaryKeyRelatedField(queryset=CourierAgent.objects.all(), source='agent', write_only=True)

    class Meta:
        model = ServiceAgreement
        fields = '__all__'


class CourierReturnSerializer(serializers.ModelSerializer):
    courier = CourierSerializer(read_only=True)
    courier_id = serializers.PrimaryKeyRelatedField(queryset=Courier.objects.all(), source='courier', write_only=True)

    class Meta:
        model = CourierReturn
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
