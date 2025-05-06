from django.contrib import admin
from .models import ZulipMessage


@admin.register(ZulipMessage)
class ZulipMessageAdmin(admin.ModelAdmin):
    list_display = ("sender_email", "recipient", "message_type", "topic", "sent_at")
    search_fields = ("sender_email", "recipient", "content", "topic", "message_id")
    list_filter = ("message_type", "sent_at")
