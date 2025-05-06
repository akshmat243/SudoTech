from django.contrib import admin
from .models import JobOpening, Applicant

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'job_type', 'posted_date', 'closing_date', 'status')
    list_filter = ('department', 'job_type', 'status')
    search_fields = ('title', 'department', 'location')


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'job', 'application_date', 'status')
    list_filter = ('status', 'application_date', 'job')
    search_fields = ('full_name', 'email', 'job__title')
