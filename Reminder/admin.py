from django.contrib import admin
from .models import Reminder, ReminderCategory

@admin.register(ReminderCategory)
class ReminderCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'reminder_date', 'is_completed')
    search_fields = ('title', 'category__name', 'user__username')
    list_filter = ('category', 'user', 'is_completed')
    list_editable = ('is_completed',)
