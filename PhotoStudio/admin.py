from django.contrib import admin
from .models import Service, Package, Customer, Appointment, Billing

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_minutes', 'price')
    search_fields = ('name',)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_price')
    filter_horizontal = ('services',)
    search_fields = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'scheduled_datetime', 'service', 'package', 'created_on')
    list_filter = ('scheduled_datetime',)
    search_fields = ('customer__name',)


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'is_paid', 'payment_method', 'paid_on')
    list_filter = ('is_paid', 'payment_method')
    search_fields = ('appointment__customer__name',)
