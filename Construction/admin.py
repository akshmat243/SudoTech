from django.contrib import admin
from .models import Site, Picking, InternalPicking, Inspection, Compliance, Material, Scrap


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "manager", "start_date", "end_date")
    search_fields = ("name", "location", "manager")
    date_hierarchy = "start_date"


@admin.register(Picking)
class PickingAdmin(admin.ModelAdmin):
    list_display = ("site", "material", "quantity", "date")
    search_fields = ("material", "site__name")
    date_hierarchy = "date"


@admin.register(InternalPicking)
class InternalPickingAdmin(admin.ModelAdmin):
    list_display = ("material", "origin_site", "destination_site", "quantity", "transfer_date")
    date_hierarchy = "transfer_date"
    search_fields = ("material",)


@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ("site", "inspector", "date")
    search_fields = ("site__name", "inspector")
    date_hierarchy = "date"


@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    list_display = ("site", "requirement", "status", "due_date")
    list_filter = ("status",)
    date_hierarchy = "due_date"
    search_fields = ("site__name", "requirement")


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "unit")
    search_fields = ("name",)


@admin.register(Scrap)
class ScrapAdmin(admin.ModelAdmin):
    list_display = ("site", "material", "quantity", "date_reported")
    date_hierarchy = "date_reported"
    search_fields = ("material", "site__name")
