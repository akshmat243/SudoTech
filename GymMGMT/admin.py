from django.contrib import admin
from .models import (
    Trainer, Member, Measurement, MembershipPlan, WorkoutPlan,
    ClassSchedule, AttendanceTracking, PersonalTraining,
    NutritionalPlan, HealthAssessment, SystemSetup
)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization", "phone", "email")
    search_fields = ("name", "specialization")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "join_date", "trainer")
    search_fields = ("name", "email")
    list_filter = ("trainer",)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("member", "date", "weight", "height", "body_fat_percentage")
    date_hierarchy = "date"
    search_fields = ("member__name",)


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "duration_months", "price")
    search_fields = ("name",)


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "member", "assigned_date")
    date_hierarchy = "assigned_date"
    search_fields = ("title", "member__name")


@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ("class_name", "trainer", "day", "start_time", "end_time")
    search_fields = ("class_name",)
    list_filter = ("day",)


@admin.register(AttendanceTracking)
class AttendanceTrackingAdmin(admin.ModelAdmin):
    list_display = ("member", "date", "status")
    list_filter = ("status",)
    date_hierarchy = "date"


@admin.register(PersonalTraining)
class PersonalTrainingAdmin(admin.ModelAdmin):
    list_display = ("trainer", "member", "date")
    date_hierarchy = "date"


@admin.register(NutritionalPlan)
class NutritionalPlanAdmin(admin.ModelAdmin):
    list_display = ("member", "created_date")
    search_fields = ("member__name",)


@admin.register(HealthAssessment)
class HealthAssessmentAdmin(admin.ModelAdmin):
    list_display = ("member", "date", "overall_rating")
    search_fields = ("member__name",)
    date_hierarchy = "date"


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("setting_name", "value")
    search_fields = ("setting_name",)
