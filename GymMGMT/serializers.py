from rest_framework import serializers
from .models import Trainer, Member, Measurement, MembershipPlan, WorkoutPlan, ClassSchedule, AttendanceTracking, PersonalTraining, NutritionalPlan, HealthAssessment, SystemSetup


class TrainerSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Trainer
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)  # Nested Trainer serializer
    join_date = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Member
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)  # Nested Member serializer
    date = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Measurement
        fields = '__all__'


class MembershipPlanSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = MembershipPlan
        fields = '__all__'


class WorkoutPlanSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)  # Nested Member serializer
    assigned_date = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = WorkoutPlan
        fields = '__all__'


class ClassScheduleSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)  # Nested Trainer serializer
    start_time = serializers.TimeField(format="%H:%M")
    end_time = serializers.TimeField(format="%H:%M")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ClassSchedule
        fields = '__all__'


class AttendanceTrackingSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)  # Nested Member serializer
    date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = AttendanceTracking
        fields = '__all__'


class PersonalTrainingSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)  # Nested Trainer serializer
    member = MemberSerializer(read_only=True)  # Nested Member serializer
    date = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = PersonalTraining
        fields = '__all__'


class NutritionalPlanSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)  # Nested Member serializer
    created_date = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = NutritionalPlan
        fields = '__all__'


class HealthAssessmentSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)  # Nested Member serializer
    date = serializers.DateField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = HealthAssessment
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = SystemSetup
        fields = '__all__'
