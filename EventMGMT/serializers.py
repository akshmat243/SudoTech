from rest_framework import serializers
from .models import Event, EventBooking, EventBookingOrder, SystemSetup


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventBookingSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    
    class Meta:
        model = EventBooking
        fields = '__all__'


class EventBookingOrderSerializer(serializers.ModelSerializer):
    booking = EventBookingSerializer(read_only=True)
    
    class Meta:
        model = EventBookingOrder
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
