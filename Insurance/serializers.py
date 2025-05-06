from rest_framework import serializers
from .models import (
    PolicyType, Customer, InsurancePolicy, Invoice, Claim, RiskAssessment,
    Reinsurance, UnderwritingRequest, Compliance, CustomerSupport,
    MarketingCampaign, FraudDetection, SystemSetup
)


class PolicyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyType
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'


class RiskAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAssessment
        fields = '__all__'


class ReinsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reinsurance
        fields = '__all__'


class UnderwritingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnderwritingRequest
        fields = '__all__'


class ComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compliance
        fields = '__all__'


class CustomerSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSupport
        fields = '__all__'


class MarketingCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingCampaign
        fields = '__all__'


class FraudDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraudDetection
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
