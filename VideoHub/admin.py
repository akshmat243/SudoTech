from django.contrib import admin
from .models import Channel, Category, Video, Playlist, ViewerActivity

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_on')
    search_fields = ('name', 'created_by__username')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'channel', 'category', 'upload_date', 'is_published')
    list_filter = ('is_published', 'category', 'upload_date')
    search_fields = ('title', 'channel__name')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_on')
    filter_horizontal = ('videos',)
    search_fields = ('title', 'created_by__username')


@admin.register(ViewerActivity)
class ViewerActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'watched_on', 'liked')
    list_filter = ('liked',)
    search_fields = ('user__username', 'video__title')
