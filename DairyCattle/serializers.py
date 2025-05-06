from rest_framework import serializers
from .models import Animal, Health, Breeding, Weight, DailyMilkSheet, MilkInventory, CumulativeMilkSheet, MilkProduct, FeedManagement, Vaccination, SalesDistribution, ExpenseTracking, CalvingBirthRecord, EquipmentManagement


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class HealthSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)

    class Meta:
        model = Health
        fields = '__all__'


class BreedingSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)
    breeding_partner = AnimalSerializer(read_only=True)
    breeding_partner_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='breeding_partner', write_only=True)

    class Meta:
        model = Breeding
        fields = '__all__'


class WeightSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)

    class Meta:
        model = Weight
        fields = '__all__'


class DailyMilkSheetSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)

    class Meta:
        model = DailyMilkSheet
        fields = '__all__'


class MilkInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkInventory
        fields = '__all__'


class CumulativeMilkSheetSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)

    class Meta:
        model = CumulativeMilkSheet
        fields = '__all__'


class MilkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkProduct
        fields = '__all__'


class FeedManagementSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)

    class Meta:
        model = FeedManagement
        fields = '__all__'


class VaccinationSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)

    class Meta:
        model = Vaccination
        fields = '__all__'


class SalesDistributionSerializer(serializers.ModelSerializer):
    milk_product = MilkProductSerializer(read_only=True)
    milk_product_id = serializers.PrimaryKeyRelatedField(queryset=MilkProduct.objects.all(), source='milk_product', write_only=True)

    class Meta:
        model = SalesDistribution
        fields = '__all__'


class ExpenseTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTracking
        fields = '__all__'


class CalvingBirthRecordSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), source='animal', write_only=True)

    class Meta:
        model = CalvingBirthRecord
        fields = '__all__'


class EquipmentManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentManagement
        fields = '__all__'
