from rest_framework import serializers
from .models import Nutritionist, Member, DietPlanChart, DietSubscription, ConsultationAppointment, MealNutritionTracking, DietSetup


class NutritionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutritionist
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class DietPlanChartSerializer(serializers.ModelSerializer):
    created_by = NutritionistSerializer(read_only=True)
    
    class Meta:
        model = DietPlanChart
        fields = '__all__'


class DietSubscriptionSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    diet_plan = DietPlanChartSerializer(read_only=True)
    
    class Meta:
        model = DietSubscription
        fields = '__all__'


class ConsultationAppointmentSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    nutritionist = NutritionistSerializer(read_only=True)
    
    class Meta:
        model = ConsultationAppointment
        fields = '__all__'


class MealNutritionTrackingSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    
    class Meta:
        model = MealNutritionTracking
        fields = '__all__'


class DietSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietSetup
        fields = '__all__'
