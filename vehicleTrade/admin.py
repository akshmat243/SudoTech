from django.contrib import admin
from .models import (
    VehicleSeller, VehicleBuyer, Vehicle, VehicleTrade,
    PreviousServiceHistory, VehicleSpecification, VehicleCondition,
    VehicleHistory, VehicleInsuranceHistory, Document, VehicleReport,
    ExpertInspection, VehicleSetup
)


@admin.register(VehicleSeller)
class VehicleSellerAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "email")


@admin.register(VehicleBuyer)
class VehicleBuyerAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "email")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("plate_number", "model", "manufacturer", "year", "color")
    search_fields = ("plate_number", "model")


@admin.register(VehicleTrade)
class VehicleTradeAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "seller", "buyer", "trade_date", "price")
    date_hierarchy = "trade_date"


@admin.register(PreviousServiceHistory)
class PreviousServiceHistoryAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "service_date", "service_center")
    date_hierarchy = "service_date"


@admin.register(VehicleSpecification)
class VehicleSpecificationAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "key", "value")


@admin.register(VehicleCondition)
class VehicleConditionAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "reported_on")


@admin.register(VehicleHistory)
class VehicleHistoryAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "date_recorded")


@admin.register(VehicleInsuranceHistory)
class VehicleInsuranceHistoryAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "provider", "policy_number", "valid_from", "valid_to")
    date_hierarchy = "valid_from"


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "name", "uploaded_at")


@admin.register(VehicleReport)
class VehicleReportAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "created_at")


@admin.register(ExpertInspection)
class ExpertInspectionAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "expert_name", "inspection_date")


@admin.register(VehicleSetup)
class VehicleSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
