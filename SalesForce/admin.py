from django.contrib import admin
from .models import Account, Contact, Opportunity, Lead, Case, Task, SystemSetup

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'industry', 'phone', 'website']
    search_fields = ['name', 'industry']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'account']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['account']

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['name', 'account', 'stage', 'amount', 'close_date']
    list_filter = ['stage', 'account']
    search_fields = ['name', 'account__name']

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company', 'status']
    list_filter = ['status']
    search_fields = ['first_name', 'last_name', 'company']

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'account', 'status', 'priority']
    list_filter = ['status', 'priority', 'account']
    search_fields = ['subject', 'account__name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['opportunity', 'assigned_to', 'due_date', 'status']
    list_filter = ['status', 'due_date']
    search_fields = ['opportunity__name', 'assigned_to']

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['system_name', 'version', 'updated_at']
    search_fields = ['system_name']
