from django.contrib import admin
from .models import (
    Visitor, VisitorLog, VisitorTimeline, VisitorBadge,
    PreRegistration, VisitorDocument, VisitorCompliance,
    VisitorIncident, VisitorReport
)

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company', 'phone', 'created_at')
    search_fields = ('full_name', 'phone', 'company')

@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'check_in', 'check_out', 'host_name', 'location')
    list_filter = ('check_in', 'location')
    search_fields = ('visitor__full_name', 'host_name')

@admin.register(VisitorTimeline)
class VisitorTimelineAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'timestamp', 'note')
    search_fields = ('visitor__full_name',)

@admin.register(VisitorBadge)
class VisitorBadgeAdmin(admin.ModelAdmin):
    list_display = ('visitor_log', 'badge_number', 'issued_at', 'returned_at')

@admin.register(PreRegistration)
class PreRegistrationAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'scheduled_date', 'host_name', 'purpose')

@admin.register(VisitorDocument)
class VisitorDocumentAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'document_type')

@admin.register(VisitorCompliance)
class VisitorComplianceAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'compliance_type', 'status')

@admin.register(VisitorIncident)
class VisitorIncidentAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'incident_date', 'reported_by')
    search_fields = ('visitor__full_name', 'reported_by')

@admin.register(VisitorReport)
class VisitorReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
