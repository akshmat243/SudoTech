from rest_framework import serializers
from .models import (
    PettyCashCategory,
    PettyCash,
    PettyCashExpense,
    PettyCashRequest,
    PettyCashReimbursement
)


class PettyCashCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PettyCashCategory
        fields = '__all__'


class PettyCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = PettyCash
        fields = '__all__'


class PettyCashExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PettyCashExpense
        fields = '__all__'


class PettyCashRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PettyCashRequest
        fields = '__all__'


class PettyCashReimbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PettyCashReimbursement
        fields = '__all__'
