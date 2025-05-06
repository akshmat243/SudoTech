from django.contrib import admin
from .models import SalesAgent, Program, Order

@admin.register(SalesAgent)
class SalesAgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'region')
    search_fields = ('name', 'email', 'phone', 'region')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('agent', 'program', 'order_date', 'amount', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('agent__name', 'program__name')
