from django.contrib import admin
from .models import AsanaWorkspace

@admin.register(AsanaWorkspace)
class AsanaWorkspaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'workspace_id', 'workspace_name')
    search_fields = ('workspace_id', 'workspace_name')
