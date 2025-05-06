from django.contrib import admin
from .models import Ticket, KnowledgeBase, FAQ, SystemSetup

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_number', 'customer_name', 'subject', 'priority', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'priority']
    search_fields = ['ticket_number', 'customer_name', 'subject']
    date_hierarchy = 'created_at'

@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    search_fields = ['title', 'category']
    date_hierarchy = 'created_at'

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at']
    search_fields = ['question']
    date_hierarchy = 'created_at'

@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['setting_name', 'value']
    search_fields = ['setting_name']
