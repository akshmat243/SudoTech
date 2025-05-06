from rest_framework import serializers
from .models import ElderlyResident, Caretaker, CareRequest, DailyActivitySchedule, HealthCheckup, MealPlan


class ElderlyResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElderlyResident
        fields = '__all__'


class CaretakerSerializer(serializers.ModelSerializer):
    assigned_resident = ElderlyResidentSerializer(read_only=True)

    class Meta:
        model = Caretaker
        fields = '__all__'


class CareRequestSerializer(serializers.ModelSerializer):
    resident = ElderlyResidentSerializer(read_only=True)

    class Meta:
        model = CareRequest
        fields = '__all__'


class DailyActivityScheduleSerializer(serializers.ModelSerializer):
    resident = ElderlyResidentSerializer(read_only=True)

    class Meta:
        model = DailyActivitySchedule
        fields = '__all__'


class HealthCheckupSerializer(serializers.ModelSerializer):
    resident = ElderlyResidentSerializer(read_only=True)

    class Meta:
        model = HealthCheckup
        fields = '__all__'


class MealPlanSerializer(serializers.ModelSerializer):
    resident = ElderlyResidentSerializer(read_only=True)

    class Meta:
        model = MealPlan
        fields = '__all__'
