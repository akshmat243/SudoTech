from django.contrib import admin
from .models import (
    Class, Student, Parent, Admission, FeeManagement, Homework, Library,
    Exam, Transport, Alumni, Event, Hostel, OnlineAssessment, Notice,
    HealthRecord, Meeting, Attendance
)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "section")
    search_fields = ("name", "section")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "roll_number", "student_class", "admission_date")
    search_fields = ("first_name", "last_name", "roll_number")
    list_filter = ("student_class", "admission_date")


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ("name", "student", "phone", "email")
    search_fields = ("name", "student__first_name", "student__last_name")
    list_filter = ("student__student_class",)


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ("student_name", "date_applied", "status")
    list_filter = ("status", "date_applied")
    search_fields = ("student_name",)


@admin.register(FeeManagement)
class FeeManagementAdmin(admin.ModelAdmin):
    list_display = ("student", "amount_due", "amount_paid", "due_date")
    list_filter = ("due_date",)
    search_fields = ("student__first_name", "student__last_name")


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ("subject", "assigned_class", "due_date")
    list_filter = ("assigned_class", "due_date")
    search_fields = ("subject",)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("book_title", "author", "isbn", "available_copies")
    search_fields = ("book_title", "author", "isbn")


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("exam_name", "exam_date", "related_class")
    list_filter = ("exam_date", "related_class")
    search_fields = ("exam_name",)


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ("route_name", "driver_name", "vehicle_number")
    search_fields = ("route_name", "driver_name")


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ("student_name", "graduation_year", "current_occupation")
    search_fields = ("student_name", "current_occupation")
    list_filter = ("graduation_year",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date")
    search_fields = ("title",)
    list_filter = ("event_date",)


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ("student", "room_number", "block_name")
    search_fields = ("student__first_name", "student__last_name", "room_number", "block_name")
    list_filter = ("block_name",)


@admin.register(OnlineAssessment)
class OnlineAssessmentAdmin(admin.ModelAdmin):
    list_display = ("title", "assigned_class", "total_marks", "due_date")
    search_fields = ("title",)
    list_filter = ("assigned_class", "due_date")


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "posted_on")
    search_fields = ("title",)
    list_filter = ("posted_on",)


@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ("student", "checkup_date", "health_issue")
    list_filter = ("checkup_date",)
    search_fields = ("student__first_name", "student__last_name", "health_issue")


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title",)
    list_filter = ("date",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "present")
    list_filter = ("date", "present")
    search_fields = ("student__first_name", "student__last_name")
