from rest_framework import serializers
from .models import Spreadsheet


class SpreadsheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spreadsheet
        fields = '__all__'
