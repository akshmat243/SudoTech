from django.contrib import admin
from .models import Proposal

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('id', 'proposal', 'customer', 'account_type', 'issue_date', 'status')
    list_filter = ('account_type', 'status')
    search_fields = ('proposal', 'customer')
    readonly_fields = ('proposal',)
