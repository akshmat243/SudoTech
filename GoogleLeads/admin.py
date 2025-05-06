from django.contrib import admin
from .models import GoogleLead

@admin.register(GoogleLead)
class GoogleLeadAdmin(admin.ModelAdmin):
    list_display = ('lead_no', 'name', 'keywords', 'address', 'contacts_found')
    search_fields = ('lead_no', 'name', 'keywords', 'address')
    list_filter = ('contacts_found',)
