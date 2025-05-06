from django.contrib import admin
from .models import *

@admin.register(PolicyType)
class PolicyTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']
    search_fields = ['full_name', 'email']


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ['policy_number', 'customer', 'policy_type', 'start_date', 'end_date', 'premium', 'status']
    list_filter = ['status', 'start_date', 'end_date']
    search_fields = ['policy_number', 'customer__full_name']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['policy', 'issue_date', 'amount', 'paid']
    list_filter = ['paid', 'issue_date']


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['policy', 'claim_date', 'claim_amount', 'status']
    list_filter = ['status', 'claim_date']
    search_fields = ['policy__policy_number']


@admin.register(RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ['policy', 'assessment_date', 'risk_level']
    list_filter = ['risk_level', 'assessment_date']


@admin.register(Reinsurance)
class ReinsuranceAdmin(admin.ModelAdmin):
    list_display = ['policy', 'reinsurance_company', 'coverage_percentage', 'agreement_date']


@admin.register(UnderwritingRequest)
class UnderwritingRequestAdmin(admin.ModelAdmin):
    list_display = ['policy', 'request_date', 'status']
    list_filter = ['status']


@admin.register(Compliance)
class ComplianceAdmin(admin.ModelAdmin):
    list_display = ['policy', 'compliance_check_date', 'compliant']
    list_filter = ['compliant', 'compliance_check_date']


@admin.register(CustomerSupport)
class CustomerSupportAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer__full_name']


@admin.register(MarketingCampaign)
class MarketingCampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'budget']
    list_filter = ['start_date', 'end_date']


@admin.register(FraudDetection)
class FraudDetectionAdmin(admin.ModelAdmin):
    list_display = ['policy', 'flagged_date', 'status']
    list_filter = ['status', 'flagged_date']


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name']
    search_fields = ['setting_name']
