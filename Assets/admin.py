from django.contrib import admin
from .models import Asset, AssetHistory, DefectiveAsset, AssetSystemSetup

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_tag', 'name', 'category', 'purchase_date', 'value', 'status', 'assigned_to')
    search_fields = ('asset_tag', 'name', 'category', 'assigned_to')
    list_filter = ('status', 'category')

@admin.register(AssetHistory)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = ('asset', 'change_type', 'change_date', 'changed_by')
    search_fields = ('asset__asset_tag', 'change_type', 'changed_by')

@admin.register(DefectiveAsset)
class DefectiveAssetAdmin(admin.ModelAdmin):
    list_display = ('asset', 'reported_on', 'resolved')
    list_filter = ('resolved',)
    search_fields = ('asset__asset_tag',)

@admin.register(AssetSystemSetup)
class AssetSystemSetupAdmin(admin.ModelAdmin):
    list_display = ('setting_name', 'value')
    search_fields = ('setting_name',)
