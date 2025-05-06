from rest_framework import serializers
from .models import Member, MembershipPlan, MembershipPlanOrder, GroundAndClub, GroundAndClubBooking, CoachTrainer, ActivityEvent, TrainingSession, EquipmentInventory, Facility, SystemSetup


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'


class MembershipPlanOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlanOrder
        fields = '__all__'


class GroundAndClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundAndClub
        fields = '__all__'


class GroundAndClubBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundAndClubBooking
        fields = '__all__'


class CoachTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachTrainer
        fields = '__all__'


class ActivityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityEvent
        fields = '__all__'


class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSession
        fields = '__all__'


class EquipmentInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentInventory
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
