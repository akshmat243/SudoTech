from rest_framework import serializers
from .models import Facility, Booking, BookingOrder, BookingReceipt, SystemSetup


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    facility = FacilitySerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'


class BookingOrderSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)

    class Meta:
        model = BookingOrder
        fields = '__all__'


class BookingReceiptSerializer(serializers.ModelSerializer):
    order = BookingOrderSerializer(read_only=True)

    class Meta:
        model = BookingReceipt
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
