from django.contrib import admin
from .models import TeamMember, Task, WorkloadOverview, WorkloadSettings

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'date_joined')
    search_fields = ('name', 'email', 'role')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'priority', 'due_date', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'assigned_to__name', 'status')
    list_filter = ('priority', 'status', 'assigned_to')


@admin.register(WorkloadOverview)
class WorkloadOverviewAdmin(admin.ModelAdmin):
    list_display = ('total_tasks', 'tasks_in_progress', 'tasks_completed', 'tasks_pending')
    actions = ['update_overview']

    def update_overview(self, request, queryset):
        for overview in queryset:
            overview.update_overview()

    update_overview.short_description = "Update Workload Overview"


@admin.register(WorkloadSettings)
class WorkloadSettingsAdmin(admin.ModelAdmin):
    list_display = ('max_tasks_per_member', 'allow_task_assignment', 'notify_on_task_due', 'work_hours_per_day')
    search_fields = ('max_tasks_per_member',)
