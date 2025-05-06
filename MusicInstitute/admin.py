from django.contrib import admin
from .models import (
    Teacher, Student, Instrument, Class, Lesson, Course, Exam,
    PracticeSchedule, LibraryResource, LibraryLoan, InstrumentMaintenance,
    StudentProgress, Announcement, Report
)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "expertise", "email", "phone")
    search_fields = ("name", "expertise", "email")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date_of_birth", "enrolled_date")
    search_fields = ("name", "email")
    list_filter = ("enrolled_date",)
    date_hierarchy = "enrolled_date"


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "condition")
    search_fields = ("name", "serial_number")
    list_filter = ("condition",)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher", "schedule")
    search_fields = ("title",)
    list_filter = ("teacher",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "student", "teacher", "date")
    search_fields = ("title", "student__name", "teacher__name")
    list_filter = ("teacher", "date")
    date_hierarchy = "date"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "duration_weeks")
    search_fields = ("name",)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "student", "date", "result")
    search_fields = ("name", "student__name", "result")
    list_filter = ("date",)
    date_hierarchy = "date"


@admin.register(PracticeSchedule)
class PracticeScheduleAdmin(admin.ModelAdmin):
    list_display = ("student", "instrument", "practice_time", "duration_minutes")
    search_fields = ("student__name", "instrument__name")
    list_filter = ("instrument",)
    date_hierarchy = "practice_time"


@admin.register(LibraryResource)
class LibraryResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "resource_type", "available_copies")
    search_fields = ("title",)
    list_filter = ("resource_type",)


@admin.register(LibraryLoan)
class LibraryLoanAdmin(admin.ModelAdmin):
    list_display = ("student", "resource", "borrowed_on", "due_date")
    search_fields = ("student__name", "resource__title")
    list_filter = ("borrowed_on", "due_date")
    date_hierarchy = "borrowed_on"


@admin.register(InstrumentMaintenance)
class InstrumentMaintenanceAdmin(admin.ModelAdmin):
    list_display = ("instrument", "maintenance_date", "issue_reported", "resolved")
    search_fields = ("instrument__name", "issue_reported")
    list_filter = ("resolved", "maintenance_date")
    date_hierarchy = "maintenance_date"


@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "progress_percent", "last_updated")
    search_fields = ("student__name", "course__name")
    list_filter = ("last_updated",)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "posted_on")
    search_fields = ("title",)
    date_hierarchy = "posted_on"


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("student", "title", "created_on")
    search_fields = ("student__name", "title")
    date_hierarchy = "created_on"
