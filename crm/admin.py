from django.contrib import admin
from .models import Lead, Deal, CRMSystemSetup, CRMReport


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "source", "assigned_to", "created_at")
    search_fields = ("name", "email", "phone", "source")
    list_filter = ("source", "created_at")
    autocomplete_fields = ("assigned_to",)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("title", "lead", "value", "status", "closing_date", "created_at")
    list_filter = ("status", "closing_date", "created_at")
    search_fields = ("title", "lead__name")
    autocomplete_fields = ("lead",)


@admin.register(CRMSystemSetup)
class CRMSystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key",)


@admin.register(CRMReport)
class CRMReportAdmin(admin.ModelAdmin):
    list_display = ("report_date", "total_leads", "total_deals", "total_won", "total_lost")
    list_filter = ("report_date",)
