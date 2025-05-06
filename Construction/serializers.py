from rest_framework import serializers
from .models import (
    Site,
    Picking,
    InternalPicking,
    Inspection,
    Compliance,
    Material,
    Scrap
)


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class PickingSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='site', write_only=True)

    class Meta:
        model = Picking
        fields = '__all__'


class InternalPickingSerializer(serializers.ModelSerializer):
    origin_site = SiteSerializer(read_only=True)
    origin_site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='origin_site', write_only=True)
    destination_site = SiteSerializer(read_only=True)
    destination_site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='destination_site', write_only=True)

    class Meta:
        model = InternalPicking
        fields = '__all__'


class InspectionSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='site', write_only=True)

    class Meta:
        model = Inspection
        fields = '__all__'


class ComplianceSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='site', write_only=True)

    class Meta:
        model = Compliance
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class ScrapSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='site', write_only=True)

    class Meta:
        model = Scrap
        fields = '__all__'
