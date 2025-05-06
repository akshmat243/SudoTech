from rest_framework import serializers
from .models import ContractType, ContractTemplate, Contract


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = '__all__'


class ContractTemplateSerializer(serializers.ModelSerializer):
    contract_type = ContractTypeSerializer(read_only=True)
    contract_type_id = serializers.PrimaryKeyRelatedField(queryset=ContractType.objects.all(), source='contract_type', write_only=True)

    class Meta:
        model = ContractTemplate
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    contract_type = ContractTypeSerializer(read_only=True)
    contract_type_id = serializers.PrimaryKeyRelatedField(queryset=ContractType.objects.all(), source='contract_type', write_only=True)
    contract_template = ContractTemplateSerializer(read_only=True)
    contract_template_id = serializers.PrimaryKeyRelatedField(queryset=ContractTemplate.objects.all(), source='contract_template', write_only=True)

    class Meta:
        model = Contract
        fields = '__all__'
