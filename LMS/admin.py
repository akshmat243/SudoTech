from django.contrib import admin
from .models import (
    Course, CustomPage, Blog, Subscriber, CourseCoupon, Student,
    CourseOrder, LMSReport, SystemSetup
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "price", "published", "created_at")
    search_fields = ("title", "instructor")
    list_filter = ("published",)


@admin.register(CustomPage)
class CustomPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "created_at")
    search_fields = ("title", "slug")
    list_filter = ("is_active",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "created_at")
    search_fields = ("title", "author")
    list_filter = ("published",)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_on")
    search_fields = ("email",)


@admin.register(CourseCoupon)
class CourseCouponAdmin(admin.ModelAdmin):
    list_display = ("code", "discount_percent", "active", "valid_until")
    search_fields = ("code",)
    list_filter = ("active",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "registered_on")
    search_fields = ("full_name", "email")


@admin.register(CourseOrder)
class CourseOrderAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "amount_paid", "ordered_at")
    search_fields = ("student__full_name", "course__title")
    list_filter = ("ordered_at",)


@admin.register(LMSReport)
class LMSReportAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "progress_percent", "last_updated")
    list_filter = ("progress_percent",)


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)
