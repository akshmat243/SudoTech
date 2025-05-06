from django.contrib import admin
from .models import (
    Member, MembershipPlan, MembershipPlanOrder,
    GroundAndClub, GroundAndClubBooking, CoachTrainer,
    ActivityEvent, TrainingSession, EquipmentInventory,
    Facility, SystemSetup
)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "join_date", "active")
    search_fields = ("full_name", "email")
    list_filter = ("active",)


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "duration_months", "price")
    search_fields = ("name",)


@admin.register(MembershipPlanOrder)
class MembershipPlanOrderAdmin(admin.ModelAdmin):
    list_display = ("member", "plan", "order_date", "valid_until", "status")
    list_filter = ("status",)
    search_fields = ("member__full_name",)


@admin.register(GroundAndClub)
class GroundAndClubAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "type", "available")
    search_fields = ("name", "location")
    list_filter = ("type", "available")


@admin.register(GroundAndClubBooking)
class GroundAndClubBookingAdmin(admin.ModelAdmin):
    list_display = ("member", "facility", "booking_date", "start_time", "end_time", "status")
    list_filter = ("status", "booking_date")
    search_fields = ("member__full_name", "facility__name")


@admin.register(CoachTrainer)
class CoachTrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "expertise", "phone", "available")
    search_fields = ("name", "expertise")
    list_filter = ("available",)


@admin.register(ActivityEvent)
class ActivityEventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "location", "coach")
    search_fields = ("title", "location")
    list_filter = ("start_date",)


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ("coach", "member", "session_date", "session_time", "focus_area")
    list_filter = ("session_date",)
    search_fields = ("coach__name", "member__full_name")


@admin.register(EquipmentInventory)
class EquipmentInventoryAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "condition", "available")
    list_filter = ("condition", "available")
    search_fields = ("name",)


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name", "location")


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)
