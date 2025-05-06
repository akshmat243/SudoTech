from django.contrib import admin
from .models import AI, AIDocument, AIImage, History

@admin.register(AI)
class AIAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    search_fields = ['name']
    list_filter = ['is_active']

@admin.register(AIDocument)
class AIDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'ai', 'uploaded_at']
    search_fields = ['title']
    list_filter = ['uploaded_at']

@admin.register(AIImage)
class AIImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'ai', 'uploaded_at']
    search_fields = ['title']
    list_filter = ['uploaded_at']

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['ai', 'action', 'timestamp']
    search_fields = ['action', 'ai__name']
    list_filter = ['timestamp']
