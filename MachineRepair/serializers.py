from rest_framework import serializers
from .models import Machine, ServiceAgreement, RepairRequest, RepairHistory


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'


class ServiceAgreementSerializer(serializers.ModelSerializer):
    machine = MachineSerializer()

    class Meta:
        model = ServiceAgreement
        fields = '__all__'


class RepairRequestSerializer(serializers.ModelSerializer):
    machine = MachineSerializer()

    class Meta:
        model = RepairRequest
        fields = '__all__'


class RepairHistorySerializer(serializers.ModelSerializer):
    machine = MachineSerializer()

    class Meta:
        model = RepairHistory
        fields = '__all__'
