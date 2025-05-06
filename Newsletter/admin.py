from django.contrib import admin
from .models import Newsletter, Mail, MailHistory

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_by', 'created_at')
    search_fields = ('name', 'subject')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('newsletter', 'recipient_email', 'status', 'sent_at')
    list_filter = ('status',)
    search_fields = ('recipient_email',)


@admin.register(MailHistory)
class MailHistoryAdmin(admin.ModelAdmin):
    list_display = ('mail', 'previous_status', 'new_status', 'status_changed_by', 'changed_at')
    search_fields = ('mail__recipient_email', 'status_changed_by__username')
