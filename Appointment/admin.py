from django.contrib import admin
from .models import Appointment, Question, Schedule, AppointmentCallback


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'appointment_time', 'status')
    list_filter = ('status', 'appointment_time')
    search_fields = ('title', 'user__username')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'question_text', 'answer', 'created_at')
    search_fields = ('appointment__title', 'question_text')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'start_time', 'end_time', 'available')
    list_filter = ('available', 'start_time')
    search_fields = ('appointment__title',)


@admin.register(AppointmentCallback)
class AppointmentCallbackAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'callback_time', 'callback_status')
    list_filter = ('callback_status',)
    search_fields = ('appointment__title',)
