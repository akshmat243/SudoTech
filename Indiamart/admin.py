from django.contrib import admin
from .models import IndiaMartInquiry

@admin.register(IndiaMartInquiry)
class IndiaMartInquiryAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject')
    list_filter = ('created_at',)
