from django.contrib import admin
from .models import *

@admin.register(CourierAgent)
class CourierAgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone']


@admin.register(PendingCourier)
class PendingCourierAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'sender_name', 'recipient_name', 'destination', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['tracking_number', 'sender_name', 'recipient_name']


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'agent', 'sender_name', 'recipient_name', 'origin', 'destination', 'dispatch_date', 'delivery_date', 'status']
    list_filter = ['status', 'dispatch_date', 'delivery_date']
    search_fields = ['tracking_number', 'recipient_name']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['courier', 'amount', 'payment_date', 'method', 'paid']
    list_filter = ['paid', 'method', 'payment_date']


@admin.register(ServiceAgreement)
class ServiceAgreementAdmin(admin.ModelAdmin):
    list_display = ['agent', 'start_date', 'end_date']


@admin.register(CourierReturn)
class CourierReturnAdmin(admin.ModelAdmin):
    list_display = ['courier', 'reason', 'return_date']
    search_fields = ['courier__tracking_number']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['party_name', 'start_date', 'end_date']
    search_fields = ['party_name']


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['key']
    search_fields = ['key']
