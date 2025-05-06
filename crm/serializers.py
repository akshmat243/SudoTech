from rest_framework import serializers
from .models import Lead, Deal, CRMSystemSetup, CRMReport
from UserMGMT.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class LeadSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assigned_to', write_only=True, required=False
    )

    class Meta:
        model = Lead
        fields = '__all__'


class DealSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    lead_id = serializers.PrimaryKeyRelatedField(
        queryset=Lead.objects.all(), source='lead', write_only=True
    )

    class Meta:
        model = Deal
        fields = '__all__'


class CRMSystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMSystemSetup
        fields = '__all__'


class CRMReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRMReport
        fields = '__all__'
