from django.contrib import admin
from .models import Location, WorkOrder, Component, PMs, Supplier, PO


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_email", "phone")
    search_fields = ("name", "contact_email")


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "part_number", "supplier")
    search_fields = ("name", "part_number")
    list_filter = ("location",)


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "component", "status", "created_on", "due_date", "completed_on")
    list_filter = ("status", "location")
    search_fields = ("title",)


@admin.register(PMs)
class PMsAdmin(admin.ModelAdmin):
    list_display = ("name", "component", "frequency_days", "last_maintenance", "next_due")
    search_fields = ("name",)
    list_filter = ("next_due",)


@admin.register(PO)
class POAdmin(admin.ModelAdmin):
    list_display = ("order_number", "supplier", "order_date", "total_amount", "is_received")
    list_filter = ("is_received",)
    search_fields = ("order_number",)
