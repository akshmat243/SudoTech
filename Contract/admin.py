from django.contrib import admin
from .models import ContractType, ContractTemplate, Contract

@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(ContractTemplate)
class ContractTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'contract_type', 'template_file']
    search_fields = ['name', 'contract_type__name']
    list_filter = ['contract_type']

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['title', 'contract_type', 'contract_template', 'start_date', 'end_date', 'status']
    list_filter = ['contract_type', 'contract_template', 'status']
    search_fields = ['title', 'parties_involved']
