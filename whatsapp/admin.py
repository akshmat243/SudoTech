from django.contrib import admin
from .models import WhatsAppMessage


@admin.register(WhatsAppMessage)
class WhatsAppMessageAdmin(admin.ModelAdmin):
    list_display = ("recipient_number", "status", "sent_at")
    search_fields = ("recipient_number", "message", "external_id")
    list_filter = ("status", "sent_at")
