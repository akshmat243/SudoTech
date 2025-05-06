from django.contrib import admin
from .models import OneNoteNotebook, OneNoteSection, OneNotePage

@admin.register(OneNoteNotebook)
class OneNoteNotebookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(OneNoteSection)
class OneNoteSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'notebook', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('notebook',)


@admin.register(OneNotePage)
class OneNotePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('section',)
