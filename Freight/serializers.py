from rest_framework import serializers
from .models import FreightCustomer, FreightBooking, FreightShipping, FreightInvoice, FreightSystemSetup


class FreightCustomerSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FreightCustomer
        fields = '__all__'


class FreightBookingSerializer(serializers.ModelSerializer):
    customer = FreightCustomerSerializer(read_only=True)  # Nested FreightCustomer serializer
    booking_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FreightBooking
        fields = '__all__'


class FreightShippingSerializer(serializers.ModelSerializer):
    booking = FreightBookingSerializer(read_only=True)  # Nested FreightBooking serializer
    departure_date = serializers.DateField(format="%Y-%m-%d")
    arrival_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FreightShipping
        fields = '__all__'


class FreightInvoiceSerializer(serializers.ModelSerializer):
    booking = FreightBookingSerializer(read_only=True)  # Nested FreightBooking serializer
    issue_date = serializers.DateField(format="%Y-%m-%d")
    due_date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FreightInvoice
        fields = '__all__'


class FreightSystemSetupSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = FreightSystemSetup
        fields = '__all__'
