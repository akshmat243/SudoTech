from django.contrib import admin
from .models import (
    Nutritionist, Member, DietPlanChart, DietSubscription,
    ConsultationAppointment, MealNutritionTracking, DietSetup
)


@admin.register(Nutritionist)
class NutritionistAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "specialization", "experience_years")
    search_fields = ("name", "email", "specialization")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "age", "gender", "joined_on")
    search_fields = ("full_name", "email")
    list_filter = ("gender",)


@admin.register(DietPlanChart)
class DietPlanChartAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "created_on")
    search_fields = ("name",)
    list_filter = ("created_on",)


@admin.register(DietSubscription)
class DietSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("member", "diet_plan", "subscribed_on", "valid_until", "is_active")
    list_filter = ("is_active",)
    search_fields = ("member__full_name", "diet_plan__name")


@admin.register(ConsultationAppointment)
class ConsultationAppointmentAdmin(admin.ModelAdmin):
    list_display = ("member", "nutritionist", "appointment_date", "status")
    list_filter = ("status", "appointment_date")
    search_fields = ("member__full_name", "nutritionist__name")


@admin.register(MealNutritionTracking)
class MealNutritionTrackingAdmin(admin.ModelAdmin):
    list_display = ("member", "date", "meal_type", "calories")
    list_filter = ("meal_type", "date")
    search_fields = ("member__full_name",)


@admin.register(DietSetup)
class DietSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)

