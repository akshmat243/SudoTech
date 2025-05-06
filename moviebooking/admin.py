from django.contrib import admin
from .models import (
    MovieCast, SeatingLayout, MovieShow,
    MovieOrder, FoodOrder, BookingHistory, SystemSetup
)


@admin.register(MovieCast)
class MovieCastAdmin(admin.ModelAdmin):
    list_display = ("movie_title", "cast_name", "role")
    search_fields = ("movie_title", "cast_name")


@admin.register(SeatingLayout)
class SeatingLayoutAdmin(admin.ModelAdmin):
    list_display = ("theater_name", "total_seats", "rows", "columns")
    search_fields = ("theater_name",)


@admin.register(MovieShow)
class MovieShowAdmin(admin.ModelAdmin):
    list_display = ("movie_title", "show_time", "theater", "price_per_seat", "available_seats")
    list_filter = ("show_time",)
    search_fields = ("movie_title",)


@admin.register(MovieOrder)
class MovieOrderAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "show", "seats_booked", "total_price", "ordered_at")
    list_filter = ("ordered_at",)
    search_fields = ("customer_name",)


@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ("item_name", "quantity", "price", "movie_order")
    search_fields = ("item_name",)


@admin.register(BookingHistory)
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "movie_title", "show_time", "seats", "booked_on")
    search_fields = ("customer_name", "movie_title")
    list_filter = ("booked_on",)


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "updated_at")
    search_fields = ("key",)
