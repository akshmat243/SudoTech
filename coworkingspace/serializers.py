from rest_framework import serializers
from .models import (
    Membership, MembershipPlan, Booking,
    Amenity, ResponseSetup, CoworkingSpaceSetup
)


class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    plan = MembershipPlanSerializer(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(queryset=MembershipPlan.objects.all(), source='plan', write_only=True)

    class Meta:
        model = Membership
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    customer = MembershipSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset=Membership.objects.all(), source='customer', write_only=True)

    class Meta:
        model = Booking
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'


class ResponseSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseSetup
        fields = '__all__'


class CoworkingSpaceSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoworkingSpaceSetup
        fields = '__all__'
