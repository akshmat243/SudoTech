from rest_framework import serializers
from .models import Locker, Customer, BookingAssignment, DepositKeyAccess, Renewal, MaintenanceRepair, Membership


class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BookingAssignmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    locker = LockerSerializer()

    class Meta:
        model = BookingAssignment
        fields = '__all__'


class DepositKeyAccessSerializer(serializers.ModelSerializer):
    booking = BookingAssignmentSerializer()

    class Meta:
        model = DepositKeyAccess
        fields = '__all__'


class RenewalSerializer(serializers.ModelSerializer):
    booking = BookingAssignmentSerializer()

    class Meta:
        model = Renewal
        fields = '__all__'


class MaintenanceRepairSerializer(serializers.ModelSerializer):
    locker = LockerSerializer()

    class Meta:
        model = MaintenanceRepair
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Membership
        fields = '__all__'
