from django.contrib import admin
from .models import Advocate, CaseInitiator, CourtCategory, LegalCase, Expense, FeeReceive

@admin.register(Advocate)
class AdvocateAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'specialization']
    search_fields = ['name', 'email', 'specialization']


@admin.register(CaseInitiator)
class CaseInitiatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact']
    search_fields = ['name', 'contact']


@admin.register(CourtCategory)
class CourtCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(LegalCase)
class LegalCaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'case_number', 'advocate', 'initiator', 'court_category', 'filing_date', 'status']
    search_fields = ['title', 'case_number', 'advocate__name', 'initiator__name']
    list_filter = ['status', 'filing_date', 'court_category']
    date_hierarchy = 'filing_date'


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['legal_case', 'description', 'amount', 'date']
    list_filter = ['date']
    date_hierarchy = 'date'
    search_fields = ['legal_case__title', 'description']


@admin.register(FeeReceive)
class FeeReceiveAdmin(admin.ModelAdmin):
    list_display = ['legal_case', 'amount_received', 'received_date']
    date_hierarchy = 'received_date'
    list_filter = ['received_date']
    search_fields = ['legal_case__title']
