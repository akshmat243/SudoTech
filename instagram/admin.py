from django.contrib import admin
from .models import InstagramInteraction, InstagramPost


@admin.register(InstagramInteraction)
class InstagramInteractionAdmin(admin.ModelAdmin):
    list_display = ("type", "username", "instagram_id", "created_at", "received_at")
    search_fields = ("username", "instagram_id", "content")
    list_filter = ("type", "created_at")

@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ("username", "post_id", "post_type", "created_at", "published", "scheduled")
    search_fields = ("username", "post_id", "caption")
    list_filter = ("post_type", "published", "scheduled", "created_at")