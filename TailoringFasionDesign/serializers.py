from rest_framework import serializers
from .models import MeasurementProfile, DesignType, WorkType, FabricType, Tailor, Collection, Order


class MeasurementProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementProfile
        fields = '__all__'


class DesignTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignType
        fields = '__all__'


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = '__all__'


class FabricTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FabricType
        fields = '__all__'


class TailorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tailor
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
