from rest_framework import serializers
from .models import LedgerAccount


class LedgerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount
        fields = '__all__'
