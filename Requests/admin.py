from django.contrib import admin
from .models import Request, RequestSystemSetup

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'request_type', 'customer_name', 'status', 'created_at')
    search_fields = ('request_id', 'customer_name', 'customer_email', 'description')
    list_filter = ('request_type', 'status')

@admin.register(RequestSystemSetup)
class RequestSystemSetupAdmin(admin.ModelAdmin):
    list_display = ('setting_name', 'value')
    search_fields = ('setting_name',)
