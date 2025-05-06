from rest_framework import serializers
from .models import Teacher, Student, Instrument, Class, Lesson, Course, Exam, PracticeSchedule, LibraryResource, LibraryLoan, InstrumentMaintenance, StudentProgress, Announcement, Report


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Class
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Exam
        fields = '__all__'


class PracticeScheduleSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    instrument = InstrumentSerializer()

    class Meta:
        model = PracticeSchedule
        fields = '__all__'


class LibraryResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryResource
        fields = '__all__'


class LibraryLoanSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    resource = LibraryResourceSerializer()

    class Meta:
        model = LibraryLoan
        fields = '__all__'


class InstrumentMaintenanceSerializer(serializers.ModelSerializer):
    instrument = InstrumentSerializer()

    class Meta:
        model = InstrumentMaintenance
        fields = '__all__'


class StudentProgressSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = StudentProgress
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Report
        fields = '__all__'
