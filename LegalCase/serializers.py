from rest_framework import serializers
from .models import (
    Advocate,
    CaseInitiator,
    CourtCategory,
    LegalCase,
    Expense,
    FeeReceive
)


class AdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'


class CaseInitiatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseInitiator
        fields = '__all__'


class CourtCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtCategory
        fields = '__all__'


class LegalCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalCase
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class FeeReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeReceive
        fields = '__all__'
