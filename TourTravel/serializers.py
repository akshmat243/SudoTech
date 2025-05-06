from rest_framework import serializers
from .models import Tour, TourBooking, TouristInquiry, Guide, Promotion, TravelInsurance, SystemSetup

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class TourBookingSerializer(serializers.ModelSerializer):
    tour = TourSerializer()

    class Meta:
        model = TourBooking
        fields = '__all__'


class TouristInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristInquiry
        fields = '__all__'


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class TravelInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelInsurance
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
