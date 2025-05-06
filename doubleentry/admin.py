from django.contrib import admin
from .models import Account, JournalEntry, JournalLine

class JournalLineInline(admin.TabularInline):
    model = JournalLine
    extra = 2

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'reference')
    search_fields = ('reference', 'description')
    inlines = [JournalLineInline]

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'account_type')
    search_fields = ('name',)

@admin.register(JournalLine)
class JournalLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'journal_entry', 'account', 'debit', 'credit')
    list_filter = ('account',)
