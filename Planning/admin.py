from django.contrib import admin
from .models import (
    Challenge, Charter, BusinessPlan, MarketingPlan, BusinessModel,
    McKinsey7SModel, PortersFiveForces, SWOTAnalysis,
    PESTAnalysis, PESTELAnalysis, PlanningSystemSetup
)


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ('title',)
    ordering = ('-created_on',)


@admin.register(Charter)
class CharterAdmin(admin.ModelAdmin):
    list_display = ('name', 'objective', 'created_on')
    search_fields = ('name', 'stakeholders')
    list_filter = ('created_on',)


@admin.register(BusinessPlan)
class BusinessPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'goal')
    list_filter = ('start_date', 'end_date')
    date_hierarchy = 'start_date'


@admin.register(MarketingPlan)
class MarketingPlanAdmin(admin.ModelAdmin):
    list_display = ('campaign_name', 'budget')
    search_fields = ('campaign_name', 'strategy')
    list_filter = ('budget',)


@admin.register(BusinessModel)
class BusinessModelAdmin(admin.ModelAdmin):
    list_display = ('model_name',)
    search_fields = ('model_name', 'revenue_streams')


@admin.register(McKinsey7SModel)
class McKinsey7SModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'strategy', 'structure')
    search_fields = ('shared_values', 'strategy', 'style')


@admin.register(PortersFiveForces)
class PortersFiveForcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'industry_rivalry')
    search_fields = ('threat_new_entrants', 'industry_rivalry')


@admin.register(SWOTAnalysis)
class SWOTAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('strengths', 'weaknesses', 'opportunities', 'threats')


@admin.register(PESTAnalysis)
class PESTAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('political', 'economic', 'social', 'technological')


@admin.register(PESTELAnalysis)
class PESTELAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('political', 'environmental', 'legal')


@admin.register(PlanningSystemSetup)
class PlanningSystemSetupAdmin(admin.ModelAdmin):
    list_display = ('config_name', 'config_value')
    search_fields = ('config_name',)
