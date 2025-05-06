from rest_framework import serializers
from .models import (Asset, AssetHistory, DefectiveAsset, AssetSystemSetup
)

for model in [Asset, AssetHistory, DefectiveAsset, AssetSystemSetup
]:
    class DoctorSerializer(serializers.ModelSerializer):
        class Meta:
            model = model
            fields = '__all__'
