from django.contrib import admin
from .models import GoogleDoc

@admin.register(GoogleDoc)
class GoogleDocAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner_email', 'doc_id', 'created_at', 'last_synced']
    search_fields = ['title', 'doc_id', 'owner_email']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'last_synced']
