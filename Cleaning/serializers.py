from rest_framework import serializers
from .models import (
    CleaningTeam,
    BookingRequest,
    Inspection,
    Invoice,
    Maintenance,
    Complaint,
    Expense,
    SystemSetup
)


class CleaningTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningTeam
        fields = '__all__'


class BookingRequestSerializer(serializers.ModelSerializer):
    team = CleaningTeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=CleaningTeam.objects.all(), source='team', write_only=True, required=False
    )

    class Meta:
        model = BookingRequest
        fields = '__all__'


class InspectionSerializer(serializers.ModelSerializer):
    booking = BookingRequestSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=BookingRequest.objects.all(), source='booking', write_only=True
    )

    class Meta:
        model = Inspection
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    booking = BookingRequestSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=BookingRequest.objects.all(), source='booking', write_only=True
    )

    class Meta:
        model = Invoice
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    team = CleaningTeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=CleaningTeam.objects.all(), source='team', write_only=True
    )

    class Meta:
        model = Maintenance
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    booking = BookingRequestSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=BookingRequest.objects.all(), source='booking', write_only=True
    )

    class Meta:
        model = Complaint
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
