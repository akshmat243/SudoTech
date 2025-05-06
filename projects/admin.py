from django.contrib import admin
from .models import Project, ProjectTemplate, ProjectReport

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stage', 'start_date', 'end_date', 'assigned_user')
    list_filter = ('stage', 'assigned_user')
    search_fields = ('name', 'assigned_user__username')

@admin.register(ProjectTemplate)
class ProjectTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'assigned_user')
    search_fields = ('name', 'assigned_user__username')
    list_filter = ('assigned_user',)
    
@admin.register(ProjectReport)
class ProjectReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'due_date', 'progress', 'stage')
    list_filter = ('stage', 'start_date', 'due_date')
    search_fields = ('name',)
