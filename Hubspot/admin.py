from django.contrib import admin
from .models import HubSpotTicket

@admin.register(HubSpotTicket)
class HubSpotTicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'subject', 'priority', 'owner', 'created_at', 'last_modified', 'stage', 'status')
    search_fields = ('ticket_id', 'subject', 'owner', 'description')
    list_filter = ('priority', 'stage', 'status')
    ordering = ('-created_at',)
