from django.contrib import admin
from .models import (
    Student, Vehicle, DrivingClass, Lesson, Invoice,
    ProgressReport, LicenceTracking, DrivingTestHub, SystemSetup
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "date_of_birth", "enrolled_date")
    search_fields = ("name", "email")
    date_hierarchy = "enrolled_date"


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("registration_number", "model", "type", "available")
    search_fields = ("registration_number", "model")
    list_filter = ("available", "type")


@admin.register(DrivingClass)
class DrivingClassAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "schedule")
    search_fields = ("title", "instructor")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("student", "vehicle", "driving_class", "date", "duration_minutes")
    search_fields = ("student__name",)
    date_hierarchy = "date"
    list_filter = ("driving_class",)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("student", "issue_date", "amount", "paid")
    search_fields = ("student__name",)
    list_filter = ("paid",)
    date_hierarchy = "issue_date"


@admin.register(ProgressReport)
class ProgressReportAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "score")
    search_fields = ("student__name",)
    date_hierarchy = "date"


@admin.register(LicenceTracking)
class LicenceTrackingAdmin(admin.ModelAdmin):
    list_display = ("student", "application_date", "test_date", "result")
    list_filter = ("result",)
    date_hierarchy = "application_date"


@admin.register(DrivingTestHub)
class DrivingTestHubAdmin(admin.ModelAdmin):
    list_display = ("location", "examiner", "test_date", "slots_available")
    search_fields = ("location", "examiner")
    date_hierarchy = "test_date"


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("setting_name", "value")
    search_fields = ("setting_name",)
