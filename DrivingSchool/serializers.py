from rest_framework import serializers
from .models import Student, Vehicle, DrivingClass, Lesson, Invoice, ProgressReport, LicenceTracking, DrivingTestHub, SystemSetup


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class DrivingClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingClass
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    vehicle = VehicleSerializer(read_only=True)
    driving_class = DrivingClassSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'


class ProgressReportSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = ProgressReport
        fields = '__all__'


class LicenceTrackingSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = LicenceTracking
        fields = '__all__'


class DrivingTestHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingTestHub
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
