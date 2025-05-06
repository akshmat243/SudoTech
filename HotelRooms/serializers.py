from rest_framework import serializers
from .models import (
    Hotel, Room, Facility, HotelCustomer, Booking,
    Coupon, CustomPage, CustomerReview, BankTransferRequest
)


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)

    class Meta:
        model = Facility
        fields = '__all__'


class HotelCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCustomer
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    customer = HotelCustomerSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class CustomPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPage
        fields = '__all__'


class CustomerReviewSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(read_only=True)
    customer = HotelCustomerSerializer(read_only=True)

    class Meta:
        model = CustomerReview
        fields = '__all__'


class BankTransferRequestSerializer(serializers.ModelSerializer):
    customer = HotelCustomerSerializer(read_only=True)

    class Meta:
        model = BankTransferRequest
        fields = '__all__'
