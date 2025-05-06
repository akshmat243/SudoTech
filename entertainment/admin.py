from django.contrib import admin
from .models import (
    Playlist, Content, Customer, Orders, OrdersSummary,
    CustomPage, Coupon, Blog, SystemSetup
)


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("title", "is_public", "created_at")
    search_fields = ("title",)
    list_filter = ("is_public",)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("title", "content_type", "release_date", "is_premium")
    search_fields = ("title",)
    list_filter = ("content_type", "is_premium", "release_date")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "registered_on")
    search_fields = ("full_name", "email")


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("customer", "content", "price_paid", "ordered_at")
    list_filter = ("ordered_at",)
    search_fields = ("customer__full_name", "content__title")


@admin.register(OrdersSummary)
class OrdersSummaryAdmin(admin.ModelAdmin):
    list_display = ("customer", "total_orders", "total_spent", "last_order_date")


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "discount_percent", "active", "valid_until")
    list_filter = ("active",)
    search_fields = ("code",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "created_at")
    list_filter = ("published",)
    search_fields = ("title", "author")


@admin.register(CustomPage)
class CustomPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "slug")


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)
