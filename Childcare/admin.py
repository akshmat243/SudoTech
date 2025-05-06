from django.contrib import admin
from .models import (
    Parent, Inquiry, Child, Attendance, ParentCommunication,
    DailyReport, BehavioralRecord, LearningOutcome, SystemSetup
)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email")


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("parent_name", "contact_info", "date")
    search_fields = ("parent_name", "contact_info")
    date_hierarchy = "date"


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "date_of_birth", "enrolled_date")
    search_fields = ("name", "parent__name")
    list_filter = ("enrolled_date",)
    date_hierarchy = "enrolled_date"


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("child", "date", "status")
    search_fields = ("child__name",)
    list_filter = ("status",)
    date_hierarchy = "date"


@admin.register(ParentCommunication)
class ParentCommunicationAdmin(admin.ModelAdmin):
    list_display = ("parent", "date_sent")
    search_fields = ("parent__name",)
    date_hierarchy = "date_sent"


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("child", "date")
    search_fields = ("child__name",)
    date_hierarchy = "date"


@admin.register(BehavioralRecord)
class BehavioralRecordAdmin(admin.ModelAdmin):
    list_display = ("child", "date")
    search_fields = ("child__name",)
    date_hierarchy = "date"


@admin.register(LearningOutcome)
class LearningOutcomeAdmin(admin.ModelAdmin):
    list_display = ("child", "milestone", "date")
    search_fields = ("child__name", "milestone")
    date_hierarchy = "date"


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("setting_name", "value")
    search_fields = ("setting_name",)
