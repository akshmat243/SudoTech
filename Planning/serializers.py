from rest_framework import serializers
from .models import (
    Challenge, Charter, BusinessPlan, MarketingPlan, BusinessModel,
    McKinsey7SModel, PortersFiveForces, SWOTAnalysis,
    PESTAnalysis, PESTELAnalysis, PlanningSystemSetup
)


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'


class CharterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charter
        fields = '__all__'


class BusinessPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPlan
        fields = '__all__'


class MarketingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingPlan
        fields = '__all__'


class BusinessModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessModel
        fields = '__all__'


class McKinsey7SModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = McKinsey7SModel
        fields = '__all__'


class PortersFiveForcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortersFiveForces
        fields = '__all__'


class SWOTAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWOTAnalysis
        fields = '__all__'


class PESTAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PESTAnalysis
        fields = '__all__'


class PESTELAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PESTELAnalysis
        fields = '__all__'


class PlanningSystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanningSystemSetup
        fields = '__all__'
