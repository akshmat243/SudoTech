from django.contrib import admin
from .models import File, Activity, Trash, FileVerification

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'uploaded_at', 'is_verified', 'is_trashed')
    list_filter = ('is_verified', 'is_trashed')
    search_fields = ('name', 'owner__username')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('file', 'user', 'action', 'timestamp')
    list_filter = ('action',)
    search_fields = ('file__name', 'user__username')


@admin.register(Trash)
class TrashAdmin(admin.ModelAdmin):
    list_display = ('file', 'trashed_by', 'trashed_at')
    search_fields = ('file__name', 'trashed_by__username')


@admin.register(FileVerification)
class FileVerificationAdmin(admin.ModelAdmin):
    list_display = ('file', 'verifier', 'verified_at')
    search_fields = ('file__name', 'verifier__username')
