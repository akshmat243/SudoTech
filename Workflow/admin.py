from django.contrib import admin
from .models import Workflow, Task, TaskStatus

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Number of empty forms to display

@admin.register(Workflow)
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at', 'user')
    inlines = [TaskInline]

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('workflow', 'title', 'status', 'assigned_to', 'due_date')
    search_fields = ('title', 'workflow__title', 'assigned_to__username')
    list_filter = ('workflow', 'status', 'assigned_to')
    list_editable = ('status',)
