from django.contrib import admin
from .models import Service, Counter, Call, Report

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'is_open')
    list_filter = ('service', 'is_open')
    search_fields = ('name',)


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('token_number', 'service', 'counter', 'called_at', 'served')
    list_filter = ('service', 'counter', 'served')
    search_fields = ('token_number',)
    date_hierarchy = 'called_at'


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('date', 'service', 'total_tokens', 'tokens_served', 'tokens_missed')
    list_filter = ('date', 'service')
    search_fields = ('service__name',)
