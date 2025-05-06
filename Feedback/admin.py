from django.contrib import admin
from .models import FeedbackTemplate, Feedback, FeedbackHistory

@admin.register(FeedbackTemplate)
class FeedbackTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
    search_fields = ('title',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'template', 'submitted_at')
    search_fields = ('user__username', 'template__title')


@admin.register(FeedbackHistory)
class FeedbackHistoryAdmin(admin.ModelAdmin):
    list_display = ('feedback', 'updated_by', 'updated_at')
    search_fields = ('feedback__id', 'updated_by__username')
