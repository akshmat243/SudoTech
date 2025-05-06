from django.contrib import admin
from .models import BusinessMapping

@admin.register(BusinessMapping)
class BusinessMappingAdmin(admin.ModelAdmin):
    list_display = ('no', 'title', 'related', 'related_to')
    search_fields = ('no', 'title', 'related', 'related_to')
    list_filter = ('related_to',)
