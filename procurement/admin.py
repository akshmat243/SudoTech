from django.contrib import admin
from .models import (
    Procurement, RFx, RFxApplication, RFxApplicant, RFxArchived,
    Vendor, VendorOnBoarding, RFxVendor, CustomQuestion,
    InterviewSchedule, SystemSetup
)

@admin.register(Procurement)
class ProcurementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by")
    search_fields = ("title", "description")
    list_filter = ("created_by",)


@admin.register(RFx)
class RFxAdmin(admin.ModelAdmin):
    list_display = ("title", "procurement", "created_at", "is_archived")
    search_fields = ("title", "description")
    list_filter = ("created_at", "is_archived", "procurement")
    autocomplete_fields = ("procurement",)


@admin.register(RFxApplication)
class RFxApplicationAdmin(admin.ModelAdmin):
    list_display = ("rfx", "vendor", "submitted_on")
    list_filter = ("rfx", "submitted_on", "vendor")
    search_fields = ("rfx__title", "vendor__name")
    autocomplete_fields = ("rfx", "vendor")


@admin.register(RFxApplicant)
class RFxApplicantAdmin(admin.ModelAdmin):
    list_display = ("application", "contact_person")
    search_fields = ("contact_person", "application__rfx__title", "application__vendor__name")
    autocomplete_fields = ("application",)


@admin.register(RFxArchived)
class RFxArchivedAdmin(admin.ModelAdmin):
    list_display = ("original_rfx", "archived_on")
    search_fields = ("original_rfx__title",)
    autocomplete_fields = ("original_rfx",)


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_email", "registered_on")
    search_fields = ("name", "contact_email")


@admin.register(VendorOnBoarding)
class VendorOnBoardingAdmin(admin.ModelAdmin):
    list_display = ("vendor", "status")
    list_filter = ("status",)
    search_fields = ("vendor__name",)
    autocomplete_fields = ("vendor",)


@admin.register(RFxVendor)
class RFxVendorAdmin(admin.ModelAdmin):
    list_display = ("rfx", "vendor", "invited_on")
    search_fields = ("rfx__title", "vendor__name")
    list_filter = ("invited_on",)
    autocomplete_fields = ("rfx", "vendor")


@admin.register(CustomQuestion)
class CustomQuestionAdmin(admin.ModelAdmin):
    list_display = ("rfx", "question")
    search_fields = ("question", "rfx__title")
    autocomplete_fields = ("rfx",)


@admin.register(InterviewSchedule)
class InterviewScheduleAdmin(admin.ModelAdmin):
    list_display = ("application", "scheduled_on", "interviewer")
    search_fields = ("application__rfx__title", "interviewer")
    list_filter = ("scheduled_on",)
    autocomplete_fields = ("application",)


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key",)
