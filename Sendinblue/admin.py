from django.contrib import admin
from .models import SendinblueMail, SendinblueTemplate, SendinblueContact

@admin.register(SendinblueMail)
class SendinblueMailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender_email', 'recipient_email', 'status', 'sent_at', 'created_at')
    list_filter = ('status',)
    search_fields = ('subject', 'sender_email', 'recipient_email')


@admin.register(SendinblueTemplate)
class SendinblueTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(SendinblueContact)
class SendinblueContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'subscribed_at', 'unsubscribed_at')
    search_fields = ('email', 'first_name', 'last_name')
