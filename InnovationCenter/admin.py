from django.contrib import admin
from .models import UpcomingChallenge, NewCreativity, InnovationSystemSetup

@admin.register(UpcomingChallenge)
class UpcomingChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'deadline', 'created_at')
    search_fields = ('title',)
    list_filter = ('deadline',)

@admin.register(NewCreativity)
class NewCreativityAdmin(admin.ModelAdmin):
    list_display = ('name', 'submitted_by', 'submitted_on')
    search_fields = ('name', 'submitted_by')

@admin.register(InnovationSystemSetup)
class InnovationSystemSetupAdmin(admin.ModelAdmin):
    list_display = ('config_name', 'config_value')
    search_fields = ('config_name',)
