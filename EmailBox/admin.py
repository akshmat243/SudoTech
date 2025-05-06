from django.contrib import admin
from .models import EmailBox, Email, EmailHistory

@admin.register(EmailBox)
class EmailBoxAdmin(admin.ModelAdmin):
    list_display = ('user', 'inbox_count', 'sent_count', 'draft_count', 'created_at')
    search_fields = ('user__username',)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'subject', 'status', 'sent_at')
    list_filter = ('status',)
    search_fields = ('sender', 'recipient', 'subject')


@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    list_display = ('email', 'previous_status', 'new_status', 'changed_by', 'changed_at')
    search_fields = ('email__subject', 'changed_by__username')
