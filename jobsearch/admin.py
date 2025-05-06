from django.contrib import admin
from .models import JobSearch

@admin.register(JobSearch)
class JobSearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'posted_date', 'expiry_date', 'is_active')
    list_filter = ('job_type', 'location', 'is_active')
    search_fields = ('title', 'company', 'location')
