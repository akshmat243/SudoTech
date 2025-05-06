from rest_framework import serializers
from .models import (
    EyeCarePatient,
    EyeTestPrescription,
    EyeCareAppointment,
    EyewearCustomization,
    EyewearOrder,
)


class EyeCarePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = EyeCarePatient
        fields = '__all__'


class EyeTestPrescriptionSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = EyeTestPrescription
        fields = '__all__'


class EyeCareAppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = EyeCareAppointment
        fields = '__all__'


class EyewearCustomizationSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = EyewearCustomization
        fields = '__all__'


class EyewearOrderSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    customization_details = EyewearCustomizationSerializer(source='customization', read_only=True)

    class Meta:
        model = EyewearOrder
        fields = '__all__'
