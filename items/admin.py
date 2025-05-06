from django.contrib import admin
from .models import Items

@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'image_tag', 'name', 'sku', 'sale_price', 'purchase_price',
        'tax', 'category', 'unit', 'quantity', 'type'
    )
    search_fields = ('name', 'sku', 'category')
    list_filter = ('category', 'type')
    readonly_fields = ('sku',)
    
    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return 'No Image'
    image_tag.allow_tags = True
    image_tag.short_description = 'Image'
