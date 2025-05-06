from django.contrib import admin
from .models import Messenger

@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
