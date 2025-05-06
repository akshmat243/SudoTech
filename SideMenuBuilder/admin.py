from django.contrib import admin
from .models import SideMenuBuilder

@admin.register(SideMenuBuilder)
class SideMenuBuilderAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'menu_type', 'parent_module', 'which_window', 'owner')
    search_fields = ('menu_name', 'menu_type', 'parent_module', 'owner')
