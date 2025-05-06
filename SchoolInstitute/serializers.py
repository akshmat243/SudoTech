from rest_framework import serializers
from .models import (
    Class, Student, Parent, Admission, FeeManagement, Homework, Library,
    Exam, Transport, Alumni, Event, Hostel, OnlineAssessment, Notice, 
    HealthRecord, Meeting, Attendance
)


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    student_class = ClassSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Parent
        fields = '__all__'


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'


class FeeManagementSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = FeeManagement
        fields = '__all__'


class HomeworkSerializer(serializers.ModelSerializer):
    assigned_class = ClassSerializer(read_only=True)

    class Meta:
        model = Homework
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    related_class = ClassSerializer(read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'


class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class HostelSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Hostel
        fields = '__all__'


class OnlineAssessmentSerializer(serializers.ModelSerializer):
    assigned_class = ClassSerializer(read_only=True)

    class Meta:
        model = OnlineAssessment
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class HealthRecordSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = HealthRecord
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'
