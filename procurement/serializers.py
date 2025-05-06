from rest_framework import serializers
from .models import (
    Vendor, Procurement, RFx, RFxApplication, RFxApplicant, RFxArchived,
    VendorOnBoarding, RFxVendor, CustomQuestion, InterviewSchedule, SystemSetup
)
from UserMGMT.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # adjust based on your actual User model


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class ProcurementSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Procurement
        fields = '__all__'


class RFxSerializer(serializers.ModelSerializer):
    procurement = ProcurementSerializer(read_only=True)

    class Meta:
        model = RFx
        fields = '__all__'


class RFxApplicationSerializer(serializers.ModelSerializer):
    rfx = RFxSerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = RFxApplication
        fields = '__all__'


class RFxApplicantSerializer(serializers.ModelSerializer):
    application = RFxApplicationSerializer(read_only=True)

    class Meta:
        model = RFxApplicant
        fields = '__all__'


class RFxArchivedSerializer(serializers.ModelSerializer):
    original_rfx = RFxSerializer(read_only=True)

    class Meta:
        model = RFxArchived
        fields = '__all__'


class VendorOnBoardingSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = VendorOnBoarding
        fields = '__all__'


class RFxVendorSerializer(serializers.ModelSerializer):
    rfx = RFxSerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = RFxVendor
        fields = '__all__'


class CustomQuestionSerializer(serializers.ModelSerializer):
    rfx = RFxSerializer(read_only=True)

    class Meta:
        model = CustomQuestion
        fields = '__all__'


class InterviewScheduleSerializer(serializers.ModelSerializer):
    application = RFxApplicationSerializer(read_only=True)

    class Meta:
        model = InterviewSchedule
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
