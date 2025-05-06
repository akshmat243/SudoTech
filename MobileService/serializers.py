from rest_framework import serializers
from .models import SLAPolicy, ServiceContract, PendingRequest, ServiceRequest, ServiceHistory, SystemSetup


class SLAPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = SLAPolicy
        fields = '__all__'


class ServiceContractSerializer(serializers.ModelSerializer):
    sla_policy = SLAPolicySerializer()

    class Meta:
        model = ServiceContract
        fields = '__all__'


class PendingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingRequest
        fields = '__all__'


class ServiceRequestSerializer(serializers.ModelSerializer):
    service_contract = ServiceContractSerializer()
    sla_policy = SLAPolicySerializer()

    class Meta:
        model = ServiceRequest
        fields = '__all__'


class ServiceHistorySerializer(serializers.ModelSerializer):
    service_request = ServiceRequestSerializer()

    class Meta:
        model = ServiceHistory
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
