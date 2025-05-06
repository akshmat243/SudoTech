from rest_framework import serializers
from .models import (
    LabPatient,
    PatientCard,
    LabAppointment,
    LabTestRequest,
    LabInventory,
    LabBilling,
    LabResult,
    PatientHistory,
    LabSystemSetting
)


class LabPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabPatient
        fields = '__all__'


class PatientCardSerializer(serializers.ModelSerializer):
    patient = LabPatientSerializer()

    class Meta:
        model = PatientCard
        fields = '__all__'


class LabAppointmentSerializer(serializers.ModelSerializer):
    patient = LabPatientSerializer()

    class Meta:
        model = LabAppointment
        fields = '__all__'


class LabTestRequestSerializer(serializers.ModelSerializer):
    appointment = LabAppointmentSerializer()

    class Meta:
        model = LabTestRequest
        fields = '__all__'


class LabInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LabInventory
        fields = '__all__'


class LabBillingSerializer(serializers.ModelSerializer):
    patient = LabPatientSerializer()

    class Meta:
        model = LabBilling
        fields = '__all__'


class LabResultSerializer(serializers.ModelSerializer):
    lab_test = LabTestRequestSerializer()

    class Meta:
        model = LabResult
        fields = '__all__'


class PatientHistorySerializer(serializers.ModelSerializer):
    patient = LabPatientSerializer()

    class Meta:
        model = PatientHistory
        fields = '__all__'


class LabSystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabSystemSetting
        fields = '__all__'
