from django.contrib import admin
from .models import FacebookInteraction, FacebookPost


@admin.register(FacebookInteraction)
class FacebookInteractionAdmin(admin.ModelAdmin):
    list_display = ("type", "sender_name", "facebook_id", "created_at", "received_at")
    search_fields = ("sender_name", "facebook_id", "content")
    list_filter = ("type", "created_at")

@admin.register(FacebookPost)
class FacebookPostAdmin(admin.ModelAdmin):
    list_display = ("page_name", "post_id", "created_at", "published", "scheduled")
    search_fields = ("page_name", "post_id", "message")
    list_filter = ("published", "scheduled", "created_at")