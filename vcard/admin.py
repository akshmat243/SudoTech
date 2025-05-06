from django.contrib import admin
from .models import Business, Contact, Appointment


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "website")
    search_fields = ("name", "email", "phone")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email", "phone", "business")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("business",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("subject", "contact", "scheduled_for", "location")
    search_fields = ("subject", "contact__full_name", "location")
    list_filter = ("scheduled_for",)
