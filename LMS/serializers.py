from rest_framework import serializers
from .models import (
    Course,
    CustomPage,
    Blog,
    Subscriber,
    CourseCoupon,
    Student,
    CourseOrder,
    LMSReport,
    SystemSetup
)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CustomPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPage
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class CourseCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCoupon
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseOrderSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()
    coupon = serializers.StringRelatedField()

    class Meta:
        model = CourseOrder
        fields = '__all__'


class LMSReportSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()

    class Meta:
        model = LMSReport
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
