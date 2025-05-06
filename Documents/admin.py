from django.contrib import admin
from .models import DocumentType, DocumentTemplate, Document

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'document_type', 'template_file']
    list_filter = ['document_type']
    search_fields = ['name', 'document_type__name']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'document_template', 'created_at', 'updated_at']
    list_filter = ['document_type']
    search_fields = ['title']
    date_hierarchy = 'created_at'
