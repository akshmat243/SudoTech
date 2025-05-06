from django.contrib import admin
from .models import Project, Task, Tag

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_by', 'created_at')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'due_date', 'assigned_to')
    list_filter = ('status', 'priority', 'project', 'due_date')
    search_fields = ('title', 'description')
    autocomplete_fields = ['project', 'assigned_to', 'tags']
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)
