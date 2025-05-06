from django.contrib import admin
from .models import RoadMap, Idea

@admin.register(RoadMap)
class RoadMapAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status')
    search_fields = ('title',)
    list_filter = ('status',)

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'roadmap', 'submitted_by', 'submission_date', 'status')
    search_fields = ('title', 'submitted_by')
    list_filter = ('status', 'submission_date')
